from neauron import neuron
from gene import gene


# inputarr=[
#     [0,0],
#     [0,1],
#     [1,0],
#     [1,1],
# ]
# outputarr=[
#     [0,0],
#     [0,1],
#     [0,1],
#     [1,0],
# ]
inputarr=[
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]
]
outputarr=[
    [0,0,0],
    [0,0,1],
    [0,0,1],
    [0,1,0],
    [0,0,1],
    [0,1,0],
    [0,1,0],
    [0,1,1]
]


def main():
    # n = neuron(len(inputarr[0]))
    # print(n)
    # print(n.output(inputarr[1]))
    # [1, 1, 0, 0, 1, 0, 1, 1]
    g=gene()
    g.setTarget(inputarr,outputarr)
    g.setPopulation(4000,40)
    # for i in g.offsprings:
    #     print(g.fitness(i))
    for i in range(100):
        ans=g.run()
        print(ans)
    # print(g.fitness(g.offsprings[0])) 

if __name__ == '__main__':
    main()

