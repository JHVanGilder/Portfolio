////////////////////////////////////////////////////////////////////////////////
//
// Copyright 2019 Jim Skrentny
// Posting or sharing this file is prohibited, including any changes/additions.
// Used by permission, Fall 2020, Deb Deppeler
//
////////////////////////////////////////////////////////////////////////////////
// Main File:        mySigHandler.c
// This File:        mySigHandler.c
// Other Files:      sendsig.c
// 		     division.c
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
#include <unistd.h>
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>

int alarmTime = 3;
int SIGUSR1cnt = 0;

/* 
 * handler for general signals
 * handles alarms and prints PID and current date, then rearms the alarm
 */
void sigHandler() {
	int PID = getpid();
	time_t current_time;
        struct tm *local_time;
	current_time = time(NULL);
	local_time = localtime(&current_time);
	printf("PID: %d CURRENT TIME: %s", PID, asctime(local_time));
	alarm(alarmTime);
	return;
}

/*
 * handles SIGUSR1 signals and increments the count of sigs caught
 */
void sigHandlerSIGUSR1() {
	printf("SIGUSR1 detected!\n");
	SIGUSR1cnt++;
}

/*
 * catches interrupt signals and prints an exit message
 */
void sigHandlerSIGINT() {
	printf("\nSIGINT handled.\nSIGUSR1 was handled %d times. Exiting now.\n", SIGUSR1cnt);
	exit(0);
}

/*
 * main function, no input, no output
 * generates and handles 3 sigaction structs
 * starts an infinte loop to generate alarms that signal every 3 seconds
 */
int main() {
	printf("PID and time print every %d seconds.\nType Ctrl-C to end the program.\n", alarmTime);
	alarm(alarmTime);
	struct sigaction act;
	memset (&act, 0, sizeof(act));
	act.sa_handler = sigHandler;
	if (sigaction(SIGALRM, &act, NULL) != 0) {
		printf("ERROR\n");
		return -1;
	}	
	struct sigaction sigusr1;
	memset (&sigusr1, 0, sizeof(sigusr1));
	sigusr1.sa_handler = sigHandlerSIGUSR1;
	if (sigaction(SIGUSR1, &sigusr1, NULL) != 0) {
		printf("ERROR WITH SIGUSR1\n");
		return -1;
	}
	struct sigaction siginit;
	memset (&siginit, 0, sizeof(siginit));
	siginit.sa_handler = sigHandlerSIGINT;
	if (sigaction(SIGINT, &siginit, NULL) != 0) {
		printf("ERROR WITH SIGINT\n");
		return -1;
	}
	
	while(1) {
	}
}
