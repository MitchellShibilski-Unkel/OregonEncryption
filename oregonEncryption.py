import base64


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijkmlnopqrstuvqxyz"

def encoding(file, writeToFile = False, returnValue = True):

    with open(file, 'r') as i:
        text = i.read()

    getLetters = iter(text)

    decmialNums = []
    for l in getLetters:
        if l in LETTERS or l in LOWERCASE_LETTERS:
            if l == str("A") or l == str("a"):
                decmialNums.append(0)
            elif l == str("B") or l == str("b"):
                decmialNums.append(1)
            elif l == str("C") or l == str("c"):
                decmialNums.append(2)
            elif l == str("D") or l == str("d"):
                decmialNums.append(3)
            elif l == str("E") or l == str("e"):
                decmialNums.append(4)
            elif l == str("F") or l == str("f"):
                decmialNums.append(5)
            elif l == str("G") or l == str("g"):
                decmialNums.append(6)
            elif l == str("H") or l == str("h"):
                decmialNums.append(7)
            elif l == str("K") or l == str("k"):
                decmialNums.append(8)
            elif l == str("J") or l == str("j"):
                decmialNums.append(9)
            elif l == str("K") or l == str("k"):
                decmialNums.append(10)
            elif l == str("L") or l == str("l"):
                decmialNums.append(11)
            elif l == str("M") or l == str("m"):
                decmialNums.append(12)
            elif l == str("N") or l == str("n"):
                decmialNums.append(13)
            elif l == str("O") or l == str("o"):
                decmialNums.append(14)
            elif l == str("P") or l == str("p"):
                decmialNums.append(15)
            elif l == str("Q") or l == str("q"):
                decmialNums.append(16)
            elif l == str("R") or l == str("r"):
                decmialNums.append(17)
            elif l == str("S") or l == str("s"):
                decmialNums.append(18)
            elif l == str("T") or l == str("t"):
                decmialNums.append(19)
            elif l == str("U") or l == str("u"):
                decmialNums.append(20)
            elif l == str("V") or l == str("v"):
                decmialNums.append(21)
            elif l == str("W") or l == str("w"):
                decmialNums.append(22)
            elif l == str("X") or l == str("x"):
                decmialNums.append(23)
            elif l == str("Y") or l == str("y"):
                decmialNums.append(24)
            elif l == str("Z") or l == str("z"):
                decmialNums.append(25)   
            else:
                print("ERROR")
                break

    decmialNums.reverse()

    convertString = []
    for d in decmialNums:
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