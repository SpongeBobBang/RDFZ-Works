Exam-Style Questions 
===
S3CS3 Stefan Yuzhao Heng

1
---
a. 
i. & ii.
```Prolog
cityIn(london,uk).
iVisited(strabourg).
```

b.
```Prolog
chile, argentina
```

c.
```Prolog 
countriesIVisited(Country) :-
	iVisited(City),cityIn(City,Country).
```

2
---
a.
i. Clause 01   
ii. Clause 15   

b.
i. ii. iii.
```Prolog
Who = jack.

False.

False.
```

c. 
i. 
```Prolog
qualifiedDriver(Driver,car).
```

ii.
```Prolog
theoryOnly(X) :-
	passedTheoryTest(X),not(passedDrivingTest(X)).
```

d.
```Prolog
C11 hasLicence(mike). /* - True */ 
C01 minimumAge(car,L). /* - True, L = 18. */ 
C05 age(mike,A). /* - True, A = 17. */ 
C15 A >= L. /* - False. */ 

/* So */ False.
```
