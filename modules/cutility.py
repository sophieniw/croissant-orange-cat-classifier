#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:45:44 2019

@author: sophie
"""
import os

def count_files(path):
    num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])
    print (num_files)
    