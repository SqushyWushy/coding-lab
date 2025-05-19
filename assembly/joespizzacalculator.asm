#MIPS Assembly Program: Pizza Area Calculator
#This program is going to calculate the total square feet of pizzas sold in a day
#Author: Jr Hector Gonzalez
#Date: October 15th, 2024


.data
newline: .asciiz "\n" #This creates a newline char to use later on when printing
prompt_num_round_pizzas: .asciiz "Enter the number of round pizzas sold: " #asks user for round pizzas sold
prompt_num_square_pizzas: .asciiz "Enter the number of square pizzas sold: " #asks user for square pizzas sold
prompt_estimate: .asciiz "Enter your estimate of total pizzas sold in square feet: " #asks for total pizza estimate in square feet
msg_total_area: .asciiz "Total number of square feet of pizza sold: "
msg_total_area_round: .asciiz "Total number of square feet of round pizzas: "
msg_total_area_square: .asciiz "Total number of square feet of square pizzas: "
msg_woosh: .asciiz "Woosh!\n" #Message that shows if estimate was less than actual like, yes we made more than we thought!
msg_bummer: .asciiz "Bummer!\n" #Message that shows if estimate is greater than actual like, dang we did not sell as much as we thought...

pi: .float 3.14159265 #stores the value of pi as a floating point number
sixteen: .float 16.0 #this is the radius squared of the round pizza with 8 inch diameter
one_fourty_four: .float 144.0 #there are 144 square inches in a square foot - we need this value for conversions


.text
.globl main
main:

	#Prompt for number of round pizzas sold
	li $v0, 4 #this is our value register for system calls and 4 tells system to print a string
	la $a0, prompt_num_round_pizzas #this is our argument register used to pass data needed for our print string action
	syscall #prints the string
	
	#Read integer
	li $v0, 5 #tells the system we want to read an integer using syscall code 5
	syscall #executes the system call
	move $t0, $v0 #we take our user input which is now is $v0, then copy and store it into $t0 = num of round pizzas
	
	#Prompt for number of square pizza sold
	li $v0, 4 #tells system to print another string
	la $a0, prompt_num_square_pizzas #load the string address for square pizzas
    syscall

    #Read another integer
    li $v0, 5 #tells system we are going to read an integer
    syscall
    move $t1, $v0 #we already have a value in $t0, so we will copy and store this integer in $t1 = num of square pizzas

    #Prompt for estimate
    li $v0, 4 #code for printing a string
    la $a0, prompt_estimate #load the address of the prompt estimate string
    syscall  #executes the printing of the string

    #Read the floating integer
    li $v0, 6 #syscall code for reading a floating point integer
    syscall #executes the reading of the floating point integer
    mov.s $f4, $f0 #the float integer will be copied and stored into $f4 = user estimate - b/c even number reg is for single precision operations

    #ROUND PIZZA CALCUATIONS

    #compute area_one_round_pizza = pi * 16
    l.s $f6, pi #loads pi into $f6
    l.s $f8, sixteen #loads 16.0 into $f8
    mul.s $f10, $f6, $f8 #multiplies floats pi times 16 and stores into $f10 = area of one round pizza in square inches

    #convert num_round_pizza to float
    mtc1 $t0, $f12 #moves our integer into a floating point register in order to do math with it
    cvt.s.w $f12, $f12 #converts our integer in $f12 into a single precision float so $f12 = num of round pizzas

    #compute total area of round pizzas in square inches
    mul.s $f14, $f10, $f12 #multiples area of one round pizza * num of round pizzas = $f14

    #covert total area of round pizzas into square feet
    l.s $f16, one_fourty_four #$f16 = 144.0
    div.s $f18, $f14, $f16 #$f18 = total area of round pizzas in square feet

    #SQUARE PIZZA CALCULATIONS

    #convert num of square pizzas to float
    mtc1 $t1, $f20 #move num of square pizza integer into float register
    cvt.s.w $f20, $f20 #$f20 = float num of pizzas
    #each square pizza is 1 square foot so total area is just num of square pizzas which is in $f20

    #total area of round + square  pizzas:
    add.s $f22, $f18, $f20 #f22 = total area in sq feet

    #PRINT OUT RESULTS
    
    #i) total number of square feet of pizza sold
    li $v0, 4 #call to print string
    la $a0, msg_total_area
    syscall

    li $v0, 2 #calling code 2 which prints floats
    mov.s $f12, $f22 #to print floats, we need value to be in $f12(mips rules) so move $f22(total area) into $f12
    syscall

    li $v0, 4 #code to print string
    la $a0, newline #load address of newline char
    syscall #execute the print of a new line

    #ii) total number of square feet of round pizzas
    li $v0, 4
    la $a0, msg_total_area_round
    syscall

    li $v0, 2
    mov.s $f12, $f18 #move total area of square feet of round pizzas into $f12 to print
    syscall #prints the value stored in $f12

    li $v0, 4
    la $a0, newline
    syscall

    #iii) total number of square feet of square pizzas
    li $v0, 4
    la $a0, msg_total_area_square
    syscall

    li $v0, 2
    mov.s $f12, $f20 #move the value of total num of square feet into $f12
    syscall #execute the print of the float

    li $v0, 4
    la $a0, newline
    syscall

    #compare total area in square feet with Joe's estimate
    c.le.s $f22, $f4 #compare if total area in square feet <= joe's estimate
    bc1t less_or_equal #branches to less_or_equal if the comparison is true
    nop #no operation(to safely handle branch delay)

    #If total area in square feet > Joe's estimate, print "Woosh!"
    li $v0, 4
    la $a0, msg_woosh
    syscall
    j end_compare #jump to end compare to skip the "Bummer" part if estimate was too low

    less_or_equal:
    #Print "Bummer!" if total area in square feet <= Joe's estimate
    li $v0, 4
    la $a0, msg_bummer
    syscall

    end_compare:
    #exit the program
    li $v0, 10 #load syscall code 10 which exits program
    syscall #executes syscall to exit program
