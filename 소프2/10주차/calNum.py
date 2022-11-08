from keypad import functionList
import calcFunctions

def func(fun, num):
    try:
        if fun == functionList[0]:
            res = calcFunctions.factorial(num)
        elif fun == functionList[1]:
            res = calcFunctions.decToBin(num)
        elif fun == functionList[2]:
            res = calcFunctions.binToDec(num)
        elif fun == functionList[3]:
            res = calcFunctions.decToRoman(num)
        elif fun == functionList[4]:
            res = calcFunctions.romanToDec(num)
    except:
        res = 'Error!'
    return res
