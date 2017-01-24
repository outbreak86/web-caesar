def alphabet_position(letter):
	if(letter.isupper()):
		return ord(letter)-65##stip out casing
	else:
		return ord(letter)-97##strip out casing
		
def rotate_character(char, rot):
	if (ord(char) > 64 and ord(char) <91): #This checks for uppercase
		return chr(((alphabet_position(char)+rot)%26)+65)
	elif (ord(char) > 96 and ord(char) <123):#Lower case check
		return chr(((alphabet_position(char)+rot)%26)+97)
	else:#Otherwise we let it through
		return char
		
def encrypt(text, rot):
	finalStr = ''
	for c in text:
		finalStr += rotate_character(c,rot)
	return finalStr
	