Tasks C28
===
S3CS3 Stefan Yuzhao Heng

.01
--- 
* A <- 2   
LDM #2   
STO A 

* B <- 10   
LDM #10   
STO B 

* C <- A + B   
LDD A   
ADD B   
STO C 

* D <- A - B   
LDD B   
XOR #&FF   
INC ACC   
ADD A   
STO D 

.02 
---
|Label|Opcode&Operand|
|:-:|-|
||LDD A|
||CMP #0| 
||JPE ELSE|
|THEN|STO B| 
||JMP ENDIF| 
|ELSE|LDD B|
||DEC ACC|
||STO B| 
|ENDIF|...|

.03 
---
|Label|Opcode&Operand|
|:-:|-|
||LDM #1|
||STO Number|
||LDM #0| 
||STO Totoal| 
||LDM #5| 
||STO Max| 
|LOOP|LDD Total| 
||ADD Number| 
||STO Total| 
||LDD Number|
||INC ACC| 
||STO Number|
||CMP Max| 
||JPN Loop| 

.04 
---
|Label|Opcode&Operand|
|:-:|-|
||LDM #0|
||STO Count| 
||LDM #78| 
||STO Letter| 
|LOOP|LDD Count| 
||INC ACC| 
||STO Count| 
||IN| 
||CMP Letter|
||JPN LOOP|

.05
---
|Label|Opcode&Operand|
|:-:|-|
||LDM #0|
||STO Count| 
||LDM #78|
||STO Letter|
|LOOP|LDD Count|
||INC ACC|
||STO Count|
||IN|
||CMP Letter|
||JPN LOOP|
||LDM #48|
||ADD Count|
||Out|

.06
---
StackBase: Address of beginning of stack   
...: Next part of the program

|Label|Opcode&Operand|
|:-:|-|
||LDD StackBase|
||STO Pointer|
|LOOP1|IN|
||CMP #13|
||JPE LOOP2|
||STI Pointer|
||LDD Pointer|
||INC ACC|
||STO Pointer|
||JMP LOOP1|
|LOOP2|LDD Pointer|
||CMP StackBase|
||JME END|
||LDI StackPointer|
||OUT|
||LDD StackPointer|
||DEC ACC|
||STO StackPointer|
||JMP LOOP2|
|End|...|
