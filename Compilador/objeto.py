
def iniciaObj():
    file = open('code.c', 'a')
    file.write("#include<stdio.h>\ntypedef char literal[256];\nvoid main(void){\n")

def makeObj(gramNum,token):
    file = open('code.c', 'a')

    if(gramNum==5):
        file.write("\n\n")

    if(gramNum==6): ############  A
        file.write(f";\n")
    
    if(gramNum==7): ############  B
        file.write("")

    if(gramNum==8): ############  C
        file.write("")
        file.write(f"{token}")

    if(gramNum==9):
        file.write("\tint ")

    if(gramNum==10):
        file.write("\tdouble ")

    if(gramNum==11):
        file.write(f"\t{token}")

    if(gramNum==12):
        file.write("")
    
    if(gramNum==13):
        file.write("")

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

    


