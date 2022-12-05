def scanner(file):
    char = file.read(1)
    #print(char)

    while(char == '\t' or char == '\n' or char == ' '): 
        char = file.read(1)

    if(char.isnumeric()):
        pass
        #return token lexema tipo

    if(char == '\"'):
        lexema = char
        char = file.read(1)
        while(char != '\"'):
            char = file.read(1)
            lexema += char
            if not char:
                return "ERRO \" não foi fechada"
        return f"Lit {lexema}"
        

    if(char.isalpha()):
        lexema = char
        char = file.read(1)
        while not (char == '\t' or char == '\n' or char == ' ' or not char) and (char.isalpha() or char.isnumeric() or char =='_'):
            lexema += char
            char = file.read(1)
        if(char == '\t' or char == '\n' or char == ' ' or not char):
            return f"id {lexema}"
        else:
            lexema += char
            return f"ERRO id \"{lexema}\" não valido, id não pode ter \"{char}\""
        #return token lexema tipo

    if(char == '{'):
        lexema = char
        while(char != '}'):
            char = file.read(1)
            lexema += char
            if not char:
                return " { não foi fechada"
        return f"Comentario {lexema}"
    
    if not char:
        return "EOF"

    if(char == '<'):
        char = file.read(1)
        if(char == '>'):
            return "OPR <>"
        if(char == '='):
            return f"OPR <="
        if(char == '-'):
            return f"ATR <-"
        if(char == '\t' or char == '\n' or char == ' ' or not char): #not char necessário ?
            return f"OPR <"
        else:
            return f"ERRO \">{char}\" não conhecido"
    if(char == '='):
        return f"OPR {char}"
    if(char == '>'):
        char = file.read(1)
        if(char == '='):
            return "OPR >="
        if(char == '\t' or char == '\n' or char == ' ' or not char): #not char necessário ?
            return "OPR >"
        else:
            return f"ERRO \">{char}\" não conhecido"


    if(char == '+'):
        return f"OPA {char}"
    if(char == '-'):
        return f"OPA {char}"
    if(char == '*'):
        return f"OPA {char}"
    if(char == '/'):
        return f"OPA {char}"


    if(char == '('):
        return "AB_P ("

    if(char == ')'):
        return "FC_P )"

    if(char == ';'):
        return "PT_V ;"

    if(char == ','):
        return "VIR ,"
    return f"ERRO {char} não conhecido"


file = open('code.txt', 'r')
Scanner = scanner(file)
while(Scanner != "EOF"):
    print(Scanner)
    Scanner = scanner(file)

# ADD linha e culuna do erro

