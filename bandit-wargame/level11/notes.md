# level11 Notes

## What I Learned

In this level, I learned about something called ROT13, which is basically a simple way to scramble text by rotating each letter 13 positions forward in the alphabet. So like, A becomes N, B becomes O, and so on — and it wraps around at the end. The cool part is that if you do it again, it just turns back into the original message, which makes it kind of fun to mess with.

I also got introduced to the tr command, which is used in the terminal to translate or swap characters one by one. That part was confusing at first, especially the 'A-Za-z' 'N-ZA-Mn-za-m' bit, but I eventually understood that it’s just defining two sets of characters — the original alphabet and the rotated version — and telling tr to map each character from the first set to the one in the second.

This level definitely helped me get more comfortable thinking through what a command is actually doing instead of just copying and pasting stuff blindly.

## My Solution

```
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
bandit11@bandit:~$ cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
bandit11@bandit:~$
```
