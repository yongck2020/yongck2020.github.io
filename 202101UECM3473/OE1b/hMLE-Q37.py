from random import randint, seed
from numpy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im

seed(20220101203)
global omega
for c in range(0,20):
        u1 = randint(10,15)*10
        x1 = randint(20,25)
        x2 = randint(45,55)
        x3 = randint(50,60)
        x4 = randint(80,90)
        n1 = randint(2,5)
        sumxi = x1+x2+x3+x4+u1+n1*u1
        ththat = sumxi/5.
        ans = ththat
        all_ans = ans
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ3{s}::
 An auto liability coverage has a claims limit of {u1}. 
Claim sizes observed are
<center> {x1},        {x2}, {x3}, {x4}, {u1}</center>
where the claim at {u1} was for exactly {u1}. 
In addition, there are {n1} claims above the limit. 
The data are fitted to an exponential distribution. 
Determine the MLE of &theta;.
""" .format (s = chr(97+c), x1 = x1, x2 = x2, x3 = x3, x4 = x4, u1 = u1, n1 = n1, )

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

