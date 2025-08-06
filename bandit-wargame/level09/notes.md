# level09 Notes

## What I Learned

In this level, I learned how to work with binary files on the command line. The file `data.txt` wasn’t a normal text file — it contained binary data, which caused `grep` to behave differently. When I tried `grep "=" data.txt`, it returned `binary file matches`, which meant it found something, but wouldn’t show the actual line because it detected non-text characters.

I also learned that using `grep -a` or `grep --text` forces `grep` to treat a file as text even if it's binary. However, the output was extremely messy and unreadable in this case.

The cleanest solution was to use the `strings` command. `strings` extracts just the printable ASCII characters from a binary file. Piping that output into `grep "="` made it easy to find the line that looked like a key-value pair with the password.

This was a good lesson in recognizing when a file isn’t plain text and how to handle it safely using the right tools.

## My Solution

```
bandit9@bandit:~$ strings data.txt
%H2j
Wr<h8w
^y=7
1ga7_
1{?kI
Y<w{f+
eR($
=?t)
}wW0
"J^F
=&]'
ZRu%h
========== the
If=q
g2>x
U.=4!
k={7
'7,h
lTOB=
8!R7
){6/
#6r&g
$N")
I,^IZ
c.K]_
i3w;T
3	{(
Z3EX
-;/C
{1p\)
FBy)s
c&RL
HZ{'R
YZ=*
f4yq
`Tk9
84|6G';:G
A4BSB
@qDy
Y;B:
c8i<
UzwOr	P
&u`rk*
l{BL
g6:<
g6~#z
zYEC
}7L]
!V4s{\
D========== password
"&2T
?nO6
aOqR
	,em]o
2!k$
pZO ^$$3
(	_s
,1Q}
-ddA
:^<(x
 U1-
8 `p^
rE1a+2F
r:V\x
q}bi
7B3[
9g&E
5O#:
\>W|
cv[QvQ#
w========== is
O9}P
`>{H
O(BF*
mg}
]v@3`
;Q^<
=*{>
jSgN
oa#(q
l?yX
hAkU
gki0
W$$D
sqKqS
HHc |
t8oW
}cpm%m9
]	G?
n4)%'
:mfZ
,x,b
y?o!AI
3tK2
=wu,
#OkwAx
iO}(
'jizM
-r[2
@9~U
~oP
ZG|X
&jWn
 QO'
1Vlir
-`(;q
4YZa
yZ X
|cf4Q~0\r
|h"@S
b/R]hO
9\W|.
LDzx
C<6Z
pNr$h
ilRv8
}Eh:
5+$&
tr]$
aT|j#
(4#H
sSL^
yr;)
h=O"
)*V*
*!Mr
Kx'(
4,=Y
@(+a
*y=1
H*B5
ti8G
@P(Y
/e_o
F!Rk
4=+0
y\	r{
3K&RAQ
S}H{d
[(ZBUkb
fb+],iGAB
'5w}
pVM;)Q(p
WH3G
I5H0
:opf
5!v{
.SeX+
^V-`-
;1CX
n0Y{^
U__U
%>3(H
zMlJ
]q-W{
24^h
JP1r
1nm.
7jwR
\&VT
(se,
n}TC
su[9
Q2U9
E>dd
$ZHN
5KoF_
	3U*
CtZ7
`&],
afo)
<+OPg/s
}|re
ta."Z
FxfQy
7]J=0
]|,G
ox	W
^B#b
$V^/
NC/L>
zSKc=
*I&0q
]2m==
m-@Wj
:ElX"
'R,t
0`D0
0OI>-
~O\K
Q\@Q
(Yf4/
z!SD
========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
t|HfY=
9R9|
%3oC<
4?9d
>]+N
D	z.
[gO9p
A"U}
n{VP
q).F
<[[S
|v/K;
3N%~
jm	v|"5:R
MCB'W
t*]N
,N+:
`fO.
'657
 Bn`
`S43
^ j+
^#@.V
<m\ip%
I[\n
:c)_
0`rf
nr/L
.0"x
'nw9
tilTk:
><}]
hu#v|
#ROT
9)Ig\3
YTBi
P_lx:r
Tyf.
\1\X
my&^n
WD#
L5@&h0
ZM9(Q
bandit9@bandit:~$ strings data.txt | grep "="
^y=7
=?t)
=&]'
========== the
If=q
U.=4!
k={7
lTOB=
YZ=*
D========== password
w========== is
=*{>
=wu,
h=O"
4,=Y
*y=1
4=+0
7]J=0
zSKc=
]2m==
========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
t|HfY=
bandit9@bandit:~$
```
