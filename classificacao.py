porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]
marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

teste = [misterioso1, misterioso2, misterioso3]
marcoes_teste = [-1, 1, -1]

resultado = modelo.predict(teste)

diferencas = resultado - marcoes_teste
acertos = [d for d in diferencas if d == 0]
total_acertos = len(acertos)
total_elementos = len(teste)
taxa_acerto = (total_acertos / total_elementos) * 100.0

print(resultado)
print(diferencas)
print(taxa_acerto)