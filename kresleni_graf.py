import pylab as pl
from pylab import pi 

f = 50
w = 2* pi * f

#časová osa
t = pl.linspace(0, 0.1, 100)

#napětí
u = 5* pl.sin(w*t)

#proud
i = 2.874* pl.cos(w*t)

pl.plot(t, u)
pl.plot(t, i)

pl.show

