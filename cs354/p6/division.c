////////////////////////////////////////////////////////////////////////////////
//
// Copyright 2019 Jim Skrentny
// Posting or sharing this file is prohibited, including any changes/additions.
// Used by permission, Fall 2020, Deb Deppeler
//
////////////////////////////////////////////////////////////////////////////////
// Main File:        mySigHandler.c
// This File:        division.c
// Other Files:      sendsig.c
// Semester:         CS 354 Lecture 003 Fall 2021
// Instructor:       deppeler
// 
// Author:           James Van Gilder
// Email:            jhvangilder@wisc.edu
// CS Login:         jvan-gilder
//
/////////////////////////// OTHER SOURCES OF HELP //////////////////////////////
//                   fully acknowledge and credit all sources of help,
//                   other than Instructors and TAs.
//
// Persons:          None
//
// Online sources:   None
//////////////////////////// 80 columns wide ///////////////////////////////////

#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// global variable to keep track of number of completed division operations

int completedDivs = 0;

/* 
 * Function to be used as a sig handler for divide by 0 errors
 * Prints error, how many divisions were successful, and termination
 */


void sigfpeHandler() {
	printf("Error: a division by 0 operation was attempted.");
	printf("\nTotal number of operations completed successfully: %d", completedDivs);
	printf("\nThe program will be terminated.\n");
	exit(0);
}

/* 
 * Function to be used as a sig handler for ctrl-C interrupts
 * Prints how many divisions were successful and termination
 */

void sigintHandler() {
	printf("\nTotal number of operations completed successfully: ");
	printf("%d\nThe program wil now be terminated.\n", completedDivs);
	exit(0);
}

/* 
 * main function, generates sigaction() structs and how to handle signals,
 * prompts the user for two integers, and divides the two, printing out
 * the first and second inputs, the result of the integer division, and
 * the remainder of the division. Any non-integer input is treated by 
 * the atoi() function and acts as an int.
 *
 * input: none
 */

int main() {
	// signal for divide by zero error
	struct sigaction sigfpe;
	memset(&sigfpe, 0, sizeof(sigfpe));
	sigfpe.sa_handler = sigfpeHandler;
	if (sigaction(SIGFPE, &sigfpe, NULL) != 0) {
		printf("ERROR WITH SIGFPE\n");
		return -1;
	}
	// signal for ctr-c interrupt
	struct sigaction sigint;
	memset(&sigint, 0, sizeof(sigint));
	sigint.sa_handler = sigintHandler;
	if (sigaction(SIGINT, &sigint, NULL) != 0) {
		printf("ERROR WITH SIGINT\n");
		return -1;
	}
	
	int buffer = 100;
	char firstInput[buffer];
	char secondInput[buffer];
	int firstInt;
	int secondInt;
	// infinite loop that does actual division
	while(1){
		printf("Enter first integer: ");
		fgets(firstInput, buffer, stdin);
		firstInt = atoi(firstInput);
		printf("Enter second integer: ");
		fgets(secondInput, buffer, stdin);
		secondInt = atoi(secondInput);
		int result = (firstInt/secondInt);
		int remainder = (firstInt % secondInt);
		completedDivs++;
		printf("%d / %d is %d with a remainder of %d\n", firstInt, secondInt, result, remainder);
		
	}
}
