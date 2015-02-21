import integrator

def squared(x):
    return x*x

print(integrator.riemann_integration(squared, 1, 0, 3))

"""

0 + 1 + 4

"""
