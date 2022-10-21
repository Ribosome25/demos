# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""
from rdkit import Chem
#%%
suppl = Chem.SDMolSupplier('March2012_2d/March2012_2d_dos.sdf')
for mol in suppl:
    meta = mol.GetPropsAsDict()  # get properties as a dict.
    print(meta)
    smiles = Chem.MolToSmiles(mol)
    print(smiles)
    break
#%% Show the Mol image
from rdkit.Chem import Draw
import PIL
fig = Draw.MolToImage(mol)
fig.show()
#%% Generate a FP
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs
import numpy as np

fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=256)
array = np.zeros((0, ), dtype=np.int8)
DataStructs.ConvertToNumpyArray(fp, array)

#%% Another way is to read from SMILES
mol = Chem.MolFromSmiles("S(SC1=Nc2ccccc2S1)C3=Nc4ccccc4S3")
