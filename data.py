# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:07:51 2019

@author: Rashid Haffadi
"""

"""Every Dataset Type Should Inherent Dataset Class

"""

class Dataset():
    def __init__(self, *args, **kwargs):
        pass
    
    def __len__(self):
        pass
    
    def __getitem__(self):
        pass
      
class IterableDataset(Dataset):
    def __init__(self, *args, **kwargs):
        pass
    
    def __iter__(self):
        pass 
    #return iter(elements)
        
class Sampler(Dataset):
    pass
        
class Dataloader():
    def __init__(self, dataset:Dataset, bs:int, shuffle:bool=False):
        pass
    
    def __iter__(self):
        pass
    