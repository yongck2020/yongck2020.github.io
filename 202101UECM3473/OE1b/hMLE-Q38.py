from random import randint, seed
from scipy import exp, sqrt, log
from scipy.integrate import quadrature
from scipy.stats import poisson, norm, gamma
from numpy import double, around, mean, var
from sympy.solvers import solve
from sympy import symbol, im

seed(20220101208)
global omega
for c in range(0,20):
        bt = randint(2,2)
        n1 = randint(75,100)
        sumpsi = randint(165, 185)
        sumpsisq = randint(375,395)
        sumphi = randint(147,157)
        sumphisq = randint(312,352)
        bpsi = round(float(sumpsi)/n1,4)
        vpsi = round((sumpsisq-n1*bpsi**2)/float(n1),4)
        if vpsi <=0: continue
        bs1 = round(float(sumpsi)/n1-bt,4)
        mse1 = round(vpsi+bs1**2,4)        
        bphi = round(float(sumphi)/n1,4)
        vphi = round((sumphisq-n1*bphi**2)/float(n1),4)
        if vphi <=0: continue
        bs2 = round(float(sumphi)/n1-bt,4)
        mse2 = round(vphi+bs2**2,4)        
        ans = round(mse1/mse2,4)
        all_ans = ans
        error = 0.05*all_ans 
        
        question = """
::CTOE1bQ08{s}::
 Two different estimators, &psi; and &phi;, are available for estimating the paramentes, &beta;, of a given loss distribution. To test their performance, you have {n1} simulated trials of each estimator, using &beta; = {bt}, with the following results:
<center> &sum;<sub>i=1</sub><sup>{n1}</sup> &psi;<sub>i</sub> = {sumpsi}, &sum;<sub>i=1</sub><sup>{n1}</sup> &psi;<sub>i</sub><sup>2</sup> = {sumpsisq}, &sum;<sub>i=1</sub><sup>{n1}</sup> &phi;<sub>i</sub> = {sumphi}, &sum;<sub>i=1</sub><sup>{n1}</sup> &phi;<sub>i</sub><sup>2</sup> = {sumphisq}</center>
Calculate MSE<sub>&psi;</sub>(&beta;)/MSE<sub>&phi;</sub>(&beta;).
""" .format (s = chr(97+c), n1 = n1, bt = bt, sumpsi = sumpsi, sumpsisq = sumpsisq, sumphi = sumphi, sumphisq = sumphisq,  )

        print(question, end=' ')
        print("{#%f:%f}" % (all_ans, error))
        print("<br/>")
        print("<br/>")

