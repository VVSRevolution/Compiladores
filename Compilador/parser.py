from scanner import *
from objeto import *
import pandas as pd

PRINT_PILHA = False
GET_ON_TABLE = False
REDUCTION_GRAM = True
REDUCE = False
SHIFT = False
TOKEN = False
FULL_PILHA = False
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

def main():


    global pilha, gram
    Tabela = pd.read_csv("Tabela1.csv")
    file = open('code.txt', 'r')
    #scan(file)

    token = getToken(file)
    if(TOKEN):
        print(f"TOKEN {token}")
    #print(Tabela[["inteiro"]])

    

    #print(Tabela)
    while(True):
        
        if((token["classe"]=="EOF" and pilha[-1] == "0")):
            break


        while(token == None):#comentario
            token = getToken(file)
            if(TOKEN):
                print(f"TOKEN {token}")

        UltimoPilha = pilha.pop()
        
        #print(Tabela.loc[2,"varinicio"])
        if(GET_ON_TABLE):
            print(f"GET TABELA1 [{UltimoPilha}] , [{token['classe']}] = {Tabela.loc[int(UltimoPilha),token['classe']]} ")
        
        Action = Tabela.loc[int(UltimoPilha),token['classe']]
        while pd.isnull(Tabela.loc[int(UltimoPilha),token['classe']]):
            
            print(f"[ERRO_PARSER]\t{getLinhaColuna()} -> SRL TABLE[{UltimoPilha}][{token['classe']}] = {Action}, A sintaxe não valida, ferifique o Token: {token}" )
            token = getToken(file)
            if(GET_ON_TABLE):
                print(f"GET TABELA1 [{UltimoPilha}] , [{token['classe']}] = {Tabela.loc[int(UltimoPilha),token['classe']]} ")
            Action = Tabela.loc[int(UltimoPilha),token['classe']]

        if Action == "acc": break
        #print(Action)
        
        
        Action = Action.split(".")
        #print (f"Action {Action}")
        #print(Action)
        
        while(Action[0] == 'R'):
            if(REDUCE):
                print(f"-->\t\tReduce {Action[1]}")

            Gram = gram[int(Action[1])]

            makeObj(int(Action[1])+1)

            if(REDUCTION_GRAM):
                print(f">>>>>>>>>>>>>>>>> Gram[{int(Action[1])+1}] - {Gram[0]} ->",end=' ')
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
                print(f"GET TABELA2 [{int(UltimoPilha)}] , [{Gram[0]} ] = {Tabela.loc[int(UltimoPilha),Gram[0]]}")
            
            pilha.append(Tabela.loc[int(UltimoPilha),Gram[0]])
            
            if(PRINT_PILHA):
                print(pilha)

            UltimoPilha = pilha.pop()
            Action = Tabela.loc[int(UltimoPilha),token['classe']]

            while pd.isnull(Tabela.loc[int(UltimoPilha),token['classe']]):
                print(f"[ERRO_PARSER]\t{getLinhaColuna()} -> SRL TABLE[{UltimoPilha}][{token['classe']}] = {Action}, A sintaxe não valida, verifique o Token: {token}" )
                token = getToken(file)
                if(GET_ON_TABLE):
                    print(f"GET TABELA1 [{UltimoPilha}] , [{token['classe']}] = {Tabela.loc[int(UltimoPilha),token['classe']]} ")
                Action = Tabela.loc[int(UltimoPilha),token['classe']]

            if Action == "acc": break
            if(GET_ON_TABLE):
                print(f"GET TABELA3 [{UltimoPilha}] , [{token['classe'] }] = {Action}")
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

        if Action == "acc": break
        if(Action[0] != 'S' and Action[0] != 'R'):
            print(f"[ERRO_PARSER]\t{getLinhaColuna()}\t{Action} nao valida" )
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



