User = {}
status = ""

def Menu():
	status = input("Are you a new User? ").lower()
	if status == "no":
		ReturningUser()
	elif status == "yes":
		NewUser()

def NewUser():
	name = input("Please enter a username: ")
	if name in User:
		print("You are already a registered user.")
		ReturningUser()
	else:
		password = input("Please enter your password: ")
		User[name] = password
		print("Registeration Successful")
		ReturningUser()

def ReturningUser():
	name = input("Please enter a username: ")
	if name in User:
		password = input("Please enter your password: ")
		if name in User and User[name] == password:
			print("Login Successful")
		else:
			print("Wrong Password")
	else:
		print("User not found. Please register")
		NewUser()



Menu()
