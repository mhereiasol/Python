user = ["Dani", "Jano", "Kaki", "Lala"]
password = ["j1j1", "j3j3", "j4j4", "j5j5"]

currusername = input("Username : ")
currpassword = input("Password : ")

for x in range(len(user)):
	if currusername == user[x] and currpassword == password[x]:
		print("Welcome" + " " + user[x])
		break
else:
	print("Access Denied")
