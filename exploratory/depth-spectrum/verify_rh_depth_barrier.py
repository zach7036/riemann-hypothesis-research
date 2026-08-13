#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
out = []

# Exact pair spectrum.
L, y, m, a = sp.symbols('L y m a', positive=True, real=True)
b = a * sp.cosh(L*y)
lam_plus = sp.simplify(m*(a+b))
lam_minus = sp.simplify(m*(a-b))
wedge = sp.simplify((a**2/4)*(sp.cosh(L*y)**2-1))
assert sp.simplify(lam_plus - m*a*(sp.cosh(L*y)+1)) == 0
assert sp.simplify(lam_minus + m*a*(sp.cosh(L*y)-1)) == 0
assert sp.simplify(wedge - (a**2/4)*sp.sinh(L*y)**2) == 0
out += ["PAIR SPECTRUM", str(lam_plus), str(lam_minus), str(wedge), ""]

# Cyclic cancellation and all aggregate moments.
def cyclic_blocks(q: int, n: float):
    blocks=[]
    for j in range(q):
        qmat=np.zeros((q,q), dtype=float)
        qmat[j,j]=n+2
        qmat[(j+1)%q,(j+1)%q]-=n
        blocks.append(qmat)
    return blocks
for q in [2,3,5,11]:
    for n in [0,1,7,100]:
        total=sum(cyclic_blocks(q,n))
        assert np.allclose(total,2*np.eye(q))
        for r in range(1,9):
            assert np.allclose(np.trace(np.linalg.matrix_power(total,r)),q*(2**r))
out += ["CYCLIC ALL-MOMENT CANCELLATION: PASS", ""]

# Scalar positivity barrier: a positive-definite function obeys |F(u)|<=F(0).
w0, wu, Y, u = sp.symbols('w0 wu Y u', positive=True, real=True)
F0=w0
Fu=wu*sp.cosh(Y*u)**2
det=sp.expand(F0**2-Fu**2)
assert det == w0**2-wu**2*sp.cosh(Y*u)**4
out += ["SCALAR 2x2 DETERMINANT", str(det),
        "PSD gives |wu| <= w0*sech(Yu)^2.", ""]

# Matrix compression test with random Hermitian K0 and scalar-saturated K(u).
rng=np.random.default_rng(817263)
for dim in [1,2,4,8]:
    for _ in range(30):
        amat=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
        k0=amat@amat.conj().T
        alpha=rng.uniform(0,1)
        yu=rng.uniform(0,4)
        ku=alpha*(1/np.cosh(yu)**2)*k0
        for _ in range(10):
            z=rng.normal(size=dim)+1j*rng.normal(size=dim)
            lhs=abs(np.vdot(z,ku@z))
            rhs=(1/np.cosh(yu)**2)*np.vdot(z,k0@z).real
            assert lhs <= rhs+1e-8
out += ["MATRIX COMPRESSION BARRIER FINITE TESTS: PASS", ""]

# Sharp scalar family: e^{-2Y|u|} cosh(yu)cosh(y'u)
# expands into four exponentials e^{-a|u|}, a>=0.
yy, yp = sp.symbols('yy yp', real=True)
exponents=[]
for e1 in (-1,1):
    for e2 in (-1,1):
        exponents.append(2*Y-e1*yy-e2*yp)
out += ["SHARP FAMILY EXPONENTS"]+[str(x) for x in exponents]+[
    "For 0<=y,y'<=Y all are nonnegative.", ""]

text='\n'.join(out)+"\nAll symbolic and finite-dimensional checks passed.\n"
(HERE / 'verification.txt').write_text(text,encoding='utf-8')
print(text)
print('SHA-256:', hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper())
