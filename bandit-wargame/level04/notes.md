# level04 Notes

## What I Learned

Filenames starting with a dash (-) can cause issues with commands like cat, because they’re interpreted as command-line options.
You can safely reference these files using:
-- (e.g., cat -- -file07) to stop option parsing
./ (e.g., cat ./-file07) to provide an explicit path
The file command is extremely useful for identifying the type of content within a file. It doesn’t rely on extensions — it reads the actual data to determine if it’s text, binary, encrypted, etc.

Wildcards like _ can be used to reference multiple files at once, and ./_ ensures paths are unambiguous and safe from flag misinterpretation.

Among many binary/noisy files, the password was hidden in the one readable ASCII text file.

## My Solution

```
bandit4@bandit:~/inhere$ ls -l
total 40
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file00
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file01
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file02
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file03
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file04
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file05
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file06
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file07
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file08
-rw-r----- 1 bandit5 bandit4 33 Apr 10 14:23 -file09
bandit4@bandit:~/inhere$ ls -a
.   -file00  -file02  -file04  -file06  -file08
..  -file01  -file03  -file05  -file07  -file09
bandit4@bandit:~/inhere$ ls
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
bandit4@bandit:~/inhere$ file ./*
./-file00: PGP Secret Sub-key -
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```
