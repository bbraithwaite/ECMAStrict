# Throw-away code for testing/checking (to be deleted)

from lexer.jslexer import lexer

with open ("examples/run-file.js", "r") as jsFile:
    lexer.input(jsFile.read())
    result = [ ] 
    while True:
        tok = lexer.token()
        if not tok: break
        result = result + [(tok.type,tok.value)]
    print result