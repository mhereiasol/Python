def summationOf(*numbers):
  sum = 0
  for number in numbers:
    sum += number
  return sum
print(summationOf(1,1,2,3,85,4566,5,668,7,8))