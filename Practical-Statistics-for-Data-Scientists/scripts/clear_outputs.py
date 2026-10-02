from pathlib import Path
import nbformat
root=Path(__file__).resolve().parents[1]
for p in sorted((root/'notebooks').glob('Bab_*.ipynb')):
    nb=nbformat.read(p,4)
    for c in nb.cells:
        if c.cell_type=='code':
            c.outputs=[]
            c.execution_count=None
            c.metadata.pop('execution',None)
    nb.metadata.pop('widgets',None)
    nbformat.write(nb,p)
    print(p.name, ': semua output dikosongkan')
