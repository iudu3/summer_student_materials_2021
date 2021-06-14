import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
def model_pp(y,t,pars):
    """
    Returns the rate of change of prey and predator in the standard LV model
    """
    dydt = np.zeros(2)
    dydt[0] = pars['r']*y[0]*(1-y[0]/pars['K'])-pars['b']*y[0]*y[1]
    dydt[1] = pars['c']*y[0]*y[1]-pars['m']*y[1]
    return dydt

pars = {}
pars['r'] = 1
pars['K'] = 10**7
pars['c']= 0.1 * 1/10**6
pars['m']= 0.1
pars['b'] = 1/10**6

#Two ways to move forwards
#brute force
#b - what happens if I increase b just a teeny little bit, what happens? And keep going until it's different and reaches non-coexistence
#Not sure what this line does
y0 = [100,5]
t=np.linspace(0,100)
#integrate.odient
y = integrate.odeint(model_pp, y0, t, args=(pars,))
#plot the prey and predator
plt.plot(y[:,0],y[:,1])
plt.show()
plt.plot(t,y[:,0], label ='prey')
plt.plot(t,y[:,1], label = 'predator')
#default for position of legend 
plt.legend(loc='best')
plt.title('Predator and Prey Dynamics Over Time')
plt.xlabel('prey')
plt.show()

#attracting spiral
#