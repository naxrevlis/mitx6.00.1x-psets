def evalQuadratic(a, b, c, x):
    return a * x * x + b * x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    # Your code here
    return evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)

print twoQuadratics(-1.22,-9.64,5.3,-1.7,-4.4,-5.71,-2.19,6.64)
