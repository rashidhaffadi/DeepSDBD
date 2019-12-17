# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:37:42 2019

@author: Rashid Haffadi
"""
import numpy as np
from functools import partial
# Activations
acts = ["relu", "sigmoid", "softmax", "tanh", "leaky_relu", "selu", "elu"]

def get_act(index, *args, **kwargs):
    if index==0:
            return relu
    elif index==1:
        return sigmoid
    elif index==2:
        return softmax
    elif index==3:
        return tanh
    elif index==4:
        if kwargs['leak'] and kwargs['leak'] is not None:
            return partial(leaky_relu, leak=kwargs['leak'])
        else: return leaky_relu
        
    elif index==5:
        f = selu
        if kwargs['alpha'] and kwargs['alpha'] is not None:
            f = partial(f, alpha=kwargs['alpha'])
        if kwargs['lamda'] and kwargs['lamda'] is not None:
            f = partial(f, lamda=kwargs['lamda'])
        return f
    elif index==6:
        if kwargs['alpha'] and kwargs['alpha'] is not None:
            return partial(elu, alpha=kwargs['alpha'])
        else: return elu
    else:   raise ActivationFunctionNotFound
        
class Activation():
    # Initialize The Activation With Activation Name
    # Note: if we choose leaky_relu we must specify leak=?
    def __init__(self, act='relu', *args, **kwargs):
        if isinstance(act, str):
            index = acts.index(act)
            self.activation = get_act(index)
        else:   
            self.activation = act
    
    def __call__(self, h, *args, **kwargs):
        if len(h.shape) != 1:
            h = h.squeeze()
        return self.activation(h, args, kwargs)

def relu(h):
    if len(h.shape) != 1:
        h = h.squeeze()
    return h * (h > 0)

def sigmoid(h):
    if len(h.shape) != 1:
        h = h.squeeze()
    return 1/(1+np.exp(-h))
    
def softmax(h):
    if len(h.shape) != 1:
        h = h.squeeze()
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(h - np.max(h))
    return e_x / e_x.sum()

def tanh(h):
    if len(h.shape) != 1:
        h = h.squeeze()
    return (np.exp(h) - np.exp(-h))/(np.exp(h) + np.exp(-h))

def leaky_relu(h, leak:float=0.2):
    if len(h.shape) != 1:
        h = h.squeeze()
    return h * (h > 0) + leak * h * (h <= 0)

def elu(h, alpha=0.2):
    if len(h.shape) != 1:
        h = h.squeeze()
    return (h > 0)*h + (h <= 0)*alpha*(np.exp(h) - 1)

def selu(h, alpha=1.6732, lamda=1.0507):
    if len(h.shape) != 1:
        h = h.squeeze()
    return lamda*((h > 0)*h + (h <= 0)*alpha*(np.exp(h) - 1))

# =============================================================================
# We have to use Linear with each activation
# Activation(linear)
# =============================================================================

def linear(x, w, b):
    return x @ w + b

# =============================================================================
# relu_ = Activation('relu')
# relu_(linear(x, w, b))
# =============================================================================



# =============================================================================
# ##########################"Exceptions########################################
# =============================================================================
class ActivationFunctionNotFound(Exception):
    pass