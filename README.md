# ECMAScript (JavaScript) Implementation

As a coding challenge, during evenings and weekends I've been implementing a lexer, parser, and runtime of the ECMAScript language specification.

I chose Python as the language so that I could make use of the excellent [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/) implementation.

I'm not aiming for 100% completion, likely a sub-set of the language that resembles "strict mode".

For reference you can check out:

* [Standard ECMA-262 Spec - 5.1](http://www.ecma-international.org/publications/standards/Ecma-262.htm)
* [Annotated version of the ES5 spec](https://es5.github.io/#toc)

Still work in progress, current status:

* lexer (near complete)
* parser (50% complete)
* runtime (started implementing type system)
* interpreter (basic POC)