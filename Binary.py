from pythonds.basic.stack import Stack
decimalValue = int(input("Decimal Number: "))

def binaryNumber(decimalValue):
  remainderStack = Stack()

  while decimalValue > 0:
    remainderValue = decimalValue % 2
    remainderStack.push(remainderValue)
    decimalValue = decimalValue // 2

  binString = " "
  while not remainderStack.isEmpty():
    binString = binString + str(remainderStack.pop())

  return "Number in Binary: "+ binString

print(binaryNumber(decimalValue))

