import binascii

a = binascii.unhexlify("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")

binascii.b2a_base64(a)
#things get a bit weird since len("49276d...") > 57.

input = raw_input()
ans = input.decode('hex').encode('base64')
print "======================================================= \n", ans
