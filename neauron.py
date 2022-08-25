import random
import copy
class neuron:
    def __init__(self,size) -> None:
        self.__size = size
        self.__weights = []
        self.__latent = []
        for i in range(size):
            a=[]
            for j in range(size):
                b=[]
                for j in range(size):
                    x=random.randint(0,1)
                    b.append(x)
                    self.__latent.append(x)
                a.append(b)
            self.__weights.append(a)
        # print(self.__latent)
        # print(self.toWeight(self.__latent))
        # print(self.toLatent(self.toWeight(self.__latent)))

    def construct(self,latent) -> None:
        self.__weights = self.toWeight(latent)
        self.__latent = latent
        self.__size=len(self.__weights)

    def notval(self,x) -> int:
        if(x==0):return 1
        else:return 0

    def calculate(self,inputarr,weight) -> list:
        notarr=[]
        for i in range(len(inputarr)):
            if(weight[i]):
                notarr.append(self.notval(inputarr[i]))
            else:
                notarr.append(inputarr[i]) 
        ans=1
        for i in range(len(notarr)):
            ans*=notarr[i]
        return ans

    def output(self,inputarr) -> list:
        ans=inputarr.copy();
        for i in range(self.__size):
            a=[]
            for j in range(self.__size):
                a.append(self.calculate(ans,self.__weights[i][j]))
            ans=a
        return ans

    def __str__(self) -> str:
        s=""
        for i in range(self.__size):
            for j in range(self.__size):
                for k in range(self.__size):
                    s+=str(self.__weights[i][j][k])
                s+=" "
            s+="\n"
        return s

    def toWeight(self,latent) -> list:
        w=[];count=0;
        for i in range(self.__size):
            a=[]
            for j in range(self.__size):
                b=[]
                for k in range(self.__size):
                    x=latent[count]
                    b.append(x)
                    count+=1
                a.append(b)
            w.append(a)
        return w

    def toLatent(self,weight) -> list:
        l=[];count=0;
        for i in range(self.__size):
            for j in range(self.__size):
                for k in range(self.__size):
                    l.append(weight[i][j][k])
                    count+=1
        return l