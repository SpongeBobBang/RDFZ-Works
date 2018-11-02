/* Path: ['D:/RDFZ/S3 Courses/AL Computer Science/2017A2CS/CH29/Task 29.06.pl']. */

writeList([]).
writeList([H|T]) :-
	write(H),nl,writeList(T).