# Import PuLP modeler required functions
from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, lpSum, value

#### Problem data

# Indexes
items = [ i for i in range(4) ]
# Parameters
v = [ 15, 10, 9, 5 ]    # values
w = [ 1, 5, 3, 4 ]      # weights
C = 8                   # total capacity

#### Problem statement

myProblem = LpProblem('Knapsack Problem', LpMaximize)
x = LpVariable.dicts(
    'item', items,
    cat='Binary'    # Indicate PuLP modeler decision variables are binary
)
myProblem += lpSum([v[i] * x[i] for i in items])    # Objective function
myProblem += lpSum([w[i] * x[i] for i in items]) <= C   # Capacity constraint

#### Problem solution

myProblem.writeLP('KnapsackModel.lp')
myProblem.solve()
# Print the results
status = LpStatus[myProblem.status]
print('Status:', status)
if status == 'Optimal':
    print('Optimal values:')
    for v in myProblem.variables(): print(v.name, '=', v.varValue)
    print('Optimal objective function value:', value(myProblem.objective))
