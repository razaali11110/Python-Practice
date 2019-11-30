def binary(num):
    """ Function to convert a decimal number into binary """

    binary_number = ""  # in this variable...the binary number will be added after conversion
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif num >= 2:
        while num > 1:
            remainder = num % 2
            binary_number = str(remainder) + binary_number
            num //= 2  # this will reduce the number for the loop

            if num == 1:
                binary_number = str(1) + binary_number
    return binary_number


def bit(binary_num):
    """ This function will convert the binary number into four bits """
    len_bin_number = len(binary_num)
    modulus = len_bin_number % 4  # this will check if the number is already in bit or not
    bits = ""
    if modulus != 0:
        for b in range(modulus * 4):
            bits = b * str(0) + str(binary_num)  # this will add zeros till the bit is closest bit is made
            if len(bits) <= modulus * 4 and len(bits) % 4 == 0:
                break
    else:
        bits = binary_num  # if the number does not need any zero addition this will return the number

    return bits


def hexa(bits):
    """ Function to convert bits into hexa decimal """
    len_bits = len(bits)
    range1 = 0
    range2 = 4
    final = []  # in this list...the hex number will be added for each bit

    while len_bits >= 0:
        total = 0  # here the total for each bit will be added... 8 4 2 1 method total

        each_bit = str(bit)[range1:range2]
        for i in range(len(each_bit)):
            if each_bit[0] == str(1):
                total += 8
            elif each_bit[0] == str(0):
                total += 0
            if each_bit[1] == str(1):
                total += 4
            elif each_bit[1] == str(0):
                total += 0
            if each_bit[2] == str(1):
                total += 2
            elif each_bit[2] == str(0):
                total += 0
            if each_bit[3] == str(1):
                total += 1
            elif each_bit[3] == str(0):
                total += 0
            if total <= 16:   # else the total will be multiplied by 4 because of for loop
                break

        # now replacing the number exceeding 9 with alphabets
        if total > 0 and total != 10 and total != 11 and total != 12 and total != 13 and total != 14 and total != 15:
            final.append(total)
        if total > 0 and total == 10:
            final.append("A")
        if total > 0 and total == 11:
            final.append("B")
        if total > 0 and total == 12:
            final.append("C")
        if total > 0 and total == 13:
            final.append("D")
        if total > 0 and total == 14:
            final.append("E")
        if total > 0 and total == 15:
            final.append("F")

        # for the next bit
        range1 += 4
        range2 += 5
        len_bits -= 4
        total = ""
    final_answer = "".join(str(element) for element in final)
    return final_answer

