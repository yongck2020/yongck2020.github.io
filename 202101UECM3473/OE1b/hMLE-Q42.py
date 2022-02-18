from random import randint, seed
from numpy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im
from numpy import matrix

seed(202101020)
global omega
for c in range(0,20):
        m1 = randint(3,8)
        q1 = round(randint(4,7)*0.1,1)
        sm = round(randint(5,9)*0.1,1)
        sq = round(randint(2,5)*0.01,2)
        cor = -round(randint(25,45)*0.01,2)
        mqhat = round(m1*q1,2)
        vm = sm**2
        vq = sq**2
        covmq = cor*sm*sq
        vgmq = matrix([[q1,m1]]).dot(matrix([[vm, covmq],[covmq,vq]])).dot(matrix([[q1],[m1]]))
        vgmq1 = vgmq[0,0]
        ulimit = mqhat + 1.96*sqrt(vgmq1) 
        ans = round(ulimit,4)
        all_ans = ans
        error = 0.05*all_ans 
        
        question = """
::CTOE1Q20{s}::
Parameters for a binomial distribution have been estimated as:
  <center>
   <table border = "l">
      <tr><td></td><td>Estimate</td><td>Standard deviation</td></tr><td>
      m</td><td>{m1}</td><td>{sm}</td><tr><td> 
      q</td><td>{q1}</td><td>{sq}</td>
    </table>
  </center>
  The correlation between the estimated m and estimated q is {cor}<br>
  Using the delta method, determine the upper limit of  a 95% symmetric normal confidence
  interval for the mean of the distribution. 
""" .format (s = chr(97+c),m1 = m1, q1 = q1, sm = sm, sq = sq, cor = cor,  )

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

