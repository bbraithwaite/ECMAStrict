"""
Interpreter for the js-lang (subset of JavaScript).
"""

def eval_exp(exp):
	return exp[1]

def evaluate(node, env):
    if node[0] == 'var':
    	var_name = node[1]
    	var_type = node[2]
    	env[var_name] = eval_exp(var_type)


def interpret(parse_tree):
    env = {}
    for node in parse_tree:
        evaluate(node, env)
    return env

