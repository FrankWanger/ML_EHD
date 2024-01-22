## ML-EHD
Predicting with pre-trained model for PLGA particle diameter

##  Steps for using this model
1. Install python dependencies (specified in the notebook file)
2. Populate experiments in validation.csv similar to the example entry
3. Run through the jupyter notebook. The results will be automatically saved to the original file.

## Variable and meanings in the data file
| Name          | Meaning                                                       | Unit    |
|---------------|---------------------------------------------------------------|---------|
| Polymer_Conc  | Concentration of the PLGA polymer in the solution             | w/v%     |
| Solvent       | Solvent used in electrospray solution                         | -       |
| FR            | Flow rate of the syringe pump                                 | mL/h    |
| Vol           | Voltage                                                       | kV      |
| Distance      | Collection distance, the distance between gauge and collector | mm      |
| Gauge         | Gauge size (needle size)                                      | mm      |
| Diameter_Mean | Diameter of the particle                                      | micrometers |

For Solvents, please use the following Abbreviations:
- DMF 
- DMA 
- DCM 
- Acetone 
- ACN 
- TFE 
- DMC 
- Chloroform 
- Toluene 
- AceticAcid 
- EA 
- THF 
- MeOH 
- EtOH 
- Water

## Data Access
Data used for training this model has been uploaded on [FigShare](https://doi.org/10.6084/m9.figshare.25040459.v1)

## Citation
Wang, F. et al. Machine learning predicts electrospray particle size. Materials & Design 219, 110735 (2022). https://doi.org/10.1016/j.matdes.2022.110735

## References
The original data was sourced from the following publications:

1. Morais, A. Í. S. et al. Fabrication of Polymeric Microparticles by Electrospray: The Impact of Experimental Parameters. Journal of Functional Biomaterials 11, 4 (2020).
2. Narváez-Muñoz, C., Ryzhakov, P. & Pons-Prats, J. Determination of the Operational Parameters for the Manufacturing of Spherical PVP Particles via Electrospray. Polymers 13, 529 (2021).
3. Smeets, A., Clasen, C. & Van den Mooter, G. Electrospraying of polymer solutions: Study of formulation and process parameters. European Journal of Pharmaceutics and Biopharmaceutics 119, 114–124 (2017).
4. Kibler, E. et al. Electrosprayed poly(lactic-co-glycolic acid) particles as a promising drug delivery system for the novel JNK inhibitor IQ-1. European Polymer Journal 127, 109598 (2020).
5. Dong, X., Zheng, Y., Xin, B., Liu, H. & Lin, L. Effects of Electric Filed on Electrospray Process: Experimental and Simulation Study. Fibers Polym 21, 2695–2705 (2020).
6. Faramarzi, A.-R., Barzin, J. & Mobedi, H. Effect of solution and apparatus parameters on the morphology and size of electrosprayed PLGA microparticles. Fibers Polym 17, 1806–1819 (2016).
7. Karimi Zarchi, A. A. et al. Development and optimization of N-Acetylcysteine-loaded poly (lactic-co-glycolic acid) nanoparticles by electrospray. International Journal of Biological Macromolecules 72, 764–770 (2015).
8. Lu, J., Hou, R., Yang, Z. & Tang, Z. Development and characterization of drug-loaded biodegradable PLA microcarriers prepared by the electrospraying technique. International Journal of Molecular Medicine 36, 249–254 (2015).
9. Chen, J.-M., Liu, K.-C., Yeh, W.-L., Chen, J.-C. & Liu, S.-J. Sustained Release of Levobupivacaine, Lidocaine, and Acemetacin from Electrosprayed Microparticles: In Vitro and In Vivo Studies. Int J Mol Sci 21, 1093 (2020).
10. Bohr, A., Kristensen, J., Stride, E., Dyas, M. & Edirisinghe, M. Preparation of microspheres containing low solubility drug compound by electrohydrodynamic spraying. International Journal of Pharmaceutics 412, 59–67 (2011).
11. Nath, S. D., Son, S., Sadiasa, A., Min, Y. K. & Lee, B. T. Preparation and characterization of PLGA microspheres by the electrospraying method for delivering simvastatin for bone regeneration. International Journal of Pharmaceutics 443, 87–94 (2013).
12. Zarrabi, A., Vossoughi, M., Alemzadeh, I. & Chitsazi, M. R. Monodispersed Polymeric Nanoparticles Fabrication by Electrospray Atomization. International Journal of Polymeric Materials and Polymeric Biomaterials 61, 611–626 (2012).
13. Zhao, W. et al. Fabrication and characterization of dual drug-loaded poly (lactic-co-glycolic acid) fiber-microsphere composite scaffolds. International Journal of Polymeric Materials and Polymeric Biomaterials 68, 375–383 (2019).
14. Anda, D. A. R. de, Ohannesian, N., Martirosyan, K. S. & Chew, S. A. Effects of solvent used for fabrication on drug loading and release kinetics of electrosprayed temozolomide-loaded PLGA microparticles for the treatment of glioblastoma. Journal of Biomedical Materials Research Part B: Applied Biomaterials 107, 2317–2324 (2019).
15. Almería, B., Deng, W., Fahmy, T. M. & Gomez, A. Controlling the morphology of electrospray-generated PLGA microparticles for drug delivery. Journal of Colloid and Interface Science 343, 125–133 (2010).
16. Almería, B. & Gomez, A. Electrospray synthesis of monodisperse polymer particles in a broad (60nm–2μm) diameter range: guiding principles and formulation recipes. Journal of Colloid and Interface Science 417, 121–130 (2014).
17. Aragón, J., Salerno, S., De Bartolo, L., Irusta, S. & Mendoza, G. Polymeric electrospun scaffolds for bone morphogenetic protein 2 delivery in bone tissue engineering. Journal of Colloid and Interface Science 531, 126–137 (2018).
18. Xie, J., Lim, L. K., Phua, Y., Hua, J. & Wang, C.-H. Electrohydrodynamic atomization for biodegradable polymeric particle production. Journal of Colloid and Interface Science 302, 103–112 (2006).
19. Ding, L., Lee, T. & Wang, C.-H. Fabrication of monodispersed Taxol-loaded particles using electrohydrodynamic atomization. Journal of Controlled Release 102, 395–413 (2005).
20. Bohr, A. et al. Pharmaceutical microparticle engineering with electrospraying: the role of mixed solvent systems in particle formation and characteristics. J Mater Sci: Mater Med 26, 61 (2015).
21. Bohr, A., Kristensen, J., Dyas, M., Edirisinghe, M. & Stride, E. Release profile and characteristics of electrosprayed particles for oral delivery of a practically insoluble drug. J R Soc Interface 9, 2437–2449 (2012).
22. Enayati, M., Ahmad, Z., Stride, E. & Edirisinghe, M. Size mapping of electric field-assisted production of polycaprolactone particles. J R Soc Interface 7, S393–S402 (2010).
23. Shams, T. et al. Electrosprayed microparticles for intestinal delivery of prednisolone. Journal of The Royal Society Interface 15, 20180491 (2018).
24. Hong, Y., Li, Y., Yin, Y., Li, D. & Zou, G. Electrohydrodynamic atomization of quasi-monodisperse drug-loaded spherical/wrinkled microparticles. Journal of Aerosol Science 39, 525–536 (2008).
25. Bae, J., Lee, J. & Kim, S. H. Effects of polymer properties on jetting performance of electrohydrodynamic printing. Journal of Applied Polymer Science 134, 45044 (2017).
26. Imanparast, F. et al. Preparation, optimization, and characterization of simvastatin nanoparticles by electrospraying: An artificial neural networks study. Journal of Applied Polymer Science 133, (2016).
27. Park, C. H. & Lee, J. Electrosprayed polymer particles: Effect of the solvent properties. Journal of Applied Polymer Science 114, 430–437 (2009).
28. Wang, L., Zhang, Q., Wang, X., Liu, J. & Yang, J. The preparation and forming mechanism of the red blood cell-shaped microspheres via electrospraying. Journal of Applied Polymer Science 122, 2552–2556 (2011).
29. Nguyen, T. T. & Jeong, J. Development of a single-jet electrospray method for producing quercetin-loaded poly (lactic-co-glycolic acid) microspheres with prolonged-release patterns. Journal of Drug Delivery Science and Technology 47, 268–274 (2018).
30. Pan, X., Liu, X., Zhuang, X., Liu, Y. & Li, S. Co-delivery of dexamethasone and melatonin by drugs laden PLGA nanoparticles for the treatment of glaucoma. Journal of Drug Delivery Science and Technology 60, 102086 (2020).
31. Si, S., Li, H. & Han, X. Sustained release olmesartan medoxomil loaded PLGA nanoparticles with improved oral bioavailability to treat hypertension. Journal of Drug Delivery Science and Technology 55, 101422 (2020).
32. Roine, J., Murtomaa, M. & Salonen, J. Influence of parallel nozzle electroencapsulation parameters on microcapsule properties – A case study using the Taguchi robust design method. Journal of Electrostatics 90, 91–105 (2017).




Copyright (C) Fanjin Wang 2021 - All Rights Reserved
Fanjin.Wang.20@ucl.ac.uk
