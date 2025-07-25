# level03 Notes

## What I Learned

In this level, I learned that in Unix-based systems like Linux, any file that starts with a dot (.) is considered hidden. This means it won’t show up when I use the regular ls command to list files in a directory. To see hidden files, I have to use ls -a, which tells the system to list all files, including the ones starting with a dot. I also learned that I can combine flags with ls, like -l for long-format listings and -a for showing all files, by typing ls -la.

Another important thing I picked up was how to deal with weird or tricky file names. The file in this level was named ...Hiding-From-You, and even though it looked strange with the three dots, it’s actually just a normal file name. The extra dots don’t give it any special behavior — they just make it easy to miss or hard to work with unless you know what you’re doing. To safely interact with files like that, I can put the file name in quotes or use a relative path like ./filename. This level really helped me get more comfortable with the basics of file visibility and working with the shell in a more precise way.

## My Solution

```
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Apr 10 14:23 .
drwxr-xr-x 3 root    root    4096 Apr 10 14:23 ..
-rw-r----- 1 bandit4 bandit3   33 Apr 10 14:23 ...Hiding-From-You
bandit3@bandit:~/inhere$ cat ..
../                 ...Hiding-From-You
bandit3@bandit:~/inhere$ cat ..
../                 ...Hiding-From-You
bandit3@bandit:~/inhere$ cat ...Hiding-From-You
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
bandit3@bandit:~/inhere$ cat ./...Hiding-From-You
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
bandit3@bandit:~/inhere$
```
