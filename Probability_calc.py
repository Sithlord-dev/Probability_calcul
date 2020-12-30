#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:40:57 2020

@author: sithlord-dev
"""

import copy
import random
import collections
# Consider using the modules imported above.

class Hat(object):
    def __init__(self,**kwargs) :
        self.contents=[]
        for k,v in kwargs.items() :
            for i in range(v) :
                self.contents.append(k)
    
    def draw(self,n) :
      
      if n >= len(self.contents) :
          balls=self.contents
          self.contents=[]
          return balls
      else :
          balls = []
          for i in range(n) :
              ball=random.choice(self.contents)
              balls.append(ball)
              self.contents.remove(ball)
          return balls
    def __str__(self):
      return "Your experiment: {}".format(collections.Counter(self.contents))


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i=0
    for n in range(num_experiments) :
        hat_p=copy.deepcopy(hat)
        balls=hat_p.draw(num_balls_drawn)
        exp = {ball: balls.count(ball) for ball in set(balls)}
        result = True
        for k, v in expected_balls.items():
         if k not in exp or exp[k] < expected_balls[k]:
           result = False
           break

        if result:
         i=i+1

    return i / num_experiments