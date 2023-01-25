from scanner import *
import pandas as pd


gram = [
    ["P'", "P"],                #1
    ["P","inicio","V","A"],     #2
    ["V","varincio", "LV"],     #3
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

    global pilha,gram
    Tabela = pd.read_csv("Tabela.csv")
    file = open('code.txt', 'r')
    token = getToken(file)

    #print(Tabela)
    while(token != "EOF"):
        while(token == None):#comentario
            token = getToken(file)

        UltimoPilha = pilha.pop()

        #print(f"{UltimoPilha} , {token['classe'] }")

        #print(Tabela.loc[2,"varinicio"])
        Action = Tabela.loc[int(UltimoPilha),token['classe']]
        #print(Action)
        
        Action = Action.split(".")
        #print (f"Action {Action}")
        #print(Action)
        
        while(Action[0] == 'R'):
            print(f"Reduce {Action[1]}")
            Gram = gram[int(Action[1]) - 1]
            #print(Gram)
            for i in reversed(range(1,len(Gram))):
                UltimoPilha = pilha.pop()
                if((UltimoPilha['classe'] != Gram[i]) == True): 
                    print(UltimoPilha['classe'] != Gram[i])
                    print(UltimoPilha['classe'] , Gram[i])
                if(UltimoPilha['classe'] != Gram[i]):#!!!!!!!
                    print("[ERRO]\tTabela e gramatica não bate.")
                UltimoPilha = pilha.pop()
            pilha.append(UltimoPilha)
            pilha.append(token)
            pilha.append(Tabela.loc[int(UltimoPilha),Gram[0]])

            UltimoPilha = pilha.pop()
            Action = Tabela.loc[UltimoPilha,token["classe"]]
            Action = Action.split(".")
        
        if(Action[0] == 'S'):
            print(f"Shift {Action[1]}")
            pilha.append(UltimoPilha)
            pilha.append(token)
            pilha.append(Action[1])

        token = getToken(file)
        print(pilha)
        
if __name__ == "__main__":
    main()
    #print(pilha)
