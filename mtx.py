from math import cos,sin,pi

from systemUtils import rndSysOk
from matrixUtils import multiplyMatrix,addMatrix,inverseMatrix





numVar=10

sys0,ok0=rndSysOk(numVar)
sys1,ok1=rndSysOk(numVar)

def func(eqs,x):
	ret=[]
	for i in range(len(eqs)):
		eq=eqs[i]
		assert(len(eq[0])==len(eq[1]) and len(eq[0])==len(x)+1)
		s=[sum(x[i] for i in range(len(x)) if l[i]) for l in eq]
		if eq[0][-1]: s[0]+=1
		if eq[1][-1]: s[1]+=1
		s=[l*pi/2. for l in s]
		prod=sin(s[0])*sin(s[1])
		ret.append(prod*prod-x[i])
	return ret


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
		if eq[0][i] or eq[1][i]:
			sn=[sin(s[0]),sin(s[1])]
			cs=[cos(s[0]),cos(s[1])]
			if eq[0][i] and eq[1][i]:
				t= 2*sn[0]*sn[1]
				ret.append(t*(sn[0]*cs[1]+cs[0]*sn[1]))
			elif eq[0][i]:
				t=sn[1]*sn[1]*2*sn[0]
				ret.append(t*(cs[0]))
			elif eq[1][i]:
				t=sn[0]*sn[0]*2*sn[1]
				ret.append(t*(cs[1]))
			else: bs
		else:
			ret.append(0)
		ret[-1]*=pi/2
	# var on the left not included
	return ret

def jcb(eqs,x):
	assert(len(eqs)==len(x))
	ret=[partDerivs(l,x) for l in eqs]
	for i in range(len(eqs)):
		ret[i][i]-=1
	return ret


from random import getrandbits
x=ok0.copy()
for i in range(len(x)):
	x[i]+=(getrandbits(1)*2-1)*0.1

lx=[3 for _ in range(numVar)]
acc=pow(10,-10)
for i in range(100):
	f=func(sys0,x)
	j=jcb(sys0,x)
	ji=inverseMatrix(j)
	prod=multiplyMatrix(ji,[[l] for l in f])
	x=[x[i]-prod[i][0] for i in range(len(x))]
	if all(abs(x[i]-lx[i])<acc for i in range(numVar)): 
		print("acc reached @",i)
		break
	lx=x.copy()
print(x)







































