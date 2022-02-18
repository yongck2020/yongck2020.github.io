from random import randint, seed
from numpy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im

seed(20220102)
global omega
for c in range(0,10):
        tau = randint(3,7)
        deduct = randint(55, 90)*10
        limit = randint(15, 20)*100
        x1 = randint(50, 85)*5
        x2 = randint(86,150)*5
        x3 = randint(151, 200)*5
        x4 = randint(201,219)*5
        u =  limit-deduct
        p1 = randint(70,90)
        p1p = p1*0.01
        p1pc = 1-p1p
        theta = round((((x1+deduct)**tau+(x2+deduct)**tau+(x3+deduct)**tau
                             +(x4+deduct)**tau+2*(u+deduct)**tau-6*(deduct)**tau)/4.0)**(1.0/tau),2)
        SD = round(exp(-(deduct/theta)**tau),4)
        Fpip = 1-p1pc*SD
        m = round((-log(1-Fpip))**(1.0/tau)*theta,2)
        all_ans = m
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ6{s}::
For an insurance policy, you are given:
<ul>
<li> Ground-up losses follow a Weibull distribution with parameters &tau; ={tau} 
  and &theta;(unknown).
<li> Losses under {deduct} are not reported to the insurer.
<li> For each loss over {deduct}, there is a deductible of {deduct} and a policy limit
  of {limit}. 
<li>  A random sample of six claim payments for this policy is:
{x1} &nbsp;   {x2} &nbsp; {x3} &nbsp   {x4} &nbsp   {u}+    {u}+ 
</ul>
 where + indicates that the original loss exceeds {limit}. 
Determine the {p1}<sup>th</sup> percentile of the ground-up distribution.
""" .format (s = chr(97+c),  tau = tau, deduct= deduct, limit = limit, x1 = x1, x2 = x2, x3 = x3, x4 = x4, u =  u, p1 = p1)

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

