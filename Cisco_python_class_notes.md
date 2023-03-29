Revup to Recert
execute directly by python3 filename.py
py3 releases 2008
last release in 2 is in 2010
in 3 all strings are unicode
clear sepration between strings and bytes
int/int returns a float

zen python style guide pep 8
indent with 4 spaces, never tab
max 79 charcaters per line
"flat is better than nested"
use Camel case for class names , lowercase or lowercase_with_uderscores
one statement perline




--
lesson 2
python3 -v or python -v tells you the version
the interacive interpriter is Read Eval Print Loop (REPL)
primary prompt is >>> secondary is ... which means more code is needed when you press enter a second time you are telling it you are done
== is used for comparison
** is power of 

OPERATOR TYPES
operand and operator these words mean the symbol like + or -

Operator types examples
Mathematical + - * / // % **
Comparison
Identity: is, is not
Contanintment in, not in
Bitwise: & | ~ ^ <<, >>
Boolean and, or not
Assignment: =, +=, -=

// floor division
Modulo %
Power **
+ and - are also unary operators

!= Inequaliy

Containment
in and not in
Bitwise is not commonly used

Assignment and augmented assignment
operator	Example		Description
=			x = 8		assign 8 to x
+=			x += 8		same as x = x + 8
-=			x -= 8		same as x = x - 8
op=			x -= 8		same as x = x op 8
*op can be any operator

Augmented assignments as things like 
x += 6

OPERATORS PRECEDENCE 
Highest precedence
**
----------------
+x, -x
----------------
*,/,//,%
----------------
+-
==, !=, <, <=, >, >=
in,not in,is,is not
----------------
not x
and
----------------
or
Lowest precedence

Precedence rules FOLLOW THE SAME AS YOU LEARNED IN MATH
Parentheses can be used to change precedence, the same with multiple parentheses 
MORE ON BOOLEAN OPERATORS
In other languages it might use 1 or 0 in place of True or False
True, False, None (none indicates absence of value) other languages might use NULL or nil
“And” truth table
x	y	x and y
False	False	False
False	True	False
True	False	False
True	True	True
To summarize: The results are True only if both operands are True

“or” truth table
x	y	x and y
False	False	False
False	True	True
True	False	True
True	True	True
To summarize: the result is True if at least one operand is True

“not” truth table
X	not x
True	False
false	True

Short circuit evaluation
Means: if the first operand is enough to determine the result, the second operand is not evaluated


