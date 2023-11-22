def invalidElemnent(element):

	rules, msg = element.split(':')
	msg = msg.strip()

	letter = rules[-1]
	
	min, max = map(int, rules[:-2].split('-'))

	count = msg.count(letter)

	return (count > max) or (count < min), msg


f = open("Challenge03/encryption_polices.txt", "r")
contador = 0
for x in f:
	invalid,msg = invalidElemnent(x) 
	if invalid:
		contador += 1
		if contador == 42:
				print(msg)
f.close()

# element = "1-6 h: hhhhhh"
# sol = invalidElemnent(element)
# if sol[0]:
# 	print(sol[1])