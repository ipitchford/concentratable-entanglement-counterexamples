# Concentratable entanglement: counterexamples and sharp repairs

Scholarly creator: **Anonymous**. Research candidate, 13 October 2026.

The nonzero-even local-SWAP probability is not a universal upper bound on mixed-state total concentratable entanglement (CE). A Bell pair with a mixed spectator already fails; this package also proves exact genuinely tripartite-entangled examples and an explicit neighbourhood of full-rank examples.

Read [the manuscript source](paper.tex), its [extension proofs](extensions.tex), the [claim map](CLAIMS.json), and [assurance limits](ASSURANCE.md). Read the [typeset manuscript](paper.pdf) or [accessible manuscript](paper.md); final document QA is recorded separately. The planned public repository is https://github.com/ipitchford/concentratable-entanglement-counterexamples and planned candidate tag is `v0.1.0-candidate`. These planned identifiers do not attest publication. Reserved DOI: https://doi.org/10.5281/zenodo.23336463. See external release receipts for archive identity and public readback.

## Results and boundaries

- Both roofs of the Bell spectator equal 1/4, while the proposed statistic is 3/16.
- The sharp correction coefficient uniformly over system size is 1/2 for both roofs.
- At fixed n the sharp concave-roof coefficient is 1/2−2^−n. The convex coefficient is zero for n=2; three qubits are the minimum for a convex-roof violation.
- Mixed single-qubit spectators preserve the convex roof of arbitrary mixed cores. A globally depolarised family gives full-rank violations, with a trace-distance ball of radius 1/200 around the q=19/20 example.
- A separate rank-two genuinely tripartite-entangled family has exact convex and concave roofs. The full-rank ball is not certified genuinely tripartite entangled.
- The exact fixed-three-qubit convex correction remains open here: 1/8 ≤ c_3^cup ≤ 3/8.

## Replay

Use Python 3.10 or newer and `python -m pip install -r requirements.txt` (SymPy 1.14.0). From this directory:

```sh
python verify_ce_counterexample.py
python -O verify_ce_counterexample.py
python independent_pauli_check.py
python verify_extensions.py --negative-controls
python -O verify_extensions.py --negative-controls
```

Each command prints JSON with PASS on success and exits nonzero on a check failure. See [recorded replay scope](REPLAY_RECEIPT.md). Finite and symbolic checks do not replace the universal proofs. [REVIEW_RESPONSE.md](REVIEW_RESPONSE.md) records dispositions of the original review and targeted extension checks. Public content uses CC0-1.0; original executable code uses MIT, as mapped in [LICENSES.md](LICENSES.md).
