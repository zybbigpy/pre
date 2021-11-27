---
marp: true
theme: gaia
footer: 'Wangqian Miao 11/26/2021'
paginate: true
date: 11/26/2021
---

# Surface State of Bi$_2$Se$_3$

## Von Neumann Lattice Basis

Two sets of coordinates: $(\xi, \eta)$ [relative coordinates]. $(X,Y)$[guiding center coordinates]

$$
\begin{aligned}
\xi &= (eB)^{-1}(p_y+eA_y)\\
\eta &=-(eB)^{-1}(p_x+eA_x)\\
X& = x-\xi\\
Y &= y-\eta\\
\end{aligned}
$$
The one body Hamiltonian can be written as
$$
H_0 = \frac{1}{2}m\omega_c^2(\xi^2+\eta^2)
$$
where $\omega_c=eB/m$. $H_0$ is independent of $X, Y$.(corresponds to the degenaracy of Landau level)
$$
H_0\ket{f_\ell}=E_\ell\ket{f_\ell}, E_\ell = \hbar\omega_c (\ell+\frac{1}{2})
$$


---
## hahah
Use coherent state defined by 
$$
(X+\mathrm{i}Y) \ket{\alpha_{mn}} = z_{mn}\ket{\alpha_{mn}},z_{mn} = (m\omega_x+n\omega_y)
$$
$$
\begin{array}{c}
\left|\alpha_{m n}\right\rangle=e^{i \pi(m+n+m n)+\sqrt{\pi}\left(A^{\dagger} \frac{z_{m n}}{a}-A \frac{z_{m n}^{*}}{a}\right)}\left|0\right\rangle \\
A=\frac{\sqrt{\pi}}{a}(X+\mathrm{i} Y), \left[A, A^{\dagger}\right]=1, a= \sqrt{\frac{2\pi\hbar}{eB}}
\end{array}
$$
where $m,n$ are integers and $\omega_x, \omega_y$ are <font color=red>complex numbers</font> satisfy
$$
\Im[\omega_x^*\omega_y] =1
$$
$z_{mn}$ is a point on the lattice site in the complex plane with an area of the unit cell is $a^2$. We call this lattice the `magnetic von Neumann lattice` which is parameterized by $\tau = -\omega_x/\omega_y$.

- For $\tau = i$, square lattice
- For $\tau = e^{i2\pi/3}$, triangular lattice.



---

<!-- ---
## Lattice Structure of Bi$_2$Se$_3$

hello




---
## DFT Band Structure

<!-- ![bg right w:15cm](band_dft.png) -->
some description here.




---
## DOS Analysis



---
## Low Energy Effective TB Model



---
## Surface State



---
## Togological Index -->