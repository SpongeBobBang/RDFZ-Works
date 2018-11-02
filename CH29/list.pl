/* List, S3CS3 Stefan Yuzhao Heng */
/* Path: ['D:/RDFZ/S3 Courses/AL Computer Science/2017A2CS/CH29/list.pl']. */

join([],L,L).
join([H|T],L,[H|R]) :-
	join(T,L,R).

last([I],I).
last(_|I,T) :-
	last(I,T).

lastButOne([A,_],A).
lastButOne([_|T],R) :-
	lastButOne(T,R).

at(I,[I|_],1).
at(I,[_|T],N) :-
	at(I,T,P),
	N is P+1.

len([],0).
len([_|T],L) :-
	len(T,X),L is X+1. 

reverse([],[]).
reverse(A|B,R) :-
	reverse(B,X),
	join(X,[A],R).

equal([],[]).
equal([A|B],[A|C]) :-
	equal(B,C).

palindrome([A],[A]).
palindrome(L,R) :-
	eq(rev(R),L).