
def decimal_to_quaternary_number(dec_num):
    """
    This function converts a decimal number into a quaternary number (base 4) with Binary operations.
    The algorithm evaluates the Bit Pattern of a decimal number. The bits are grouped into pairs.
    Each bit pair represents a quaternary number: 00 -> 0, 01 -> 1, 10 -> 2, 11 -> 3
    Bitshifting is used to evaluate each bit pair starting at the end

    : param dec_num: decimal number
    : type dec_num: int
    : return: quaternary number
    : rtype: int
    """

    if dec_num < 0:
        raise ValueError("Input must be a non negative number.")

    if dec_num == 0:
        return 0

    result = ""
    while dec_num > 0:
        lastBits = dec_num & 0b11
        result = str(lastBits) + result
        dec_num = dec_num >> 2

    return int(result)


user_input = input("Enter a number: ")
dec_num = int(user_input)
print("Number in Quaternary numeral system (base 4):",
      decimal_to_quaternary_number(dec_num))
