# level05 Notes

## What I Learned

The find command is a powerful tool used to search for files and directories recursively from a starting point (like . for current directory).
You can apply filters to find using flags like:
-type f to search for regular files only.
-size 1033c to find files of exactly 1033 bytes, where c stands for bytes (not blocks).
The command find . -type f -size 1033c helped isolate the one file that matched the challenge’s description in Bandit Level 5.
I learned that find by default uses 512-byte blocks if no size suffix is provided — so always use c for bytes when precision matters.
After finding the file, I used the cat command to read its contents and retrieve the password:

## My Solution

```
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere02  maybehere04  maybehere06  maybehere08  maybehere10  maybehere12  maybehere14  maybehere16  maybehere18
maybehere01  maybehere03  maybehere05  maybehere07  maybehere09  maybehere11  maybehere13  maybehere15  maybehere17  maybehere19
bandit5@bandit:~/inhere$ cd ..
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ find . -type f -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```
