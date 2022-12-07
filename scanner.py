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

def main():
    file = open('code.txt', 'r')
    global char,coluna,linha
    char = file.read(1)
    while True:
        
        token = scanner(file)

        if (token["classe"] == "ERRO"):
            print(f"ERRO LÉXICO – Caractere inválido na linguagem, linha {linha}, coluna {coluna}")
        if (token["classe"] != "id"):
            char = file.read(1)
            coluna+=1
        
        if (buscaTabelaDeSimbolos(tabelaDeSimbolos, token)):
            if token["lexema"] == "inicio":
                token["classe"] = "inicio"
                token["tipo"]   = "inicio"
            elif token["lexema"] == "varinicio":
                token["classe"] = "varinicio"
                token["tipo"]   = "varinicio"
            elif token["lexema"] == "varfim":
                token["classe"] = "varfim"
                token["tipo"]   = "varfim"
            elif token["lexema"] == "escreva":
                token["classe"] = "escreva"
                token["tipo"]   = "escreva"
            elif token["lexema"] == "leia":
                token["classe"] = "leia"
                token["tipo"]   = "leia"
            elif token["lexema"] == "se":
                token["classe"] = "se"
                token["tipo"]   = "se"
            elif token["lexema"] == "entao":
                token["classe"] = "entao"
                token["tipo"]   = "entao"
            elif token["lexema"] == "fimse":
                token["classe"] = "fimse"
                token["tipo"]   = "fimse"
            elif token["lexema"] == "fim":
                token["classe"] = "fim"
                token["tipo"]   = "fim"
            elif token["lexema"] == "inteiro":
                token["classe"] = "inteiro"
                token["tipo"]   = "inteiro"
            elif token["lexema"] == "literal":
                token["classe"] = "literal"
                token["tipo"]   = "literal"
            elif token["lexema"] == "real":
                token["classe"] = "real"
                token["tipo"]   = "real"
        else:
            if token["classe"] == "id":
                adicionarTabelaDeSimbolos(tabelaDeSimbolos, token)

        if (token["classe"] != "ERRO"):
            print(token)
        #print("Classe: " + token["classe"] + ", Lexema: " + token["lexema"] + ", Tipo: " + token["tipo"])
        
        if token["lexema"] == "fim":
            break



def scanner(file):
    global char, linha, coluna
    while(char == '\t' or char == '\n' or char == ' '):
        if(char == '\t' or char == '\n'):
            coluna = 1
            linha +=1
        else:
            coluna +=1
        char = file.read(1)

    """
    if(char.isnumeric()):
        pass
        #return token lexema tipo

    """

    if(char == '\"'):
        lexema = char
        char = file.read(1)
        while(char != '\"'):
            char = file.read(1)
            lexema += char
            if not char:
                return {"classe" : "ERRO", "lexema": lexema, "tipo":"NULO"}
        return {"classe" : "LIT", "lexema": lexema, "tipo":"Constante Literal"}
    


    if(char.isalpha()):
        lexema = ''
        while (char.isalpha() or char.isnumeric() or char =='_'):
            lexema += char
            coluna += 1
            char = file.read(1)
            
        
        return {"classe" : "id", "lexema" : lexema, "tipo" : "nulo"}
        #return token lexema tipo

    
    if(char == '{'):
        lexema = char
        while(char != '}'):
            char = file.read(1)
            linha+=1
            lexema += char
            if not char:
                return {"classe" : "ERRO", "lexema": lexema, "tipo":"NULO"}
        return {"classe" : "Comentario", "lexema": lexema, "tipo":"Comentario"}
    
    """

    if not char:
        return "EOF"

    """

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
    
    return {"classe" : "ERRO", "lexema": char, "tipo":"NULO"}
      
def buscaTabelaDeSimbolos(tabelaDeSimbolos, token):

    if(token["classe"] == "ERRO"):
        return False
    for x in tabelaDeSimbolos:
        if x["lexema"] == token["lexema"]:
            return True

    return False

def adicionarTabelaDeSimbolos(tabelaDeSimbolos, token):
    tabelaDeSimbolos.append(token)


if __name__ == "__main__":
    main()

print("\n\nTabela de Simbolos\n\n")

for x in tabelaDeSimbolos:
    print(x)