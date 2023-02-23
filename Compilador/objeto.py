from scanner import *


#var declaradas
varInt  = []
varDouble  = []
varLit = []
ARG = []

def listVar():
    global varInt, varDouble, varLit
    print(f"int{varInt}")
    print(f"double{varDouble}")
    print(f"lit{varLit}")

def iniciaObj():
    file = open('code.c', 'a')
    file.write("#include<stdio.h>\ntypedef char literal[256];\nvoid main(void){\n")



def makeObj(gramNum,token):

    global varInt, varDouble, varLit, ARG
    file = open('code.c', 'a')

    if(gramNum==5):
        file.write("\n\n")

    if(gramNum==6): ############  A
        file.write(f";\n")
        #print (token)
    #if False:
        if (token[0] == "literal"):
            #print("lit")
            for i in (range(1,len(token),2)):
                varLit.append(token[i])
                modTabelaDeSimbolosTipo(token[i],"literal")
                #print(f"test lit[{token[i]}]")
        elif (token[0] == "real"):
            #print("real")
            for i in (range(1,len(token),2)):
                varDouble.append(token[i])
                modTabelaDeSimbolosTipo(token[i],"real")
                #print(token[i])
        elif (token[0] == "inteiro"):
            #print("int")
            for i in (range(1,len(token),2)):
                varInt.append(token[i])
                modTabelaDeSimbolosTipo(token[i],"inteiro")
                #print(token[i])
        else:
            print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} Tipo {token[0]} não conhecido" )
        
    
    if(gramNum==7): ############  B !!!!!!!!!! nao printa o inteiro B arumar no 5
        # L→ id vir L
        file.write("")

    if(gramNum==8): ############  C
        # L→ id
        file.write(f"\t{token[0]}")

    if(gramNum==9):
        
        file.write("\tint ")

    if(gramNum==10):
        
        file.write("\tdouble ")

    if(gramNum==11):
        #print ( token)
        file.write(f"\t{token[0]}")#literal
    
    if(gramNum==13):
        
        if(token[1] in varInt):
            file.write(f"\tscanf(\"%d\",&{token[1]});\n")
        elif (token[1] in varDouble):
            file.write(f"\tscanf(\"%lf\",&{token[1]});\n")
        elif(token[1] in varLit):
            file.write(f"\tscanf(\"%s\",{token[1]});\n")
        else:
            print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Variável [{token[1]}] não conhecido" )

    if(gramNum==14):####### arrumar bug print variavel
        #print (token)
        #print (ARG)
        for x in (range(0,len(ARG))):
            if(ARG[x][1] == token[1]):
                if(ARG[x][0] == "id"):
                    if(ARG[x][1] in varInt):
                        file.write(f"\tprintf(\"%d\",{ARG[x][1]});\n")
                    elif(ARG[x][1] in varDouble):
                        file.write(f"\tprintf(\"%lf\",{ARG[x][1]});\n")
                    elif(token[1] in varLit):
                        file.write(f"\tprintf(\"%s\",{ARG[x][1]});\n")
                elif(ARG[x][0] == "num"):
                    file.write(f"\tprintf(\"%ld\",{ARG[x][1]});\n")
                elif(ARG[x][0] == "literal"):
                    file.write(f"\tprintf(\"{token[1]}\");\n") 
                else:
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Variável [{token[1]}] não conhecido" )
                ARG.pop()

    if(gramNum==15): #lit
        #print(token)
        temp = ['literal', token[0]]
        ARG.append(temp)
        file.write("")

    if(gramNum==16): #num (real ou int)
        temp = ['num', token[0]]
        ARG.append(temp)
        
    
    if(gramNum==17): #id (variavel)

        if not((token[0] in varInt) or (token[0] in varDouble) or (token[0] in varLit)):
            print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Variável [{token[0]}] não declarada")
        else:
            temp = ['id', token[0]]
            ARG.append(temp)


    if(gramNum==19): # fazer erro
        file.write("")

    if(gramNum==20): # fazer erro
        file.write("")

    if(gramNum==21):
        file.write("")

    if(gramNum==22): # fazer erro
        file.write("")
    
    if(gramNum==23):
        file.write("")

    if(gramNum==25):
        file.write("\t}\n")

    if(gramNum==26):
        file.write("\tif( ")
        for i in (range(2,len(token)-1)):   
            file.write(f"{token[i] } ")
        file.write("{\n")
    
    if(gramNum==27): # fazer erro
        file.write("")

    if(gramNum==30):
        file.write("")

    if(gramNum==31): ############  D
        file.write("")

    if(gramNum==32): ############  E
        file.write("}")
        


    


