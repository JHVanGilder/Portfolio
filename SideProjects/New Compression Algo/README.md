This is a new compression algorithm I am creating.

This algorithm currently works best on plain text ASCII strings and functions in the following way:

Because Python has 100 printable ASCII characters in its base library, each ASCII character is assigned a double digit equivalent (i.e. 'a' = 10, 'b' = 11, 'c' = 12,...)
Once a string is converted to a series of 2 digit codes, a decimal is added to the start in order to generate a rational, positive decimal between 0 and 1
Because the text string is now represented as a rational, positive decimal, it can be represented as a negative exponent of 2.

Example Input:
"The common integer system that we’re used to, the decimal system, uses a base of ten, meaning that it has ten different symbols. These symbols are the numbers from 0 through to 9, which allow us to make all combinations of numbers that we’re familiar with.
"

->

55 17 14 94 12 24 22 22 24 23 94 18 23 29 14 16 14 27 94 28 34 28 29 14 22 94 29 17 10 29 94 32 14 68 27 14 94 30 28 14 13 94 29 24 73 94 29 17 14 94 13 14 12 18 22 10 21 94 28 34 28 29 14 22 73 94 30 28 14 28 94 10 94 11 10 28 14 94 24 15 94 29 14 23 73 94 22 14 10 23 18 23 16 94 29 17 10 29 94 18 29 94 17 10 28 94 29 14 23 94 13 18 15 15 14 27 14 23 29 94 28 34 22 11 24 21 28 75 94 55 17 14 28 14 94 28 34 22 11 24 21 28 94 10 27 14 94 29 17 14 94 23 30 22 11 14 27 28 94 15 27 24 22 94 00 94 29 17 27 24 30 16 17 94 29 24 94 09 73 94 32 17 18 12 17 94 10 21 21 24 32 94 30 28 94 29 24 94 22 10 20 14 94 10 21 21 94 12 24 22 11 18 23 10 29 18 24 23 28 94 24 15 94 23 30 22 11 14 27 28 94 29 17 10 29 94 32 14 68 27 14 94 15 10 22 18 21 18 10 27 94 32 18 29 17 75

->

Information Stored:

-0.85800504365650576144020078572793863713741302490234375


This negative exponent can then be stored instead of the original text string and takes less storage than the original string. This exponent can then be put over 2 and decoded.
