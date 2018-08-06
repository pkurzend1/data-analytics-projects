
import numpy as np
import numpy.random




class OptimizationProblem():
    def __init__(   self,
                    costFunction,    # Fitness: for NN eg accuracy on eval set                    
                    nVar,               # int: number of variables (= len(varNames))
                    varMin,             # list: len = nVar, minimal values for each variable
                    varMax,             # list: len= = nVar, maximal values for each variable
                    varNames            # list of variable names to be optimized
                ):
        
        self.costFunction = costFunction
        self.varNames = varNames
        self.solutionDict = None
        self.nVar = nVar
        self.varMin = varMin
        self.varMax = varMax
        assert np.all(self.varMax > self.varMin), 'All upper-bound values must be greater than lower-bound values'
        if isinstance(self.varMax, np.ndarray):
            assert self.varMin.shape == self.varMax.shape, "varMax has different shape than varMin"
        
         


class Particle():
    def __init__(self):
        self.position = None
        self.velocity = None
        self.cost = None
        self.best_position = None
        self.best_cost = None




class PSO():

    def __init__(
                    self,   
                    problem,                # optimizatrion problem
                    MaxIter = 200,           # number if iterations
                    epsilon = 0.0000001,    # finish after fitness is better than epsilon
                    PopSize = 50,           # number of particles
                    c1 = 1.5,
                    c2 = 2, 
                    w = 1,
                    wdamp = 0.995            # change w over time
                ):
        
        self.PopSize = PopSize              # population size: number of particles
        self.problem = problem              # problem to optimize
        self.dim = self.problem.nVar        # dim of particles (:= problem.nVar)
        self.MaxIter = MaxIter
        self.epsilon = epsilon
        self.c1 = c1
        self.c2 = c2
        self.w = w
        self.wdamp = wdamp
        self.t = 0                         # time stamp, := iteration step
        self.gbest = {'position': None, 'cost': np.inf} # init global best
        
        


    def optimize(self):
        # extract Problem Info:
        costFunction = self.problem.costFunction
        varMin = self.problem.varMin
        varMax = self.problem.varMax
        nVar = self.problem.nVar

        # init population
        pop = []
        for i in range(self.PopSize):
            pop.append(Particle())
            pop[i].position = np.random.uniform(varMin, varMax, nVar)
            pop[i].velocity = np.random.uniform(size=nVar)
            pop[i].cost = costFunction(pop[i].position)
            pop[i].best_position = pop[i].position.copy()
            pop[i].best_cost = pop[i].cost.copy()

            if pop[i].best_cost < self.gbest["cost"]:
                self.gbest["position"] = pop[i].best_position.copy()
                self.gbest["cost"] = pop[i].best_cost

        # pso loop
        for it in range(self.MaxIter):
            for i in range(self.PopSize):
                pop[i].velocity = self.w*pop[i].velocity + \
                                  self.c1*np.random.rand(nVar)*(pop[i].best_position - pop[i].position) + \
                                  self.c2*np.random.rand(nVar)*(self.gbest['position'] - pop[i].position)
                
                pop[i].position += pop[i].velocity

                pop[i].position = np.maximum(pop[i].position, varMin)
                pop[i].position = np.minimum(pop[i].position, varMax)

                pop[i].cost = costFunction(pop[i].position)

                if pop[i].cost < pop[i].best_cost:
                    pop[i].best_position = pop[i].position.copy()
                    pop[i].best_cost = pop[i].cost.copy()

                    if pop[i].best_cost < self.gbest["cost"]:
                        self.gbest["position"] = pop[i].best_position.copy()
                        self.gbest["cost"] = pop[i].best_cost.copy()

            self.w *= self.wdamp
            print('Iteration {}: Best Cost = {}'.format(it, self.gbest['cost']))

        self.problem.solutionDict = {self.problem.varNames[i] : self.gbest["position"][i] for i in range(self.gbest["position"].shape[0])}
        return self.gbest


    def get_solution(self):           
        assert self.gbest["position"] is not None, "Swarm not trained"
        return self.problem.solutionDict






if __name__=="__main__":
    # A Sample Cost Function
    # x: list or np.array
    def Sphere(x):        
        return np.sum(x**2)


    # Optimization Problem
    problem = OptimizationProblem(costFunction=Sphere, varNames=["x{}".format(i) for i in range(1, 11)], nVar=10, varMin=-5, varMax=5)
    pso = PSO(problem)
    g = pso.optimize()
    print(pso.get_solution())



