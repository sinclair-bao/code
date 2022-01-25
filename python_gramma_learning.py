import numpy as np
import pandas as pd
import os
import io
import torch
print(torch.__version__)
print(pd.__version__)
print(np.__version__)


s = ['I', 'am', 'a', 'student']
mapping = {}
for i, v in enumerate(s):
    mapping[v] = i
print(mapping)

