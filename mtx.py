from math import cos,sin,pi

from systemUtils import rndSysOk
from matrixUtils import multiplyMatrix,addMatrix,inverseMatrix





numVar=10

sys0,ok0=rndSysOk(numVar)
sys1,ok1=rndSysOk(numVar)

# def func(eqs,x):
# 	ret=[]
# 	for i in range(len(eqs)):
# 		eq=eqs[i]
# 		assert(len(eq[0])==len(eq[1]) and len(eq[0])==len(x)+1)
# 		s=[sum(x[i] for i in range(len(x)) if l[i]) for l in eq]
# 		if eq[0][-1]: s[0]+=1
# 		if eq[1][-1]: s[1]+=1
# 		s=[l*pi/2. for l in s]
# 		prod=sin(s[0])*sin(s[1])
# 		ret.append(prod*prod-x[i])
# 	return ret


# def partDerivs(eq,x):
# 	# var on the left not included
# 	# eq=[0,1,1..]*[0,1,1,..]
# 	assert(len(eq)==2)
# 	assert(len(eq[0])==len(eq[1]) and len(eq[0])==len(x)+1)
# 	s=[sum(x[i] for i in range(len(x)) if l[i]) for l in eq]
# 	if eq[0][-1]: s[0]+=1
# 	if eq[1][-1]: s[1]+=1
# 	s=[l*pi/2. for l in s]
# 	ret=[]
# 	for i in range(len(x)):
# 		if eq[0][i] or eq[1][i]:
# 			sn=[sin(s[0]),sin(s[1])]
# 			cs=[cos(s[0]),cos(s[1])]
# 			if eq[0][i] and eq[1][i]:
# 				t= 2*sn[0]*sn[1]
# 				ret.append(t*(sn[0]*cs[1]+cs[0]*sn[1]))
# 			elif eq[0][i]:
# 				t=sn[1]*sn[1]*2*sn[0]
# 				ret.append(t*(cs[0]))
# 			elif eq[1][i]:
# 				t=sn[0]*sn[0]*2*sn[1]
# 				ret.append(t*(cs[1]))
# 			else: bs
# 		else:
# 			ret.append(0)
# 		ret[-1]*=pi/2
# 	# var on the left not included
# 	return ret


# def func(eqs0,eqs1,t0,t1,x):
# 	ret=[]
# 	for i in range(len(eqs0)):
# 		s=[]
# 		eq=eqs0[i]
# 		s.extend(sum(x[i] for i in range(len(x)) if l[i]) for l in eq)
# 		if eq[0][-1]: s[0]+=1
# 		if eq[1][-1]: s[1]+=1
# 		eq=eqs1[i]
# 		s.extend(sum(x[i] for i in range(len(x)) if l[i]) for l in eq)
# 		if eq[0][-1]: s[2]+=1
# 		if eq[1][-1]: s[3]+=1
# 		s=[l*pi/2. for l in s]
# 		prod=t0*sin(s[0])*sin(s[1])+t1*sin(s[2])*sin(s[3])
# 		ret.append(prod*prod-x[i])
# 	return ret

def func(eqs0,eqs1,t0,t1,x):
	ret=[]
	for i in range(len(eqs0)):
		s=[]
		eq=eqs0[i]
		s.extend(sum(x[i] for i in range(len(x)) if l[i]) for l in eq)
		if eq[0][-1]: s[0]+=1
		if eq[1][-1]: s[1]+=1
		eq=eqs1[i]
		s.extend(sum(x[i] for i in range(len(x)) if l[i]) for l in eq)
		if eq[0][-1]: s[2]+=1
		if eq[1][-1]: s[3]+=1
		s=[l*pi/2. for l in s]
		prod=sin(t0*s[0]+t1*s[2])*sin(t0*s[1]+t1*s[3])
		ret.append(prod*prod-x[i])
	return ret

# def partDerivs(eqs0,eqs1,t0,t1,x):
# 	ret=[]
# 	for i in range(len(eqs0)):
# 		e0=eqs0[i]
# 		e1=eqs1[i]
# 		s=[]
# 		for e in (e0,e1,):
# 			for l in e:
# 				s.append(sum(x[i] for i in range(len(x)) if l[i]))
# 		if e0[0][-1]: s[0]+=1
# 		if e0[1][-1]: s[1]+=1
# 		if e1[0][-1]: s[2]+=1
# 		if e1[1][-1]: s[3]+=1
# 		s=[l*pi/2. for l in s]
# 		ar=[]
# 		sn=[sin(l) for l in s]
# 		cs=[cos(l) for l in s]
# 		tmp=2*(t0*sn[0]*sn[1]+t1*sn[2]*sn[3])
# 		for j in range(len(x)):
# 			sm=0
# 			if e0[0][j] and e0[1][j]:
# 				sm+=t0*(sn[0]*cs[1]+cs[0]*sn[1])
# 			elif e0[0][j]:
# 				sm+=t0*(cs[0]*sn[1])
# 			elif e0[1][j]:
# 				sm+=t0*(sn[0]*cs[1])
			
			
# 			if e1[0][j] and e1[1][j]:
# 				sm+=t1*(sn[2]*cs[3]+cs[2]*sn[3])
# 			elif e1[0][j]:
# 				sm+=t1*(cs[2]*sn[3])
# 			elif e1[1][j]:
# 				sm+=t1*(sn[2]*cs[3])
			
# 			sm*=pi/2.
# 			v=tmp*sm-1 if i==j else tmp*sm
# 			ar.append(v)
# 		ret.append(ar)
# 	return ret

# def jcb(eqs,x):
# 	assert(len(eqs)==len(x))
# 	ret=[partDerivs(l,x) for l in eqs]
# 	for i in range(len(eqs)):
# 		ret[i][i]-=1
# 	return ret

def jcb(eqs0,eqs1,t0,t1,x):
	f0=func(eqs0,eqs1,t0,t1,x)
	x1=x.copy()
	delta=pow(10,-6)
	ret=[[] for _ in range(len(x))]
	for i in range(len(x)):
		x1[i]+=delta
		f1=func(eqs0,eqs1,t0,t1,x1)
		for ii in range(len(f1)):
			ret[ii].append((f1[ii]-f0[ii])/delta)
		x1[i]=x[i]
	return ret

from random import getrandbits
x=ok0.copy()
# for i in range(len(x)):
	# x[i]+=(getrandbits(1)*2-1)*0.01

acc=pow(10,-13)

stp=1000
for vn in range(1000):
	print("vn:",vn)
	# sys0,ok0=rndSysOk(numVar)
	sys1,ok1=rndSysOk(numVar)
	ok0=[int(getrandbits(1) and getrandbits(1)) for _ in range(len(ok1))]
	sys0=[[l[0].copy(),l[1].copy()] for l in sys1]
	for i in range(len(sys0)):
		s0=sum(ok0[ii] for ii in range(len(ok0)) if sys0[i][0][ii])%2
		if sys0[i][0][-1]: s0=1-s0
		s1=sum(ok0[ii] for ii in range(len(ok0)) if sys0[i][1][ii])%2
		if sys0[i][1][-1]: s1=1-s1
		if ok0[i]:
			if not s0: sys0[i][0][-1]=1-sys0[i][0][-1]
			if not s1: sys0[i][1][-1]=1-sys0[i][1][-1]
		elif s0 and s1:
			ix=getrandbits(1)
			sys0[i][ix][-1]=1-sys0[i][ix][-1]
	# 	print(i)
	# 	print(sys0[i])
	# 	print(sys1[i])
	# print()
	# print(func(sys0,sys1,1,0,ok0))
	# exit()

	x=ok0.copy()
	txS=0.1
	tx=1-txS
	while tx>0:
		t0=tx
		t1=1-t0
		lx=[3 for _ in range(numVar)]
		fd=False
		for i in range(1000):
			print("tx,i:",tx,i)
			# f0=func(sys0,x)
			# j0=jcb(sys0,x)
			# f1=func(sys1,x)
			# j1=jcb(sys1,x)
			# f0=multiplyMatrix(f0,t0)
			# f1=multiplyMatrix(f1,t1)
			# f=addMatrix(f0,f1)
			# j0=multiplyMatrix(j0,t0)
			# j1=multiplyMatrix(j1,t1)
			# j=addMatrix(j0,j1)

			f=func(sys0,sys1,t0,t1,x)
			j=jcb(sys0,sys1,t0,t1,x)

			
			ji=inverseMatrix(j)
			

			prod=multiplyMatrix(ji,[[l] for l in f])
			x=[x[i]-prod[i][0] for i in range(len(x))]
			if any(abs(l)>100000000 for l in x):
				print("exceeded1 @",tx)
				break
			if all(abs(x[i]-lx[i])<acc for i in range(numVar)): 
				# print("acc reached @",i)
				fd=True
				break

			lx=x.copy()
		if not fd: 
			txS/=2
			tx=tx-txS
		else:
			tx-=txS

	if fd:
		print("fd")
		print(x)
		print(ok1)
		# exit()
	# exit()
	
# print(x)

print([round(l) for l in x]==ok0)
# print(ok0)




































