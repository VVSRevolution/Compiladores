from scanner import *


def main():
    file = open('code.txt', 'r')
    token = getToken(file)

    while(token != "EOF"):

        print (token)

        if(token == None): # None = ERRO
            token = getToken(file)


        #CODE


        token = getToken(file)

if __name__ == "__main__":
    main()
