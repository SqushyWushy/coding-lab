# level08 Notes

## What I Learned

I learned how to identify unique lines in a file using a combination of `sort` and `uniq`. Specifically, I now understand that `uniq` only detects duplicate lines that are adjacent, so it's necessary to use `sort` beforehand to group all matching lines together.

I also learned the difference between `uniq -u` and `uniq -c`:

- `uniq -u` returns only lines that appear exactly once.
- `uniq -c` prefixes each line with the number of times it appears, which is useful for verifying frequency.

Finally, I understand that `sort -u` is **not** the same as `uniq -u` — it just removes duplicates, keeping one copy, regardless of how many times a line appears.

## My Solution

```
bandit8@bandit:~$ sort data.txt | uniq -c
     10 0KFjx0YNyiScs5m9bP7TALBQ1FnD0sBX
     10 206qRNE53VBTTvhS0CxxJzkv1RuAZGYu
     10 27Dt22kSXiiZyFL1yrwZR85RKGDGwcdH
     10 2gE83JhgGF2cXjV1ErugBYzGxe6stMMf
     10 2MNstSLPfXwoybkAp3ow0B0OHSq2QWUX
     10 2SPrkAR4oFkkPtWV3of0Z7rR7GkEArp5
     10 2t2sOTXDwEQeObR6WGAqXXDBBum2TR5d
     10 3bWHAOcHJggMxm5NgPkMpeA9GzFQG5vo
     10 3HT5LY4uSXQXsRRNK3uUW0enxPbarRYQ
     10 3mr60VTCYFuQFCgD2QRl2ojnF3nbcXdL
      1 4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
     10 51T6T1zM6XPVhTlNzVfqpM94ed3dS39n
     10 52JmRMNVxV0iiAep6voOaBOyfFqG62PC
     10 5J6LfcYB30UUQsUTyjMC0xDq76F6Syry
     10 5Ts8Y3d8pVhxsMzXNrgDHHpeVT2tqmhD
     10 6ZYAZU8PvoUSXATpzoPwQ2iqC3E2yvUS
     10 7idNOOeLKpD1sHOwRMYqnjvOizSIqAzN
     10 85X2LqA8sKG9VaeYz5isEZZkONVUHgom
     10 8ODDg1YTM4Ec87IKfBA16nDPXpdkVvGz
     10 93GCuRfoZRlPKB5nVKVvmtUAXuLhdSqO
     10 9mmJH4gjeyhXNbykPAIXamgwy7X7UITg
     10 9v0A8d12o1ej6szuvDlo5X7lvg3yjauQ
     10 AAkcadbQGhg7tgaeYZlgOddYIuboNyVI
     10 aDVZxgiMmhNZF58qnbtlZhk0vyr7CjLk
     10 AgsVNPr1QnFQZLxbCFAFNm2292Wh3Er5
     10 alXiX56M27WErPzMItK78pWSTb6phftn
     10 AoXzYWS0kjTdLngcV7adTU4QfyvrPtJe
     10 B0wMy53xLbCcfypsUjhAEr712zfUEpkG
     10 bm74Prqzqe7H2llEWi59bR11UpiUr1JG
     10 br1kdEDM9ot0cALaqeTQDJDNk1e0Xfvf
     10 bsfVo5CyQVMqa5lfvPGQECRn6rFoc2hM
     10 bWxv7GJDLd20QiXbzj6eAoSEJjYcadq6
     10 D9LalkWr9TnwEn8Q9QLLnLfEOeNjroVz
     10 dd6KJP6wrHRv5uIAKWLUoL98XrpUAKGC
     10 DhtfYwBmJO8AsORBVlCQykgH3ExEzDma
     10 ECUYUMcwx2KjqTa9fxPgzFwlYOzOUlBW
     10 ennBEbDSxwgbU4TFj9WOWJJmC8PT7t4f
     10 eVOBxAYQqFJ1SRvZq8UEuIZtTHjuSGs7
     10 fs2ySmJlASO3vyo1WAyYkVyyZb1W9vVW
     10 GIVuZ06PWjyYzTVjbptxdFF4FOItcv2q
     10 gNo6OcO0cZfz8kGZhGRIbx6Dp5TkQzGS
     10 gQmgM8PieNyiJP5jwzsFLdExhcfkeadj
     10 GwjpFxdCZhrJvvOVDqDAA6whjpt73z2Y
     10 hb4B6eLVcpITAY0BEieRgfbKlh8dZxq0
     10 HmH5UuE7ag9U9J0Kx5IkiwNYX84MUXBl
     10 hNPzbsVKSUDq8yTthvuxjnrkfE9Q6u4e
     10 HoDEYgURvsceHHMDAR50I8kyDrHoBAHj
     10 Hry5CJ0jbyFS18Z2M2COxjupnDNcuejR
     10 HTKEYDz9zojDKBzCUoJd7CBKzAaE2Mtx
     10 iqhmcCslaOLRVWo3l1C0uudWTm70xibA
     10 IYLYluarRDCGk5Vad7NPfCGmY3yBoMFh
     10 JCk9JBcSglaeMztzsLtreveSidHLTckX
     10 jh1q1B9HoLzUtcD8m3BBIx89idCpVAOQ
     10 jIRsdzOzQf3hTzfaHTwusRnP5o7LRCXg
     10 jrqXY8T6A1dU31QEjLbATELr5Wu2xu7U
     10 kc3g7DoeeXNrsPHjDYzYrxApROdMdFpV
     10 klnp6EGe6obv6nce68KiK74EySYrvkCL
     10 kOpusTECh0lACB1uDVuSJdc7uyeWSijL
     10 Kp8tlnJCpomZJHMlu4b8Go79p1uOcqBt
     10 KpH5fMjIMQzm0i7SmmenmdkTkcpdUCMR
     10 kvpVao8Nd5xGIvrgrEvYKUUbkIVvLO30
     10 kYWAybafyWBbVkbPMzA8r3c7GDdvLPg5
     10 lpzwSxSs5ZOB0lKQRW5czUbXxMrm3dEe
     10 Myr0aiVlXy7ZBUcaUMbGCCEsSlJxNqH9
     10 nA5ZaDzOI6ghzt7vXnbFnXtibNxwqNz7
     10 nbknQRevmS71bxvHJIGZFPrRs1VFIHOf
     10 NCR7eU4L9Odk2DTEMgYps2Vo4brXPh8H
     10 NIBemZRo4rDgHCC3prbHlaydyRotWq5l
     10 NLUlQRdlqR7hmi2KRELetFoqNL7BaQ6b
     10 ONv1DzNWKfPCn5XIaBbKU6ynY1sdUyP2
     10 oqMErvJXHlo4B6xCYebiVvHwCLX7ieNS
     10 oTKift8S6bPcuQTAwR4NAEaBOL7J5owy
     10 pKROSltPiWBLg5d0pOiQrKYbi2pmv2NA
     10 PnqTDd7bjt1WQurZFEPbW5VV5Pnp7ay4
     10 Q4dqghYemzzt4dYc3739GcM8HzO0YgDm
     10 QP85LJyLsQTUT7kom7Vsi38idtrLT4gB
     10 qRNN29pIRiY1ODwwkbRVJyHuQRU3Juef
     10 r8mTdXVCPfLjoGqSqsvJfRZ7eObxkb83
     10 rFkArD8DJvJJFVr635inD2TSEEq7Ilej
     10 rJrYMvkpjF6ao3oSaMH9hXN2WhpfL3Ba
     10 ro8XdJOd4djcsJFNkkAw4ybydZHp6GzT
     10 sm3wGI2XdmpC2rHZFQdvYQwmQKcsc1L9
     10 SNLoaqqqWnhdofixLOc9cF770CbVqamg
     10 SSwsGzxqHeS0H5jirGsyrDHhnvElDWnb
     10 SukiFx4joXXBFGp22aQ2Wbd2CI6XMVH8
     10 SW6fQ9JW02h8NlxxtSsUquZa3zgIOWon
     10 U5JWCgnoXUeaN8WK578NbBxY1Ia8WUtb
     10 U9XNOPRyt2eq61LWsxADPXbIcO3J9iit
     10 uD2zqAPGiu5mrIVdxbUSgWwKQgItC9GH
     10 v1K6f8r4xSh2p9UZrgNsw9Lph3vD009Y
     10 vmkNsA7kvr4Emux4gPsbZUFvXYn9oUQp
     10 vNiSmQ930qBWxnQwoJxgu2zYtYuE5evy
     10 VyGI0jsb8gStsVQbcNkBFeXnxoSBJPxe
     10 wdduZjINs8TQYx3ejJFq5tJTYwvqBeRl
     10 WeiUpJBtplRUupD4DppdWFnnpHujRNZ3
     10 woTehaYBwNP2c1Akuvk82y1AVBgGm5QC
     10 XliGfuvvrcfORMPNcWLu8bNxXIvrBqdV
     10 xo6n8O1IE9rSEBGKOGNDWKwFyqZLKUFh
     10 xQ09TWzF7J6oR40cFuTl4mQufbWr8Joj
     10 ycCiUT9KCUDzSbbrpQduOpl88AjjNVmc
     10 yosL7anMOURQRZHzLkVLBZxl6Ol7AOmh
bandit8@bandit:~$ sort data.txt | uniq -u
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
bandit8@bandit:~$
```
