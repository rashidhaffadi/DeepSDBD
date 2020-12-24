# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:08:17 2019

@author: Rashid Haffadi
"""


class Optimizer():
    def __init__(self, fct, lr, *args, **kwargs):
        self.lr = lr
        self.fct = fct
        
    def get_grads(self, W):
        return W*