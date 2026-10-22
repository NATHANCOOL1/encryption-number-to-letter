letterencrypt = 0
encrypted = 0
fileinput = input("name of the file for encrypting with .txt/")
fileoutput = input("name of the file for the output with .txt/")
file = open(fileoutput, 'w+')
r = open(fileinput, 'r')
r.read()
character = int(r.tell())
r.seek(0)
while character > 0:
 if encrypted == 0:
      rcontents = r.read(1)
 else:
      encrypted -= 1
      r.read(encrypted)
      rcontents = r.read(1)
 if rcontents == 'a':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('197')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'b':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('208')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'c':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('213')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'd':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('241')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'e':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('156')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'f':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('183')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'g':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('172')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'h':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('133')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'i':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('170')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'j':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('148')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'k':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('198')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'l':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('174')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'm':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('112')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'n':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('251')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'o':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('187')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'p':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('123')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'q':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('168')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'r':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('245')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 's':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('165')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 't':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('224')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'u':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('141')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'v':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('253')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'w':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('182')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'x':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('145')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'y':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('247')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'z':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('134')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'A':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('211')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'B':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('242')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'C':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('201')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'D':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('219')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'E':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('252')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'F':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('212')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'G':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('144')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'H':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('151')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'I':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('116')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'J':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('186')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'K':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('179')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'L':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('119')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'M':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('207')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'N':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('157')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'O':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('222')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'P':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('110')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'Q':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('124')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'R':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('225')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'S':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('102')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'T':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('175')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'U':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('152')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'V':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('128')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'W':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('193')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'X':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('164')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'Y':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('237')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == 'Z':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('137')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == '1':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('227')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == '2':
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('142')
     letterencrypt += 3
     encrypted += 1
     character -= 1

 if rcontents == '3':
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('206')
     letterencrypt += 3
     encrypted += 1
     character -= 1

 if rcontents == '4':
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('106')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == '5':
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('218')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == '6':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('244')
    letterencrypt += 3
    encrypted += 1
    character -= 1

 if rcontents == '7':
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('192')
     letterencrypt += 3
     encrypted += 1
     character -= 1

 if rcontents == '8':
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('118')
     letterencrypt += 3
     encrypted += 1
     character -= 1

 if rcontents == '9':
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('246')
      letterencrypt += 3
      encrypted += 1
      character -= 1
      
 if rcontents == '0':
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('147')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "\n" :
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('811')
    letterencrypt += 3
    encrypted += 1
    character -= 2

 if rcontents == " " :
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('844')
     letterencrypt += 3
     encrypted += 1
     character -= 1

 if rcontents == "&" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('388')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "é" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('288')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "~" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('555')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == '"' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('855')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "#" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('755')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "'" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('699')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "{" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('166')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == '(' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('700')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "[" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('511')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "-" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('911')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "|" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('135')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == 'è' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('999')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "`" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('255')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "_" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('655')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "\\" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('455')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == 'ç' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('488')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "^" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('556')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "à" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('100')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "@" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('322')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == '°' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('444')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == ")" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('223')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "]" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('688')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "+" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('588')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == '=' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('200')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "}" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('101')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "<" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('522')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == ">" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('400')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == 'â' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('366')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "ê" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('500')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "û" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('399')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "ô" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('900')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == 'î' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('877')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "Â" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('933')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "Ê" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('800')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "Û" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('577')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == 'Ô' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('544')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "Î" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('799')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "ä" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('422')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "ë" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('722')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == 'ï' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('248')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "ö" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('411')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "ü" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('677')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "Ä" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('177')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == 'Ë' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('822')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "Ï" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('311')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "Ö" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('944')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "Ü" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('566')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == '£' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('777')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "$" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('533')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "¤" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('199')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "µ" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('701')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == '*' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('955')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "ù" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('733')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "%" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('744')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "?" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('499')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == ',' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('355')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "." :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('188')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == ";" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('600')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "/" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('299')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == ':' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('866')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "§" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('344')
      letterencrypt += 3
      encrypted += 1
      character -= 1

 if rcontents == "!" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('233')
       letterencrypt += 3
       encrypted += 1
       character -= 1

 if rcontents == "²" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('833')
      letterencrypt += 3
      encrypted += 1
      character -= 1
print("finish the encryption")
input("press enter to close/")