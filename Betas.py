import yfinance as yf
import statsmodels.api as sm
import datetime as dt
import pandas as pd
import matplotlib as plt

#Interação com usuário, pede a quantidade de ações e o ticker de cada uma
print('Olá, este programa foi desenvolvido para calcular o beta de ações com o Ibovespa, do início de 2000 pra cá.')
answer = "s"
while answer == "s":
    num = int(input('Quantas ações gostaria de checar o beta? '))
    stocks = ['^BVSP']

    i = 0
    while i < num:
        new = str(input('Digite o Ticker da %sª ação seguido de .SA (padrão Yahoo Finance): '%(i+1)))
        stocks.append(new)
        i = i+1

    #Encontra cotações e calcula os retornos diários
    date = dt.datetime.now()
    year_2000 = date - dt.timedelta(days = 8453)

    cot = yf.download(stocks, year_2000, date)['Adj Close']
    ret = cot.pct_change().dropna()

    #Calcula beta de cada papel
    X = ret['^BVSP']
    j = 0
    while j < num:
        Y = ret[stocks[j+1]]
        X = sm.add_constant(X)
        model = sm.OLS(Y, X).fit()
        print('O beta de {0} é {1}, com um R² é de {2}'.format(stocks[j+1], model.params[1], model.rsquared))
        j = j+1
    
    answer = str(input('Gostaria de fazer uma nova consulta (o programa se fechará caso negativo) (s/n)? '))