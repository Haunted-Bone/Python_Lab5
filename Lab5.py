


def is_valid_part(part):


    if not part.isdigit():
        return False
    num = int(part)
    if 0 <= num <= 255:
        return str(num) == part
    return False



print(is_valid_part("192"))
print(is_valid_part("256"))
print(is_valid_part("01"))
print(is_valid_part("0"))
print(is_valid_part("abc"))
#print(is_valid_part(input("Give me a segment of an IP address please.")))

def is_valid_ip(address):
    if not address.isdigit():
        return False
    parts = address.split('.')
    if len(parts) == 4:
        for i in range(0, len(parts)):
            piece = parts[i:i]
            print(is_valid_part(piece))
    if len(parts) <= 4:
        print('Too few segments')
    if len(parts) >= 4:
        print('Too many segments')



#is_valid_ip(input("Give me a prospective IP address with periods included please"))


def convt_int_bin(num):


    print((bin(num)[2:]))


convt_int_bin(42)

