# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Predefined Loss Functions
losses = ["mse", "binary_cross_entropy", "categorical_cross_entropy"]
import numpy as np
from metrics import *
from loss_functions import *
from activations import *

             
""" Initializer Class (type)


"""           



class OneLayerNN():
    def __init__(self, n_in, n_out, name='Layer', activation='relu', initializer='kaimer'):
        self.n_in = n_in
        self.n_out = n_out
        self.activation = Activation(activation)
        self.weights, self.biases = self.initialize(n_in, n_out, initializer)
        self.grads = np.zeros((n_in, n_out))

    def initialize(self, n_in, n_out, initializer):
        init = Initializer(initializer)
        return init(n_in, n_out)
    
    def forward(self):        
        return self.activation(h)
    
    def backward(self):
        self.grades = 


        
        
class Model():
    def __init__(self, layers):
        self.layers = layers
        for 
            
    def compile(self, bs, ):
        self.steps
    


# Dataset  === Dataloader === Optimizer === Backpropagation === Update

