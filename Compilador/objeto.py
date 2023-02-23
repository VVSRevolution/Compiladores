from scanner import *


#var declaradas
varInt  = []
varDouble  = []
varLit = []
tempInt  = []
tempDouble  = []
tempLit = []
ARGfix = []
ARG = []
Cont = 0
tab = 0
def listVar():
    global varInt, varDouble, varLit, tempInt
    print(f"int{varInt}")
    print(f"double{varDouble}")
    print(f"lit{varLit}")
    print(f"temp int{tempInt}")
    print(f"temp double{tempDouble}")



def iniciaObj():
    file = open('code.c', 'a')
    file.write("#include<stdio.h>\ntypedef char literal[256];\nvoid main(void){\n\n\n\n")



def makeObj(gramNum,token):

    global varInt, varDouble, varLit, ARG, Cont, tab, tempDouble, tempLit
    file = open('code.c', 'a')

    if(gramNum==5):
        file.write("\n")

    if(gramNum==6): ############  A
        file.write(f";\n")
        print (token)
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
        
    
    if(gramNum==7): ############  B 
       # L→ id vir L

        file.write(f", {token[0]}")

    if(gramNum==8): ############  C
        print(token)
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
        for x in range(0,tab):
            file.write("\t")
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

    if(gramNum==16): #num (real ou int)
        temp = ['num', token[0]]
        ARG.append(temp)
    
    if(gramNum==17): #id (variavel)

        if not((token[0] in varInt) or (token[0] in varDouble) or (token[0] in varLit)):
            print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Variável [{token[0]}] não declarada")
        else:
            temp = ['id', token[0]]
            ARG.append(temp)


    if(gramNum==19): 
        #print(token)

        vars = []
        
        for x in range(0,len(token),2):
            temp = returnTipoDotoken(token[x])
            if(temp == "nulo"):
                if (token[x] in varInt or token[x] in tempInt): 
                    vars.append("int")
                elif (token[x] in varDouble or token[x] in tempDouble):
                    vars.append("double")
                elif (token[x] in varLit):
                    vars.append("lit")
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Não é possivel operar variavel literal")
                else: 
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 19 - token[x] = [{token[x]}]")
            elif (temp == False): 
                print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 19 - Função returnTipoDotoken retornou Falso")
            else: 
                if(temp == "inteiro"): vars.append("int")
                elif (temp == "real"): vars.append("double")
                else: print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 19 - Variavel [{token[x]}] = {temp}, não e possivel operar")
        
        ERRO = False
        
        for i in range(1,len(vars)):
            if(vars[0] != vars[i]):
                ERRO = True
        
        if(ERRO):
            msgErro = ''
            for x, i in zip(range(0,len(token),2), range(0,len(vars))):
                msgErro += f"Variavel [{token[x]}] é um [{vars[i]}]; "

            print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Tipos diferentes para atribuição -> {msgErro}")
        else:
            for x in range(0,tab):
                file.write("\t")
            file.write(f"\t{token[0]} = ")
            if(len(token) > 4 ):
                file.write(f"T{Cont-1};\n")
            else:
                file.write(f"{token[2]};\n")

    if(gramNum==20): 
        # LD→ OPRD opa OPRD
        #print (token)
        vars = []
        for x in range(0,tab):
            file.write("\t")
        for x in range(0,len(token),2):
            temp = returnTipoDotoken(token[x])
            if(temp == "nulo"):
                if (token[x] in varInt): vars.append("int")
                elif (token[x] in varDouble): 
                    vars.append("double")
                elif (token[x] in varDouble): 
                    vars.append("lit") 
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Não é possivel operar variavel literal")
                else: 
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 20 - token[x] = [{token[x]}]")
            elif (temp == False): print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 20 - Função returnTipoDotoken retornou Falso")
            else: 
                if(temp == "inteiro"): 
                    vars.append("int")
                elif (temp == "real"): 
                    vars.append("double")
                elif (temp == "literal"):
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Não é possivel operar variavel literal")
                else: print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 20 - Variavel [{token[x]}] = {temp}, não e possivel operar")
        
        ERRO = False
       
        for i in range(1,len(vars)):
            if(vars[0] != vars[i]):
                ERRO = True
        
        if(ERRO):
            msgErro = ''
            for x, i in zip(range(0,len(token),2), range(0,len(vars))):
                msgErro += f"Variavel [{token[x]}] é um [{vars[i]}]; "

            print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Tipos diferentes para atribuição -> {msgErro}")
        else:
            if(vars[0] == "int"):
                tempInt.append(f"T{Cont}")
            if(vars[0] == "double"):
                tempDouble.append(f"T{Cont}")

            file.write(f"\tT{Cont} = ")
            for x in range(0,len(token)):
                file.write(f"{token[x]} ")
            file.write(";\n")
            Cont+=1

    if(gramNum==21):
        #print (token)
        file.write("") # nao tem nessecidade, ja e feito no 27

    if(gramNum==22): 
        #print(token)

        if not((token[0] in varInt) or (token[0] in varDouble)):
            print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Variável [{token[0]}] não declarada")
        
    
    if(gramNum==23): # nao tem nessecidade, ja e feito no 27
        file.write("")

    if(gramNum==25):
        for x in range(0,tab):
            file.write("\t")
        file.write("\t}\n")

    if(gramNum==26):
        for x in range(0,tab):
            file.write("\t")
        file.write("\tif(")
           
        file.write(f"T{Cont-1})")
        file.write("{\n")
        tab+=1
    if(gramNum==27): # fazer erro
        #print(token)

        vars = []
        for x in range(0,tab):
            file.write("\t")
        for x in range(0,len(token),2):
            temp = returnTipoDotoken(token[x])
            if(temp == "nulo"):
                if (token[x] in varInt):
                    vars.append("int")
                elif (token[x] in varDouble): 
                    vars.append("double")
                elif (token[x] in varDouble): 
                    vars.append("lit") 
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Não é possivel operar variavel literal")
                else: 
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 27 - token[x] = [{token[x]}]")
            elif (temp == False): print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 27 - Função returnTipoDotoken retornou Falso")
            else: 
                if(temp == "inteiro"): 
                    vars.append("int")
                elif (temp == "real"): 
                    vars.append("double")
                elif (temp == "literal"):
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Não é possivel operar variavel literal")
                else: 
                    print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - ERRO INESPERADO - CODIGO 27 - Variavel [{token[x]}] = {temp}, não e possivel operar")
        ERRO = False
       
        for i in range(1,len(vars)):
            if(vars[0] != vars[i]):
                ERRO = True
        
        if(ERRO):
            msgErro = ''
            for x, i in zip(range(0,len(token),2), range(0,len(vars))):
                msgErro += f"Variavel [{token[x]}] é um [{vars[i]}]; "

            print(f"[ERRO_LEXEMA]\t{getLinhaColuna()} - Tipos diferentes para atribuição -> {msgErro}")
        else:
            tempInt.append(f"T{Cont}")

            file.write(f"\tT{Cont} = ")
            for x in range(0,len(token)):
                file.write(f"{token[x]} ")
            file.write(";\n")
            Cont+=1

    if(gramNum==31): ############  D
        tab-=1

    if(gramNum==32): ############  E
        file.write("}")
        file.close()
        colocarAsTemp()


def colocarAsTemp():
    with open('code.c','r',encoding='utf-8') as file:
        data = file.readlines()
    addTemp = "\t/*----Variaveis temporarias----*/\n"
    if(len(tempInt)>0):
        addTemp+="\tint"
        for x in range(0,len(tempInt)-1):
            addTemp+=f" {tempInt[x]},"
        addTemp+=f" {tempInt[len(tempInt)-1]}"
        addTemp+=";\n"
    if(len(tempDouble)>0):
        addTemp+="\tdouble"
        for x in range(0,len(tempDouble)-1):
            addTemp+=f" {tempDouble[x]},"
        addTemp+=f" {tempDouble[len(tempDouble)-1]}"
        addTemp+=";\n"
    if(len(tempLit)>0):
        addTemp+="\tliteral"
        for x in range(0,len(tempLit)-1):
            addTemp+=f" {tempLit[x]},"
        addTemp+=f" {tempLit[len(tempLit)-1]}"
        addTemp+=";\n"
    addTemp+="\t/*------------------------------*/"
    data[4] = addTemp
    file.close()

    with open('code.c', 'w', encoding='utf-8') as file:
        file.writelines(data)

    


