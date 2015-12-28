"""
lambdas:
lambda expressions (sometimes is called lambda forms) are used to create anonymous
functions. The expression lambda arguments: expression yields a function object.
The unnamed object behaves like a function object defined with the following.
"""

lambda_expr ::= "lambda" [parameter_list]: expression
lambda_expr_nocond ::= "lambda" [parameter_list]: expression_nocond

def <lambda>(arguments):
    return expression


"""
origin function
"""
def f(x):
    return x+2
f(3)

"""
which can be replace by
"""
g = lambda x: x+2
g(3)
(lambda x: x+2)(3)

"""
real world lambda functions
"""
process_function = collapse and (lambda s: " ".join(s.splite())) or (lambda s: s)
