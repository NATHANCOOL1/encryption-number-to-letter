letterencrypt = 0
encrypted = 0
fileinput = input("name of the file for encrypting with .txt/")
fileoutput = input("name of the file for the output with .txt/")
file = open(fileoutput, 'w+')
r = open(fileinput, 'r')
r.read()
character = int(r.tell())
print(character)
r.seek(0)
while character > 0:
 print(character)
 if encrypted == 0:
     rcontents = r.read(3)
 else:
     encrypted -= 3
     r.read(encrypted)
     rcontents = r.read(3)
 if rcontents == '197':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('a')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '208':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('b')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '213':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('c')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '241':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('d')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '156':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('e')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '183':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('f')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '172':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('g')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '133':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('h')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '170':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('i')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '148':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('j')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '198':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('k')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '174':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('l')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '112':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('m')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '251':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('n')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '187':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('o')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '123':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('p')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '168':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('q')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '245':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('r')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '165':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('s')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '224':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('t')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '141':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('u')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '253':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('v')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '182':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('w')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '145':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('x')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '247':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('y')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '134':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('z')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '211':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('A')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '242':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('B')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '201':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('C')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '219':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('D')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '252':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('E')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '212':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('F')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '144':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('G')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '151':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('H')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '116':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('I')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '186':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('J')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '179':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('K')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '119':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('L')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '207':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('M')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '157':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('N')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '222':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('O')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '110':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('P')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '124':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('Q')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '225':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('R')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '102':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('S')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '175':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('T')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '152':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('U')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '128':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('V')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '193':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('W')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '164':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('X')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '237':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('Y')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '137':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('Z')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '227':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('1')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '142':
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('2')
     letterencrypt += 1
     encrypted += 3
     character -= 3

 if rcontents == '206':
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('3')
     letterencrypt += 1
     encrypted += 3
     character -= 3

 if rcontents == '106':
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('4')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '218':
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('5')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == '244':
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('6')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == '192':
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('7')
     letterencrypt += 1
     encrypted += 3
     character -= 3

 if rcontents == '118':
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write('8')
     letterencrypt += 1
     encrypted += 3
     character -= 3

 if rcontents == '246':
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('9')
      letterencrypt += 1
      encrypted += 3
      character -= 3
      
 if rcontents == '147':
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('0')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "811" :
    w = open(fileoutput, 'r+')
    w.read(letterencrypt)
    w.write('\n')
    letterencrypt += 1
    encrypted += 3
    character -= 3

 if rcontents == "844" :
     w = open(fileoutput, 'r+')
     w.read(letterencrypt)
     w.write(' ')
     letterencrypt += 1
     encrypted += 3
     character -= 3

 if rcontents == "388" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('&')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "288" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('é')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "555" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('~')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '855' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('"')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "755" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('#')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "699" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write("'")
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "166" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('{')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '700' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('(')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "511" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('[')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "911" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('-')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "135" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('|')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '999' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('è')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "255" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('`')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "655" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('_')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "455" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('\\')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '488' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('ç')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "556" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('^')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "100" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('à')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "322" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('@')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '444' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('°')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "223" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write(')')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "688" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write(']')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "588" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('+')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '200' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('=')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "101" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('}')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "522" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('<')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "400" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('>')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '366' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('â')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "500" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('ê')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "399" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('û')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "900" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('ô')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '877' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('î')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "933" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('Â')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "800" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('Ê')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "577" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('Û')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '544' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('Ô')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "799" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('Î')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "422" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('ä')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "722" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('ë')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '248' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('ï')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "411" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('ö')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "677" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('ü')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "177" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('Ä')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '822' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('Ë')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "311" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('Ï')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "944" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('Ö')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "566" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('Ü')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '777' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('£')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "533" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('$')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "199" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('¤')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "701" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('µ')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '955' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('*')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "733" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('ù')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "744" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('%')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "499" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('?')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '355' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write(',')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "188" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('.')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "600" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write(';')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "299" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('/')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == '866' :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write(':')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "344" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('§')
      letterencrypt += 1
      encrypted += 3
      character -= 3

 if rcontents == "233" :
       w = open(fileoutput, 'r+')
       w.read(letterencrypt)
       w.write('!')
       letterencrypt += 1
       encrypted += 3
       character -= 3

 if rcontents == "833" :
      w = open(fileoutput, 'r+')
      w.read(letterencrypt)
      w.write('²')
      letterencrypt += 1
      encrypted += 3
      character -= 3

print("finish the decryption")
input("press enter to close/")