var foo = 'bar';
var bar = 'baz';

// var baz = '\'; Not allowed, escape slash invalid
// var baz = '''; Not allowed, quote must be escaped


var escapeSequenceSingleQuote = 'hello \'';
var escapeSequenceDoubleQuote = 'hello \"';
var escapeSequenceBackSlash = 'hello \\';

var escapeSequenceB = 'hello \b';

var multiline = 'this \
spans \
multiple \
lines.';

// SourceCharacter ::
// 	any Unicode code unit

// LineTerminatorSequence :: 
// 	<LF>
// 	<CR> [lookahead 􏰀 <LF> ] 
// 	<LS>
// 	<PS>
// 	<CR> <LF>

// \b	Backspace
// \f	Form feed
// \n	New line
// \r	Carriage return
// \t	Tab
// \v	Vertical tab
// \'	Apostrophe or single quote
// \"	Double quote
// \\	Backslash character

// EscapeSequence :: 
// 	CharacterEscapeSequence
// 	0 [lookahead 􏰀 DecimalDigit] 
// 	HexEscapeSequence 
// 	UnicodeEscapeSequence


console.log(escapeSequenceSingleQuote);
console.log(escapeSequenceDoubleQuote);
console.log(escapeSequenceBackSlash);
console.log(escapeSequenceB);
console.log(multiline);


var example5 = 'hello\
world';
console.log(example5);

