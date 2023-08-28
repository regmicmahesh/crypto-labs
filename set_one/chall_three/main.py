import string

char_set = string.ascii_letters + string.digits

inp_ = bytearray.fromhex(
    "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
)

for i in char_set:
    temp_ = inp_.copy()
    for j in range(len(temp_)):
        temp_[j] = temp_[j] ^ ord(i)
    print(f"{i}\t\t" + temp_.decode("utf-8"))


# Ans: X is the key
