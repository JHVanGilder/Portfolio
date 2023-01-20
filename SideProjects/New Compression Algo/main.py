import string
from decimal import Decimal
import sys

ascii_dict = {}
for i in range(len(string.printable)):
    ascii_dict[string.printable[i]] = str(i).zfill(2)
print(ascii_dict)
def str_to_dec(input_text):
    dec = "."
    for letter in input_text:
        dec += ascii_dict.get(letter, "68")
    return dec


test_str = "The common integer system that we’re used to, the decimal system, uses a base of ten, meaning that it has ten different symbols. These symbols are the numbers from 0 through to 9, which allow us to make all combinations of numbers that we’re familiar with."
test = str_to_dec(test_str)


def dec_to_ratio(input_dec):
    return Decimal(input_dec).as_integer_ratio()

def ratio_to_dec(input_dec):
    return str(dec_to_ratio(input_dec)[0] / dec_to_ratio(input_dec)[1])

print(ratio_to_dec(test))

def dec_to_str(input_dec):
    input_dec = input_dec[1:]
    pair = 0
    output_text = ""
    for duo in range(len(input_dec) - 1):
        pair += 1
        if pair % 2 == 1:
            output_text += [k for k, v in ascii_dict.items() if v == input_dec[duo:duo+2]][0]
        else:
            pass
    return str(output_text)

print(sys.getsizeof(test_str))
print(sys.getsizeof(str_to_dec(test_str)))
print(sys.getsizeof(dec_to_ratio(test)))
print(sys.getsizeof(dec_to_str(str_to_dec(test_str))))