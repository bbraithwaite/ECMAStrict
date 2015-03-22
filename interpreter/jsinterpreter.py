"""
Interpreter for the js-lang (subset of JavaScript).
"""

def eval_exp(exp, env):
    etype = exp[0]
    if etype == 'identifier':
        vname = exp[1]
        return env[vname]
    
    return exp[1]

def evaluate(node, env):
    ntype = node[0]
    vname = node[1]
    vtype = node[2]
    if ntype == 'var':    
        env[vname] = eval_exp(vtype, env)
    elif ntype == 'assign':
        env[vname] = eval_exp(vtype, env)

def interpret(parse_tree):
    env = {}
    for node in parse_tree:
        evaluate(node, env)
    return env
