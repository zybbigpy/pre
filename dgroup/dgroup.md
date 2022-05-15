---
marp: true
_class: lead
paginate: true
backgroundColor: #fff
---

# Spin and Double Group
- Wangqian Miao
- Materials Dept, UCSB
- 05/2022



---
## Spin Degeneracy and SOC

- If We treat Spin $\mathbf{S}, S_z$ as good number 
  - Each state is doubly degenerate and is an eigenstate of $S_z = \pm\frac{1}{2}$
  - $E_{n\mathbf{k}}$: $\psi_{n,\mathbf{k},\uparrow}$, $\psi_{n,\mathbf{k},\downarrow}$.
-  If we consider Spin Orbital Coupling (SOC), $\mathbf{J} = \mathbf{L}+\mathbf{S}, J_z$ should be good quantum number 
   - The states are no longer eigenstates  of $S_z$
   - A spinor: $\psi_{n,\mathbf{k}} = a \psi_{n,\mathbf{k}, \uparrow} + b \psi_{n,\mathbf{k}, \downarrow}$. 



---

## Double Group

- The character table for angular momentum $j$:
  - $$\chi_j(\alpha) = \frac{\sin (j+1/2)\alpha}{\sin(\alpha/2)},$$ 
    $$\chi_j(\alpha+2\pi) = \chi_j(\alpha)(-1)^{2j}.$$
  
  - 🚩 If $j$ is a half integer, like spin,   rotation of $2\pi$ brings a negtive sign before the character and $4\pi$ generate the same character.

- A new Group element: $\mathcal{R}\rightarrow$ a rotation by $2\pi$.
  - 🚩 Group elements doubled: $\{E, A_i\} \rightarrow \{E, A_i, \mathcal{R}E, \mathcal{R}A_i\}$.
  - 🚩 But the nuumber of classes are not necessary to be doubled.

---

## Character Table for Double Group

- $\chi(E) = \chi(\mathcal{R}E)$ or $\chi(E) = -\chi(\mathcal{R}E)$.
- $\{A_k\}$ forms a class in the original point group, then $\{A_k\}$ and $\{\mathcal{R}A_k\}$ form 2 different classes in the double group, except:
  - $C_2, \mathcal{R}C_2$ in the same class, if and only if there is another two-fold axis ⊥ to the 2-fold axis under consideration.
- Any irreducible representation of the original group is also an irreducible representation of the double group, with the same set of characters.
- For additional double group representations: $\chi(C_k) = -\chi(\mathcal{R}C_k)$.



---



| $O^{\mathrm{D}}$ | $E$ | $\mathcal{R}E$ | $3C_{4}^2+3\mathcal{R}C_{4}^2$ | $6C_4$      | $6\mathcal{R}C_4$ | $6C_2+6\mathcal{R}C_2$ | $8C_3$ | $8\mathcal{R}C_3$ |
|------------------|-----|----------------|--------------------------------|-------------|-------------------|------------------------|--------|-------------------|
| $\Gamma_1$       | 1   | 1              | 1                              | 1           | 1                 | 1                      | 1      | 1                 |
| $\Gamma_2$       | 1   | 1              | 1                              | -1          | -1                | -1                     | 1      | 1                 |
| $\Gamma_{12}$    | 2   | 2              | 2                              | 0           | 0                 | 0                      | -1     | -1                |
| $\Gamma_{15'}$   | 3   | 3              | -1                             | 1           | 1                 | -1                     | 0      | 0                 |
| $\Gamma_{25'}$   | 3   | 3              | -1                             | -1          | -1                | 1                      | 0      | 0                 |
| $\color{red}{\Gamma_{6}}$     | 2   | -2             | 0                              | $\sqrt{2}$  | $-\sqrt{2}$       | 0                      | 1      | -1                |
| $\color{red}{\Gamma_{7}}$     | 2   | -2             | 0                              | $-\sqrt{2}$ | $\sqrt{2}$        | 0                      | 1      | -1                |
| $\color{red}{\Gamma_{8}}$     | 4   | -4             | 0                              | 0           | 0                 | 0                      | -1     | 1                 |

---

## $d$  Orbital Energy Splitting due to SOC

- $O_{h}^{\mathrm{D}} = O^{\mathrm{D}}\otimes \{E, I\}$
- For a single $d$ electron, $s=1/2$, the double group rep for the spinor:
  - $D^{1/2} = \Gamma_{6}^{+}$
- And we have:
  - $\Gamma_{12}^{+}\otimes\Gamma_{6}^{+}=\Gamma_{8}^{+}$, $\Gamma_{12}^{+}$ is original $E_g$ in $O_h$.
  - $\Gamma_{25}^{+}\otimes\Gamma_{6}^{+}=\Gamma_{7}^{+}+\Gamma_{8}^{+}$, $\Gamma_{25}^{+}$ is original $T_{2g}$ in $O_h$.
- If Crystal Field is stronger than SOC: 
  ![width:500px](soc.png) 