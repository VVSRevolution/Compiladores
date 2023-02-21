tabelaDeSimbolos = [{"classe": "inicio", "lexema": "inicio", "tipo": "inicio"},
                    {"classe": "varinicio", "lexema": "varinicio", "tipo": "varinicio"},
                    {"classe": "varfim", "lexema": "varfim", "tipo": "varfim"},
                    {"classe": "escreva", "lexema": "escreva", "tipo": "escreva"},
                    {"classe": "leia", "lexema": "leia", "tipo": "leia"},
                    {"classe": "se", "lexema": "se", "tipo": "se"},
                    {"classe": "entao", "lexema": "entao", "tipo": "entao"},
                    {"classe": "fimse", "lexema": "fimse", "tipo": "fimse"},
                    {"classe": "fim", "lexema": "fim", "tipo": "fim"},
                    {"classe": "inteiro", "lexema": "inteiro", "tipo": "inteiro"},
                    {"classe": "literal", "lexema": "literal", "tipo": "literal"},
                    {"classe": "real", "lexema": "real", "tipo": "real"},
                   ]

linha = 1
coluna = 1
char = ''
CHAR=False
 
def getToken(file):
    
    global char,coluna,linha

    if(char==''):
        char = file.read(1) 
        if(CHAR): print(f"CHAR1 {char}")
    token = ''
    token = scanner(file)
    #print (f"TOKEN {token}")

    while(token==None):
        char = file.read(1)
        if(CHAR): print(f"CHAR2 {char}")
        coluna+=1
        token = scanner(file)

    if(token["classe"] == "EOF"):
        return token

    if (token["classe"] != "ID" and token != token["lexema"] != ">" and token != token["lexema"] != "<" and token["classe"] != "NUM"):
            #print (token["lexema"])
            char = file.read(1)
            if(CHAR): print(f"CHAR3 {char}")
            coluna+=1
    
    naTabela = buscaTabelaDeSimbolos(tabelaDeSimbolos, token)
    
    if (naTabela != False):
        token["classe"] = naTabela["classe"]
        token["tipo"]   = naTabela["tipo"]
    elif (token["classe"] == "ID"):
            adicionarTabelaDeSimbolos(tabelaDeSimbolos, token)

    if (token["classe"] != "Comentario"):
        #print(token)

        return token
    #print("Classe: " + token["classe"] + ", Lexema: " + token["lexema"] + ", Tipo: " + token["tipo"])
        

def scanner(file):
    global char, linha, coluna
    while(char == '\t' or char == '\n' or char == ' '):
        if(char == '\n'):
            coluna = 1
            linha +=1
        else:
            coluna +=1
        char = file.read(1)
        if(CHAR): print(f"CHAR4 {char}")

    if(char == ';'):
        return {"classe" : "PT_V", "lexema": ";", "tipo":"Ponto e Vírgula"}

    if(isNum(char)):
        #print(char)
        lexema = char
        coluna +=1
        char = file.read(1)
        if(CHAR): print(f"CHAR5 {char}")
        Tipo = "inteiro"
        while(isNum(char)):
            lexema += char
            coluna +=1
            char = file.read(1)
            if(CHAR): print(f"CHAR6 {char}")
        if(char =="."):
            Tipo = "real"
            lexema += char
            coluna +=1
            char = file.read(1)
            if(CHAR): print(f"CHAR7 {char}")
            if not (isNum(char)):
                lexema+=char
                print(f"[ERRO]\tLinha{linha}:Coluna{coluna}\t{lexema} não é valido, dever tem número apois '.'")
                return None
            while(isNum(char)):
                lexema += char
                coluna +=1
                char = file.read(1)
                if(CHAR): print(f"CHAR8 {char}")
            #opicional
            if(char =="e" or char =="E"):
                lexema += char
                coluna +=1
                char = file.read(1)
                if(CHAR): print(f"CHAR9 {char}")
            
                if(char =="+" or char =="-"):
                    lexema += char
                    coluna +=1
                    char = file.read(1)
                    if(CHAR): print(f"CHAR10 {char}")
                if not (char.isnumeric()):
                    lexema+=char
                    print(f"[ERRO]\tLinha{linha}:Coluna{coluna}\t{lexema} não é valido, dever tem número apois 'E'/'e' .")
                    return None
                while(char.isnumeric()):
                    lexema += char
                    coluna +=1
                    char = file.read(1)
                    if(CHAR): print(f"CHAR11 {char}")
            while(char.isnumeric()):
                lexema += char
                coluna +=1
                char = file.read(1)
                if(CHAR): print(f"CHAR12 {char}")
        return {"classe" : "NUM", "lexema": lexema, "tipo":Tipo}

        #return token lexema tipo

    if(char == '\"'):
        lexema = char
        coluna +=1
        char = file.read(1)
        if(CHAR): print(f"CHAR13 {char}")
        
        while(char != '\"'):
            lexema += char
            
            if(char == '\n'):
                coluna = 1
                linha +=1
            else:
                coluna +=1
            char = file.read(1)
            if(CHAR): print(f"CHAR14 {char}")
            if not char:
                lexema+=char
                print(f"[ERRO]\tLinha{linha}:Coluna{coluna}\t{lexema} não é valido, fim de arquivo sem fechar '\"'.")
                return None
        return {"classe" : "LIT", "lexema": lexema, "tipo":"Constante Literal"}
    


    if(char.isalpha()):
        lexema = ''
        while (char.isalpha() or char.isnumeric() or char =='_'):
            lexema += char
            coluna +=1
            char = file.read(1)
            if(CHAR): print(f"CHAR15 {char}")
        return {"classe" : "ID", "lexema" : lexema, "tipo" : "nulo"}
        #return token lexema tipo

    
    if(char == '{'):
        lexema = char
        while(char != '}'):
            char = file.read(1)
            if(CHAR): print(f"CHAR16 {char}")
            if(char == '\n'):
                coluna = 1
                linha +=1
            else:
                coluna +=1
            lexema += char
            if not char:
                lexema+=char
                print(f"[ERRO]\tLinha{linha}:Coluna{coluna}\t{lexema} não é valido, fim de arquivo sem fechar '}}'.")
                return None
        return {"classe" : "Comentario", "lexema": lexema, "tipo":"Comentario"}

    if not char:
        return {"classe" : "EOF", "lexema": "EOF", "tipo":"EOF"}



    if(char == '<'):
        lexema = char
        char = file.read(1)
        if(CHAR): print(f"CHAR17 {char}")
        coluna+=1
        if(char == '>'):
            lexema += char
            return {"classe" : "OPR", "lexema": lexema, "tipo":"Operador relacional"}
        elif(char == '='):
            lexema += char
            return {"classe" : "OPR", "lexema": lexema, "tipo":"Operador relacional"}
        elif(char == '-'):
            lexema += char
            return {"classe" : "ATR", "lexema": lexema, "tipo":"Atribuição"}
        else:
            return {"classe" : "OPR", "lexema": "<", "tipo":"Operador relacional"}

    if(char == '='):
        return {"classe" : "OPR", "lexema": "=", "tipo":"Operador relacional"}

    if(char == '>'):
        char = file.read(1)
        if(CHAR): print(f"CHAR18 {char}")
        coluna+=1
        if(char == '='):
            return {"classe" : "OPR", "lexema": ">=", "tipo":"Operador relacional"}
        elif(char == '\t' or char == '\n' or char == ' ' or not char): #not char necessário ?
            return {"classe" : "OPR", "lexema": ">", "tipo":"Operador relacional"}
        else:
            return {"classe" : "OPR", "lexema": ">", "tipo":"Operador relacional"}

    if(char == '+'):
        return {"classe" : "OPA", "lexema": "+", "tipo":"Operador aritmético"}
    if(char == '-'):
        return {"classe" : "OPA", "lexema": "-", "tipo":"Operador aritmético"}
    if(char == '*'):
        return {"classe" : "OPA", "lexema": "*", "tipo":"Operador aritmético"}
    if(char == '/'):
        return {"classe" : "OPA", "lexema": "/", "tipo":"Operador aritmético"}


    if(char == '('):
        return {"classe" : "AB_P", "lexema": "(", "tipo":"Abre Parênteses"}

    if(char == ')'):
        return {"classe" : "FC_P", "lexema": ")", "tipo":"Fecha Parênteses"}



    if(char == ','):
        return {"classe" : "VIR", "lexema": ",", "tipo":"Vírgula"}
    
    print(f"[ERRO]\tLinha{linha}:Coluna{coluna}\tCaracter '{char}' não é valido.") 

    return(None)
      
def buscaTabelaDeSimbolos(tabelaDeSimbolos, token):

    for x in tabelaDeSimbolos:
        if x["lexema"] == token["lexema"]:
            return x

    return False

def adicionarTabelaDeSimbolos(tabelaDeSimbolos, token):
    tabelaDeSimbolos.append(token)

def isNum(num):
    if(num == '0' or num == '1' or num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '5' or num == '8' or num == '9'):
        return True
    else:
        return False

def getLinhaColuna():
    global linha,coluna

    return f"Linha[{linha}] : Colinha[{coluna}]"