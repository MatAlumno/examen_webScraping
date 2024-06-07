import json
import requests
import os
import pyperclip

response = requests.get('https://jsonplaceholder.typicode.com/posts')
response.raise_for_status
if response.status_code == 200:
    dataJson = response.json()
    nPost = input(f'Ingrese la cantidad de posteos entre 1 y 100: ')
    while 'a' <= nPost <= 'z' or nPost == '':
        nPost = input(f'NO, ingrese un numero de posteos: ')
    while nPost == '' or int(nPost) < 1 or int(nPost) > 100:
        nPost = input(f'NO, ingrese un numero entre 1 y 100: ')

    word = input(f'Ingrese una palabra para buscar entre los posts: ')
    while word == '':
        word = input(f'NO, ingrese una palabra: ')   
    
    primes = []
    notPrimes = []
    
    count = 0
    print(f'Post ID    |    Ocurrencias de {word} ')
    for n in range(int(nPost)):
        if word in dataJson[n]['title'] or word in dataJson[n]['body']:
            dataJson[n]['title']
            count += 1
            print(f'  {n}     |     si hay {word}')
    print(f'Cantidad de ocurrencias de {word} ')
    print(f'      {count}')
            #no supe como hacer que los cuente las ocurrencias
            #recuerdo que use algo para identificar palabras pero no me acuerdo

    