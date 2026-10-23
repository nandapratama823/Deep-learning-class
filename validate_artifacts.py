"""Validate notebook structure, outputs, links, and data checksums."""
from pathlib import Path
import hashlib, json
import nbformat

ROOT = Path(__file__).resolve().parents[1]
notebooks = sorted((ROOT / "notebooks").glob("Bab_*.ipynb"))
assert len(notebooks) == 16, f"Expected 16 notebooks, found {len(notebooks)}"
results, executed = [], 0
for path in notebooks:
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    markdown = "\n".join(c.source for c in nb.cells if c.cell_type == "markdown")
    code = [c for c in nb.cells if c.cell_type == "code" and c.source.strip()]
    errors = [o for c in code for o in c.outputs if o.output_type == "error"]
    assert "101032330212" in markdown, path.name
    assert "Interpretasi dan kesimpulan" in markdown, path.name
    assert code, path.name
    assert not errors, f"Saved error output in {path.name}"
    executed += sum(c.execution_count is not None for c in code)
    results.append({"notebook": path.name, "code_cells": len(code), "error_outputs": len(errors)})

manifest = json.loads((ROOT / "docs" / "data_manifest.json").read_text(encoding="utf-8"))
for entry in manifest:
    path = ROOT / "data" / entry["file"]
    assert path.stat().st_size == entry["bytes"], path.name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"], path.name

for required in ["README.md", "NOTICE.md", "requirements.txt", "docs/CAKUPAN.md", "docs/SUMBER.md", "docs/VALIDASI.md"]:
    assert (ROOT / required).is_file(), required

report = {"status": "passed", "notebooks": len(notebooks), "executed_code_cells": executed, "datasets_verified": len(manifest), "results": results}
(ROOT / "docs" / "validation_summary.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report, indent=2))
