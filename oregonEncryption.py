import base64


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijkmlnopqrstuvqxyz"
NUMBERS = "0123456789"
SPACE = " "

def encoding(file, writeToFile = False, returnValue = True):

    with open(file, 'r') as i:
        text = i.read()

    getLetters = iter(text)

    decimalNums = []
    for l in getLetters:
        if l in LETTERS or l in LOWERCASE_LETTERS:
            if l == str("A") or l == str("a"):
                decimalNums.append(0)
            elif l == str("B") or l == str("b"):
                decimalNums.append(1)
            elif l == str("C") or l == str("c"):
                decimalNums.append(2)
            elif l == str("D") or l == str("d"):
                decimalNums.append(3)
            elif l == str("E") or l == str("e"):
                decimalNums.append(4)
            elif l == str("F") or l == str("f"):
                decimalNums.append(5)
            elif l == str("G") or l == str("g"):
                decimalNums.append(6)
            elif l == str("H") or l == str("h"):
                decimalNums.append(7)
            elif l == str("K") or l == str("k"):
                decimalNums.append(8)
            elif l == str("J") or l == str("j"):
                decimalNums.append(9)
            elif l == str("K") or l == str("k"):
                decimalNums.append(10)
            elif l == str("L") or l == str("l"):
                decimalNums.append(11)
            elif l == str("M") or l == str("m"):
                decimalNums.append(12)
            elif l == str("N") or l == str("n"):
                decimalNums.append(13)
            elif l == str("O") or l == str("o"):
                decimalNums.append(14)
            elif l == str("P") or l == str("p"):
                decimalNums.append(15)
            elif l == str("Q") or l == str("q"):
                decimalNums.append(16)
            elif l == str("R") or l == str("r"):
                decimalNums.append(17)
            elif l == str("S") or l == str("s"):
                decimalNums.append(18)
            elif l == str("T") or l == str("t"):
                decimalNums.append(19)
            elif l == str("U") or l == str("u"):
                decimalNums.append(20)
            elif l == str("V") or l == str("v"):
                decimalNums.append(21)
            elif l == str("W") or l == str("w"):
                decimalNums.append(22)
            elif l == str("X") or l == str("x"):
                decimalNums.append(23)
            elif l == str("Y") or l == str("y"):
                decimalNums.append(24)
            elif l == str("Z") or l == str("z"):
                decimalNums.append(25)   
            else:
                print("ERROR")
                break
        if l in NUMBERS:
            if l == str("0"):
                decimalNums.append("aa")
            elif l == str("1"):
                decimalNums.append("ab")
            elif l == str("2"):
                decimalNums.append("ac")
            elif l == str("3"):
                decimalNums.append("ad")
            elif l == str("4"):
                decimalNums.append("ae")
            elif l == str("5"):
                decimalNums.append("af")
            elif l == str("6"):
                decimalNums.append("ag")
            elif l == str("7"):
                decimalNums.append("ah")
            elif l == str("8"):
                decimalNums.append("ai")
            elif l == str("9"):
                decimalNums.append("aj")
            else:
                print("ERROR")
                break
        if l in SPACE:
            if l == str("."):
                decimalNums.append("<>")
            else:
                print("ERROR")
                break

    decimalNums.reverse()

    convertString = []
    for d in decimalNums:
        string = str(d)
        convertString.extend(string)

    mergeNumsToStr = str(", ").join(convertString)
    removeWaste = mergeNumsToStr.replace(", ", "")

    convertToBase_64_bytes = base64.b64encode(removeWaste.encode("ascii"))
    convertToBase_64 = convertToBase_64_bytes.decode("ascii")

    if writeToFile == True:
        with open(file, "w") as wr:
            wr.write(convertToBase_64)
    elif returnValue == True:
        return convertToBase_64
    else:
        print("ERROR: Please Select Either [writeToFile/returnValue]")