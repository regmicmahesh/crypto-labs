

inp = bytearray.fromhex("1c0111001f010100061a024b53535009181c")

print(inp)

operand = bytearray.fromhex("686974207468652062756c6c277320657965")


assert len(inp) == len(operand)


for i in range(len(inp)):
    temp = inp[i] ^ operand[i]
    inp[i] = temp
