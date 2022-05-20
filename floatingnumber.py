number = input("Enter your floating point value : ")

decimalPlaces = int(input("Enter the number of decimal places of the result : "))

def floatBinary(number, decimalPlaces ):
    wholeNum, dec = str(number).split(".")

    wholeNum = int(wholeNum)
    dec = int (dec)

    result = bin(wholeNum).lstrip("0b") + "."
    for i in range(decimalPlaces):
        wholeNum, dec = str((convertDecimal(dec)) * 2).split(".")
        dec = int(dec)

        result += wholeNum

    return result

def convertDecimal(num): 
    while num > 1:
        num /= 10
    return num



print(number + " in Binary = " + floatBinary(number,decimalPlaces))