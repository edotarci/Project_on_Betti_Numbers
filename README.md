# Computational and combinatorial methods for Betti Numbers of weighted trees.
_Page under development_

- Results: I developed, together with Lorenzo Varesio, an algorithm in Python, based on a combinatorial approach, to evaluate Betti Numbers for weighted and non-weighted chains.
- Supervisors: prof. Roberto Notari (PoliMi) and prof. Paolo Lella (PoliMi).

The idea of the project is to study the behavior of Betti numbers in weighted trees as the weights' values and their positions vary. Our contribution has specifically focused on studying chain graphs using computational methods in Python based on combinatorial considerations. 

The notions and references, divided by topic, we had to delve into to proceed in the project are:
- General (Discrete Mathematics and Algebra): Definition of a graph, weighted graph, and tree, rings, modules, polynomial ideals.
  https://bit.ly/Notes_discMath_Notari, https://rb.gy/67f9a.
  
- Specific: Edge Ideal of a weighted and unweighted graph, minimal free resolution of an ideal, Betti Numbers.
  https://arxiv.org/pdf/math/0410107.pdf, https://rb.gy/u7wur.

To confirm our results, develop conjectures and analyse Betti numbers we used the software system Macaulay2.(http://www2.macaulay2.com/Macaulay2/, https://www.unimelb-macaulay2.cloud.edu.au/#home) 

General idea of the algorithm: the code takes the length of the chain as an input (and the wieghts of the edges) and returns the Betti numbers of the chain. To do so, instead of evaluating matrixes, lists of zeros and ones of progressive length are built and discarded according to precise rules. 
Precise rules (and relative proof) will be added to this page when ready to be shared.

  
