from random import randint, seed
from numpy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im

seed(20220101202)
global omega
for c in range(0,20):
        x1 = randint(10,15)*100
        x2 = 2*x1
        n1 = randint(10,15)
        n2 = randint(5,8)
        n3 = randint(2,4)
        n1pn2 = n1+n2
        tn3 = 2*n3
        n2ptn3 = n2+tn3
        n2ptn3pn2 = n2ptn3+n1pn2
        ththat = round(-float(x1)/(log(float(n2ptn3)/n2ptn3pn2)),2)
        ans = ththat
        all_ans = ans
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ2{s}::
You are given the following data for claim sizes:
<center>
<table border = "l">
<tr><td>Claim size</td><td>Number of claims</td></tr><tr><td>
  Under {x1}</td><td> {n1} </td></tr><tr><td>
  [{x1}, {x2})</td><td> {n2} </td></tr><tr><td>
  {x2} and up</td><td>{n3}</td></tr>
</table>
</center>        
The data are fit to an exponential 
distribution using maximum likelihood. 
Determine the fitted mean. 
""" .format (s = chr(97+c), x1 = x1, x2 = x2, n1 = n1, n2 = n2, n3 = n3, )

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

