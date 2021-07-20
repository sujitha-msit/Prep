# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	shift=shift%26
	string=''
	s=0
	for i in msg:
		if  ord(i) in range(65,91) or ord(i) in range(97,123):
			if ord(i) in range(65,91):
				
				if ord(i)+shift>90:
					s=ord(i)+shift-26
					print("It is shifted eback",s )
				elif ord(i)+shift<65:
					s=ord(i)+shift+26
				else:
					s=ord(i)+shift
			
		
			elif ord(i) in range(97,123):
				print(i)
				if ord(i)+shift>122:
					s=ord(i)+shift-26
				elif ord(i)+shift<97:
					s=ord(i)+shift+26
				else:
					s=ord(i)+shift	
			string=string+chr(s)
		else:
			print("hey space encountered",i)
			string+=i
	return string
print(fun_applycaesarcipher("Hi I @m sujitha",2))



