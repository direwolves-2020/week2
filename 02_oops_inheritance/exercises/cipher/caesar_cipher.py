import string

def encrypt_caesar(msg, num):
	encrypted_msg = ''
	shifted = ''

	#get lists of lowercase letters and uppercase
	lower_letters = list(string.ascii_lowercase)
	upper_letters = list(string.ascii_uppercase)

	#loop through the string
	for m in msg:
		if m in lower_letters:
			#if the char is lowercase, find its location (index) in the abc list
			#add the shift num and calc mod of the total
			#shifted value will be the mod
			shifted_index = (lower_letters.index(m) + num) % 26
			shifted = lower_letters[shifted_index]
			encrypted_msg += shifted
		elif m in upper_letters:
			#follow same for uppercase
			shifted_index = (upper_letters.index(m) + num) % 26
			shifted = upper_letters[shifted_index]
			encrypted_msg += shifted
		else:
			#if char isn't alpha, add to string as is
			encrypted_msg += m
		
	return encrypted_msg


def decrypt_caesar(msg, num):
	decrypted_msg = ''
	shifted = ''

	#get lists of lowercase letters and uppercase
	lower_letters = list(string.ascii_lowercase)
	upper_letters = list(string.ascii_uppercase)

	#loop through the string
	for m in msg:
		if m in lower_letters:
			#if the char is lowercase, find its location (index) in the abc list
			#add the shift num and calc mod of the total
			#shifted value will be the mod
			shifted_index = (lower_letters.index(m) - num) % 26
			shifted = lower_letters[shifted_index]
			decrypted_msg += shifted
		elif m in upper_letters:
			#follow same for uppercase
			shifted_index = (upper_letters.index(m) - num) % 26
			shifted = upper_letters[shifted_index]
			decrypted_msg += shifted
		else:
			#if char isn't alpha, add to string as is
			decrypted_msg += m
		
	return decrypted_msg

assert encrypt_caesar("My name is Judith.", 17) == "Dp erdv zj Aluzky."
assert decrypt_caesar("Dp erdv zj Aluzky.", 17) == "My name is Judith."

assert encrypt_caesar("xX, zZ, aA", -10) == "nN, pP, qQ"
assert decrypt_caesar("nN, pP, qQ", -10) == "xX, zZ, aA"

assert encrypt_caesar("A.B.C.1.x.y.z", 3) == "D.E.F.1.a.b.c" 
assert decrypt_caesar("D.E.F.1.a.b.c", 3) == "A.B.C.1.x.y.z"