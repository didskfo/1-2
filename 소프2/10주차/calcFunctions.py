from math import factorial as fact


def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r


def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r


def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r


def decToRoman(numStr):
    try:
        n = int(numStr)
    except ValueError:
        return '알맞지 않은 수입니다.'
    except:
        return 'Error!'

    if n >= 4000:
        return '4000이하의 수를 입력해주세요'

    romans = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    result = ''
    for value in sorted(romans.keys(), reverse=True):
        while n >= value:
            result += romans[value]
            n -= value

    return result

def romanToDec(numStr):
    try:
        n = str(numStr)
        if n.isdigit():
            return '로마숫자가 아닙니다'
    except:
        return 'Error!'
    try:
        romans = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
            1: 'I'
        }

        result = 0
        for value in sorted(romans.keys(), reverse=True):
            i = 1
            while n.find(romans[value]) == 0:
                if n.find(romans[value]) == 0:
                    if len(romans[value]) == 2:
                        i = 2
                    result += value
                    n = n[i:]
        if n != '':
            return '알맞은 입력이 아닙니다'
        return str(result)
    except:
        return '에러가 발생했습니다'