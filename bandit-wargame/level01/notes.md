# level01 Notes

## What I Learned

- Filenames that start with a dash (`-`) can break normal command behavior because most Unix tools treat `-` as a signal for command-line **flags** (like `-l`, `-i`, etc.)
- When you type something like `cat -`, it doesn't read a file called `-` — it assumes you're trying to pipe in input from the keyboard (standard input).
- To read or interact with files that are named in a tricky or dangerous way (like just `-`), you need to be **explicit** with the command.

  I learned two ways to do that:
  - `cat ./-` → tells the shell to look in the current directory for a file literally named `-`
  - `cat -- -` → tells the command to stop parsing flags and treat `-` as a normal file

## My Solution

```
bandit1@bandit:~$ ls
-
bandit1@bandit:~$ cat ./-
263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```
