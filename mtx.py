from math import cos,sin,pi

from systemUtils import rndSysOk
from matrixUtils import multiplyMatrix,addMatrix,inverseMatrix





numVar=10

sys0,ok0=rndSysOk(numVar)
sys1,ok1=rndSysOk(numVar)


def partDerivs(eq,x):
	# var on the left not included
	# eq=[0,1,1..]*[0,1,1,..]
	assert(len(eq)==2)
	assert(len(eq[0])==len(eq[1]) and len(eq[0])==len(x)+1)
	s=[sum(x[i] for i in range(len(x)) if l[i]) for l in eq]
	if eq[0][-1]: s[0]+=1
	if eq[1][-1]: s[1]+=1
	s=[l*pi/2. for l in s]
	ret=[]
	for i in range(len(x)):
		if eq[0][i] and eq[1][i]:
			ret.append(sin(s[0])*cos(s[1])+cos(s[0])*sin(s[1]))
		elif eq[0][i]:
			ret.append(cos(s[0])*sin(s[1]))
		elif eq[1][i]:
			ret.append(sin(s[0])*cos(s[1]))
		else:
			ret.append(0)
		ret[-1]*=pi/2
	# var on the left not included








































