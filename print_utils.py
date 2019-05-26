from pulp import LpStatus, value

def printModelSolution(model):
    status = LpStatus[model.status]
    print('Status:', status)
    if status == 'Optimal':
        print('Optimal values:')
        for v in model.variables(): print(v.name, '=', v.varValue)
        print('Optimal objective function value:', value(model.objective))