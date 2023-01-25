from scanner import *


def main():
    file = open('code.txt', 'r')
    token = getToken(file)

    while(token != "EOF"):
        while(token == None):#comentario
            token = getToken(file)
             
        print (token)
        

        #CODE


        token = getToken(file)

if __name__ == "__main__":
    main()
