import numpy as np
import scipy.stats as sp

print('Olá, esse programa tem o objetivo de calcular o preço teórico de uma Call ou Put para determinado ativo')

answer = 'S'
while answer == 'S':
    type = str(input('Estamos falando de uma Call ou de uma Put (C/P)? '))
    type = type.upper()

    while type != "C" and type != "P":
        type = str(input('Não entendi, por favor, digite C caso queira calcular o preço de uma Call, ou digite P caso queria de uma Put '))
        type = type.upper()

    print('Ok, vou precisar de algumas informações para calcular o preço teórico dessa opção')
    Price = float(input('Qual o Preço do ativo subjacente? '))
    Strike = float(input('Qual o Strike dessa opção? '))
    Vol = float(input('Qual foi a Volatilidade Implícita do ativo no último ano (em %)? '))/100
    r = float(input('Qual a Taxa Livre de Risco da economia (em %)? '))/100
    Time = float(input('Por fim, quantos dias faltam para o vencimento? '))/365

    d1 = (np.log(Price/Strike)+(r+(Vol**2)/2)*Time)/(Vol*Time**(1/2))
    d2 = d1 - Vol*Time**(1/2)

    if type == "C":
        Price_Call = Price*sp.norm.cdf(d1, 0, 1) - Strike*np.exp(-r*Time)*sp.norm.cdf(d2, 0, 1)
        print(Price_Call)

    if type == "P":
        Price_Put = Strike*np.exp(-r*Time)*sp.norm.cdf(-d2, 0, 1) - Price*sp.norm.cdf(-d1, 0, 1)
        print(Price_Put)

    answer = str(input('Quer fazer um novo cálculo (o programa fechará se negativo) (s/n)? '))
    answer = answer.upper()