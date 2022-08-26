#!/usr/bin/env python
# coding: utf-8

# Домашнее задание (семинар 11)
# 
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# 
# Определить корни
# 
# Найти интервалы, на которых функция возрастает
# 
# Найти интервалы, на которых функция убывает
# 
# Построить график
# 
# Вычислить вершину
# 
# Определить промежутки, на котором f > 0
# 
# Определить промежутки, на котором f < 0

# In[43]:


import sympy 
import numpy as np
from sympy.plotting import plot
from sympy import symbols


# Построим график заданной функции:

# In[44]:


x = symbols('x')
plot(-12*x**4*sympy.sin(sympy.cos(x))-18*x**3 + 5*x**2 + 10*x - 30, (x, -100, 100))


# Найдем корни:

# In[45]:


sympy.solveset(sympy.Eq(-12*x**4*sympy.sin(sympy.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30, 0), x)


# Определим промежутки, на котором f > 0 и f < 0:

# In[46]:


x = np.arange(-10, 10, 1)
func = -12*x**4 * (np.sin(np.cos(x))) - 18*x**3 + 5*x**2 + 10*x - 30

pos_list = []
neg_list = []

for i in x:
    res = -12*i**4 * (np.sin(np.cos(i))) - 18*i**3 + 5*i**2 + 10*i - 30
    if res > 0:
        pos_list.append(res)
    else:
        neg_list.append(res)
        
print(f'\n{pos_list[0]} --> {pos_list[-1]}\n')
print(pos_list)
print(f'\n{neg_list[0]} --> {neg_list[-1]}\n')
print(neg_list)

