#imprimindo linha a linha com um \n no final 
# coding=utf-8
with open ("tweets.txt") as arquivo:
    for linha in arquivo:
       
        print(linha)
