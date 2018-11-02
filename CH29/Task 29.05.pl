factorial(0,1).
factorial(N,F) :- 
	X is N-1,
	factorial(X,Y),
	F is N * Y.

/* 120 */