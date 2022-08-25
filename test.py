from neauron import neuron
from gene import gene

arr=[1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]
neauron=neuron(3)
neauron.construct(arr)
print(neauron)
print(neauron.output([0,0,0]))
print(neauron.output([0,1,0]))
print(neauron.output([1,0,1]))
print(neauron.output([1,1,1]))