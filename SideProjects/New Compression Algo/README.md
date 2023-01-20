This is a new compression algorithm I am creating.

This algorithm currently works best on plain text ASCII strings and functions in the following way:

Because Python has 100 printable ASCII characters in its base library, each ASCII character is assigned a double digit equivalent (i.e. 'a' = 10, 'b' = 11, 'c' = 12,...)
Once a string is converted to a series of 2 digit codes, a decimal is added to the start in order to generate a rational, positive decimal between 0 and 1
Because the text string is now represented as a rational, positive decimal, it can be represented as a ratio of two integers and stored as such.

Example:
"My name is James Van Gilder! I am 22 and attend UW - Madison"

48 34 94 23 10 22 14 94 18 28 94 45 10 22 14 28 94 57 10 23 94 42 18 21 13 14 27 62 44 94 10 22 94 02 02 94 10 23 13 94 10 29 29 14 23 13 56 58 94 74 94 48 10 13 18 28 24 23

.48349423102214941828944510221428945710239442182113142762449410229402029410231394102929142313565894749448

4834942310220001:10000000000000000


This ratio can then be stored instead of the original text string and takes less storage than the original string. This ratio can be divided and unencoded to generate the orignal string.
