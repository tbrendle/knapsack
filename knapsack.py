import numpy as np

class Estimator():
    def __init__(self, value, size):
        self.value = value
        self.size = size
        self.n = len(value)

    def bestRelaxedValue(self,index, capacity):
        bestValue = 0
        capa = 0
        for i in xrange(index, self.n):
            capa+= self.size[i]
            bestValue+=self.value[i]
            if capa>=capacity:
                return int(bestValue-self.value[i]*(capa-capacity)/self.size[i])    
        return int(bestValue)




def knapsack(value, size, capacity):
    """
        Compute the optimum knapsack given values, sizes and capacity
 
        :param value: Array of values
        :param size: Array of sizes 
        :param capacity: Capacity of the knapsack
        :type value: list
        :type size: list
        :type capacity: float
        :return: a tuple (max value, repartition of items)
        :rtype: (float, list)
 
        :Example:
 
        >>> knapsack([12, 10, 7], [10, 7, 6], 12.5)
        (12.0, array([1, 0, 0]))
        >>> knapsack([12, 10, 7], [10, 7, 6], 14)
        (17.0, array([0, 1, 1]))
    """
    #Sort value, size by decreasing efficiency
    n = len(value)
    a = [(value[i], size[i], i, value[i]/size[i]) for i in xrange(n)]
    dtype = [('value', float), ('size', float), ('index', int),  ('ratio', float),]
    a = np.array(a, dtype=dtype)
    a = np.sort(a, order='ratio')
    a = a[::-1]
    sortedValues = [] 
    sortedSize = []
    hashTable = []
    for i in xrange(n):
        sortedValues.append(a[i][0])
        sortedSize.append(a[i][1])
        hashTable.append(a[i][2])
    #Initialize the estimator in order to not clone the list 
    estimator = Estimator(sortedValues, sortedSize)
    DP = {}
    #DP(i) = DP[weight] = [value, estimatedValue, items]
    #DP(i+1) = DP2 (in order to reduce memory cost)
    DP[0]= (0, estimator.bestRelaxedValue(0,capacity), [])
    bestSolution = (0, [0]*n)
    for i in xrange(n):
        DP2 = {}
        for s, v in DP.iteritems():
            for x in xrange(2):
                weight=s+x*sortedSize[i]
                #Cut invalid capacity
                if(weight<=capacity):
                    newValue = v[0]+sortedValues[i]*x
                    #Merge branches with same weight
                    if (not weight in DP2 or newValue>DP2[weight][0]):
                        if(weight in DP2):
                            estimate = DP2[weight][1]-DP2[weight][0]+newValue
                        else:
                            estimate = estimator.bestRelaxedValue(i+1, capacity-weight)+newValue
                        #Cut bad branches
                        if(estimate>bestSolution[0]):
                            DP2[weight] = (newValue, estimate, v[2]+[x])
                            if(newValue>bestSolution[0]):
                                bestSolution = (newValue, v[2]+[x]+[0]*(n-i-1))
        DP = DP2
    #Take the best
    final_items = np.zeros(n, 'int')
    for i in xrange(n):
        final_items[hashTable[i]]=bestSolution[1][i]
    #Retrive data
    return bestSolution[0], final_items


