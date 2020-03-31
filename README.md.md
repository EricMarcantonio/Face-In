# Facial Recognition Check In System

Originally built for checking in users at a hackathon, this project aims to check users in after detecting their face. Written in ``python``.

The design of the program is as follows
```flow  
st=>start: Start:>http://www.google.com[blank]
e=>end:>http://www.google.com
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?:>http://www.google.com
io=>inputoutput: catch something...
para=>parallel: parallel tasks

st->op1->cond
cond(yes)->io->e
cond(no)->para
para(path1, bottom)->sub1(right)->op1
para(path2, top)->op1
```



<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc0NDQ0MzM0MSwtMTMxODM4NTI0MV19
-->