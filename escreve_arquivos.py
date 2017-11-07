# coding=utf-8
with open("tweets.txt") as tweets:
    with open ("saida.txt", "w") as saída:
        saída.write(tweets)
print (saída.read())