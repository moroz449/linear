from itertools import product, combinations
from random import seed,getrandbits,randint
seed(3225423343542); del seed


def rndEq(numVar):
	return [getrandbits(1) for _ in range(numVar+1)]
def rndSys(numVar):
	return [[rndEq(numVar),rndEq(numVar)] for _ in range(numVar)]
def rndSysOk(numVar):
	def prod(ar,ok):
		ret=sum(ar[i] for i in range(numVar) if ok[i])%2
		if ar[-1]: ret=1-ret
		return ret
	sys=rndSys(numVar)
	ok=[int(getrandbits(1) and getrandbits(1)) for _ in range(numVar)]
	for i in range(numVar):
		s=prod(sys[i][0],ok)
		if ok[i]:
			if not s: sys[i][0][-1]=1-sys[i][0][-1]
			s=prod(sys[i][1],ok)
			if not s: sys[i][1][-1]=1-sys[i][1][-1]
		elif s:
			if prod(sys[i][1],ok):
				ix=int(getrandbits(1))
				sys[i][ix][-1] = 1-sys[i][ix][-1]
	return sys,ok
def checkEq(eq,ok,ix):
	s=sum(eq[0][i] for i in range(len(eq[0])-1) if ok[i])%2
	if eq[0][-1]: s=1-s
	if not s: 
		return (0 if ok[ix] else 1)
	s=sum(eq[1][i] for i in range(len(eq[1])-1) if ok[i])%2
	if eq[1][-1]: s=1-s
	return int(s==ok[ix])
def sysOks(sys):
	oks=[]
	nv=len(sys)
	assert(nv+1==len(sys[0][0]))
	for p in product((0,1,), repeat=nv):
		ok=True
		for n in range(nv):
			if not checkEq(sys[n],p,n):
				ok=False
				break
		if ok: oks.append(p)
	return oks			
def linSysOks(sys,varOnLeft=True):
	assert(len(sys[0])-1==len(sys))
	assert(not isinstance(sys[0][0],list))
	eqs=[l.copy() for l in sys]
	if isinstance(eqs[0][0],bool):
		for i in range(len(eqs)):
			eqs[i]=[int(l) for l in eqs[i]] 
	if varOnLeft:
		for i in range(len(eqs)):
			eqs[i][i]=1-eqs[i][i]
	oks=[]
	for p in product((0,1,),repeat=len(eqs)):
		ok=True
		for e in eqs:
			s=sum(e[i] for i in range(len(eqs)) if p[i])%2
			if e[-1]: s=1-s
			if s:
				ok=False
				break
		if ok: oks.append(p)
	return oks
def ar2Set(ar):
	ret={(i,) for i in range(len(ar)-1) if ar[i]}
	if ar[-1]: ret.add(tuple())
	return ret
def mlt(s0,s1):
	if not isinstance(s0,set): s0=ar2Set(s0)
	if not isinstance(s1,set): s1=ar2Set(s1)
	s0c=s0.copy()
	s1c=s1.copy()
	ret=set()
	for l0 in s0c:
		for l1 in s1c:
			ret.symmetric_difference_update([tuple(sorted(set(l0+l1)))])
	return ret
def setOks(s):
	ret=[]
	for ok in product((0,1,),repeat=numVar):
		if sum(all(ok[i] for i in l) for l in s)%2: 
			ret.append(ok)
	return ret
