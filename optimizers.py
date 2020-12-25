# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:08:17 2019

@author: Rashid Haffadi
"""


class Optimizer():
    def __init__(self, acf, lr, *args, **kwargs):
        self.lr = lr
        self.acf = acf #activation function
        
    def init_grads(self, W, X):
        self.grads = self.acf.get_grads(W, X)

    def one_step(self, W, X):
    	self.init_grads(W, X)
    	# self.acf