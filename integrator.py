def riemann_integration(funx, dx, beginning, end):

    i = beginning
    sum = 0
    while i < end:
        sum += funx(i) * dx
        i += dx

    return sum