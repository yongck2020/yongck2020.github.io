from random import randint, seed
from numpy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im

seed(20220102)
global omega
for c in range(0,20):
        u1 = randint(10,10)*1000
        d1 = randint(5,5)*100
        p1 = randint(65,85)
        p1p = round(p1*0.01,2)
        x1 = d1+300
        x2 = x1+200
        x3 = x2*2
        x4 = x3+500
        x5 = x3*2
        x6 = x5+1000
        suminvxi = round(1./x1+1./x2+1./x3+1./x4+1./x5+1./x6,4)
        ththat = round(6./(4./d1+suminvxi-10./u1),3)
        m1 = round(-ththat/log(p1p*exp(-ththat/u1)),2)
        all_ans = m1
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ9{s}::
 For an insurance coverage, your department 
only handles claims below {u1:,d}. Among 
these claims, you observe 6 claims for 
{x1}, {x2}, {x3}, {x4}, {x5}, and {x6}. 
In addition, there are 4 claims for amounts 
below {d1}, who exact amounts are unknown. 
You fit these claims to an inverse exponential 
distribution using maximum likelihood. 
Determine the resulting estimate 
for the {p1}<sup>th</sup> percentile of claim size for all claims.
""" .format (s = chr(97+c), x1 = x1, x2 = x2, x3 = x3, x4 = x4,x5 = x5, x6 = x6, u1 = u1, d1 = d1, p1=p1, )

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

