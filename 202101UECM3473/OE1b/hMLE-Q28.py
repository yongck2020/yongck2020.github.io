from random import randint, seed
from scipy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im, gamma
def fact(x): return (1 if x==0 else x*fact(x-1))

seed(20220101201)
global omega
for c in range(0,20):
        tau = randint(2,5)
        taum1 = tau - 1
        GM1 = round(gamma(1.+1./tau),4)
        GM1a = round(GM1*tau**(1./tau),4)
        x1 = round(randint(42,49)*0.1,1)
        x2 = round(randint(11,18)*0.1,1)
        x3 = round(randint(30,39)*0.1,1)
        x4 = round(randint(60,69)*0.1,1)
        x5 = round(randint(40,49)*0.1,1)
        xb = (x1+x2+x3+x4+x5)/5.
        bth = xb/GM1a
        all_ans = bth
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ1{s}::
The random variable X ha the density function with parameter &beta; given by 
<center> f(x;&beta;) = (1/&beta;<sup>{tau}</sup>)x<sup>{taum1}</sup>e<sup>-(1/{tau})(x/&beta;)<sup>{tau}</sup></sup>, x > 0, &beta;>0.</center>
You are given the following observationof X:
<center> {x1}, {x2}, {x3}, {x4}, {x5}.</center>
Determine the method of moments estimate of &beta;. [Note: &Gamma;(1+1/{tau}) = {GM1}.]
""" .format (s = chr(97+c),  tau = tau, taum1 = taum1, GM1 = GM1, GM1a = GM1a, x1 = x1, x2 = x2, x3 = x3, x4 = x4, x5 = x5,)

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

