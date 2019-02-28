/*S3CS3 Stefan Yuzhao Heng */
/* Path: ['D:/RDFZ/S3 Courses/AL Computer Science/Prolog/kb.pl']. */

/* Fact */
cat(jack).
cat(blacky).
dog(erniu).
dog(aliang).

/* Formula */
animal(X) :- 
	dog(X);cat(X).
enemies(P1,P2) :- 
	cat(P1),dog(P2).
enemies(P2,P1) :- 
	dog(P2),cat(P1).

capitalCity(ottawa).
capitalCity(beijing).

/* Variable */
cityInCountry(ottawa,cannada).
cityInCountry(beijing,china).
cityInCountry(toronto,canada).

vegetable(celery).
vegetable(carrot).
meat(chicken).
meat(beef).
meat(lamb).

ingredient(chicken,chkSoup,250).
ingredient(carrot,chkSoup,100).

containsMeat(Dish) :- 
	ingredient(Ingred,Dish,_),meat(Ingred).

even(X) :- 0 is mod(X,2).
odd(X) :- not(even(X)).

factorial(0,1).

factorial(N,F) :- 
	X is N-1,
	factorial(X,Y),
	F is N * Y.

len([],0).
len([_|T],L) :-
	len(T,X),L is X+1. 

in(I,[I|_]).
in(I,[_|T]) :-
	in(I,T).