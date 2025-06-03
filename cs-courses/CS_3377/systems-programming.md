CS 3377 Systems Programming in UNIX and Other Environments (3 semester credit hours) Basic UNIX concepts, commands and utilities, organization of UNIX file system including links and access control, creating and managing UNIX processes and threads, implementing algorithms using shell scripts, basic networking concepts including socket and client-server programming, inter-process communication using pipes and signals, using a version control system to manage work, and introduction to cloud computing. Design and implementation of a comprehensive programming project is required.
Now we’re talking — CS 3377: Systems Programming in UNIX is where you leave the high-level safety of Java and dive into the raw power of C, Linux, and the terminal.

⸻

1. Use Linux Like a Power User
   • File navigation with cd, ls, pwd
   • File permissions: chmod, chown, umask
   • Symbolic vs hard links: ln -s vs ln
   • Redirection, pipes, background jobs

⸻

2. Shell Scripting (Bash)

Automate tasks using scripts

#!/bin/bash
for file in \*.txt; do
echo "Processing $file"
done

    •	Conditionals: if, else
    •	Loops: for, while
    •	Reading/writing files
    •	Command substitution: $(...)

⸻

3. C Programming with the UNIX API

Write low-level code that controls the OS directly

    •	File I/O using open(), read(), write(), close()

int fd = open("file.txt", O_RDONLY);
read(fd, buffer, sizeof(buffer));

    •	Error handling with errno, perror()

⸻

4. Processes & Forking
   • fork() creates a new process
   • exec() replaces a process with a new program
   • wait() waits for child processes

pid_t pid = fork();
if (pid == 0) {
execlp("ls", "ls", "-l", NULL);
}

⸻

5. Signals

Communicate between processes using messages like SIGINT, SIGKILL

    •	kill(pid, SIGTERM)
    •	signal(SIGINT, handlerFunction);

⸻

6. Pipes & IPC (Inter-Process Communication)

Let processes talk to each other

    •	Anonymous pipes: pipe(), used for parent-child comms
    •	Named pipes (FIFOs): mkfifo()
    •	Example: cat file.txt | grep "hello" becomes actual pipes in C

⸻

7. Multithreading (POSIX Threads / pthreads)
   • Create threads with pthread_create()
   • Share memory between threads (race conditions!)
   • Use mutexes and semaphores for safety

⸻

8. Sockets & Client-Server Networking
   • Basic TCP server/client in C using:
   • socket(), bind(), listen(), accept() (server)
   • connect() (client)
   • Build simple chat servers or data senders

⸻

9. Version Control with Git
   • You used git init, git add, git commit, git push
   • Maybe collaborated with GitHub

⸻

10. Comprehensive Project

You probably built a:
• Custom shell (like mysh)
• Server-client game or chat system
• System tool (e.g., file watcher, data logger, etc.)

⸻
