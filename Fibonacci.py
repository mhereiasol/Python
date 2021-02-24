fibonacciOne = int(input("First Term: "))
fibonacciTwo = int(input("Second Term: "))
Nterm = int(input("Number of Term: "))
print(fibonacciOne)
print(fibonacciTwo)
fibonacci = 3
while (fibonacci <= Nterm):
  fibonacciThree = fibonacciOne + fibonacciTwo
  print(fibonacciThree)
  fibonacciOne = fibonacciTwo
  fibonacciTwo = fibonacciThree
  fibonacci += 1