# Concentratable entanglement: counterexamples and sharp repairs

Anonymous · 13 October 2026 · Version 0.1.0-candidate · Unrefereed

DOI: [10.5281/zenodo.23336463](https://doi.org/10.5281/zenodo.23336463)

## Abstract

A conjectured upper bound on mixed-state concentratable entanglement equals the probability of a nonzero even-parity outcome in a parallel SWAP test. We show that a Bell pair tensored with one maximally mixed, uncorrelated qubit has both convex-roof and concave-roof concentratable entanglement $1/4$, whereas the proposed bound is $3/16$. A support argument determines every pure-state ensemble average, so no optimisation is needed. More generally, a mixed spectator qubit of purity $r$ multiplies this statistic by $(1+r)/2$ while leaving both roofs of a pure core unchanged. Counterexamples therefore persist arbitrarily close to pure states. We further give full-rank noisy counterexamples, an explicit perturbation ball, and genuinely tripartite-entangled rank-two examples with both roofs determined exactly. Three qubits is minimal for the convex-roof violation. The fixed-size concave-roof correction is sharp. We also prove that the smallest coefficient $c$, independent of the number of qubits, for which adding $c(1-\operatorname{tr}\rho^2)$ always repairs the upper bound is $c=1/2$.


## The precise claim

Concentratable entanglement (CE) was introduced as a family of pure-state multipartite entanglement measures \[5\]. We use total CE, in which all $n$ qubits belong to the label set. For an $n$-qubit density matrix $\rho$, set $$

 F_n(\rho)=2^{-n}\sum_{A\subseteq[n]}\operatorname{tr}(\rho_A^2),
 \qquad \operatorname{tr}(\rho_\varnothing^2)=1.
$$ The sum includes both the empty subsystem and the full system. For a normalised pure state, $$

 \mathcal C_n(\psi)=1-F_n(\lvert \psi\rangle\langle \psi\rvert).
$$ Write the two ensemble roofs as $$\begin{aligned}
 \mathcal C_n^\cup(\rho)&=\inf_{\rho=\sum_i p_i\lvert \psi_i\rangle\langle \psi_i\rvert}
                       \sum_i p_i\mathcal C_n(\psi_i),\\
 \mathcal C_n^\cap(\rho)&=\sup_{\rho=\sum_i p_i\lvert \psi_i\rangle\langle \psi_i\rvert}
                       \sum_i p_i\mathcal C_n(\psi_i).
\end{aligned}$$ The convex-roof extension is also developed by Beckey et al. \[2, eq. (10)\]. These are the quantities in equations (3.5) and (3.6) of Foulds, Prove and Kendon \[4\]. Their equations (3.18) and (5.1) propose $$

 U_n(\rho)=\frac{1+\operatorname{tr}(\rho^2)}{2}-F_n(\rho)
$$ as an upper bound. The abstract labels the upper bound a conjecture. The source also expressly acknowledges, on p. 15 after equation (3.23), that CE may exceed the calculated upper bound. Our contribution is an exact refutation and repair of the universal statement, not the discovery that the source never recognised possible failure. We disprove the universal inequality $\mathcal C_n^\cup(\rho)\leq U_n(\rho)$, and therefore also the stronger interpretation with $\mathcal C_n^\cap$ on the left.

Our examples use two identical copies of $\rho$. Thus they do not involve the copy-mismatch approximation also discussed in \[4\]. They address the universal total-CE claim, not a conjecture restricted solely to a specified depolarising or Werner-type noise family.

## Two elementary lemmas

::: {#lem:product .lemma}
**Lemma 1** (Product rule). *For states $\rho$ and $\sigma$ on disjoint sets of $m$ and $k$ qubits, $$

 F_{m+k}(\rho\otimes\sigma)=F_m(\rho)F_k(\sigma).
$$ In particular, adjoining a pure single-qubit state does not change pure-state total CE.*
:::

::: proof
*Proof.* Each subsystem of the combined system is uniquely $A\cup B$, with $A$ in the first set and $B$ in the second. Its reduced state is $\rho_A\otimes\sigma_B$, so its purity is $\operatorname{tr}(\rho_A^2)\operatorname{tr}(\sigma_B^2)$. The double sum factors. For a pure single qubit $c$, $F_1(\lvert c\rangle\langle c\rvert)=(1+1)/2=1$. ◻
:::

The pure-state form of this product rule is also part of the existing CE hierarchy \[6\]; we include the direct proof to fix all normalisations.

::: {#lem:support .lemma}
**Lemma 2** (Support restriction). *Every positively weighted vector in a pure-state decomposition of $\rho$ belongs to $\operatorname{supp}\rho$.*
:::

::: proof
*Proof.* For $v\in\ker\rho$, $$0=\langle v\rvert\rho\lvert v\rangle=\sum_i p_i|\langle v\mid\psi_i\rangle|^2.$$ Every summand is nonnegative. For $p_i>0$, $\psi_i$ is therefore orthogonal to $\ker\rho$. The same argument holds almost everywhere for a measure-valued ensemble. ◻
:::

## The spectator theorem and the counterexample

::: {#thm:spectator .theorem}
**Theorem 3** (Mixed single-qubit spectator). *Let $\phi$ be a pure $m$-qubit state, let $e=\mathcal C_m(\phi)$, and let $\tau$ be any single-qubit density matrix of purity $r=\operatorname{tr}(\tau^2)\in[1/2,1]$. Set $\rho=\lvert \phi\rangle\langle \phi\rvert\otimes\tau$. Then $$\begin{aligned}
 \mathcal C_{m+1}^\cup(\rho)=\mathcal C_{m+1}^\cap(\rho)&=e,\\
 U_{m+1}(\rho)&=\frac{1+r}{2}e,\\
 \mathcal C_{m+1}^\cup(\rho)-U_{m+1}(\rho)&=\frac{1-r}{2}e.
\end{aligned}$$ Consequently, the proposed upper bound fails whenever $e>0$ and $\tau$ is mixed.*
:::

::: proof
*Proof.* The support of $\rho$ is $\operatorname{span}\{\phi\}\otimes\operatorname{supp}\tau$. By Lemma 2, every pure-state component has the form $\phi\otimes c_i$, with $c_i$ a normalised single-qubit vector. Lemma 1 gives $\mathcal C_{m+1}(\phi\otimes c_i)=e$. Every ensemble average is therefore exactly $e$, proving both roof identities.

Next, $\operatorname{tr}(\rho^2)=r$, $F_m(\lvert \phi\rangle\langle \phi\rvert)=1-e$, and $F_1(\tau)=(1+r)/2$. Applying Lemma 1 to (5) gives $$U_{m+1}(\rho)=\frac{1+r}{2}-(1-e)\frac{1+r}{2}
             =e\frac{1+r}{2}.$$ Subtracting proves (9). ◻
:::

::: {#cor:bell .corollary}
**Corollary 4** (An exact three-qubit counterexample). *Let $$\lvert \Phi^+\rangle_{AB}=\frac{\lvert 00\rangle+\lvert 11\rangle}{\sqrt2},
 \qquad \rho_{ABC}=\lvert \Phi^+\rangle\langle \Phi^+\rvert_{AB}\otimes\frac{I_C}{2}.$$ Then $$

 \mathcal C_3^\cup(\rho)=\mathcal C_3^\cap(\rho)=\frac14
  >\frac3{16}=U_3(\rho).
$$*
:::

:::: proof
*Proof.* The four subsystem purities of a Bell pair are $1,1/2,1/2,1$, so $F_2=3/4$ and $e=1/4$. The spectator has $r=1/2$. Theorem 3 proves the claim. A direct calculation independently gives:

::: center
  Subsystem     $\varnothing$     $A$     $B$     $C$   $AB$    $AC$    $BC$   $ABC$
  ----------- --------------- ------- ------- ------- ------ ------- ------- -------
  Purity                  $1$   $1/2$   $1/2$   $1/2$    $1$   $1/4$   $1/4$   $1/2$
:::

The sum is $9/2$, and hence $F_3(\rho)=9/16$ and $U_3(\rho)=\tfrac12(1+\tfrac12)-\tfrac9{16}=\tfrac3{16}$. ◻
::::

An explicit matrix certificate, in lexicographic computational-basis order, is $$\rho=\frac14
 \begin{pmatrix}
 1&0&0&0&0&0&1&0\\
 0&1&0&0&0&0&0&1\\
 0&0&0&0&0&0&0&0\\
 0&0&0&0&0&0&0&0\\
 0&0&0&0&0&0&0&0\\
 0&0&0&0&0&0&0&0\\
 1&0&0&0&0&0&1&0\\
 0&1&0&0&0&0&0&1
 \end{pmatrix}.$$ It is the equally weighted mixture of two orthogonal pure states $\Phi^+\otimes\lvert 0\rangle$ and $\Phi^+\otimes\lvert 1\rangle$, so it is positive semidefinite with trace one and rank two. Positivity is not inferred from floating-point eigenvalues.

::: {#cor:near .corollary}
**Corollary 5** (Failure arbitrarily near purity). *For $0<\epsilon<1$, let $$\tau_\epsilon=(1-\epsilon)\lvert 0\rangle\langle 0\rvert+\epsilon\lvert 1\rangle\langle 1\rvert,
 \qquad \rho_\epsilon=\lvert \Phi^+\rangle\langle \Phi^+\rvert\otimes\tau_\epsilon.$$ Then $$\begin{aligned}
 \operatorname{tr}(\rho_\epsilon^2)&=1-2\epsilon(1-\epsilon),\\
 \mathcal C_3^\cup(\rho_\epsilon)=\mathcal C_3^\cap(\rho_\epsilon)&=\frac14,\\
 U_3(\rho_\epsilon)&=\frac{1-\epsilon+\epsilon^2}{4},\\
 \mathcal C_3^\cup(\rho_\epsilon)-U_3(\rho_\epsilon)&=\frac{\epsilon(1-\epsilon)}{4}>0.
\end{aligned}$$ Moreover, $\tfrac12\|\rho_\epsilon-\rho_0\|_1=\epsilon$.*
:::

::: proof
*Proof.* The first formula follows by squaring the two eigenvalues of $\tau_\epsilon$; the next three follow from Theorem 3. The difference from $\rho_0$ has two nonzero eigenvalues $\epsilon$ and $-\epsilon$, proving the trace-distance formula. ◻
:::

## A sharp dimension-independent additive correction

::: {#thm:repair .theorem}
**Theorem 6**. *The smallest real constant $c$, independent of $n$, such that $$

 \mathcal C_n^\cup(\rho)\leq U_n(\rho)+c\bigl(1-\operatorname{tr}(\rho^2)\bigr)
$$ for every finite $n$ and every $n$-qubit density matrix is $c=1/2$. The same optimal constant applies to $\mathcal C_n^\cap$.*

*For each fixed $n$, the following stronger bound holds (Equation (22) establishes the optimal concave-roof coefficient): $$

 \mathcal C_n^\cap(\rho)\leq U_n(\rho)
       +\left(\frac12-2^{-n}\right)\bigl(1-\operatorname{tr}(\rho^2)\bigr).
$$*
:::

::: proof
*Proof.* For any pure-state ensemble of $\rho$, let $\rho_{i,A}$ be the reduced state of $\psi_i$ on $A$. With $\|X\|_2^2=\operatorname{tr}(X^\dagger X)$, expanding the Hilbert--Schmidt norm gives $$\sum_i p_i\operatorname{tr}(\rho_{i,A}^2)-\operatorname{tr}(\rho_A^2)
       =\sum_i p_i\|\rho_{i,A}-\rho_A\|_2^2\geq0.$$ Therefore every ensemble satisfies the exact variance identity $$

 \sum_i p_i\mathcal C_n(\psi_i)
 =1-F_n(\rho)-2^{-n}\sum_{A\subseteq[n]}\sum_i p_i
                         \|\rho_{i,A}-\rho_A\|_2^2.
$$ Discarding the nonnegative sum gives $$\mathcal C_n^\cap(\rho)\leq1-F_n(\rho)
       =U_n(\rho)+\frac12\bigl(1-\operatorname{tr}(\rho^2)\bigr).$$ Since $\mathcal C_n^\cup\leq\mathcal C_n^\cap$, this proves sufficiency for both roofs. Retaining the full-system term in (17), whose value is $1-\operatorname{tr}(\rho^2)$, proves (16).

To prove dimension-independent optimality, take a pure core comprising $k$ independent Bell pairs: $$\lvert \phi_k\rangle=\lvert \Phi^+\rangle^{\otimes k},\qquad
 e_k=1-\left(\frac34\right)^k.$$ The expression for $e_k$ follows from Lemma 1. Append any fixed mixed single qubit $\tau$, with $r=\operatorname{tr}(\tau^2)<1$, to obtain a $(2k+1)$-qubit state $\omega_k$. Theorem 3 gives $$\frac{\mathcal C_{2k+1}^\cup(\omega_k)-U_{2k+1}(\omega_k)}
 {1-\operatorname{tr}(\omega_k^2)}
 =\frac{e_k}{2}
 =\frac12\left[1-\left(\frac34\right)^k\right]
 \longrightarrow\frac12.$$ Both roofs coincide on these states. Every $c<1/2$ fails for some finite $k$, proving necessity for both roofs. ◻
:::

The sufficient bound $1-F_n$ is the usual concavity-based upper estimate. Vairogs, Hermes and Leditzky give the same purity-convexity argument for CE of assistance \[3, Theorem 3 and Appendix B\]. The measurable mixed-state quantity $1-F_n$ is explicitly discussed by Schatzki et al. \[6, Supplement, Section XI\]; it is not itself an entanglement monotone. Theorem 6 does not claim that this estimate is the best bound at any fixed $n$, nor that nonlinear or state-dependent corrections are excluded.

## Why the measured probability decreases

For identical copies, the statistic $U_n$ equals the probability of a nonzero even number of antisymmetric outcomes in local SWAP measurements, whereas the odd-parity probability is $(1-\operatorname{tr}\rho^2)/2$ \[4, eqs. (3.3)--(3.4)\]. Label a symmetric outcome by $0$ and an antisymmetric outcome by $1$.

For two copies of a Bell pair, the outcomes $00$ and $11$ have probabilities $3/4$ and $1/4$. A spectator of purity $r$ gives probabilities $(1+r)/2$ and $(1-r)/2$. The core and spectator measurements factor, since their input density matrices factor. The core event $11$ remains even only when the spectator outcome is $0$. Its counted probability is consequently $(1/4)(1+r)/2$.

For $\tau=I/2$, the full distribution is

::: center
  Nonzero-probability outcome      $000$    $001$    $110$    $111$
  ----------------------------- -------- -------- -------- --------
  Probability                     $9/16$   $3/16$   $3/16$   $1/16$
:::

All other outcomes have probability zero. The $111$ event is excluded by the proposed statistic. It accounts exactly for the $1/16$ deficit. The Bell-pair entanglement has not changed; the spectator has changed the parity selection. The uniform repair adds back all odd outcomes, giving $1-F_3=7/16$ here. The fixed-three-qubit repair gives $3/8$. Both exceed the exact roof $1/4$: uniform sharpness does not mean pointwise tightness.

## Two qubits suffice for no convex-roof violation

For two qubits, established concurrence theory gives $$

\mathcal C_2^\cup(\sigma)=C(\sigma)^2/4.
$$ Indeed pure CE equals $C^2/4$, every ensemble has mean concurrence at least $C(\sigma)$, and Wootters constructs an ensemble with every concurrence equal to $C(\sigma)$ \[1\]. Jensen's inequality proves the lower bound and that ensemble attains it.

Write $\widetilde\sigma=(Y\otimes Y)\sigma^*(Y\otimes Y)$ and let $\lambda_1\geq\cdots\geq\lambda_4\geq0$ be the square roots of the eigenvalues of $\sigma\widetilde\sigma$. The concurrence formula gives $$C(\sigma)^2=\max(0,\lambda_1-\lambda_2-\lambda_3-\lambda_4)^2
\leq\sum_j\lambda_j^2=\operatorname{tr}(\sigma\widetilde\sigma).$$ Single-qubit inversion $X\mapsto\operatorname{tr}(X)I-X$, applied to both factors, yields $\widetilde\sigma=I-\sigma_A\otimes I-I\otimes\sigma_B+\sigma$. Thus $\operatorname{tr}(\sigma\widetilde\sigma)=1-\operatorname{tr}\sigma_A^2-\operatorname{tr}\sigma_B^2+\operatorname{tr}\sigma^2=4U_2(\sigma)$. Consequently $\mathcal C_2^\cup\leq U_2$ always. Together with the trivial one-qubit case, Corollary 4 is minimal in qubit count for the convex-roof claim. This is a corollary of established concurrence theory, not a new concurrence formula; the concave roof behaves differently.

## Mixed cores, full-rank failure and experimental certification

::: {#lem:discard .lemma}
**Lemma 7** (Discarding a qubit). *For every $(m+1)$-qubit state $R$ with core marginal $\sigma$, $\mathcal C_m^\cup(\sigma)\leq\mathcal C_{m+1}^\cup(R)$. Hence for any single-qubit state $\tau$, $$\mathcal C_{m+1}^\cup(\sigma\otimes\tau)=\mathcal C_m^\cup(\sigma).$$*
:::

::: proof
*Proof.* First suppose $R=\lvert \Psi\rangle\langle \Psi\rvert$ is pure. Complementary subsystem purities coincide, giving $\mathcal C_{m+1}(\Psi)=1-2^{-m}\sum_{A\subseteq[m]}\operatorname{tr}R_A^2$. Measure the last qubit in an orthonormal basis. The conditional pure core states $\phi_j$ with probabilities $q_j$ have marginals averaging to $R_A$. Convexity of purity gives $\sum_jq_j\mathcal C_m(\phi_j)\leq\mathcal C_{m+1}(\Psi)$. Apply this construction to every member of any pure ensemble of a mixed $R$. The combined ensemble decomposes $\sigma$, so taking the infimum proves the discard inequality. For $\sigma\otimes\tau$, the reverse inequality follows from a near-optimal ensemble of $\sigma$, any pure ensemble of $\tau$, and pure-spectator invariance. ◻
:::

The concave roof does not share mixed-core invariance: $\mathcal C_1^\cap(I_2/2)=0$, whereas the Bell ensemble gives $\mathcal C_2^\cap(I_4/4)=1/4$. The product rule also gives $$U_{m+1}(\sigma\otimes\tau)=\frac{1+r}{2}U_m(\sigma)+\frac{(1-r)(1-P)}4,
\quad P=\operatorname{tr}\sigma^2,\quad r=\operatorname{tr}\tau^2.$$

::: {#thm:noisy .theorem}
**Theorem 8** (Full-rank noisy counterexamples). *For $0\leq q\leq1$, set $$\rho_q=\left(q\lvert \Phi^+\rangle\langle \Phi^+\rvert+(1-q)I_4/4\right)\otimes I_2/2.$$ Then $$\mathcal C_3^\cup(\rho_q)=\frac{\max(0,3q-1)^2}{16},\qquad
U_3(\rho_q)=\frac{9+3q^2}{64}.$$ For $(12+\sqrt{309})/33<q<1$ the state is full rank and violates the proposed upper bound for both roofs.*
:::

::: proof
*Proof.* The two-qubit factor is unchanged by spin flip, with eigenvalues $(1+3q)/4$ and $(1-q)/4$ three times. Wootters' formula, (18) and Lemma 7 give the roof. Its purity is $(1+3q^2)/4$, and its $F_2$ is $(9+3q^2)/16$. The product rule gives the displayed $U_3$. For $q\geq1/3$ the deficit is $(33q^2-24q-5)/64$, whose positive root is the stated threshold. The eigenvalues of $\rho_q$ are $(1+3q)/8$ twice and $(1-q)/8$ six times. Finally $\mathcal C^\cap\geq\mathcal C^\cup$. ◻
:::

For any three-qubit state $R$, let $f=\langle \Phi^+\rvert R_{AB}\lvert \Phi^+\rangle$. A pure two-qubit state has squared overlap with a fixed maximally entangled vector at most $(1+C)/2$, by its Schmidt decomposition and the singular-value trace inequality. Averaging over ensembles and using concurrence's convex-roof definition gives $C(R_{AB})\geq\max(0,2f-1)$. Hence $$

\mathcal C_3^\cup(R)\geq\frac{\max(0,2f-1)^2}{4}.
$$ Comparison of this lower bound with a measured $U_3(R)$ certifies failure without a product-state or depolarising-noise assumption. The fidelity is $f=(1+\langle XX\rangle-\langle YY\rangle+\langle ZZ\rangle)/4$ on $AB$. This uses an established concurrence witness, not a new fidelity witness. Simultaneous valid confidence bounds $f\geq f_L$ and $U\leq U_H$ suffice if $\max(0,2f_L-1)^2/4>U_H$; statistical and identical-copy assumptions must be supplied by an experiment.

There is also an explicit neighbourhood of full-rank counterexamples. At $q=19/20$, $f=77/80$, $U=4683/25600$, $\mathcal C^\cup=1369/6400$, and the smallest eigenvalue is $1/160$. If $D(R,\rho_{19/20})=\|R-\rho_{19/20}\|_1/2\leq\delta$, fidelity changes by at most $\delta$ and the two-copy event probability $U$ changes by at most $2\delta$. Equation (19) therefore gives $$\mathcal C_3^\cup(R)-U_3(R)\geq\frac{(37/40-2\delta)^2}{4}-\frac{4683}{25600}-2\delta
\quad(\delta\leq37/80).$$ At $\delta=1/200$ this is $10481/640000>0$. Since a traceless Hermitian difference has operator norm at most its trace distance, $\lambda_{\min}(R)\geq1/160-1/200=1/800$. Every physical state in this ball is therefore full rank and violates the bound, including correlated perturbations. This ball is not claimed to consist of genuinely tripartite-entangled states.

## Exact genuinely tripartite-entangled counterexamples

::: {#thm:gme .theorem}
**Theorem 9**. *For $0<z<1$, put $c=\sqrt{1-z}$, $s=\sqrt z$, and define $$v_0=(\lvert 000\rangle+\lvert 110\rangle)/\sqrt2,\qquad
v_1=c(\lvert 001\rangle+\lvert 111\rangle)/\sqrt2+s\lvert 010\rangle,\qquad
R_z=(\lvert v_0\rangle\langle v_0\rvert+\lvert v_1\rangle\langle v_1\rvert)/2.$$ The rank-two state $R_z$ is genuinely tripartite entangled and satisfies $$\begin{aligned}
\mathcal C_3^\cup(R_z)&=\frac14-\frac{3z^2}{16},&
\mathcal C_3^\cap(R_z)&=\frac14+\frac z4-\frac{3z^2}{8},\\
U_3(R_z)&=\frac3{16}+\frac z{16}-\frac{3z^2}{16},&
\mathcal C_3^\cup(R_z)-U_3(R_z)&=\frac{1-z}{16}>0.
\end{aligned}$$*
:::

::: proof
*Proof.* By Lemma 2, every ensemble vector is $xv_0+yv_1$. Across $A|BC$, the coefficient-matrix minor in columns $00,10$ is $x^2/2$; when $x=0$, the minor in columns $01,11$ is $y^2c^2/2$. The same minors apply across $B|AC$. Thus no nonzero support vector is product across these two cuts. Across $C|AB$, the minor in columns $00,01$ is $-y^2cs/\sqrt2$, so only the ray $v_0$ is product. A biseparable decomposition, allowing different bipartitions in different components, would consequently use only that one ray and have rank one. Since $R_z$ has rank two, it is genuinely tripartite entangled.

For a normalised support vector set $t=|y|^2$. Direct partial traces, valid for arbitrary complex relative phase, give $$P_A=P_B=\tfrac12+t(1-t)z+\tfrac12t^2z^2,\qquad
P_C=1-2t^2z(1-z).$$ Pure three-qubit CE equals $(3-P_A-P_B-P_C)/4$, hence $$f_z(t)=\mathcal C_3(xv_0+yv_1)=\tfrac14-\tfrac12zt+z(1-3z/4)t^2.$$ Every ensemble of $R_z$ has mean $t=1/2$. The quadratic is convex. Jensen gives the lower bound $f_z(1/2)$, attained by the equally weighted vectors $(v_0\pm v_1)/\sqrt2$. Its endpoint chord gives the upper bound $[f_z(0)+f_z(1)]/2$, attained by the spectral ensemble $v_0,v_1$. These prove both roofs.

In the order $\varnothing,A,B,C,AB,AC,BC,ABC$, the mixed-state purities are $$1,\quad\tfrac12+\tfrac{z^2}8,\quad\tfrac12+\tfrac{z^2}8,\quad
\tfrac12+\tfrac{z^2}2,\quad1-z+\tfrac{z^2}2,\quad
\tfrac14+\tfrac z4+\tfrac{z^2}8,\quad
\tfrac14+\tfrac z4+\tfrac{z^2}8,\quad\tfrac12.$$ Their sum is $9/2-z/2+3z^2/2$. Substitution into (5) proves the remaining formulas. ◻
:::

At $z=1/2$, the exact values are $\mathcal C^\cup=13/64$, $U=11/64$, and $\mathcal C^\cap=9/32$. At $z=0$ the original spectator example is recovered; at $z=1$ both the GME property and the strict convex-roof violation disappear. No full-rank GME radius is claimed.

## Sharpness at fixed size: the two roofs differ

Define $c_n^\cup$ and $c_n^\cap$ as the least coefficients repairing the respective inequalities for all $n$-qubit states. Then $$

c_n^\cap=\frac12-2^{-n}\quad(n\geq1),\qquad c_2^\cup=0.
$$ The second equality follows from the two-qubit argument and a mixed product with one pure factor, for which $U_2=\mathcal C_2^\cup=0$. For the first, sufficiency follows from Theorem 6. For $n\geq2$, let $$g_\pm=(\lvert 0^n\rangle\pm\lvert 1^n\rangle)/\sqrt2,\qquad
\eta_q=q\lvert g_+\rangle\langle g_+\rvert+(1-q)\lvert g_-\rangle\langle g_-\rvert,\qquad 0<q<1.$$ Every nonempty proper marginal has purity $1/2$, and $P=\operatorname{tr}\eta_q^2=q^2+(1-q)^2$. Writing $e_n=1/2-2^{-n}$, the known pure GHZ value \[6\], one obtains $$F_n(\eta_q)=\tfrac12+2^{-n}P,\qquad U_n(\eta_q)=Pe_n,
\qquad\mathcal C_n^\cap(\eta_q)=e_n.$$ The displayed ensemble attains $e_n$ and the sufficient bound equals $e_n$, proving the last identity. Its deficit-to-impurity ratio is exactly $e_n$. Thus sharpness holds at every purity in $[1/2,1)$, not just at one state. The case $n=1$ is trivial. At $q=1/2$, $\eta_q$ is fully separable and its convex roof is zero, illustrating why concave-roof sharpness cannot be transferred to the convex roof.

The present results leave $1/8\leq c_3^\cup\leq3/8$ unresolved. We claim neither the optimal fixed-size convex coefficient nor the optimal nonlinear, state-dependent correction.

## Checks, scope and provenance

The accompanying standard-library Python verifier uses exact rational arithmetic. It checks normalisation, the rank-two support projector, all eight subsystem purities and all eight local-SWAP outcome probabilities. It calculates the latter directly from permutations on two copies, rather than from the partial-trace implementation. It also checks rational points in the near-pure family and a two-Bell-pair core. The recorded result is `PASS`. A separately implemented Pauli-basis checker confirms the original certificates. A SymPy 1.14.0 checker additionally checks the extension identities, arbitrary-phase GME marginals, noisy-family formulas, GHZ saturation and perturbation radius, with semantic negative controls. None of these algebraic checks replaces the support, optimisation or concurrence arguments. These are finite arithmetic checks; the support and variance arguments above supply the proofs over all ensembles and all dimensions.

Sanity checks include the pure endpoints $\epsilon=0,1$, where the gap is zero; the maximally mixed spectator $\epsilon=1/2$, where the gap is $1/16$; and a pure product core $e=0$, for which both roofs and $U$ are zero. The original spectator example is biseparable; Theorem 9 removes that restriction. Total CE is the quantity at issue; excluding an uncorrelated spectator would add a hypothesis absent from the universal claim.

The statement audited is the published 2024 paper, also available as arXiv:2112.04333v8 (revised 2 January 2025). A targeted search on 13 October 2026 inspected the source, its version history, related CE papers, and search results for an upper-bound correction or spectator counterexample. No earlier resolution was located in those inspected materials. This bounded search does not establish priority or exclude an unindexed result. The note and verifier were produced in an AI-assisted session; there has been no independent external review or proof-assistant formalisation. No unresolved analytic step is used in the stated refutation.

## References {#references .unnumbered}

#### \[1\]

Wootters, W. K. (1998). Entanglement of formation of an arbitrary state of two qubits. *Physical Review Letters, 80*, 2245--2248. <https://doi.org/10.1103/PhysRevLett.80.2245>.

#### \[2\]

Beckey, J. L., Pelegrí, G., Foulds, S., and Pearson, N. J. (2023). Multipartite entanglement measures via Bell basis measurements. *Physical Review A, 107*, 062425. <https://doi.org/10.1103/PhysRevA.107.062425>.

#### \[3\]

Vairogs, C., Hermes, S., and Leditzky, F. (2026). Localizing multipartite entanglement with local and global measurements. *Quantum, 10*, 2007. <https://doi.org/10.22331/q-2026-02-23-2007>.

#### \[4\]

Foulds, S., Prove, O., & Kendon, V. (2024). Generalizing multipartite concentratable entanglement for practical applications: mixed, qudit and optical states. *Philosophical Transactions of the Royal Society A, 382*(2287), 20240411. <https://doi.org/10.1098/rsta.2024.0411>. Version inspected: <https://arxiv.org/abs/2112.04333v8>.

#### \[5\]

Beckey, J. L., Gigena, N., Coles, P. J., & Cerezo, M. (2021). Computable and operationally meaningful multipartite entanglement measures. *Physical Review Letters, 127*(14), 140501. <https://doi.org/10.1103/PhysRevLett.127.140501>.

#### \[6\]

Schatzki, L., Liu, G., Cerezo, M., & Chitambar, E. (2024). Hierarchy of multipartite correlations based on concentratable entanglement. *Physical Review Research, 6*(2), 023019. <https://doi.org/10.1103/PhysRevResearch.6.023019>.
