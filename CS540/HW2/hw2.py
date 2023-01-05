import math
import string

def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    described in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)


def shred(filename):
    '''
    counts the frequency at which printable ASCII characters
    appear in the input file

    params: str filename: string referencing .txt file that
        contains text to be analyzed
    output: dict X: dictionary with ASCII characters as keys
        and frequency of a character in the input file as
        values
        list Z: list of keys in X
    '''
    X=dict()
    with open(filename,encoding='utf-8') as f:
        for acsii_char in string.ascii_uppercase:
            X[acsii_char] = 0
        for line in f:
            for character in line:
                if character.upper() in string.ascii_uppercase:
                    X[character.upper()] += 1
    Z = "Q1"
    for entry in X:
        Z += ("\n" + entry + " " + str(X.get(entry)))
    # print(Z)
    return (X, Z)

def lang_ident_a_coef(filename):
    '''
    calculates the X1*log(e1) and X1*log(s1)

    params: str filename: string referencing .txt file that
         contains text to be analyzed
    output: formatted string with the calculated values
        '''
    shred_dict = shred(filename)[0]
    e = get_parameter_vectors()[0]
    s = get_parameter_vectors()[1]
    x = list(shred_dict.values())
    coef_s = str(f"{x[0] * math.log(s[0]):.4f}")
    coef_e = str(f"{x[0] * math.log(e[0]):.4f}")
    return("\nQ2\n" + coef_e + "\n" + coef_s + "\n")

def F_calculator(filename):
    '''
    computes the F(English) and F(Spanish) of the input text file

    params: str filename: string referencing .txt file that
         contains text to be analyzed
    output: str Q2_e: F(English)
            str Q2_s: F(Spansih)
    '''
    P_e = .6
    P_s = .4
    shred_dict = shred(filename)[0]
    shred_list = list(shred_dict.values())
    e = get_parameter_vectors()[0]
    s = get_parameter_vectors()[1]
    sum_e = 0
    for i in range(len(shred_list)):
        sum_e += (shred_list[i] * math.log(e[i]))
    Q2_e = math.log(P_e) + sum_e
    sum_s = 0
    for i in range(len(shred_list)):
        sum_s += (shred_list[i] * math.log(s[i]))
    Q2_s = math.log(P_s) + sum_s
    return (Q2_e, Q2_s)

def Prob_calc(filename):
    '''
    calculates P(Y = y | X) for y = English

    input: str filename: string referencing .txt file that
         contains text to be analyzed
    output: float Prob_e: probability coefficient of y = English
    '''
    if F_calculator(filename)[1] - F_calculator(filename)[0] >= 100:
        return 0
    if F_calculator(filename)[1] - F_calculator(filename)[0] <= -100:
        return 1
    F_e = F_calculator(filename)[0]
    F_s = F_calculator(filename)[1]
    Prob_e = (1 / (1 + (math.e ** (F_s - F_e))))
    return Prob_e

def output_formatted(filename):
    '''
    formatter for output

    input: str filename: string referencing .txt file that
         contains text to be analyzed
    output: str: formatted string with all calculated values
                in desired order
    '''
    F_coefs = F_calculator(filename)
    F_e = str(f"{F_coefs[0]: .4f}")
    F_s = str(f"{F_coefs[1]: .4f}")
    P_e = str(f"{Prob_calc(filename): .4f}").strip()
    Q1 = str(shred(filename)[1])
    Q2 = str(lang_ident_a_coef(filename))
    Q3 = str("Q3\n" + F_e + "\n" + F_s + "\n")
    Q4 = str("Q4\n" + P_e)
    return (Q1 + Q2 + Q3 + Q4)

print(output_formatted("samples/letter0.txt"))
