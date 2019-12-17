# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:37:41 2019

@author: Rashid Haffadi
"""
import numpy as np

class LossFunct():
    def __init__(self, f=metrics.relu):
        if isinstance(f, str):
            index = losses.index()
        elif isinstance():
    #return function
    def __call__(self, *args, **kwargs):
        return self.loss_func(args, kwargs)
    
     
class Loss():
    def __init__(self, loss_func:LossFunct, *args, **kwargs):
               
            self.loss_func = loss_func
            
    #return values        
    def __call_(self, *args, **kwargs):
            return self.loss_func(args, kwargs)
        
    def reset(self):
            self.loss = 0

# =============================================================================
# ############## Custum Loss Functions ########################################
# =============================================================================
def mse(true, pred):
    true = true.squeeze()
    pred = pred.squeeze()
    assert true.shape == pred.shape
    return np.power(true - pred, 2).mean()

def rmse(true, pred):
    return np.sqrt(mse(true, pred))

def rmsle(true, pred):
    true = true.squeeze()
    pred = pred.squeeze()
    assert true.shape == pred.shape
    return np.power(true - pred, 2).mean()

def binary_cross_entropy(true, pred):
    pass


# =============================================================================
#######################################"" Exceptions ##########################
# =============================================================================
class LossNotFound(Exception):
    pass
