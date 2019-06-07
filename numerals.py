RMN2ARAB = { 'I':1, 'V':5 , 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000 }
SPECIAL_ROM2ARAB = {'IV': 4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900, }

ARAB2ROMAN = { 1:'I', 5:'V', 10:'X', 50: 'L', 100:'C', 500:'D', 1000:'M' }
SPECIAL_ARAB2ROMAN = { 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM' }



def convert_roman_2_arab(str):

    tally = 0
    strlen = len(str)


    for i in range (0, strlen):

        chr = str[i]
        next = 'Z'
        prev = 'Z' # dummy letter it wouldn't matter what we put here

        if i < strlen-1: # not at end
            next = str[i+1]

        if i > 0: # not at start
            prev = str[i-1]

        if (isspecialcase(prev+chr)):
            tally += SPECIAL_ROM2ARAB[prev + chr]
        elif (not isspecialcase(chr+next)):
            tally += RMN2ARAB[chr]

    return tally


def isspecialcase(strpair):
    return (strpair in SPECIAL_ROM2ARAB.keys())



def convert_arab_2_roman(num):

    romanstr = ''
    tmp = num

    ARABICdict = merge_dicts(ARAB2ROMAN, SPECIAL_ARAB2ROMAN)
    multipliers = sorted(ARABICdict.keys())[::-1]

    print multipliers


    length = len(multipliers)

    for i in range(0, length):
        multiplier = multipliers[i]

        while (tmp >0 and tmp % multiplier != tmp):
                tmp = tmp - multiplier
                romanstr += ARABICdict[multiplier]
    return romanstr


def merge_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z



def isspecialarabcase():
    pass



def test1():
    ans = convert_roman_2_arab('CCXCI')
    print ans
    assert ans == 291


def test2():
   ans = convert_roman_2_arab('XXIX')
   print ans
   assert ans == 29

def test3():
   ans = convert_roman_2_arab('XXXVIII')
   print ans
   assert ans == 38

def test4():
   ans = convert_roman_2_arab('MCMXCIX')
   print ans
   assert ans == 1999


def test5():
   ans = convert_roman_2_arab('LXXXVIII')
   print ans
   assert ans == 88

def test6():
   ans = convert_roman_2_arab('MDLXXXII')
   print ans
   assert ans == 1582

def test7():
   ans = convert_roman_2_arab('DLV')
   print ans
   assert ans == 555

def test7():
   ans = convert_roman_2_arab('CD')
   print ans
   assert ans == 400

def test8():
   ans = convert_roman_2_arab('CDXC')
   print ans
   assert ans == 490

## integer to roman numeral tests

def test1a():
    ans = convert_arab_2_roman(291)
    print ans
    assert ans == 'CCXCI'


def test2a():
   ans = convert_arab_2_roman(29)
   print ans
   assert ans == 'XXIX'

def test3a():
   ans = convert_arab_2_roman(38)
   print ans
   assert ans == 'XXXVIII'

def test4a():
   ans = convert_arab_2_roman(1999)
   print ans
   assert ans == 'MCMXCIX'


def test5a():
   ans = convert_arab_2_roman(88)
   print ans
   assert ans == 'LXXXVIII'

def test6a():
   ans = convert_arab_2_roman(1582)
   print ans
   assert ans == 'MDLXXXII'

def test7a():
   ans = convert_arab_2_roman(555)
   print ans
   assert ans == 'DLV'



