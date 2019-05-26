## Import PuLP modeler required functions
from pulp import LpProblem, LpVariable, LpMinimize, LpStatus, lpSum, value

#### Problem data

# Indexes
foods = [ 'a', 'b' ]
nutrients = [ 'protein', 'calcium', 'vitamin' ]
# Parameters
# Here we need to define three parameters: 
# (a) the quantity of nutrient j per kilogram of food i -> p[i][j]
# (b) the minimum intake required of nutrient j -> q[j]
# (c) the cost per kilogram of food i -> c[j]
p = {
    'a': { 'protein': 30, 'calcium': 2, 'vitamin': 10 },
    'b': { 'protein': 45, 'calcium': 1, 'vitamin': 5 }
}
q = { 'protein': 700, 'calcium': 28, 'vitamin': 150 }
c = { 'a': 0.3, 'b': 0.35 }

#### Problem statement

# Create a variable to store problem information
myProblem = LpProblem('Diet Problem', LpMinimize)
# Create a variable to store decision variables;
# they will be named as <name>_<index> by PuLP modeler
x = LpVariable.dicts(
    'food', # name
    foods,  # array of indexes
    0       # lower bound
)
# Add objective function (must be added first)
myProblem += lpSum([c[i] * x[i] for i in foods])
# Add problem constraints
for j in nutrients: myProblem += lpSum([p[i][j] * x[i] for i in foods]) >= q[j]
# Note there is no need to include x[i] >= 0 constraint since x has been
# created with lower bound equals to zero

#### Problem solution

myProblem.writeLP('DietModel.lp')
myProblem.solve()   # This will use the default PuLP solver
# Print the results
status = LpStatus[myProblem.status]
print('Status:', status)
if status == 'Optimal':
    print('Optimal values:')
    for v in myProblem.variables(): print(v.name, '=', v.varValue)
    print('Optimal objective function value:', value(myProblem.objective))
