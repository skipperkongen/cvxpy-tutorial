# f(x) = 4x^(4) + 8x^(3) + x^(2) - 4x - 2
import cvxpy as cp

x = cp.Variable()

# Create no constraints
constraints = []

# Form objective
obj = cp.Minimize(4*x**4 + 8*x**3 + x**2 -4*x -2)

# Form and solve problem
prob = cp.Problem(obj)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value)
