Exam-Style Questions C28
===
S3CS3 Yuzhao Heng Stefan 

1
---
a. 
Takes 2 binary bits, retuns 1 if both inputs are 1, otherwise return 0. 

b. 
AND #00001111

c.
IN   
AND Mask
LSL #4   
STO   
IN   
AND Mask   
OR Result   
STO Result   
END   
   
&0F      

2
---
LDR #0   
IN   
STI STRING   
INC IX
CMP #33
END
