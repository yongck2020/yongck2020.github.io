from random import randint, seed
from numpy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im

seed(202201205)
global omega
for c in range(0,20):
        x1 = randint(5,8)
        n1 = randint(2,3)
        n2 = randint(4,7)
        n = n1+n2
        xm1 = x1-1
        xm2 = x1-2    
        yh = solve("-{n1}/(1.-y) + {n2}/y - {n2}*{xm1}*y^{xm2}/(1.-y^({xm1}))+ {n}*{x1}*y^({xm1})/(1.-y^({x1}))".format(
                n = n, n1=n1, n2=n2, x1 = x1, xm1=xm1, xm2 = xm2),"y")
        for a in yh: 
            if im(a) == 0 :
                 yhpr = round(float(a),5) 
        ans = round(-log(yhpr),4)
        all_ans = ans
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ05{s}::
{n} losses have been recorded in thousands of dollars and 
are grouped as follows:
<center>
<table border="l">
<tr>
<td>Interval</td><td>[0, 1)</td><td>[1, {x1})</td></tr><tr><td>
    Number of Losses</td><td>{n1}</td><td>{n2}</td></tr>
</table>
</center>
There is no record of the number of losses at or above {x1},000.
The random variable X underlying the losses, in thousands, has the 
density function <center> f(x) = &lambda; e<sup>-&lambda; x</sup>, x > 0, &lambda; > 0.</center>
Determine L(&lambda;) and MLE of &lambda;.
""" .format (s = chr(97+c),  n = n, x1 = x1, n1 = n1, n2 = n2, )

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

