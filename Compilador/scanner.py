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

def getToken(file):
    
    global char,coluna,linha
    char = file.read(1)
    token = ''

    token = scanner(file)

    if(token == "EOF" and token == None):
        return token

    if (token != "EOF" and token["classe"] != "id" ):
        char = file.read(1)
        coluna+=1
    
    naTabela = buscaTabelaDeSimbolos(tabelaDeSimbolos, token)
    if (naTabela != False):
        
        token["classe"] = naTabela["classe"]
        token["tipo"]   = naTabela["tipo"]
    elif (token["classe"] == "id"):
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

    
    if(isNum(char)):
        lexema = char
        coluna +=1
        char = file.read(1)
        Tipo = "inteiro"
        while(char.isnumeric()):
            lexema += char
            coluna +=1
            char = file.read(1)
        if(char =="."):
            Tipo = "real"
            lexema += char
            coluna +=1
            char = file.read(1)
            if not (char.isnumeric()):
                return {"classe" : "ERRO", "lexema": lexema, "tipo":"NULO"}
            while(char.isnumeric()):
                lexema += char
                coluna +=1
                char = file.read(1)
        #opicional
        if(char =="e" or char =="E"):
            lexema += char
            coluna +=1
            char = file.read(1)
        
            if(char =="+" or char =="-"):
                lexema += char
                coluna +=1
                char = file.read(1)
            if not (char.isnumeric()):
                return {"classe" : "ERRO", "lexema": lexema, "tipo":"NULO"}
            while(char.isnumeric()):
                lexema += char
                coluna +=1
                char = file.read(1)
        while(char.isnumeric()):
            lexema += char
            coluna +=1
            char = file.read(1)
        return {"classe" : "Num", "lexema": lexema, "tipo":Tipo}

        #return token lexema tipo

    if(char == '\"'):
        lexema = char
        coluna +=1
        char = file.read(1)
        
        while(char != '\"'):
            lexema += char
            
            if(char == '\n'):
                coluna = 1
                linha +=1
            else:
                coluna +=1
            char = file.read(1)
            if not char:
                return {"classe" : "ERRO", "lexema": lexema, "tipo":"NULO"}
        return {"classe" : "Lit", "lexema": lexema, "tipo":"Constante Literal"}
    


    if(char.isalpha()):
        lexema = ''
        while (char.isalpha() or char.isnumeric() or char =='_'):
            lexema += char
            coluna +=1
            char = file.read(1)
            
        
        return {"classe" : "id", "lexema" : lexema, "tipo" : "nulo"}
        #return token lexema tipo

    
    if(char == '{'):
        lexema = char
        while(char != '}'):
            char = file.read(1)
            if(char == '\n'):
                coluna = 1
                linha +=1
            else:
                coluna +=1
            lexema += char
            if not char:
                return {"classe" : "ERRO", "lexema": lexema, "tipo":"NULO"}
        return {"classe" : "Comentario", "lexema": lexema, "tipo":"Comentario"}

    if not char:
        return "EOF"


    if(char == '<'):
        char = file.read(1)
        coluna+=1
        if(char == '>'):
            return {"classe" : "OPR", "lexema": "<>", "tipo":"Operador relacional"}
        if(char == '='):
            return {"classe" : "OPR", "lexema": "<=", "tipo":"Operador relacional"}
        if(char == '-'):
            return {"classe" : "ATR", "lexema": "<-", "tipo":"Atribuição"}
        if(char == '\t' or char == '\n' or char == ' ' or not char): #not char necessário ?
            return {"classe" : "OPR", "lexema": "<", "tipo":"Operador relacional"}
        else:
            return {"classe" : "ERRO", "lexema": "<"+char, "tipo":"NULO"}
    if(char == '='):
        return {"classe" : "OPR", "lexema": "=", "tipo":"Operador relacional"}
    if(char == '>'):
        char = file.read(1)
        coluna+=1
        if(char == '='):
            return {"classe" : "OPR", "lexema": ">=", "tipo":"Operador relacional"}
        if(char == '\t' or char == '\n' or char == ' ' or not char): #not char necessário ?
            return {"classe" : "OPR", "lexema": ">", "tipo":"Operador relacional"}
        else:
            return {"classe" : "ERRO", "lexema": "<"+char, "tipo":"NULO"}


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

    if(char == ';'):
        return {"classe" : "PT_V", "lexema": ";", "tipo":"Ponto e Vírgula"}

    if(char == ','):
        return {"classe" : "VIR", "lexema": ",", "tipo":"Vírgula"}
    
    print("[ERRO]\tCaracter não e valido.") 
      
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


if False: 
    print("\n\nTabela de Simbolos\n\n")

    for x in tabelaDeSimbolos:
        print(x)