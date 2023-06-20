#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:16:01 2023

@author: nahidferdous
"""
## Scatter Plot

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

a= np.random.rand(5)
b=pd.DataFrame(np.random.rand(5,2),columns=["a","b"])
c=pd.DataFrame(np.random.rand(50,2),columns=["c","d"])

c.plot(kind="scatter", x="c", y="d")
