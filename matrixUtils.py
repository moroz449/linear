def multiplyMatrix(a,b):
	assert(len(a[0])==len(b))
	ret=[[sum(a[i][k]*b[k][j] for k in range(len(b)))\
			for j in range(len(b[0]))] 
					for i in range(len(a))]
	return ret
def addMatrix(a,b,sub=0):
	assert(len(a)==len(b))
	assert(len(a[0])==len(b[0]))
	if sub:
		ret=[[a[i][j]-b[i][j] for j in range(len(a[0]))]\
									 for i in range(len(a))]
	else:
		ret=[[a[i][j]+b[i][j] for j in range(len(a[0]))]\
									 for i in range(len(a))]
	return ret
def inverseMatrix(a):
	def is0(n):
		return abs(n)<0.000001
	def changeLines(a,i,ii):
		t=a[ii].copy()
		a[ii]=a[i]
		a[i]=t
	assert(len(a)==len(a[0]))
	e=[[0]*len(a) for _ in range(len(a))]
	for i in range(len(e)): e[i][i]=1
	a=[l.copy() for l in a]
	for i in range(len(a)):
		for ii in range(i,len(a)):
			if not is0(a[ii][i]): break
		assert(not is0(a[ii][i]))
		if ii!=i:
			changeLines(a,i,ii)
			changeLines(e,i,ii)
		for ii in range(i+1,len(a)):
			k=a[ii][i]/a[i][i]
			for j in range(len(a[ii])): 
				a[ii][j]-=a[i][j]*k
				e[ii][j]-=e[i][j]*k
		k=1/a[i][i]
		for ii in range(len(a[i])): 
			a[i][ii]*=k
			e[i][ii]*=k
	for j in range(len(a)-1,-1,-1):
		assert(is0(a[j][j]-1))
		for i in range(j):
			k=a[i][j]
			for ii in range(len(a[i])):
				# a[i][ii]-=a[j][ii]*k
				e[i][ii]-=e[j][ii]*k
	return e			
