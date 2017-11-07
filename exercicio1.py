# coding=utf-8

arquivo= open ("tweets.txt")

tweets=arquivo.read()

tweets.split("  ")
tweets.seek(0)
print (tweets)
            




