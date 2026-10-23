"""Execute notebooks in fresh kernels and save outputs."""
from pathlib import Path
import argparse, concurrent.futures, json, os, sys, time
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))
os.environ["JUPYTER_CONFIG_DIR"] = str(ROOT / ".jupyter" / "config")
os.environ["JUPYTER_DATA_DIR"] = str(ROOT / ".jupyter" / "data")
os.environ["JUPYTER_RUNTIME_DIR"] = str(ROOT / ".jupyter" / "runtime")
os.environ["IPYTHONDIR"] = str(ROOT / ".ipython")
for local_dir in [os.environ["JUPYTER_CONFIG_DIR"], os.environ["JUPYTER_DATA_DIR"], os.environ["JUPYTER_RUNTIME_DIR"], os.environ["IPYTHONDIR"]]:
    Path(local_dir).mkdir(parents=True, exist_ok=True)
KERNEL = ROOT / ".jupyter" / "kernels" / "grokking"
KERNEL.mkdir(parents=True, exist_ok=True)
(KERNEL / "kernel.json").write_text(json.dumps({
    "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
    "display_name": "Grokking Deep Learning",
    "language": "python",
}), encoding="utf-8")

def run(path):
    start = time.time()
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
    status, error = "passed", ""
    km = KernelManager(kernel_name="grokking", kernel_spec_manager=KernelSpecManager(kernel_dirs=[str(KERNEL.parent)]))
    try:
        NotebookClient(nb, km=km, timeout=1800, resources={"metadata": {"path": str(path.parent)}}).execute()
    except Exception as exc:
        status, error = "failed", str(exc)
    finally:
        if km.has_kernel:
            km.shutdown_kernel(now=True)
    nbformat.write(nb, path)
    result = {"notebook": path.name, "status": status, "seconds": round(time.time()-start, 2), "error": error}
    (ROOT / "docs" / f"{path.stem}_execution.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=True), flush=True)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapters", nargs="*", type=int, default=list(range(1, 17)))
    parser.add_argument("--jobs", type=int, default=1)
    args = parser.parse_args()
    paths = [ROOT / "notebooks" / f"Bab_{n:02d}.ipynb" for n in args.chapters]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        results = list(pool.map(run, paths))
    raise SystemExit(any(r["status"] != "passed" for r in results))
