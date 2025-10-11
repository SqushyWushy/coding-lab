# level14 Notes

## What I Learned

- **Localhost** = the same computer I’m logged into.
- **Ports** = numbered doors where different programs listen.
- The program on port **30000** expected me to give it bandit14’s password.
- When I sent the correct input, it replied with the next level’s password.
- **Telnet / nc** let me connect directly to a port and “talk” to the program.
- Core idea: networking is basically input → output between my computer and a program listening on a port.

## My Solution

```
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
bandit14@bandit:~$ whoami
bandit14
bandit14@bandit:~$ cat bandit14
cat: bandit14: No such file or directory
bandit14@bandit:~$ telnet localhost 30000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

Connection closed by foreign host.
bandit14@bandit:~$
```
