import itertools

inp = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = [ord(i) for i in "ICE"]


inp_arr = bytearray(inp, "utf8")

key_gen = itertools.cycle(key)

for i in range(len(inp_arr)):
    curr_key = next(key_gen)
    curr_item = inp_arr[i]
    inp_arr[i] = curr_item ^ curr_key

print(inp_arr.hex())
