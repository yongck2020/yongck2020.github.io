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
        mu = round(randint(60,80)*0.1,1)
        sg = round(randint(150,200)*0.01,2)
        v1= round(randint(300,400)*0.0001,4)
        v2= round(randint(100,200)*0.0001,4)
        xn = round(exp(0.8*sg + mu)- randint(100,150),0)
        z1 = round((log(xn)-mu)/sg,2)
        pz1 = round(norm.cdf(z1),4)
        partial1 = round(-norm.pdf(z1)/sg,4)
        partial2 = round(-z1*norm.pdf(z1)/sg,4)
        VAR = partial1**2*v1 + partial2**2*v2
        all_ans = VAR
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ7{s}::
 You are given:
<ul>
<li> Fifty claims have been observed from a lognormal distribution with unknown parameters &mu; and &sigma;.
<LI> The maximum likelihood estimates are &mu;&#770 = {mu} and &sigma;&#770 = {sg}.
  <LI> The covariance matrix of &mu;&#770 and &sigma;&#770 is [c<sub>11</sub> = {v1}, c<sub>12</sub> = c<sub>21</sub> = 0 , c<sub>22</sub> = {v2}]  
</ul>  
  Determine the variance of the probability that
  the next claim will be less than or equal to {xn:,.0f} using delta method. 
""" .format (s = chr(97+c),  mu = mu, sg = sg, xn = xn, v1 = v1, v2 = v2,)

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

