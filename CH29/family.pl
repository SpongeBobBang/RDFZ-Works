/* Family, S3CS3 Stefan Yuzhao Heng */
/* Path: ['D:/RDFZ/S3 Courses/AL Computer Science/2017A2CS/CH29/family.pl']. */

male(stefan).
male(ken).
male(matthew).
male(elijah).
male(oscar).
male(matt).
female(elena).
female(hayley).
female(katherine).

parent(stefan,ken). /* (S as parent, i.e. Stefan is parent of Ken) */
parent(elena,ken).
parent(stefan,matthew).
parent(elena,matthew).
parent(stefan,hayley).
parent(elena,hayley).
parent(katherine,oscar).
parent(katherine,matt).
parent(elijah,oscar).
parent(elijah,matt).
parent(dom,stefan).
parent(dom,elena).
parent(letty,stefan).
parent(letty,elena).
parent(dom,katherine).
parent(dom,elijah).
parent(letty,katherine).
parent(letty,elijah).

brother(A,B) :- /* A as brother */
	parent(P,A),parent(P,B),male(A),not(A=B).

sister(A,B) :- /* A as sister */
	parent(P,A),parent(P,B),female(A),not(A=B).

son(A,B) :- /* A as son */ 
	parent(B,A),male(A).

daughter(A,B) :- 
	parent(B,A),female(A).

married(A,B) :- 
	parent(A,K),parent(B,K),not(A=B).

ancestor(A,B) :- 
	parent(A,B);
	parent(A,T),ancestor(T,B).
