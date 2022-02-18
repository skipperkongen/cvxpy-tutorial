# f(x)=2 x^(2) - 4x -2
# f(x)=4 x^(4)+8 x^(3)+x^(2)-4 x-2
import cvxpy as cp

x = cp.Variable()

# Form objective
obj = cp.Minimize(2*x**2 - 4*x -2)

# Form and solve problem
prob = cp.Problem(obj)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", x.value)
