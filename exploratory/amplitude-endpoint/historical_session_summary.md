# Historical amplitude-endpoint session summary

> [!CAUTION]
> This is an unrefereed session summary, preserved for research continuity. It is **not** a completed `lambda = 1` xi-prime theorem and it is not a proof of the Riemann Hypothesis. Claims that particular local Lean files compiled were reported in the originating session but have not been independently replayed from the files in this repository. The hostile referee report in this directory is the controlling status assessment.

The research has produced a credible new proof architecture, but not a proof of RH. The clearest advance is a simpler amplitude-based formulation that appears to remove the last analytic obstruction at exact critical bandwidth \\(\lambda=1\\).

## Starting point

Anthropic’s result is a major unconditional advance, not “67% of a proof of RH.” It certifies asymptotic lower proportions of zeros, including approximately \\(67.250\\%\\) simple and on the critical line and \\(83.625\\%\\) distinct. The remaining zeros are uncertified, not known to violate RH. Their released argument uses finite Gabor families, Hermitian inertia, and prime-side first and second moments. [Official research page](https://www.anthropic.com/research/riemann-zeta)



## Strongest new conceptual result

The existing window construction mixes two scales:

- an energy profile with width \\(L\\);
- an independently engineered edge taper with fixed microscopic width.

That mismatch creates the troublesome endpoint error.

The replacement is almost embarrassingly simple:

\\[ \boxed{\phi\_L(u)=h(u/L)} \\]

where \\(h\\) is one fixed smooth amplitude and the energy profile is \\(v=h^2\\). Then

\\[ \widehat{\phi\_L}(r)=L\widehat h(Lr). \\]

This single identity controls both sides of the proof:

- zero-side moments come from \\(h^2\\);
- prime-side end effects become tails of the single fixed transform \\(\widehat h\\).

The resulting finite-section estimate is

\\[ \left|L^{-2}\operatorname{tr}G^2-\mathcal M\right| \ll\_h (B+1)^2, \\]

instead of the released \\(L\ell\log\ell\\,B^2\\)-type loss. At \\(\lambda=1\\), the new error is smaller than the main second-trace scale by \\(O(1/L)\\).

Two independent derivations and a hostile audit found no normalization, signed-density, logarithmic-tail, Poisson, or right-end-phase flaw. This theorem is rigorous at paper level, though its full integral statement is not yet formalized in Lean.

Main report: `move37\_amplitude\_profile.md` (source file not included)

Hostile review: `hostile\_amplitude\_referee.md` (source file not included)

## Kernel-checked advances

Several important components now pass the pinned Lean kernel without `sorry`, `admit`, or new axioms.

- `BoundaryLayer.lean` (source file not included) formalizes the endpoint deweighting and two-limit squeeze. SHA-256: `5E448B13255BC1D237EC1E7DBDD1F673D888BEFA0A3A1BB9F18551F38D381C8E`.
- `AmplitudeProfile.lean` (source file not included) exactly in the existing parameter system, proves Fourier dilation, kernel scaling, and missing-translate tail identities.
- `CriticalBandwidth.lean` (source file not included), including \\(\lambda=1\\) with a \\(T^{-1/8}\\) saving. Thus its old \\(\lambda<1\\) restriction is interface-level, not analytic.
- The earlier radial-recession and layer-cake modules prove that a homogeneous coefficient map should be bounded homogeneously and that an entry-dependent Taylor tower can be replaced by one first-variation path.
- `XiOddBridge.lean` (source file not included) zeros force an odd-multiplicity critical-line zero of \\(\xi'\\) between them.

## The log-energy compression

The three coefficient norms used in the released proof are better understood as one measure:

\\[ \mu\_T=\ell^{-2}\sum\_{n\le X}\frac{|c\_T(n)|^2}{n}        \delta\_{\log n/\ell}. \\]

The released diagonal law says these measures converge to a continuous density. Because that limit has no atom at the cutoff endpoint,

\\[ \sum\_{n\le X}|c\_T(n)|^2=o(X\ell^2), \qquad \left(\sum\_{n\le X}\frac{|c\_T(n)|}{\sqrt n}\right)^2=o(X\ell^2). \\]

This closes the fixed prime-prime estimate even at \\(X=T/(2\pi)\\). A constructed slow boundary-layer counterexample also proves that these conclusions cannot simply be substituted into the old end lemma: the end lemma itself must be replaced by the amplitude finite-section theorem.

Report: `move37\_log\_energy\_measure.md` (source file not included)

## Fixed degree-eight soft-window certificate

We no longer need a vague “take the collar sufficiently small” argument. An explicit fixed collar with \\(\eta=1/1000\\) was constructed using

\\[ q(t)=126t^5-420t^6+540t^7-315t^8+70t^9, \qquad q'(t)=630t^4(1-t)^4. \\]

The resulting amplitude is real, even, nonnegative, compactly supported, \\(C^4\\), and has four vanishing endpoint jets. Exact rational arithmetic certifies the window-functional bounds

\\[ c\_{\rm Win}>0.88368060472409212127, \\]\\[ p\_{\rm simple}>0.86836941463457173611, \qquad p\_{\rm distinct}>0.93418470731728586805. \\]

These are not yet unconditional zeta theorems; they become such only after the endpoint transfer is fully integrated.

Artifacts:

- `Fixed-collar certificate` (source file not included)
- `Exact-rational verification` (source file not included)

The original hard degree-eight profile remains computationally certified at approximately \\(86.8641500529\\%\\) simple-on-line and \\(93.4320750264\\%\\) distinct, but its complete analytic/Lean transfer is likewise unfinished.

## Short-interval work

A substantial local framework is kernel-checked:

- exact arbitrary-height phase translation;
- localized prime-prime mean values;
- two-scale parameter/grid machinery;
- sharp smooth and mixed-term freezing;
- exact kernel-edge correction;
- local \\(\xi'\\) zero counting;
- analytic odd-Rolle and multiplicity transfer.

The Fredholm calculation gives an exact-certified crossing

\\[ \lambda\_\* =0.513319759847686091\ldots \\]

for the proposed localized \\(\xi'\\) method. The numerical/Fredholm component is high confidence, but the complete short-interval analytic theorem remains unfinished.

## Literature correction

We withdrew the previously discussed exponent \\(1515/4816\\) for every-interval odd critical-line zeros. The cited Bourgain–Watt result concerns the zeta mean-square error and does not provide the literal exponent pair required by that substitution.

A defensible current exponent-pair substitution is

\\[ \frac{3943}{12011}=0.3282824077\ldots, \\]

conditional on the correctness of Khayrulloev’s general exponent-pair theorem. This correction does not affect the amplitude or critical-bandwidth arguments.

## What remains before a theorem

The remaining proof graph is finite and explicit:

1. Formalize the full finite-section interior/exterior integral theorem.
2. Supply `AdmFamily`, explicit-formula, and zero-side instances for `Params.atAmplitude`.
3. Reassemble the second trace componentwise instead of hiding everything under the old coarse common remainder.
4. Thread the homogeneous pure-density end estimate through the entire re-expansion transfer.
5. Connect the endpoint explicit-formula wrapper and fixed collared certificate.
6. Run the full pinned Lean build and independent audit.

The exact dependency map is in `move37\_endpoint\_integration\_map.md` (source file not included).

## Honest bottom line

- **PROVED/KERNEL-CHECKED:** log-energy boundary algebra, amplitude representation and scaling, explicit-formula endpoint absorption, radial recession, layer transport, and odd-\\(\xi'\\) bridge.
- **PROVED AT PAPER LEVEL:** uniform amplitude finite-section boundary theorem and the componentwise \\(\lambda=1\\) scale analysis.
- **COMPUTATIONALLY VERIFIED:** fixed-collar and hard degree-eight window constants.
- **STRONGLY SUPPORTED:** a complete fixed-amplitude \\(\lambda=1\\) two-trace theorem after the listed interface work.
- **NOT PROVED:** the integrated endpoint theorem, the proposed short-interval theorem, or the Riemann Hypothesis.

The most important organizational discovery is:

\\[ \boxed{\text{Specify one amplitude, dilate it exactly, and retain the log-energy distribution.}} \\]

That replaces several independent hypotheses and error phenomena with two simple structural objects.
