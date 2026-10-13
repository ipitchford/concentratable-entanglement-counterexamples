# Retained preparation replay receipt

Date: 13 October 2026. This records actual retained runs, not a final clean-archive replay or remote CI result.

| Evidence | Actual result and scope |
|---|---|
| receipts/original-normal.json | PASS; original rational density matrix, support rank, subsystem purities, SWAP probabilities and near-pure sample checks. |
| receipts/original-optimized.json | PASS; optimized original checker run. |
| receipts/pauli.json | PASS; separately implemented Pauli orthogonality and weight-enumeration calculation, with no submission-code imports. |
| receipts/extensions-normal.json | PASS; 105 recorded exact checks and seven rejected semantic mutants. |
| receipts/extensions-optimized.json | PASS; same structured JSON as normal extension run; Python 3.14.7, SymPy 1.14.0. |

Original and Pauli receipts come from the original-submission review. Extension receipts come from the working candidate verifier. Public replay commands are in README.md. The extension runs used `python3 verify_extensions.py --negative-controls` and `python3 -O verify_extensions.py --negative-controls` from the candidate's enclosing preparation environment, with stdout retained as JSON. Paths are rendered package-relative here to avoid disclosing private directories; this is not an assertion that the commands were already run from a clean extracted public archive.

The original verifier reports a roof value derived from the analytic support proof; it does not optimise over ensembles. The extension checker verifies identities under polynomial constraints but does not prove the support/GME reasoning, Jensen/chord logic, Wootters theorem, trace-distance inequalities, novelty or research significance. Final clean-extraction replay, final-source hashing and public CI remain separate checks.

Retained receipt SHA-256 values:

- `extensions-normal.json`: `6973c0e6ecf7de110846014b37b5fe527ef74c9f1ce546eb04aef580f0989937`
- `extensions-optimized.json`: `6973c0e6ecf7de110846014b37b5fe527ef74c9f1ce546eb04aef580f0989937`
- `original-normal.json`: `bbeeb6c82e9d7506b8c4a1b78d520266e5e2ca0f8e7e26801b2af489660459c2`
- `original-optimized.json`: `bbeeb6c82e9d7506b8c4a1b78d520266e5e2ca0f8e7e26801b2af489660459c2`
- `pauli.json`: `f006c3265b93e68f5847011132e4fcef7f89d20a3062ef9d1fdc3c9be57f6e59`
