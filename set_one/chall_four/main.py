import string

data = [bytearray.fromhex(x.strip()) for x in open("input.txt").readlines()]

char_set = set(string.ascii_letters + string.digits + " ")

for key in char_set:
    for ba in data:
        temp = ba.copy()
        for i in range(len(ba)):
            temp[i] = ba[i] ^ ord(key)
        try:
            x = temp.decode("ascii").strip()
            if all((i in char_set for i in x)):
                print(x)
        except:
            ...

# Ans: Now that the party is jumping
