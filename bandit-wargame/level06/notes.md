# level06 Notes

## What I Learned

In Level 6 of Bandit, I learned how to use the find command to search for files based on specific attributes like ownership and size, rather than just names or paths. The challenge was to locate a file that was owned by the user bandit7, belonged to the group bandit6, and was exactly 33 bytes in size. Since the file wasn’t located in my home directory, I had to search the entire file system. I used the command find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null — this tells find to look from the root directory (/) for regular files (-type f) that are owned by bandit7 and group-owned by bandit6, and exactly 33 bytes in size (-size 33c), while the 2>/dev/null part redirects all error messages (like permission denied errors) to the void so they don’t clutter the screen. I learned that 2> refers to standard error (stderr), and /dev/null is essentially a trash can for unwanted output. When I ran the command, it returned the path ./var/lib/dpkg/info/bandit7.password, and using cat on that file showed the password for the next level. This level taught me how to filter files based on ownership and size, how to suppress irrelevant errors, and how to use find for powerful system-wide file discovery.

## My Solution

```
bandit6@bandit:/$ ls
bin                krypton            mnt                 srv
bin.usr-is-merged  lib                opt                 sys
boot               lib32              proc                tmp
dev                lib64              root                usr
drifter            lib.usr-is-merged  run                 var
etc                libx32             sbin
formulaone         lost+found         sbin.usr-is-merged
home               media              snap
bandit6@bandit:/$ find . -type f -user bandit7 -group bandit6 -size 33c
find: ‘./root’: Permission denied
find: ‘./proc/tty/driver’: Permission denied
find: ‘./proc/3804255/task/3804255/fdinfo/6’: No such file or directory
find: ‘./proc/3804255/fdinfo/5’: No such file or directory
find: ‘./boot/lost+found’: Permission denied
find: ‘./boot/efi’: Permission denied
find: ‘./etc/polkit-1/rules.d’: Permission denied
find: ‘./etc/sudoers.d’: Permission denied
find: ‘./etc/xinetd.d’: Permission denied
find: ‘./etc/credstore’: Permission denied
find: ‘./etc/multipath’: Permission denied
find: ‘./etc/ssl/private’: Permission denied
find: ‘./etc/credstore.encrypted’: Permission denied
find: ‘./etc/stunnel’: Permission denied
find: ‘./home/bandit29-git’: Permission denied
find: ‘./home/ubuntu’: Permission denied
find: ‘./home/bandit27-git’: Permission denied
find: ‘./home/drifter6/data’: Permission denied
find: ‘./home/bandit30-git’: Permission denied
find: ‘./home/bandit5/inhere’: Permission denied
find: ‘./home/bandit31-git’: Permission denied
find: ‘./home/bandit28-git’: Permission denied
find: ‘./home/drifter8/chroot’: Permission denied
find: ‘./run/lock/lvm’: Permission denied
find: ‘./run/systemd/inaccessible/dir’: Permission denied
find: ‘./run/systemd/propagate/systemd-udevd.service’: Permission denied
find: ‘./run/systemd/propagate/systemd-resolved.service’: Permission denied
find: ‘./run/systemd/propagate/systemd-networkd.service’: Permission denied
find: ‘./run/systemd/propagate/irqbalance.service’: Permission denied
find: ‘./run/systemd/propagate/systemd-logind.service’: Permission denied
find: ‘./run/systemd/propagate/chrony.service’: Permission denied
find: ‘./run/systemd/propagate/polkit.service’: Permission denied
find: ‘./run/systemd/propagate/ModemManager.service’: Permission denied
find: ‘./run/lvm’: Permission denied
find: ‘./run/cryptsetup’: Permission denied
find: ‘./run/multipath’: Permission denied
find: ‘./run/screen/S-bandit20’: Permission denied
find: ‘./run/screen/S-bandit1’: Permission denied
find: ‘./run/screen/S-bandit16’: Permission denied
find: ‘./run/screen/S-bandit0’: Permission denied
find: ‘./run/screen/S-bandit21’: Permission denied
find: ‘./run/sudo’: Permission denied
find: ‘./run/user/11005’: Permission denied
find: ‘./run/user/11001’: Permission denied
find: ‘./run/user/11016’: Permission denied
find: ‘./run/user/11006/systemd/inaccessible/dir’: Permission denied
find: ‘./run/user/11012’: Permission denied
find: ‘./run/user/11020’: Permission denied
find: ‘./run/user/11014’: Permission denied
find: ‘./run/user/11008’: Permission denied
find: ‘./run/user/11011’: Permission denied
find: ‘./run/user/11000’: Permission denied
find: ‘./run/user/11013’: Permission denied
find: ‘./run/user/11023’: Permission denied
find: ‘./run/user/11025’: Permission denied
find: ‘./run/user/11004’: Permission denied
find: ‘./run/user/11007’: Permission denied
find: ‘./run/user/11031’: Permission denied
find: ‘./run/user/11009’: Permission denied
find: ‘./run/user/11032’: Permission denied
find: ‘./run/user/11024’: Permission denied
find: ‘./run/user/11028’: Permission denied
find: ‘./run/user/11017’: Permission denied
find: ‘./run/user/11003’: Permission denied
find: ‘./run/user/11015’: Permission denied
find: ‘./run/user/11002’: Permission denied
find: ‘./run/user/11010’: Permission denied
find: ‘./run/user/11021’: Permission denied
find: ‘./run/user/11019’: Permission denied
find: ‘./run/user/11026’: Permission denied
find: ‘./run/user/11022’: Permission denied
find: ‘./run/user/11027’: Permission denied
find: ‘./run/chrony’: Permission denied
find: ‘./run/udisks2’: Permission denied
find: ‘./dev/shm’: Permission denied
find: ‘./dev/mqueue’: Permission denied
find: ‘./sys/kernel/tracing’: Permission denied
find: ‘./sys/kernel/debug’: Permission denied
find: ‘./sys/fs/pstore’: Permission denied
find: ‘./sys/fs/bpf’: Permission denied
find: ‘./snap’: Permission denied
find: ‘./lost+found’: Permission denied
find: ‘./var/cache/ldconfig’: Permission denied
find: ‘./var/cache/pollinate’: Permission denied
find: ‘./var/cache/apparmor/2693c843.0’: Permission denied
find: ‘./var/cache/apparmor/ac99afeb.0’: Permission denied
find: ‘./var/cache/apt/archives/partial’: Permission denied
find: ‘./var/cache/private’: Permission denied
find: ‘./var/crash’: Permission denied
find: ‘./var/spool/rsyslog’: Permission denied
find: ‘./var/spool/cron/crontabs’: Permission denied
find: ‘./var/spool/bandit24’: Permission denied
find: ‘./var/log/chrony’: Permission denied
find: ‘./var/log/amazon’: Permission denied
find: ‘./var/log/unattended-upgrades’: Permission denied
find: ‘./var/log/private’: Permission denied
find: ‘./var/tmp’: Permission denied
find: ‘./var/lib/udisks2’: Permission denied
find: ‘./var/lib/update-notifier/package-data-downloads/partial’: Permission denied
find: ‘./var/lib/polkit-1’: Permission denied
./var/lib/dpkg/info/bandit7.password
find: ‘./var/lib/apt/lists/partial’: Permission denied
find: ‘./var/lib/chrony’: Permission denied
find: ‘./var/lib/amazon’: Permission denied
find: ‘./var/lib/ubuntu-advantage/apt-esm/var/lib/apt/lists/partial’: Permission denied
find: ‘./var/lib/snapd/cookie’: Permission denied
find: ‘./var/lib/snapd/void’: Permission denied
find: ‘./var/lib/private’: Permission denied
find: ‘./drifter/drifter14_src/axTLS’: Permission denied
find: ‘./tmp’: Permission denied
bandit6@bandit:/$ find . -type f -user bandit7 -group bandit6 -size 33c2>/dev/null
find: Invalid argument`33c2' to -size
bandit6@bandit:/$ find . -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
./var/lib/dpkg/info/bandit7.password
bandit6@bandit:/$ cat ./var/lib/dpkg/info/bandit7.password
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

```
