"""Clear saved notebook outputs and execution counts."""
from pathlib import Path
import nbformat
ROOT = Path(__file__).resolve().parents[1]
for path in sorted((ROOT / "notebooks").glob("Bab_*.ipynb")):
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.outputs = []
            cell.execution_count = None
    nbformat.write(nb, path)
    print(path.name)
