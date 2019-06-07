

RMN = { 'I':1, 'V':5 , 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000 }

def convert_between_romannumeral(strorint):
    chars = strorint
    tally = 0
    strlen = len(chars)
    for i in range (0, strlen):
        if (chars[i] == 'M'):
            if (i>0 and chars[i-1]=='C'):
                tally +=  RMN[chars900
            else:
                tally = tally + 1000
        if (chars[i] == 'D'):
            tally += tally + 500

        if (chars[i] == 'C'):
            if (i>0 and chars[i-1]=='X'):
                tally = tally + 90
            else:
                tally = tally + 100
        if (chars[i] == 'L'):
            tally = tally + 50

        if (chars[i] == 'X'):
            if (i == strlen -1):
                tally = tally + 10
            elif (i + 1 < strlen and chars[i + 1] != 'C' and chars[i + 1] != 'L'):
                tally = tally + 10
            elif (i>0 and chars[i-1]=='I'):
                tally = tally + 9
            else:
                tally = tally + 10
        if (chars[i] == 'V'):
            if (i>0 and chars[i-1]=='I'):
                tally = tally + 4
            else:
                tally = tally + 5

        if (chars[i] == 'I'):
            if (i == strlen -1):
                tally = tally + 1
            if (i + 1 < strlen and chars[i + 1] != 'X' and chars[i + 1] != 'V'):
                tally = tally + 1

    return tally







def test1():
    ans = convert_between_romannumeral('CCXCI')
    print ans
    assert ans == 291



def test2():
   ans = convert_between_romannumeral('XXIX')
   print ans
   assert ans == 29

def test3():
   ans = convert_between_romannumeral('XXXVIII')
   print ans
   assert ans == 38

def test4():
   ans = convert_between_romannumeral('MCMXCIX')
   print ans
   assert ans == 1999





