import json
import requests
import os

def isPrime(num):
    caca = 0
    for nu in range(num):
        if num % (nu+1) == 0:
            caca += 1
    if caca > 2:
        return(False)
    else:
        return(True)

response = requests.get('https://jsonplaceholder.typicode.com/posts')
response.raise_for_status
if response.status_code == 200:
    dataJson = response.json()
    nPost = input(f'Ingrese la cantidad de posteos entre 1 y 100: ')
    while 'a' <= nPost <= 'z' or nPost == '':
        nPost = input(f'NO, ingrese un numero de posteos: ')
    while nPost == '' or int(nPost) < 1 or int(nPost) > 100:
        nPost = input(f'NO, ingrese un numero entre 1 y 100: ')    
    
    primes = []
    notPrimes = []
    
    for n in range(int(nPost)):
        if isPrime(n+1):
            primes.append(dataJson[n])
            #print(dataJson[n]['id'])
        else:
            notPrimes.append(dataJson[n])

    fileP = open('dlXPrimes.json', 'w')
    fileP.write(json.dumps(primes, indent=4))
    fileP.close

    fileNP = open('dlXNotPrimes.json', 'w')
    fileNP.write(json.dumps(notPrimes, indent=4))
    fileNP.close