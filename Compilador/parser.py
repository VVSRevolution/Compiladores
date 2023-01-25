from scanner import *

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


pilha = []

def main():

    global pilha
    file = open('code.txt', 'r')
    token = getToken(file)

    while(token != "EOF"):
        while(token == None):#comentario
            token = getToken(file)
        print (token)
        pilha.append(token)

        

        #CODE


        token = getToken(file)

if __name__ == "__main__":
    main()
    print(pilha)
