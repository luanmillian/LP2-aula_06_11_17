#fechando arquivo automaticamente com with & as , e verificando se ele fecha mesmo usando .closed
# coding=utf-8
with open ("tweets.txt") as arquivo:
    posicao = arquivo.tell()
    print(posicao) # mostra posição após abir
    conteudo = arquivo.read(10) # le 10 bytes
    print(conteudo)
    posicao = arquivo.tell()
    print(posicao) # mostra posição após ler 10 bytes

print ("arquivo fechado?", arquivo.closed)   #retornará um true
