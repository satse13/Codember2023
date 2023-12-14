def real(msg):

	cadena, checksum = msg.split("-")
	checksum = checksum.rstrip()
	list = []

	for letter in cadena:
			if cadena.index(letter) == cadena.rindex(letter):
				list.append(letter)

	psw = ''.join(list)

	if(psw == checksum):
		return (True, checksum)

	return False, ""


f = open("Challenge04/input.txt", "r")
contador = 0
for x in f:
	sol = real(x)
	if sol[0]: 
		contador += 1
	if contador == 33:
		print(sol[1])


f.close()
