
def namero(Name):
    total = 0
    for c in Name.lower():
        num = ord(c) - 96
        if num >= 1 and num <=26:
            total += num
    return total

