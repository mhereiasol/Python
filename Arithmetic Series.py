frst = int(input("Enter First Term: "))
scnd = int(input("Enter Second Term: "))
n = int(input("What is your Nth Term: "))
print(frst)
print(scnd)
d = scnd - frst
An = frst + n - 1 * d
i = 3
while (i<=n):
  thrd = scnd + d
  print(thrd)
  frst = scnd
  scnd = thrd
  i = i + 1
print("Common difference: " + str(d))

