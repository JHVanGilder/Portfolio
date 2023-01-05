////////////////////////////////////////////////////////////////////////////////
//
// Copyright 2019 Jim Skrentny
// Posting or sharing this file is prohibited, including any changes/additions.
// Used by permission, Fall 2020, Deb Deppeler
//
////////////////////////////////////////////////////////////////////////////////
// Main File:        mySigHandler.c
// This File:        sendsig.c
// Other Files:      division.c
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
//////////////////////////// 80 columns wide //////////////////////////////////

#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>

/*
 * main function, takes 2 input, -i or -u and a PID number
 * outputs nothing
 * sends sig to sig handlers in mySigHandler.c
 */
int main(int argNum, char *argValue[]) {
	// if the number of args is not right, stop
	if (argNum != 3) {
		printf("Usage: sendsig <signal type> <pid>\n");
		return -1;
	}
	// if the number of inputs is not right, stop
	if (strlen(argValue[1]) != 2) {
		printf("Usage: sendsig <signal type> <pid>\n");
		return -1;
	}

	int pid = atoi(argValue[2]);
	char input = argValue[1][1];
	// input for interrupt signal (ctrl-c)
	if (input == 'i') {
		int complete = kill(pid, SIGINT);
		if (complete) {
			printf("ERROR IN SENDING SIGINT\n");
		}
	}
	// input for SIGUSR1 signal
	else if (input == 'u') {
		int complete = kill(pid, SIGUSR1);
		if (complete) {
			printf("ERROR IN SENDING SIGUSR1\n");
		}
	}
	else {
		printf("Usage: sendsig <signal type> <pid>\n");
		return -1;
	}

}
