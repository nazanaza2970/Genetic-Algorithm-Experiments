def geneticAlgorithmPlot(population,popSize,eliteSize,mutationRate,generations):
#     pop = initialPopulation(popSize,population)
#     progress = []
#     progress.append(1/rankRoutes(pop)[0][1])

#     for i in range(0,generations):
#         pop = nextGeneration(pop,eliteSize,mutationRate)
#         progress.append(1/rankRoutes(pop)[0][1])

#     plt.plot(progress)
#     plt.ylabel('Distance')
#     plt.xlabel('Generation')
#     plt.show()

# geneticAlgorithmPlot(population=cityList,popSize=100,eliteSize=20,mutationRate = 0.01,generations = 500)