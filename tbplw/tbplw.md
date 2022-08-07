---
marp: true
_class: lead
paginate: true
backgroundColor: #fff
math: mathjax
---
<style>
section { 
    font-size: 22px; 
}
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>
<style scoped>section { font-size: 30px; }</style>

# Atomic Planewave Expansion for Subband Strucuture Calculations in Moiré Systems

*Wangqian Miao, supervised by Prof. Xi Dai.*
*Materials Dept, UCSB.*
*GS$^3$ Seminar, 10th, Aug, 2022*

---

# Introduction
<!-- _footer: 'Cao, Nature, 2018' -->


Twited Bilayer Graphene (TBG)

In this presentation:
- How to calculate the band structure

---
# Structure of Twisted Bilayer Graphene
<!-- _footer: 'Kane, PRB, 2013' -->


Start from a A-A stacking Bilayer Graphene and rotate.
- AA stacking point: $D_3$ point group symmetry.
- Hexagonal center: $D_6$ point group symmetry.

A series of rotation angles will genarate a commusurate strucuture:

- magic angle: around 1$^\circ$.
  
---

# Moire Pattern

* When the rotation angle is small, moire pattern emergies.
* Extremlly large unit cell.
* Contains more than 10,000 atoms in a unit cell at first magic angle.
* Challege:
    - How to determine the band strucuture?
    - How to build an effective model Hamiltonian?
  
![bg fit right](moire_30_realspace.png)

---
# Band Structure Calculations
<!-- _footer: 'B&M, PNAS, 2010. Koshino, PRB, 2015, NJP, 2015, PRX, 2017.' -->

- **Density Functional Theory**
  - Accurate but hard to perform
- **Tight Binding**
  - Slater Koster Scheme
  - Ab initio Scheme
- **Continuum Model**
  - Rafi Bistritzer and Allan H. MacDonald.
  - Simple but caputure the most important physics.
  - Conserve highest symmetry of the system.
  
Expectation from Physicists
* Not only good band structures but also effective Hamiltonian.

---

# A Textbook Formalism: Slater Koster Tight Binding

* Construct Bloch wave function:
$$
\psi(\mathbf{k}) = \frac{1}{\sqrt{N}} \sum_{\mathbf{R}}e^{\mathrm{i}\mathbf{k}\cdot{(\mathbf{R}_{\mathrm{I}}+\tau_{i_\alpha})}} \phi_{p_z}(\mathbf{r}-\mathbf{R}_{\mathrm{I}}-\tau_{i_\alpha})
$$
* Hopping integral determined by SK-formula:
$$
t(\mathbf{r}) = -V_\pi\left(1-\frac{r_z^2}{r^2}\right)-V_\sigma\frac{r_z^2}{r^2},
$$
where $r_z = \mathbf{r} \cdot \mathbf{e}_z, V_\pi = V_\pi^0 e^{-(r-a_0)/r_0}, V_\sigma = V_\sigma^0 e^{-(r-d_0)/r_0}.$
* $\approx 10,000$ atoms. TB matrix $10,000 \times 10,000$. 
  * A long time to diagonalization, but practical. Lancoz algorithm.
  * Hard to perform further calculation.

---
# Continuum Model
Some Key ideas:


* Construct Bloch wavefunction for each layer:
$$
  \begin{eqnarray}
    \psi_{\mathbf{k},\alpha}^{(1)}(\mathbf{r}) &= \frac{1}{\sqrt{N}} \sum_{\mathbf{r}u_\alpha} \mathrm{e}^{\mathrm{i} \mathbf{k} \cdot \mathbf{r}^{(1)}_\alpha} \phi_{p_z}(\mathbf{r}-\mathbf{r}^{(1)}_\alpha), \\
    \psi_{\mathbf{p},\beta}^{(2)} (\mathbf{r})&= \frac{1}{\sqrt{N}} \sum_{\mathbf{r}u_\beta} \mathrm{e}^{\mathrm{i}\mathbf{p}\cdot \mathbf{r}^{(2)}_\beta} \phi_{p_z}(\mathbf{r}-\mathbf{r}^{(2)}_\beta).
  \end{eqnarray}
$$
* Fourier Transform the hopping integral $\rightarrow$ momentum conservation law of moire system.
$$
\boxed{\mathbf{k}=\mathbf{p}-m_1 \mathbf{G}_1-m_2 \mathbf{G}_2,}
$$

---

# Continuum Model (Cont'd)

Some Key ideas:
* Intralayer coupling $H$:
  * Low energy physics comes from Dirac cones of monolayer Graphene.
  * Mini valley concept.
* Interlayer coupling $U$:
  * Conserve three largest $\mathbf{k}-\mathbf{p}$ coupling using symmetry analysis
  * Varies smoothly in the moire scale.

![bg 65% right](cont.svg)

---
# K Space Picture

![center](tbg.svg)

---
# Tight Binding Planewave Expansion: Motivation

* Two kinds of periodicity in moire system.
  * Moire Scale periodicity
    - Full Tight Binding Description
  * Atomic Scale periodicity
    - Spirit of Continuum Model
*  *Interplay between two kinds of periodicity in moire system*!
  $$
  \boxed{
  \psi_{\alpha, n}(\bar{\mathbf{k}}) = \frac{1}{\sqrt{N_\mathrm{m} N_\mathrm{a}}}\sum_{\mathrm{I}, i} \mathrm{e}^{ \mathrm{i}\color{red}{(\bar{\mathbf{k}}+\mathbf{G}_n})\mathbf{r}_{\mathrm{I} i \alpha}} \phi_{p_z}(\mathbf{r}-\mathbf{r}_{\mathrm{I} i \alpha}).
  }
  $$
* The matrix element of the Hamiltonian $H_{\alpha n, \beta m}$:

$$
\begin{equation}
\begin{aligned}
  &\bra{\psi_{\alpha,n}(\bar{\mathbf{k}})}{\hat{H}}\ket{\psi_{\beta,m}(\bar{\mathbf{k}})} \\
=& \frac{1}{N_\mathrm{m} N_\mathrm{a}} \sum_{\mathrm{I} \mathrm{I},ij} t(\mathbf{r}_{\mathrm{I} i \alpha}-\mathbf{r}_{\mathrm{I} j \beta})
\mathrm{e}^{-\mathrm{i}(\bar{\mathbf{k}}+\mathbf{G}_n)\mathbf{r}_{\mathrm{I} i \alpha}} \mathrm{e}^{\mathrm{i}(\bar{\mathbf{k}}+\mathbf{G}_m)\mathbf{r}_{\mathrm{I} j \beta}} \\
=&\frac{1}{N_\mathrm{a}} \sum_{ij} \color{red}{\mathrm{e}^{-\mathrm{i} \mathbf{G}_n \tau_{i\alpha}}} \color{blue}{\mathrm{e}^{-\mathrm{i} \bar{\mathbf{k}} (\bar{\tau}_{i\alpha, j\beta})} 
t(\bar{\tau}_{i\alpha, j\beta})} \color{red} {\mathrm{e}^{\mathrm{i} \mathbf{G}_m \tau_{j\beta}}}. \\
\label{eq:ele}
\end{aligned}
\end{equation}
$$
---
# Tight Binding Planewave Expansion

- A more compact expression
$$
\boxed{
\begin{equation}
\begin{aligned}
\mathbf{H}_{\alpha\beta} &= \frac{1}{N_{\mathrm{a}}}\mathbf{X}^\dagger_{\alpha} \mathbf{T}_{\alpha\beta} \mathbf{X}_{\beta},
\label{eq:Hmat}
\end{aligned}
\end{equation}
}
$$
the corresponding matrix elements:
$$
\begin{equation}
\begin{aligned}
(\mathbf{X_\alpha}^\dagger)_{n,i}  &=\mathrm{e}^{\mathrm{i}\mathbf{G}_n\tau_{i\alpha}},\\
(\mathbf{T_{1\alpha \beta}})_{i, j} &= \mathrm{e}^{-\mathrm{i} \bar{\mathbf{k}} (\bar{\tau}_{i\alpha, j\beta})},\\ 
(\mathbf{T_{2\alpha \beta}})_{i, j} &=t(\bar{\tau}_{i\alpha, j\beta}),\\
(\mathbf{T_{\alpha \beta}})_{i, j} &= \mathbf{T}_1 * \mathbf{T}_2.
\end{aligned}
\end{equation}
$$
* Concrete meaning:
  * $\mathbf{T}_1$: hopping phase. $\mathbf{T}_2$ hopping integral. 
  * $\mathbf{T}_1*\mathbf{T}_2$:  <font color=red>**Full TB matrix**</font>!
  * $\mathbf{X}$: Planewave projector.

---

# Why Tight Binding Planewave should be Fast ?

* Benchmark with *WannierTools*.
* No need to diagonalize *full TB*, but the projected Hamiltonian.
  * (num of  atoms, num of atoms) $\rightarrow$ ($4\times$ num of $\mathbf{G}$, $4\times$ num of $\mathbf{G}$) per valley.
  * MATBG: (11164, 11164) $\rightarrow$ (244, 244) per valley.
* The construction of *Planewave projector* $\mathbf{X}$ and *hopping integral* $\mathbf{T}_2$ is only once!
* $\mathbf{T}_1 * \mathbf{T}_2$ element-wise production.
![bg fit right](benchmark.png)


---
# Band Strucuture Results

---

# Detailed Descripstion of Moire Potential


---

# Some Comments 🤔 

- How to design $\mathbf{T}_2$?
  * Slater Koster
    * Setup neighbours using KDTree. 
    * `Numpy` broadcasting.
  * Ab initio TB.
- Only the band strucute of TBG?
  * The projection process is general!
  * Moire phonon bands, relaxed moire strucuture.
- Further Application?
  * Electron-Electron intetaction
  * Electron-Phonon interaction (Frozen Phonon.)
---
# Thank You ! 🎉🎉🎉

*Contact me through `wmiao@ucsb.edu` for any request!*