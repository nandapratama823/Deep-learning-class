"""Validate final notebooks, their saved execution outputs, and dataset checksums."""
from pathlib import Path
import hashlib, json
import nbformat
ROOT=Path(__file__).resolve().parents[1]
def main():
    total=0; results=[]
    notebooks=sorted((ROOT/'notebooks').glob('Bab_*.ipynb'))
    assert len(notebooks)==7, 'Harus ada 7 notebook.'
    for p in notebooks:
        nb=nbformat.read(p,as_version=4); nbformat.validate(nb)
        code=[c for c in nb.cells if c.cell_type=='code' and c.source.strip()]
        # Output boleh kosong pada paket sebelum dijalankan pengguna.
        errors=[o for c in code for o in c.outputs if o.output_type=='error']
        assert not errors,f'Output error: {p.name}'
        md='\n'.join(c.source for c in nb.cells if c.cell_type=='markdown')
        assert '101032330212' in md and 'Ringkasan hasil yang diperoleh' in md
        assert '\ufffd' not in md, f'Karakter encoding rusak: {p.name}'
        total+=len(code)
        results.append({'notebook':p.name,'code_cells':len(code),'error_outputs':len(errors)})
    manifest=json.loads((ROOT/'docs'/'data_manifest.json').read_text(encoding='utf-8'))
    for entry in manifest:
        p=ROOT/'data'/entry['file']
        assert p.stat().st_size==entry['bytes'],p.name
        assert hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],p.name
    for p in ['README.md','LICENSE','requirements-lock.txt','docs/CAKUPAN.md','docs/PERUBAHAN.md','docs/SUMBER.md','docs/VALIDASI.md']:
        assert (ROOT/p).is_file(),p
    report={'status':'passed','notebooks':len(notebooks),'code_cells':total, 'executed_code_cells':sum(c.execution_count is not None for p in notebooks for c in nbformat.read(p,4).cells if c.cell_type=='code'),'datasets_verified':len(manifest),'results':results,'note':'Execution provenance is documented in docs/VALIDASI.md; this script inspects saved outputs and does not re-execute notebooks.'}
    print(json.dumps(report,indent=2))
    (ROOT/'docs'/'validation_summary.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
if __name__=='__main__': main()
