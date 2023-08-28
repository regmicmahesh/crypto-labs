import sys

base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def convert_to_base64_bitwise(input_str: str):

    bytes_ = bytes.fromhex(input_str)

    res = ""

    for i in range(0, len(bytes_), 3):

        six_bits = bytes_[i] & 0b11111100
        current_char = base64_table[six_bits >> 2]
        res += current_char

        carryover_bits = (bytes_[i] << 6) & 0b11111111

        try:
            bits_extracted = bytes_[i + 1] & 0b11110000
        except:
            current_char = base64_table[carryover_bits >> 2]
            res += current_char + "=="
            return

        temp = carryover_bits | (bits_extracted >> 2)
        second_char = temp & 0b11111100
        remaining_bits = bytes_[i + 1] & 0b1111

        current_char = base64_table[second_char >> 2]

        res += current_char

        carryover_bits = remaining_bits << 2

        try:
            third_place = (bytes_[i + 2] & 0b11000000) >> 6
        except:
            current_char = base64_table[carryover_bits]
            res += current_char + "="
            return

        third_digit = carryover_bits | third_place
        current_char = base64_table[third_digit]

        res += current_char

        next = bytes_[i + 2] & 0b111111
        current_char = base64_table[next]

        res += current_char

    print(res)


def convert_to_base64(input_str):
    bytes_ = input_str.encode("utf-8")
    del input_str

    # this will store binary digit padded in 8 bits.
    binary_str = [""] * len(bytes_)

    for i in range(len(bytes_)):
        x = bytes_[i]
        binary_str[i] = f"{x:08b}"

    result = ""

    for i in range(0, len(binary_str), 6):
        char = binary_str[i : i + 6]
        padded_char = f"{char:06}"  # pads the end with 0 to make the length 6
        idx = int(padded_char, 2)
        # print(bin(idx))
        result += base64_table[idx]

        remaining_bits = (6 - len(char)) // 2

        result += "=" * remaining_bits

    # print(result)


# convert_to_base64("A" * 100_000_000)
convert_to_base64_bitwise(
    "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
)
