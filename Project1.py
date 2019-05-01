
import math


from Heap3 import Heap2


class vertex:
	def __init__(self,ui=None,dist=float("infinity"),parent=None):
		self.ui=int(ui)
		self.dist=dist
		self.parent=parent

class weigth:
	def __init__(self,u=None,v=None,wi=0):
		self.v=v
		self.wi=wi
		self.u=u

class Graph:
	def __init__(self,n):
		self.graph=[[] for i in range(n)]
		self.V=[]
		for i in range(n):
			self.V.append(vertex(i,float("infinity"),None))

	def addEdge(self,u,v,wi):
		self.graph[u].append(weigth(u,v,wi))

	def dijkstra(self,s):
		self.V[s].dist=0
		H=Heap2()
		for i in range(len(self.V)):
			H.insert([self.V[i],self.V[i].dist])

		while H.isEmpty()!=True:
			w=H.extract_Min()
			for i in self.graph[w.ui]:
				if self.V[i.v].dist > (w.dist+i.wi):
					self.V[i.v].dist=w.dist+i.wi
					H.updatePriority(self.V[i.v],self.V[i.v].dist)
					self.V[i.v].parent=w

	def prin(self,d):
		q=[d]
		t=self.V[d].parent
		while t!=None:
			q.append(t.ui)
			t=t.parent
		return q



def Assign(Morg,M):
	for i in range(len(Morg)):
		temp=[]
		for j in range(len(Morg)):
			temp.append(Morg[i][j])
		M.append(temp)

	


def main():
	inf=math.inf
	f1=input("Enter file name:")
	file=open(f1,"r")
	arr=list(map(int,file.readline().rstrip().split()))
	#n=10
	n=arr[0]+1
	
	Morg=[None]*n
	for i in range(n):
		Morg[i]=[]
		temp=[inf]*n
		Morg[i]=temp
	
	Edg=arr[1]
	G=[]
	print("u v w")
	for h in range(Edg):
		E=list(map(int,file.readline().rstrip().split()))
		G.append(E)
		Morg[E[0]][E[1]]=E[2]
		Morg[E[1]][E[0]]=E[2]
	file.close()
	s=int(input("Enter Source node: "))
	d=int(input("Enter Destination node: "))
	k=int(input("Enter number of required disjoint paths: "))
	Q=[None]*k

	ic=0#step 1
	j=1 #step 2
	Imax=int(input("Enter maximum number of Conflicts: "))
	#Imax=2
	jflag=0
	M=[None]*k
	for i in range(k):
		M[i]=[]
		Assign(Morg,M[i])
	while j<=k: #step-3 
		
		i=0
		check=[]
		Mtemp=[]
		if j is 1:
			Assign(M[0],Mtemp)
		while i<j-1 and j is not 1:  #step-4
			Mtemp=[]
			Assign(M[j-1],Mtemp)
			Mprev=[]
			Assign(M[i],Mprev)
			length=len(Q[i])
			
			#claculating  cost  of previous i.e ith paths where i<j-1 
			iii=0
			a=Q[i][0]
			cost=0   #for forbidden paths
			while iii<length-1:
				a=Q[i][iii]
				b=Q[i][iii+1]
				cost=cost+Mprev[a][b]
				iii=iii+1



			iii=0
			while iii<len(Q[i])-1:
				a=Q[i][iii]
				check.append(a)
				b=Q[i][iii+1]
				check.append(b)
				Mtemp[a][b]=Mtemp[a][b]+cost
				Mtemp[b][a]=Mtemp[b][a]+cost
				if a is not s and a is not d:
					MM=Mtemp[a]
					lengthm=len(MM)
					mm=1
					while mm<lengthm:
						if MM[mm] is not s and MM[mm] is not inf and not(mm in check):
							Mtemp[a][mm]=Mtemp[a][mm]+cost
							Mtemp[mm][a]=Mtemp[mm][a]+cost
						mm=mm+1
				iii=iii+1
		
			
			M[j-1]=[]
			Assign(Mtemp,M[j-1])
			i=i+1
			
		g=Graph(n)             #step-5
		for i_d in range(len(G)):
			de=G[i_d]
			u=int(de[0])
			v=int(de[1])
			wi=Mtemp[u][v]
			g.addEdge(u,v,wi)
			v=int(de[0])
			u=int(de[1])
			g.addEdge(u,v,wi)
		
		
		g.dijkstra(s)
		Q[j-1]=g.prin(d)
		#check for disjoint     step-6
		jj=0
		i=0
		while i<j-1 and j is not 1:
			iii=1
			disjoint_Set=[] #stores conflicted vertex
			while iii<(len(Q[i])-1) and iii<(len(Q[j-1])-1):
				if Q[j-1][iii] in Q[i]:
					disjoint_Set.append(Q[j-1][iii])
				iii=iii+1
	
			if len(disjoint_Set) is not 0:  #yes it is disjoint
				#calculating cost of the current path 
				iii=0
				a=Q[j-1][0]
				cost=0
				jflag=1
				while iii<len(Q[j-1])-1:
					a=Q[j-1][iii]
					b=Q[j-1][iii+1]
					cost=cost+Mtemp[a][b]
					iii=iii+1
				

				
				iii=0
				while iii<len(disjoint_Set): #step 6.1
					a=disjoint_Set[iii]
					for il in range(len(G)):
						if G[il][0] is a and G[il][1] not in disjoint_Set :
							Morg[G[il][0]][G[il][1]]=Morg[G[il][0]][G[il][1]]+cost
							Morg[G[il][1]][G[il][0]]=Morg[G[il][1]][G[il][0]]+cost
						elif G[il][1] is a and G[il][0] not in disjoint_Set:
							Morg[G[il][0]][G[il][1]]=Morg[G[il][0]][G[il][1]]+cost
							Morg[G[il][1]][G[il][0]]=Morg[G[il][1]][G[il][0]]+cost
					iii=iii+1
				iii=0
				while iii<len(disjoint_Set)-1:
					a=disjoint_Set[iii]
					ii=0
					while ii<len(disjoint_Set)-iii:
						b=disjoint_Set[++iii]
						for il in range(len(G)):
							if (G[il][0] is a and G[il][1] is b) or (G[il][0] is b and G[il][1] is a):
								Morg[G[il][0]][G[il][1]]=Morg[G[il][0]][G[il][1]]+cost
								Morg[G[il][1]][G[il][0]]=Morg[G[il][1]][G[il][0]]+cost
						ii=ii+1
					iii=iii+1


			i=i+1


		if jflag is 0:
			j=j+1     #goto step 3
		else:
			for i in range(k):
				M[i]=[]
				Assign(Morg,M[i])
			Q=[None]*k
			j=1
			ic=ic+1   #step 6.2
			if ic>Imax:  #step 6.3
				print("demand rejected")
				exit(0)
			jflag=0     #else goto step 2
	print("The required disjoints paths are followings:")
	for i in range(k):
		lent=len(Q[i])
		print("Path-",(i+1),": ",end=" ")
		j=lent-2
		print(Q[i][lent-1],end=" ")
		while j>=0:
			print("-->",Q[i][j],end=" ")
			j=j-1
		print()

if __name__=='__main__':
	main()










