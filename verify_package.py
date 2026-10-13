"""Verify all shipped files against the SHA-256 manifest; no scientific claim."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
entries={}
for line in (root/'MANIFEST.sha256').read_text().splitlines():
    digest,name=line.split('  ',1)
    if name in entries or Path(name).is_absolute() or '..' in Path(name).parts:
        raise ValueError('Unsafe or duplicate manifest entry')
    entries[name]=digest
actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '.git' not in p.relative_to(root).parts and '__pycache__' not in p.relative_to(root).parts and 'ci-results' not in p.relative_to(root).parts and p.name!='MANIFEST.sha256'}
if actual!=set(entries): raise ValueError('Manifest coverage mismatch: '+repr(actual^set(entries)))
for name,digest in entries.items():
    if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest: raise ValueError('Hash mismatch: '+name)
print(json.dumps({'status':'PASS','files':len(entries),'scope':'Shipped byte identity and coverage only'}))
