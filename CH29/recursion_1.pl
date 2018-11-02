/* Recursion-1, S3CS3 Stefan Yuzhao Heng */
/* Path: ['D:/RDFZ/S3 Courses/AL Computer Science/2017A2CS/CH29/recursion_1.pl']. */

factorial(0,1).
factorial(N,R) :- 
	X is N-1,factorial(X,Y),R is Y*N.

bunnyEars(0,0).
bunnyEars(N,R) :-
	X is N-1,bunnyEars(X,Y),R is Y+2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(N,R) :-
	P is N-1,Q is N-2,
	fibonacci(P,X),fibonacci(Q,Y),
	R is X+Y. 

even(X) :- 0 is mod(X,2).
odd(X) :- not(even(X)).

bunnyEars2(0,0).
bunnyEars2(N,R) :-
	X is N-1,even(X),bunnyEars2(X,Y),R is Y+2;
	X is N-1,odd(X),bunnyEars2(X,Y),R is Y+3.

triangle(0,0).
triangle(1,1).
triangle(N,R) :-
	X is N-1,triangle(X,Y),R is Y+X+1.

sumDigits(0,0).
sumDigits(N,R) :-
	X is div(N,10),
	sumDigits(X,Y),
	R is Y+mod(N,10).

isSeven(7).
countSeven(0, 0).
countSeven(N,R) :-
	D is mod(N,10),X is div(N,10),countSeven(X,Y),
	((isSeven(D), R is Y+1 );(not(isSeven(D)), R is Y)).