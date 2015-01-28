import binascii

a = binascii.unhexlify("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

binascii.b2a_base64(a)
#things get a bit weird since len("49276d...") > 57.

def hex2base64(input):
	return input.decode('hex').encode('base64')

input = raw_input()
print "======================================================= \n", hex2base64(input)
