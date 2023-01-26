from scanner import *
import pandas as pd

PRINT_PILHA = False
GET_ON_TABLE = True
REDUCTION = True
REDUCE = True
SHIFT = True
TOKEN = False
FULL_PILHA = True
gram = [
    ["P'", "P"],                #1
    ["P","inicio","V","A"],     #2
    ["V","varinicio","LV"],     #3
    ["LV","D","LV"],            #4
    ["LV","varfim","PT_V"],     #5
    ["D","TIPO","L","PT_V"],    #6
    ["L","ID","VIR","L"],       #7
    ["L","ID"],                 #8
    ["TIPO","inteiro"],         #9
    ["TIPO","real"],            #10
    ["TIPO","literal"],         #11
    ["A","ES","A"],             #12
    ["ES","leia","ID","PT_V"],  #13
    ["ES","escreva","ARG","PT_V"],#14
    ["ARG","LIT"],              #15
    ["ARG","NUM"],              #16
    ["ARG","ID"],               #17
    ["A","CMD","A"],            #18
    ["CMD","ID","ATR","LD","PT_V"],#19
    ["LD","OPRD","OPA","OPRD"],#20
    ["LD","OPRD"],              #21
    ["OPRD","ID"],              #22
    ["OPRD","NUM"],             #23
    ["A","COND","A"],           #24
    ["COND","CAB","CP"],        #25
    ["CAB","se","AB_P", "EXP_R","FC_P","entao"],#26
    ["EXP_R","OPRD","OPR","OPRD"],#27
    ["CP","ES","CP"],           #28
    ["CP","CMD","CP"],          #29
    ["CP","COND","CP"],         #30
    ["CP","fimse"],             #31
    ["A","fim"]                 #32
]
pilha = [0]

def scan(file):
    token = getToken(file)
    while(token != "EOF"):
        print(token)
        token = getToken(file)

def main():


    global pilha,gram,linha,coluna
    Tabela = pd.read_csv("Tabela.csv")
    file = open('code.txt', 'r')
    #scan(file)

    token = getToken(file)
    if(TOKEN):
        print(f"TOKEN {token}")
    #print(Tabela[["inteiro"]])

    

    #print(Tabela)
    while(token != "EOF"):
        
        while(token == None):#comentario
            token = getToken(file)
            if(TOKEN):
                print(f"TOKEN {token}")

        UltimoPilha = pilha.pop()
        print(token)
        #print(Tabela.loc[2,"varinicio"])
        if(GET_ON_TABLE):
            print(f"GET TABELA [{UltimoPilha}] , [{token['classe'] }] ")
        Action = Tabela.loc[int(UltimoPilha),token['classe']]
        #print(Action)
        

        Action = Action.split(".")
        #print (f"Action {Action}")
        #print(Action)
        
        while(Action[0] == 'R'):
            if(REDUCE):
                print(f"-->\t\tReduce {Action[1]}")

            Gram = gram[int(Action[1]) - 1]
            if(REDUCTION):
                print(f"Gram[{int(Action[1])}] - {Gram[0]} <-",end=' ')
                for i in (range(1,len(Gram))):
                    print(f"{Gram[i]}",end=' ')
                print()

            lexemaList = []
            for i in reversed(range(1,len(Gram))):
                UltimoPilha = pilha.pop() # token
                lexemaList.append(UltimoPilha['lexema'])
                if((UltimoPilha['classe'] != Gram[i]) == True): 
                    print(UltimoPilha['classe'] != Gram[i])
                    print(f"{UltimoPilha['classe']}!={Gram[i]}.")
                if(UltimoPilha['classe'] != Gram[i]):#!!!!!!!
                    print("[ERRO]\tTabela e gramatica não bate.")
                UltimoPilha = pilha.pop() # num
            lexema = ''
            for i in reversed(range(1,len(Gram))):
                lexema += lexemaList.pop(0)
                lexema += ' '

            pilha.append(UltimoPilha)
            NewToken = {"classe" : Gram[0], "lexema": lexema, "tipo":'?'} 
            pilha.append(NewToken)
            if(GET_ON_TABLE):
                print(f"GET TABELA [{int(UltimoPilha)}] , [{Gram[0]} ] = {Tabela.loc[int(UltimoPilha),Gram[0]]}")
            
            pilha.append(Tabela.loc[int(UltimoPilha),Gram[0]])
            
            if(PRINT_PILHA):
                print(pilha)

            UltimoPilha = pilha.pop()
            Action = Tabela.loc[int(UltimoPilha),token['classe']]
            if(GET_ON_TABLE):
                print(f"GET TABLELA [{UltimoPilha}] , [{token['classe'] }] = {Action}")
            Action = Action.split(".")
            if(GET_ON_TABLE):
                print(f"ACTION{Action}")
            
        
        if(Action[0] == 'S'):
            if(SHIFT):
                print(f"-->\t\tShift {Action[1]}")
            #print(f"UltimoPilha = {UltimoPilha}")
            pilha.append(UltimoPilha)
            pilha.append(token)
            pilha.append(Action[1])

        if(Action[0] != 'S' and Action[0] != 'R'):
            print(f"[ERRO_P]\tLinha{linha}:Coluna{coluna}\t{Action} nao valida" )
            if(Action[0] != "E"): 
                #print(pilha)
                pilha.pop()
            else:
                pilha.append(UltimoPilha)

        token = getToken(file)
        if(TOKEN):
            print(f"TOKEN {token}")
        if(FULL_PILHA):
            print()
            print(*pilha, sep='\n')
            print()
        
if __name__ == "__main__":
    main()
    #print(pilha)
