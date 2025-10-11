# level13 Notes

## What I Learned

## My Solution

```
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$

coding-lab on  main [?]
❯ scp -P 2220 bandit13@bandit.labs.overthewire.org:~/sshkey.private .
                         _                     _ _ _
                        | |__   __ _ _ __   __| (_) |_
                        | '_ \ / _` | '_ \ / _` | | __|
                        | |_) | (_| | | | | (_| | | |_
                        |_.__/ \__,_|_| |_|\__,_|_|\__|


                      This is an OverTheWire game server.
            More information on http://www.overthewire.org/wargames

bandit13@bandit.labs.overthewire.org's password:
sshkey.private                                                                                                                      100% 1679     5.3KB/s   00:00

coding-lab on  main [?] took 17s
❯ ls
assembly        c           CS50x   hackathons  java  python     rust
bandit-wargame  cs-courses  cyb102  html        md    README.md  sshkey.private

coding-lab on  main [?]
❯ chmod 600 sshkey.private

coding-lab on  main [?]
❯ ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

bandit14@bandit:~$ ls
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
bandit14@bandit:~$
```
