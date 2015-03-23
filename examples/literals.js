'use strict';

// Playground for checking JS Grammar with node.

console.log('-- null ---');

// Null literal

var foo = null;

// not allowed!
// var null = 'foo';

console.log(typeof(foo));
console.log(typeof(null));

if (foo === null) {
	console.log('foo is null');
}

if (foo === undefined) {
	console.log('foo is undefined');
}

// Boolean literal

console.log('-- bool ---');

var trueFoo = true;
var falseBar = false;

console.log(typeof(trueFoo));
console.log(typeof(falseBar));

// not allowed!
//var true = 'foo';
//var false = 'bar';

// Numeric Literals

// Syntax

// Numbers can be decimal or hex literals.

// NumericLiteral :: 
// 	DecimalLiteral
// 	HexIntegerLiteral

console.log('-- decimals ---');


console.log('* DecimalLiteral');
// DecimalLiteral ::
// 	DecimalIntegerLiteral . DecimalDigits (opt) ExponentPart (opt)
// 	. DecimalDigits ExponentPart (opt)
// 	DecimalIntegerLiteral ExponentPart (opt)

var decIntLit = 0.;
var decIntLitDecExp = 1E-1;
var decLit = .012;
console.log(decIntLit);
console.log(decLit);
console.log(decIntLitDecExp);


var exp1 = 1.0e1;
var exp2 = .0e1;
var exp3 = 2E1;
var exp4 = 2e+1;
var exp5 = 2e-2;
console.log(exp1);
console.log(exp2);
console.log(exp3);
console.log(exp4);
console.log(exp5);





console.log('* DecimalIntegerLiteral');
// DecimalIntegerLiteral :: 
// 	0
// 	NonZeroDigit DecimalDigits (opt)

var decLitZero = 0;
//var decLitNotZero = 01; - NOT ALLOWED
var decLitNotZero = 1;
var decLitNotZeroWithOpt = 1012; // DecimalDigits(0-9)*

console.log(decLitZero);
console.log(decLitNotZero);
console.log(decLitNotZeroWithOpt);


console.log('-- hex ---');

// HexIntegerLiteral :: 
// 	0x HexDigit 
// 	0X HexDigit
// 	HexIntegerLiteral HexDigit

//  HexDigit :: 
//		one of 0123456789abcdefABCDEF

// can be zero 0x, or 0X
var hexExamplex = 0x1;
var hexExampleX = 0X2;
var hexExampleA = 0xA;
var hexExamplea = 0xF0;

console.log(hexExamplex);
console.log(hexExampleX);
console.log(hexExampleA);
console.log(hexExamplea);

//console.log('-- octal ---');
//console.log(051); octal literal example
console.log('-- exp ---');
console.log(1e1);