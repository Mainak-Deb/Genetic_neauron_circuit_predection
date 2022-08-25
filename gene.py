from neauron import neuron
import random

class gene:
    def __init__(self):
      pass

    def setTarget(self, inputarr,outputarr):
        self.inputarr=inputarr
        self.outputarr=outputarr
        self.size=len(inputarr[0])**3

    def setPopulation(self, population,selection=25):
        self.population = population
        self.selection =int(self.population* selection/100)
        print(self.population,self.selection)
        self.offsprings = []
        for i in range(self.population):
            self.offsprings.append(self.generateRandom(self.size))

    def fitness(self,arr):
        neauron=neuron(len(self.inputarr[0]))
        neauron.construct(arr)
        target=self.outputarr
        arrcout=[]
        for i in self.inputarr:
            arrcout.append(neauron.output(i))
        #print(arrcout)
        c=0;t=0;
        for i in range(len(arrcout)):
            for j in range(len(arrcout[0])):
                if(arrcout[i][j]==target[i][j]):
                    c+=1
                t+=1
        return c/t*100;

    def alter(self,i):
        if(i=="0"):
            return "1"
        else:
            return "0"

    def mutation(self,child):
        i=random.randint(0,int((len(child)-1)/2))
        child = child[:i] + self.alter(child[i]) + child[i+1:]
        i=random.randint(int((len(child)-1)/2),len(child)-1)
        child = child[:i] + self.alter(child[i]) + child[i+1:]
        return child

    def generateRandom(self,target):
        child=[]
        for i in range(target):
            if random.random() < 0.5:
                child.append(0)
            else:
                child.append(1)
        return  child

    def crossover(self, parent1, parent2):
        child = []
        s=[random.randint(0,int((len(parent1)-1)/2)),random.randint(int((len(parent1)-1)/2),len(parent1)-1)]
        child=parent1[:s[0]]+parent2[s[0]:s[1]]+parent1[s[1]:]
        return child



    #returns a tuple with the fittest gene and fitness
    def run(self):
        fitdata=[]
        for j in range(self.population):
            fitdata.append([self.fitness(self.offsprings[j]),self.offsprings[j]])

        fitdata.sort(key=lambda x:x[0],reverse=True)
        #print(fitdata)
        parents=[fitdata[0][1]]
        for k in fitdata:
            if k[1] not in parents:
                parents.append(k[1])

    
        parents= parents[:min(self.selection,int(len(parents)))]

        
        self.offsprings = []
        for j in range(self.population):
            child=self.crossover(random.choice(parents),random.choice(parents))
            self.offsprings.append(child)
        print(fitdata[0])
        return fitdata[0]

  