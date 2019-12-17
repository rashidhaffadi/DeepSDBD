# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:35:01 2019

@author: Rashid Haffadi
"""
import neupy.init as init
#import numpy as np

inits = ['constant', 'uniform', 'normal', 'kaiming_']

def uniform(n_in:int, n_out:int):
    w = np.random.randn(n_in, n_out)
    b = np.random.randn(n_in, n_out)
    return w, b
     
def kaiming_normal(n_in:int, n_out:int):
    w, b = uniform(n_in, n_out)
    init.kaiming_normal_(w, mode='fan_out')
    init.kaiming_normal_(b, mode='fan_out')
    return w, b

def normal(n_in, n_out):
    w = torch.randn()
    
class Initializer():
    def __init__(self, initializer, *args, **kwargs):
        self.init = initializer
    
    
    def __call__(self):
        pass
    