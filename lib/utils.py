'''
Copyright (C) Fanjin Wang 2021 - All Rights Reserved
'''

import pandas as pd 
import numpy as np
import pickle

def load_predict(modelpath='Data/model.pkl',datapath='Validation.csv'):
    with open(modelpath, "rb") as f:
        Model = pickle.load(f)

    fingerprint_file = Model['sol_feat']
    sol_list = ['DMF','DMA','DCM','Acetone','ACN','TFE','DMC','Chloroform','Toluene','AceticAcid','EA','THF','MeOH','EtOH','Water']
    # Data Loading 
    DB = pd.read_csv(datapath)
    Polymer_wt = DB.iloc[:,0]
    DB['Polymer_wt'] = Polymer_wt
    Processing_Params = DB.iloc[:,1:]

    X_raw = Processing_Params.drop(columns=['Diameter_Mean']).values.tolist()
    FPs = []
    for entry in X_raw:
        #Find featurization by index in the solvent list
        FP = fingerprint_file[sol_list.index(entry[0])]
        entry.pop(0)
        FPs.append(FP)

    #Experiment Feature Standardizing
    X_std = Model['feature'].transform(X_raw)
    FPs = Model['fingerprint'].transform(FPs)
    
    #Fingerprint Scaling
    FPs = FPs/np.sqrt(len(FPs[0]))

    #Concatenate Other Featrues with FPs
    X = np.block([X_std,FPs])
    y_pred = Model['model'].predict(X)
    return X,y_pred

def save_pred(y_pred,datapath='val.csv',verbose = 1):
    DB = pd.read_csv(datapath)
    if verbose > 0:
        print(DB)
    DB['Diameter_Mean']=y_pred
    DB.to_csv(datapath,index=False)