.data
prompt_msg: .asciiz "Enter an integer (0 to stop, between 0 and 100): "
error_msg: .asciiz "\nError: Invalid input. Please enter a value between 1 and 100.\n"
sum_msg: .asciiz "The sum of double integers from 0 to "
result_msg: .asciiz " is: "
newline: .asciiz "\n"

array: .space 400 #This gives me space for 100 integers because each integer is 4 bytes and 4 * 100 equals 400 bytes total

.text
.globl main #This is what tells MIPS where the starting point of the program is
main:
	#Prompt the user for an integer
	li $v0, 4 #This loads syscall code 4 which prints strings
	la $a0, prompt_msg #This will load address of prompt message into $a0
	syscall #This makes the system call to print the message
	
	#Next we want to read the input
	li $v0, 5 #This loads the syscall code 5 which reads integers
	syscall #This makes the system call to read to read the user's input
	move $t0, $v0 #This moves the value from the $v0 register into $t0 for easier manipulation later
	 
	#Now that we have the input, we need to check for special cases
	beq $t0, $zero, exit_program #If the input is equal to zero, then program will jump to exit
	  
	li $t1, 1 #This sets the lower bound of 1
	li $t2, 100 #This sets the upper bound of 100
	blt $t0, $t1, invalid_input #This checks if the user input value is less than our lower bound. If yes, go to invalid_input
	bgt $t0, $t2, invalid_input #This checks if user input is greater than upper bound. If yes, go to invalid_input
	  
	#Once we know the input is valid, we want to store the numbers into our array, starting with loop variables
	move $t3, $zero #Counter for array index which starts at zero
	sll $t4, $t0, 1 #t4 = 2 * N, this line causes a left shift by to multiply by 2
	  
	li $t5, 0 #We initialize the value to store (2*0)
	
	store_values:
		sw $t5, array($t3) #This stores 2 * i in an array
		addi $t3, $t3, 4 #This moves to the next array index(each word is 4 bytes)
		addi $t5, $t5, 2 #This increments the value in $t5 by 2 to get the next even number
		
		bge $t5, $t4, sum_values #If t5 is greater than or equal to t4, then jump to sum_values to stop storing
		j store_values #otherwise, we are going to jump back/loop store_values
	
	sum_values:
		li $t6, 0 #initialize our sum to 0(this register is going to hold our total sum
		move $t3, $zero #resets the array index to 0 from the beginning
		
		# Adjust $t4 to be the total byte size of the array
		addi $t4, $t0, 1   # $t4 = N + 1 (number of elements)
		sll $t4, $t4, 2    # $t4 = (N + 1) * 4 (size in bytes)
		
	sum_loop:
		lw $t7, array($t3) #This loads the current value from they array into t7
		add $t6, $t6, $t7 #Now we add t7 into the sum inside t6
		addi $t3, $t3, 4 #This moves to the next element position in the array
		bge $t3, $t4, print_result # Exit loop after all elements have been summed
		j sum_loop #otherwise loop again
		
	#Now we we are going to print the results
	print_result:
		#Print "the sum of double integers from 0 to "
		li $v0, 4
		la $a0, sum_msg
		syscall
	
		#Print user input
		li $v0, 1
		move $a0, $t0
		syscall
	
		#Print "is: "
		li $v0, 4
		la $a0, result_msg
		syscall
	
		#Print sum result
		li $v0, 1
		move $a0, $t6
		syscall
	
		#Print newline
		li $v0, 4
		la $a0, newline
		syscall
	
		#Repeat program
		j main
		
	# Error handling for invalid input
	invalid_input:
		li $v0, 4
		la $a0, error_msg
		syscall
		j main
		
	# Exit program	
	exit_program:
		li $v0, 10
		syscall