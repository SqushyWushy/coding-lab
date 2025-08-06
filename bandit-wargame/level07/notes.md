# level07 Notes

## What I Learned

I learned how to use the `grep` command to search for specific patterns inside a file. `grep` stands for "global regular expression print" and comes from an old `ed` editor command (`g/re/p`). It prints lines in a file that match a given pattern.

I also realized that while using `cat` and piping to `grep` works, it's not necessary. `grep` can read the file directly, making the command cleaner and more efficient.

This level helped reinforce how useful pattern searching can be when working with large files and trying to extract specific information like a password.

## My Solution

```
bandit7@bandit:~$ cat data.txt | grep millionth
millionth	dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
bandit7@bandit:~$ grep millionth data.txt
millionth	dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
bandit7@bandit:~$
```
