class Heap2:
    def __init__(self):
        self.items=[None]
    def __len__(self):
        return len(self.items)-1

    def isEmpty(self):
        if len(self.items)==1:
            return True
        return False

    def insert(self,x):
        self.items.append(x)
        self.up()

    def up(self):
        i=len(self)
        while i//2 > 0:
            if self.items[i][1] < self.items[i//2][1]:
                self.items[i],self.items[i//2]=self.items[i//2],self.items[i]
            i=i//2

    def extract_Min(self):
        if len(self)==0:
            return str('cannot extract_Min no elements present')
        value=self.items[1]
        self.items[1]=self.items[len(self)]
        self.items.pop()
        self.down(1)
        return value[0]

    def down(self,i):
        while 2*i<=len(self):
            mi=self.minimum(i)
            if self.items[i][1] > self.items[mi][1]:
                self.items[i],self.items[mi]=self.items[mi],self.items[i]
            i=mi



    def minimum(self,i):
        if 2*i+1 >len(self):
            return 2*i
        if self.items[2*i][1]<self.items[2*i+1][1]:
            return 2*i
        return 2*i+1

    def buildHeap(self,li):
        i=len(li)//2
        self.items=[0]+li
        while i>0:
            self.down(i)
            i=i-1

    def prin(self):
        res=[]
        for i in range(1,len(self.items)):
            res.append(self.items[i][1])
        return res

    def Heapify(self):
        i=len(self)//2
        while i>0:
            self.down(i)
            i=i-1


    def updatePriority(self,V,dis):
        for i in range(1,len(self.items)):
            if self.items[i][0]==V:
                self.items[i][1]=dis
                self.Heapify()
                return



def main():
    li=[9,6,5,2,3]
    l=Heap2()
    l.buildHeap(li)
    while True:
        ch=int(input("1.insert\n2.Min_child\n3.exract_Min\n4.print\n5.Heapify\n6.Exit\nEnter ur choice:"))
        if ch==1:
            a=int(input("Entre the value:"))
            l.insert(a)
        elif ch==2:
            a=int(input("Enter the index:"))
            print(l.items[l.minimum(a)])
        elif ch==3:
            print(l.extract_Min())
        elif ch==4:
            print(l.prin())
        elif ch==5:
            l.Heapify()
        elif ch==6:
            break
        else:
            print('Invalid choice')
if __name__ == '__main__':
    main()
