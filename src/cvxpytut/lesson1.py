# Classic
import cvxpy as cp

x = cp.Variable()
y = cp.Variable()

# Create two constraints
constraints = [
    x + y == 1,
    x - y >= 1
]

# Form objective
obj = cp.Minimize((x - y)**2)

# Form and solve problem
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value.round(3), y.value.round(3))
