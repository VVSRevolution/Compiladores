def scanner():
    file = open('code.txt', 'r')
    char = file.read(1)
    #print(char)
    
    if not char:
        return "EOF"

    if(char == '/t' or char == '/n' or char == ' '): 
        return "tab or line or space"

    if(char.isalpha()):
        pass

    if(char.isnumeric()):
        pass

    if(char == '\"'):
        while(char != '\"'):
            char = file.read(1)
            if not char:
                return "\" não foi fechada"
        return "Constante literal"

    if(char == '{'):
        while(char != '}'):
            char = file.read(1)
            if not char:
                return " { não foi fechada"
        return "Comentario"

    if(char == '+'):
        return "mais"

    if(char == '-'):
        return "menos"

    if(char == '*'):
        return "vezes"

    if(char == '/'):
        return "divisao"

    if(char == '='):
        return "igual"

    if(char == '('):
        return "abre parenteses"

    if(char == ')'):
        return "fecha parenteses"

    if(char == ';'):
        return "ponto e virgula"

    if(char == ','):
        return "virgula"

    if(char == '>'):
        char = file.read(1)
        if(char == '='):
            return "maior igual"
        if(char == '/t' or char == '/n' or char == ' ' or not char): #not char necessário ?
            return "maior"
        else:
            return f"ERROR \">{char}\" não conhecido"
    if(char == '<'):
        char = file.read(1)
        if(char == '>'):
            return "<>"
        if(char == '-'):
            return "<-"
        if(char == '='):
            return "menor igual"  
        if(char == '/t' or char == '/n' or char == ' ' or not char): #not char necessário ?
            return "menor"
        else:
            return f"ERROR \">{char}\" não conhecido"


print(scanner())