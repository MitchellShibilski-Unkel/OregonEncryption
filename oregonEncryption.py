import base64


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijkmlnopqrstuvqxyz"
NUMBERS = "0123456789"
SPACE = " "
OTHER = "!?()[]{};:|,~`_-+=/@#$%^&*"

def encoding(file, writeToFile = False, returnValue = True):

    with open(file, 'r') as i:
        text = i.read()

    getLetters = iter(text)

    decimalNums = []
    for l in getLetters:
        if l in LETTERS or l in LOWERCASE_LETTERS or l in SPACE or l in OTHER or l in NUMBERS:
            if l == str("A") or l == str("a"):
                decimalNums.append(".0")
            elif l == str("B") or l == str("b"):
                decimalNums.append(".1")
            elif l == str("C") or l == str("c"):
                decimalNums.append(".2")
            elif l == str("D") or l == str("d"):
                decimalNums.append(".3")
            elif l == str("E") or l == str("e"):
                decimalNums.append(".4")
            elif l == str("F") or l == str("f"):
                decimalNums.append(".5")
            elif l == str("G") or l == str("g"):
                decimalNums.append(".6")
            elif l == str("H") or l == str("h"):
                decimalNums.append(".7")
            elif l == str("I") or l == str("i"):
                decimalNums.append(".i")
            elif l == str("K") or l == str("k"):
                decimalNums.append(".8")
            elif l == str("J") or l == str("j"):
                decimalNums.append(".9")
            elif l == str("K") or l == str("k"):
                decimalNums.append(".10")
            elif l == str("L") or l == str("l"):
                decimalNums.append(".11")
            elif l == str("M") or l == str("m"):
                decimalNums.append(".12")
            elif l == str("N") or l == str("n"):
                decimalNums.append(".13")
            elif l == str("O") or l == str("o"):
                decimalNums.append(".14")
            elif l == str("P") or l == str("p"):
                decimalNums.append(".15")
            elif l == str("Q") or l == str("q"):
                decimalNums.append(".16")
            elif l == str("R") or l == str("r"):
                decimalNums.append(".17")
            elif l == str("S") or l == str("s"):
                decimalNums.append(".18")
            elif l == str("T") or l == str("t"):
                decimalNums.append(".19")
            elif l == str("U") or l == str("u"):
                decimalNums.append(".20")
            elif l == str("V") or l == str("v"):
                decimalNums.append(".21")
            elif l == str("W") or l == str("w"):
                decimalNums.append(".22")
            elif l == str("X") or l == str("x"):
                decimalNums.append(".23")
            elif l == str("Y") or l == str("y"):
                decimalNums.append('.24')
            elif l == str("Z") or l == str("z"):
                decimalNums.append(".25")   
            elif l == str("0"):
                decimalNums.append(".aa")
            elif l == str("1"):
                decimalNums.append(".ab")
            elif l == str("2"):
                decimalNums.append(".ac")
            elif l == str("3"):
                decimalNums.append(".ad")
            elif l == str("4"):
                decimalNums.append(".ae")
            elif l == str("5"):
                decimalNums.append(".af")
            elif l == str("6"):
                decimalNums.append(".ag")
            elif l == str("7"):
                decimalNums.append(".ah")
            elif l == str("8"):
                decimalNums.append(".ai")
            elif l == str("9"):
                decimalNums.append(".aj")
            elif l == str(" "):
                decimalNums.append(".<>")
            else:
                decimalNums.append(f".{l}")

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

def decoding(encryptedMessage):
    stringToConvert = str(encryptedMessage)

    convertToBase_64_bytes = base64.b64decode(stringToConvert.encode("ascii"))
    convertFromBase_64 = convertToBase_64_bytes.decode("ascii")

    split = convertFromBase_64.split(".")

    matchList = []
    for s in split:
        if s == str("0"):
            matchList.append("a")
        elif s == str("1"):
            matchList.append("b")
        elif s == str("2"):
            matchList.append("c")
        elif s == str("3"):
            matchList.append("d")
        elif s == str("4"):
            matchList.append("e")
        elif s == str("5"):
            matchList.append("f")
        elif s == str("6"):
            matchList.append("g")
        elif s == str("7"):
            matchList.append("h")
        elif s == str("9"):
            matchList.append("j")
        elif s == str("10"):
            matchList.append("k")
        elif s == str("11"):
            matchList.append("l")
        elif s == str("12"):
            matchList.append("m")
        elif s == str("13"):
            matchList.append("n")
        elif s == str("14"):
            matchList.append("o")
        elif s == str("15"):
            matchList.append("p")
        elif s == str("16"):
            matchList.append("q")
        elif s == str("17"):
            matchList.append("r")
        elif s == str("18"):
            matchList.append("s")
        elif s == str("19"):
            matchList.append("t")
        elif s == str("20"):
            matchList.append("u")
        elif s == str("21"):
            matchList.append("v")
        elif s == str("22"):
            matchList.append("w")
        elif s == str("23"):
            matchList.append("x")
        elif s == str("24"):
            matchList.append("y")
        elif s == str("25"):
            matchList.append("z")
        elif s == str("aa"):
            matchList.append("0")
        elif s == str("ab"):
            matchList.append("1")
        elif s == str("ac"):
            matchList.append("2")
        elif s == str("ad"):
            matchList.append("3")
        elif s == str("ae"):
            matchList.append("4")
        elif s == str("af"):
            matchList.append("5")
        elif s == str("ag"):
            matchList.append("6")
        elif s == str("ah"):
            matchList.append("7")
        elif s == str("ai"):
            matchList.append("8")
        elif s == str("aj"):
            matchList.append("9")
        elif s == str("<>"):
            matchList.append(" ")
        else:
            matchList.append(s)
            
    matchList.reverse()
            
    decryptedString = ", ".join(str(element) for element in matchList).replace(", ", "")
            
    return decryptedString