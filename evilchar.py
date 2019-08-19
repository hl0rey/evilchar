import sys

charList = {
    "A": "\u0410",
    "a": "\u0430",
    "B":"\u0412",
    "b": "\u0185",
    "C":"\u2CA4",
    "c":"\u2CA5",
    #"D":"",
    "d":"\u0501",
    "E":"\u0415",
    "e":"\u0435",
    '''
    "F":"",
    "f":"",
    "G":"",
    "g":"",
    '''
    "H":"\u041D",
    #"h":"",
    #"I":"",
    "i":"\u0456",
    "J":"\u0408",
    "j":"\u0458",
    '''
    "K":"",
    "k":"",
    "L":"",
    "l":"",
    "M":"",
    "m":"",
    "N":"",
    "n":"",
    '''
    "O":"\u2C9F",
    "o":"\u2C9E",
    "P":"\u0420",
    "p":"\u0440",
    #"Q":"",
    "q":"\u051B",
    #"R":"",
    "r":"\u0433",
    "S":"\u0405",
    "s":"\u0455",
    '''
    "T":"",
    "t":"",
    "U":"",
    "u":"",
    "V":"",
    "v":"",
    '''
    "W":"\u051C",
    "w":"\u051D",
    '''
    "X":"",
    "x":"",
    "Y":"",
    "y":"",
    '''
    "Z":"\u2C8C",
    "z":"\u2C8D"
          }

string = ""
targetChar = ""
mode=""

def generate():

    print("\r\n[-]Generate mode")

    finalstr=string

    if "," in targetChar:
        targetlist = targetChar.split(",")
        for t in targetlist:
            if t in string:
                if t in charList:
                    print("\r\n[*]Replaced char:" + t)
                    print("[*]Use unicode char:" + charList[t])
                    print("[!]The final result:" + string.replace(t, charList[t]))
                    finalstr=finalstr.replace(t, charList[t])

                else:
                    print("\r\nTargetChar maybe not be replaced.\r\n")

            else:
                print("\r\n Can not find targetChar in String\r\n")

        print("\r\n[!]Repalce all char string: "+finalstr+"\r\n")

    elif targetChar in string:

        if targetChar in charList:

            print("\r\n[*]Replaced char:"+targetChar)
            print("[*]Use unicode char:"+charList[targetChar])
            print("[!]The final result:"+string.replace(targetChar,charList[targetChar]))

        else:
            print("\r\nTargetChar maybe not be replaced.\r\n")


    else:

        print("\r\n Can not find targetChar in String\r\n")

    return


def detect():

    print("\r\n[-]Detect mode\r\n")
    for c in string:
        code = ord(c)
        if code < 0x20 or code > 0x7E:
            print("[!]Char "+c+" is a evil char!Its code is "+hex(code))
    print("\r\n[*]Detect compelete\r\n")
    print("Unicode table: https://unicode-table.com/cn/")

def autoFind():

    print("\r\n[-]Auto find char mode\r\n")
    for s in string:
        if s in charList:
            print("[*]Can replaced char:" + s+" Use unicode char: " + charList[s])
    print("\r\n[*]Auto find compelete")

def main():

    if mode=='g':
        generate()
    if mode=='d':
        detect()
    if mode=='a':
        autoFind()

    return


if __name__ == '__main__':

    if len(sys.argv) ==4:

        if not sys.argv[1]=="g":
            print("\r\n[X]mode "+sys.argv[1]+" not defined.")
            sys.exit(0)

        mode=sys.argv[1]
        string = sys.argv[2]
        targetChar = sys.argv[3]
        main()
    elif len(sys.argv) ==3:

        if not (sys.argv[1]=="d" or sys.argv[1]=="a"):
            print("\r\n[X]mode " + sys.argv[1] + " not defined.")
            sys.exit(0)

        mode = sys.argv[1]
        string = sys.argv[2]
        main()

    else:
        print("""
        
        """)
        print("\r\nusage: \r\n")
        print("\tgenerate: evilchar.py g [string] [targetchar]\r\n")
        print("\tdetect: evilchar.py d [string]\r\n")
        print("\tautofind: evilchar.py a [string]\r\n")
        print("\t[targetchar]: a\r\n")
        print("\t[targetchar]: a,b,c\r\n")

        sys.exit(0)

