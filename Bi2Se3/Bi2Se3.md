---
marp: false
_class: lead
paginate: true
backgroundColor: #fff
date: 123
---

# MTRL 279: First Principle study of Bi$_2$Se$_3$ and its Surface State
- Wangqian Miao
- Materials Dept, UCSB
- 11/26/2021

---

## Band Structure from DFT

- SOC calculation needed, non magnetic.
- PBE Functional (Band Gap problem at $\Gamma$ point, HSE?)
- Consistent well with Nature Physics **5**, 438–442 (2009)
- Conclusion: Bi$_2$Se$_3$ is a **Bulk Insulator**.

```bash
ISPIN  = 2
#NBANDS = 30 #Non SOC
NBANDS = 60  #If add SOC

LSORBIT = .TRUE.
LMAXMIX = 4
ICHARG  = 11
ISYM    = -1 
```
![bg right w:15cm](band_dft.png)



---


## Effective Tight Binding Hamiltonian

*Physicists prefer a concrete Hamiltonian!*

Construct Low energy TB model:
- Analyze the band component near Fermi level, `LORBIT=11` in VASP.
- For Bi$_2$Se$_3$, the contribution near
Fermi level mainly from $p$ orbitals from each atom.
- ⚠️Help determine projection orbitals in Wannier90.



![bg right w:15cm](pdos.png)

---
- ⚠️Use Wannier90 to construct MLWF.
  - `num_bands` same as `NBANDS` in VASP.
  - Tricky parameters: `dis_win_min`,  `dis_win_max`,  `dis_froz_min`, `dis_froz_max` .
  - check spread of wannier functions.
- ⚠️Check consistency between DFT and TB by plotting Bands.

Blue Lines from DFT. Red Dots from TB.


![bg right w:15cm](band.png)

---

## Fermi Arc, Spin Texture, Surface State

Fortunately, *WannierTools* can help!😀

We find Dirac Cone in surface DOS! 
- Study (0,0,1) surface
  ```Fortran
  SURFACE !define two k vecs
  1 0 0
  0 1 0
  ```
- Why Dirac type? (should be checked through $k \cdot p$ theory)
- Bulk insulator, However surface conducting states exist!

![bg right w:15cm](surfdos_l.png)

---

We find Dirac Cone in surface DOS! 
- Study (0,0,1) surface
  ```Fortran
  SURFACE !define two k vecs
  1 0 0
  0 1 0
  ```
- Why Dirac type? (should be checked through $k \cdot p$ theory, symmetry protected)
- Bulk insulator, However **surface conducting states exist**!
- Fermi arc, spin texture (We have SOC).

![bg right w:15cm](arcspin.png)

---
## Topological Indices
*Symmetry plays an important role!*

$Z_2$ Topological Invariants:

- Theory: *Fu and Kane, Phys. Rev. B **76**, 045302*.
- Numerics: *Yu, Dai and etc, Phys. Rev. B **84**, 075119*.
- Wannier Charge Center at TR Invariant $k$ points shows $Z_2=(1;000)$.
- Conclusion: Bi$_2$Se$_3$ is a **Strong 3D TI**.


![bg right w:15cm](topo_index.png)

---

## How to study a normal TI?



For Computational Material Scientists:
1. DFT calculation to determine low energy state. (Most of them need SOC). 
2. ⚠️Analyze the band components near Fermi level.
3. ⚠️*Most Tricky*: Construct low energy TB by wannier90 through MLWF algorithm. 
4. ⚠️Check the consistency between DFT and TB.
5. Study topological properties of the TB Hamiltonian.
6. 🎈Predict experiments results. such as Surface state, Fermi Arc, Spin texture...

For Physicists, several more steps,
1. Symmetry Analysis, construct low energy $k \cdot p$ model.
2. Topological classification.

