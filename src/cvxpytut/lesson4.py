# f(x) = 4x^(4) + 8x^(3) + x^(2) - 4x - 2
import cvxpy as cp

x = cp.Variable()
TARGET = 2

def demand(x):
    return (-0.5 * x + 5)

def revenue(x, demand):
    return x * demand(x)

constraints = [
    demand(x) <= TARGET
]

# Form objective
#obj = cp.Maximize(revenue(x, demand))
obj = cp.Maximize(-0.5 * x**2 + 5 * x)
#obj = cp.Maximize(-0.5 * x*x + 5 * x)


# Form and solve problem
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value)
