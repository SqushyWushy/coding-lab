# level10 Notes

## What I Learned

In this level, I learned how to recognize and decode Base64-encoded data. The file `data.txt` contained a string that looked like random characters but ended with `==`, which is a common sign of Base64 padding. That was the clue that the file wasn’t plain text but encoded.

Base64 is an encoding system that takes binary data (like text or files) and converts it into a readable, printable format using only 64 safe characters. It’s commonly used when data needs to be transmitted or stored in places that can’t handle raw binary safely — like email, JSON, or HTTP.

I learned that `base64 -d` decodes Base64, while running just `base64` re-encodes the input again — which can layer the encoding unnecessarily. Re-encoding a Base64 string gives you a longer Base64 string, but it doesn’t get you back to the original message. That’s why decoding once was the correct move here.

It was also helpful to see that even though the content looked readable, it wasn’t the actual password — it had to be translated back from Base64 first.

## My Solution

```
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
bandit10@bandit:~$ cat data.txt | base64 -d
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
bandit10@bandit:~$ cat data.txt | base64
VkdobElIQmhjM04zYjNKa0lHbHpJR1IwVWpFM00yWmFTMkl3VWxKelJFWlRSM05uTWxKWGJuQk9W
bW96Y1ZKeUNnPT0K
bandit10@bandit:~$ cat data.txt | base64 | base64 -d | base64 -d
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
bandit10@bandit:~$
```
