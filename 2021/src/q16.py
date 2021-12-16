from math import prod


def greater(args):
    return 1 if args[0] > args[1] else 0


def lesser(args):
    return 1 if args[0] < args[1] else 0


def middling(args):
    return 1 if args[0] == args[1] else 0


class Decoder:

    OP_MAP = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: greater,
        6: lesser,
        7: middling,
    }  # Evil is evil, Stregobor
    HEX_MAP = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    def __init__(self, hex_string):
        self.hex_string = hex_string
        self.bin_string = self.hex_to_binary()
        self.total_bits = len(self.bin_string)
        self.version_sum = 0
        _, values = self.decode_by_bits(self.bin_string, self.total_bits)
        self.value = values[0]

    def hex_to_binary(self):
        bin_string = ""
        for char in self.hex_string:
            bin_string += Decoder.HEX_MAP[char]
        return bin_string

    def decode_by_bits(self, bin_string, total_bits):
        index = 0
        values = []
        while index < (total_bits - 7):
            packet_type = "lit" if bin_string[index + 3 : index + 6] == "100" else "op"
            if packet_type == "lit":
                bits_used, value = self.decode_literal(bin_string[index:])
            else:
                bits_used, value = self.decode_operator(bin_string[index:])
            index += bits_used
            values.append(value)
        return total_bits, values

    def decode_by_packets(self, bin_string, total_packets):
        index = 0
        packets = 0
        values = []
        while packets < total_packets:
            packet_type = "lit" if bin_string[index + 3 : index + 6] == "100" else "op"
            if packet_type == "lit":
                bits_used, value = self.decode_literal(bin_string[index:])
            else:
                bits_used, value = self.decode_operator(bin_string[index:])
            packets += 1
            index += bits_used
            values.append(value)
        return index, values

    def decode_literal(self, new_string):
        version = int(new_string[:3], 2)
        self.version_sum += version
        val_string = ""
        idx = 6
        while new_string[idx] == "1":
            val_string += new_string[idx + 1 : idx + 5]
            idx += 5
        val_string += new_string[idx + 1 : idx + 5]
        val = int(val_string, 2)
        idx += 5
        return idx, val  # return number of bits to advance

    def decode_operator(self, new_string):
        version = int(new_string[:3], 2)
        op_type = int(new_string[3:6], 2)
        operator = Decoder.OP_MAP[op_type]
        self.version_sum += version
        operator_class = "BITS" if new_string[6] == "0" else "PACKETS"
        if operator_class == "BITS":
            nested_bits = int(new_string[7:22], 2)
            bits_used, values = self.decode_by_bits(new_string[22:], nested_bits)
            bits_used += 22
        else:  # operator_class == "PACKETS"
            sub_packets = int(new_string[7:18], 2)
            bits_used, values = self.decode_by_packets(new_string[18:], sub_packets)
            bits_used += 18
        value = operator(values)
        return bits_used, value


with open("2021/res/in16.txt") as file:
    puzzle_input, pt1_tests, pt2_tests = file.read().split("\n\n")

pt1_tests = [
    (test.split(" ")[0], int(test.split(" ")[1])) for test in pt1_tests.split("\n")
]
pt2_tests = [
    (test.split(" ")[0], int(test.split(" ")[1])) for test in pt2_tests.split("\n")
]

for i, test in enumerate(pt1_tests):
    hex_string, expected_sum = test
    d = Decoder(hex_string)
    if d.version_sum != expected_sum:
        print(
            f"Part 1 test # {i + 1} failed: expected {expected_sum}, got {d.version_sum}"
        )
        exit()
print("All Part 1 tests passing")

for i, test in enumerate(pt2_tests):
    hex_string, expected_val = test
    d = Decoder(hex_string)
    if d.value != expected_val:
        print(
            f"Part 1 test # {i + 1} failed: expected {expected_sum}, got {d.version_sum}"
        )
        exit()
print("All Part 2 tests passing")

puzzle_decoder = Decoder(puzzle_input)

pt1 = puzzle_decoder.version_sum
pt2 = puzzle_decoder.value
print("Part 1 solution: ", pt1)
print("Part 2 solution: ", pt2)
