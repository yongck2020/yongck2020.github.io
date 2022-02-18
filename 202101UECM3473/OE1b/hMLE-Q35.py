from random import randint, seed
from numpy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im

seed(20220101204)
global omega
for c in range(0,20):
        n0 = randint(60,100)
        n1 = randint(12,32)
        n2 = randint(2,5)
        x1 = n1+2*n2+2
        x2 = n0+n1+n2+2
        a1 = (-x1-x2 -2)*(-1)
        b1 = (-x2 +2)*(-1)
        c1 = -x1
        p1 = round((-b1+sqrt(b1**2-4*a1*c1))/(2*a1),5)
        bt = round(p1/(1-p1),4)
        ans = bt
        all_ans = ans
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ4{s}::
Annual claim counts follow a geometric distriution with mean &beta;.
 <UL>
<LI> {n0} policyholders submitted 0 claims.
<LI> {n1} policyholders submitted 1 claim.
<LI> {n2} policyholders submitted 2 claims.
<LI> For two policyholders, it is know that they submitted either 1 claim or 2 claims, but the exact number of claims is not available.
<LI> No policyholder submitted more that 2 claims.
</UL>
Estimate &beta; using maximum likelihood.
""" .format (s = chr(97+c),  n0 = n0, n1 = n1, n2 = n2,)

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

