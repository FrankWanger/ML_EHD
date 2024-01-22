# Predicting with pre-trained ML model for PLGA NP diameter

##  Steps for using the model
1. Install python dependencies (specified in the notebook file)
2. Populate experiments in validation.csv similar to the example entry

3. Run through the jupyter notebook. The results will be automatically saved to the original file.

## Variable and meanings in the data file
| Name          | Meaning                                                       | Unit    |
|---------------|---------------------------------------------------------------|---------|
| Polymer_Conc  | Concentration of the PLGA polymer in the solution             | wt%     |
| Solvent       | Solvent used in electrospray solution                         | -       |
| FR            | Flow rate of the syringe pump                                 | mL/h    |
| Vol           | Voltage                                                       | kV      |
| Distance      | Collection distance, the distance between gauge and collector | mm      |
| Gauge         | Gauge size (needle size)                                      | mm      |
| Diameter_Mean | Diameter of the particle                                      | microns |
##  Supported Solvents
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

Copyright (C) Fanjin Wang 2021 - All Rights Reserved
Fanjin.Wang.20@ucl.ac.uk
