# level15 Notes

## What I Learned

- Just like the last level, I had to give my current password to a program running on the server.
- This time the program was behind a **"locked door"** (port 30001) that only talks over a secure connection.
- `openssl s_client -connect localhost:30001` is the tool/command that does the "secret handshake" for me so I can talk through that door.
- Most of the big wall of text it prints is just details about the handshake — I can ignore it for now.
- The important part is still the same idea: **I give the correct input (password), and the program replies with the next password.**

## My Solution

```
Max Early Data: 0
---
read R BLOCK
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

closed
bandit15@bandit:~$
```
