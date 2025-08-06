# level12 Notes

## What I Learned

This level honestly felt like trying to open a Russian nesting doll that just never ends. At first, I had no idea what I was even looking at, but after going through it step-by-step, I started to understand how different types of file compression work — and how to undo them.

I learned that the xxd -r command is used to reverse a hex dump and turn it back into a real binary file. After that, the file command became my best friend — it tells you what kind of file you’re dealing with, which is super helpful when a file doesn’t have a proper extension.

From there, it was all about figuring out how to unpack different layers of compression. I got hands-on practice with:

- gunzip for .gz files (gzip),
- bunzip2 for .bz2 files (bzip2),
- and tar -xvf for .tar archives (which are like folders packed into one file).

I also learned that sometimes you have to rename files so the system knows what they actually are, even if they were originally named something generic like data. And most importantly, I realized why it’s a bad idea to just cat random files that aren’t plain text — your terminal will spit out a wall of cursed nonsense.

Even though I mostly just followed commands to get through it, I now actually understand the logic behind the tools and why the steps mattered. It wasn’t just about unzipping files — it was about recognizing file formats, knowing what tools to use, and peeling back each layer in the right order. Definitely one of the most frustrating but rewarding levels so far.

## My Solution

```
bandit12@bandit:/home$ cd bandit12
bandit12@bandit:~$ ls
data.txt
bandit12@bandit:~$ cd /tmp
bandit12@bandit:/tmp$ ls
ls: cannot open directory '.': Permission denied
bandit12@bandit:/tmp$ mktemp -d
/tmp/tmp.OXG3P5sDZn
bandit12@bandit:/tmp$ ls
ls: cannot open directory '.': Permission denied
bandit12@bandit:/tmp$ cd /tmp/tmp.OXG3P5sDZn
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ cp ~/data.txt .
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ ls
data.txt
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ xxd -r data.txt > data.bin
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data.bin
data.bin: gzip compressed data, was "data2.bin", last modified: Mon Jul 28 19:03:31 2025, max compression, from Unix, original size modulo 2^32 574
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ gzip compressed data, was "data2.bin"
gzip: compressed: No such file or directory
gzip: data,: No such file or directory
gzip: was: No such file or directory
gzip: data2.bin: No such file or directory
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ mv data.bin data.gz
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ gunzip data.gz
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ ls
data  data.txt
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data
data: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ mv data data.bz2
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ bunzip2 data.bz2
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data
data: gzip compressed data, was "data4.bin", last modified: Mon Jul 28 19:03:31 2025, max compression, from Unix, original size modulo 2^32 20480
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ mv data data.gz
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ gunzip data.gz
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ tar -xvf data
data5.bin
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ ls
data  data5.bin  data.txt
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data5.bin
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ tar -xvf data5.bin
data6.bin
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ mv data6.bin data.bz2
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ bunzip2 data.bz2
bunzip2: Output file data already exists.
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ cat data
data5.bin0000644000000000000000000002400015041744603011244 0ustar  rootrootdata6.bin0000644000000000000000000000033715041744603011254 0ustar  rootrootBZh91AY&SY�c1��jP��z2hb2ta@
2       ���OPi"z
 FFC ѓM
       #@7>8P�@�9�3h3�Ă�" >DpsQ�7�NH��أ���7kegf���VGⰩ#/�Ct`'�\��V�u�]�$Sк"(@��lmy����0IM̪Ԕ�g�P(�w$S
�3bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ rm data
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ bunzip2 data.bz2
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data
data: POSIX tar archive (GNU)
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ cat data
data8.bin0000644000000000000000000000011715041744603011252 0ustar  rootroɇhdata9.bin
�.6*K	q)w��>�2A1bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ tar -xvf data                �HU(H,..�/JQ�,Vp�7M)w+N6HNJ���0Ȱ�2J
data8.bin
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ data8.bin
data8.bin: command not found
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data8.bin
data8.bin: gzip compressed data, was "data9.bin", last modified: Mon Jul 28 19:03:31 2025, max compression, from Unix, original size modulo 2^32 49
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ mv data8.bin data.gz
gunzip data.gz
gzip: data already exists; do you wish to overwrite (y or n)? y
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ file data
data: ASCII text
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$ cat data
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
bandit12@bandit:/tmp/tmp.OXG3P5sDZn$
```
