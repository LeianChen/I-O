# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:55:44 2018

@author: HP
"""

import random

class Agent():
    def __init__(self, environment):
        self.x = random.randint(0,299)
        self.y = random.randint(0,299)
        self.environment = environment
        self.store = 0

    def move(self):

        if random.random() < 0.5:
            self.y = (self.y + 1) % 299
        else:
            self.y = (self.y - 1) % 299
        
        if random.random() < 0.5:
            self.x = (self.x + 1) % 299
        else:
            self.x = (self.x - 1) % 299

    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
