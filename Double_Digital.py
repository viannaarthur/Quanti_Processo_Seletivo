import numpy as np
import scipy.stats as sp


print('Olá, esse programa visa calcular o preço justo de uma opção double digital')

answer = 'S'
while answer == 'S':
    Price = float(input('Qual o Preço do ativo subjacente? '))
    Lim_low = float(input('Qual o Limite Inferior dessa opção? '))
    Lim_high = float(input('Qual o Limite Superior dessa opção? '))
    Vol = float(input('Qual foi a Volatilidade Implícita do ativo no último ano (em %)? '))/100
    r = float(input('Qual a Taxa Livre de Risco da economia (em %)? '))/100
    Time = float(input('Por fim, quantos dias faltam para o vencimento? '))/365

    d1_c = (np.log(Price/Lim_low)+(r+(Vol**2)/2)*Time)/(Vol*Time**(1/2))
    d2_c = d1_c - Vol*Time**(1/2)
    Price_Call = Price*sp.norm.cdf(d1_c, 0, 1) - Lim_low*np.exp(-r*Time)*sp.norm.cdf(d2_c, 0, 1)

    d1_p = (np.log(Price/Lim_high)+(r+(Vol**2)/2)*Time)/(Vol*Time**(1/2))
    d2_p = d1_p - Vol*Time**(1/2)
    Price_Put = Lim_high*np.exp(-r*Time)*sp.norm.cdf(-d2_p, 0, 1) - Price*sp.norm.cdf(-d1_p, 0, 1)

    Price_DoubleDigital = Price_Call + Price_Put
    print(Price_DoubleDigital)

    answer = input('Você gostaria de fazer uma nova operação (o programa será fechado se negativo) (s/n)? ')
    answer = answer.upper()