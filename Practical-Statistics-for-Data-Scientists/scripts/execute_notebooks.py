"""Execute notebooks in fresh kernels and save actual outputs; fail on first cell error."""
from pathlib import Path
import os, sys, json, time, argparse, concurrent.futures
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'.mplconfig')
os.environ['OMP_NUM_THREADS']='2'
os.environ['OPENBLAS_NUM_THREADS']='2'
KERNEL=ROOT/'.jupyter'/'kernels'/'statistics'
KERNEL.mkdir(parents=True,exist_ok=True)
(KERNEL/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],'display_name':'Statistics','language':'python'}))
def run(path):
    t=time.time(); nb=nbformat.read(path,as_version=4)
    for c in nb.cells:
        if c.cell_type=='code': c.outputs=[]; c.execution_count=None
    km=KernelManager(kernel_name='statistics',kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(KERNEL.parent)]))
    client=NotebookClient(nb,km=km,timeout=1800,resources={'metadata':{'path':str(path.parent)}},record_timing=True)
    status='passed'; error=''
    try: client.execute()
    except Exception as exc: status='failed'; error=str(exc)
    finally:
        if km.has_kernel: km.shutdown_kernel(now=True)
    nbformat.write(nb,path)
    result={'notebook':path.name,'status':status,'seconds':round(time.time()-t,2),'code_cells':sum(c.cell_type=='code' for c in nb.cells),'executed':sum(c.cell_type=='code' and c.execution_count is not None for c in nb.cells),'error':error}
    (ROOT/'docs'/f'{path.stem}_execution.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,ensure_ascii=True),flush=True)
    return result
if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--chapters',nargs='*',type=int,default=list(range(1,8))); parser.add_argument('--jobs',type=int,default=2)
    args=parser.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        results=list(pool.map(run,[ROOT/'notebooks'/f'Bab_{n:02d}.ipynb' for n in args.chapters]))
    sys.exit(any(r['status']!='passed' for r in results))
