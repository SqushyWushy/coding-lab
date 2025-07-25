# level02 Notes

[Bandit Level 2](https://overthewire.org/wargames/bandit/bandit2.html)

## What I Learned

This level is all about dealing with **filenames that contain spaces**, which are dangerous and tricky if you don’t handle them properly.

In the shell:

- A **space** is normally a separator between arguments.
- So if a file is named `"spaces in this filename"`, typing `cat spaces in this filename` doesn’t work — it’s treated as four separate arguments.

I already knew how to handle this using:

- `\` (escaping the spaces)
- TAB autocompletion (lets the shell handle escaping for me)

What I **learned for the first time** here is that:

- You can also just **wrap the whole filename in quotes**, and the shell will treat it as a single argument — no escaping needed.

## My Solution

```
bandit2@bandit:~$ cat spaces\ in\ this\ filename
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
bandit2@bandit:~$ cat spaces\ in\ this\ filename
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
bandit2@bandit:~$ cat "spaces in this filename"
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
bandit2@bandit:~$
```
