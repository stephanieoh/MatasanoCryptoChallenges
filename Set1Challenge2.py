
def FixedXOR(a, b):
	A = int(a, 16)
	B = int(b, 16)
	C = A^B
	return '%x' %C

print FixedXOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")

