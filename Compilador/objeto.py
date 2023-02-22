from scanner import *

varInt  = []
varDouble  = []
varLit = []

def listVar():
    global varInt, varDouble, varLit
    print(f"int{varInt}")
    print(f"double{varDouble}")
    print(f"lit{varLit}")

def iniciaObj():
    file = open('code.c', 'a')
    file.write("#include<stdio.h>\ntypedef char literal[256];\nvoid main(void){\n")

def makeObj(gramNum,token):

    global varInt, varDouble, varLit
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
                #print(token[i])
        if (token[0] == "real"):
            #print("real")
            for i in (range(1,len(token),2)):
                varDouble.append(token[i])
                #print(token[i])
        if (token[0] == "inteiro"):
            #print("int")
            for i in (range(1,len(token),2)):
                varInt.append(token[i])
                #print(token[i])
        
    
    if(gramNum==7): ############  B !!!!!!!!!! nao printa o inteiro B arumar no 5
        file.write("")

    if(gramNum==8): ############  C
        print (token)
        file.write(f"\t{token[0]}")

    if(gramNum==9):
        file.write("\tint ")

    if(gramNum==10):
        file.write("\tdouble ")

    if(gramNum==11):
        #print ( token)
        file.write(f"\t{token[0]}")
    
    if(gramNum==13):
        file.write("")
        file.write(f"\t(13){token}")

    if(gramNum==14):
        file.write("")

    if(gramNum==15):
        file.write("")

    if(gramNum==16):
        file.write("")
    
    if(gramNum==17):
        file.write("")

    if(gramNum==18):
        file.write("")

    if(gramNum==19):
        file.write("")

    if(gramNum==20):
        file.write("")

    if(gramNum==21):
        file.write("")

    if(gramNum==22):
        file.write("")
    
    if(gramNum==23):
        file.write("")

    if(gramNum==24):
        file.write("")

    if(gramNum==25):
        file.write("")

    if(gramNum==26):
        file.write("")
    
    if(gramNum==27):
        file.write("")

    if(gramNum==30):
        file.write("")

    if(gramNum==31): ############  D
        file.write("")

    if(gramNum==32): ############  E
        file.write("}")

    


