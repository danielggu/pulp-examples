## Import PuLP modeler required functions
from pulp import LpProblem, LpVariable, LpMinimize, LpStatus, lpSum, value

## Problem data
availableFoods = [ 'a', 'b' ]
# Quantity of nutrients per kilogram of each food (a, b)
protein = { 'a': 30, 'b': 45 }
calcium = { 'a': 2, 'b': 1 }
vitamin = { 'a': 10, 'b': 5 }
# Cost of each food per kilogram
costs = { 'a': 0.3, 'b': 0.35 }
# Minimum nutrients intake
proteinRequirement = 700
calciumRequirement = 28
vitaminRequirement = 150 

## Problem statement 
# Create a variable to store problem information
myProblem = LpProblem('Diet Problem', LpMinimize)
# Create a variable to store decision variables;
# they will be named as <name>_<key> by PuLP modeler
x = LpVariable.dicts(
    'food',         # name
    availableFoods, # dictionary with keys
    0               # lower bound
)
# Add objective function (must be added first)
myProblem += lpSum([costs[i] * x[i] for i in availableFoods])
# Add problem constraints
myProblem += lpSum([protein[i] * x[i] for i in availableFoods]) >= proteinRequirement
myProblem += lpSum([calcium[i] * x[i] for i in availableFoods]) >= calciumRequirement
myProblem += lpSum([vitamin[i] * x[i] for i in availableFoods]) >= vitaminRequirement

## Solve problem using default solver
myProblem.writeLP('DietModel.lp')
myProblem.solve()

## Print the results
print('Status: ', LpStatus[myProblem.status])
for v in myProblem.variables(): print(v.name, '=', v.varValue)
print('Objective function value:', value(myProblem.objective))
