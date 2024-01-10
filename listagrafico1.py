import matplotlib.pyplot as plt
# Dados em uma lista
rótulos = ['Maçãs', 'Laranjas', 'Bananas', 'Uvas', 'Figos']
valores = [5, 3, 6, 4, 7]
# Criar uma figura e eixos
fig, ax = plt.subplots()
# Criar o gráfico de barras
ax.bar(rótulos, valores)
# Inserir rótulos de dados e título do gráfico
ax.set_xlabel('Fruta')
ax.set_ylabel('Quantidade')
ax.set_title('Quantidades de Frutas')
# Exibir o gráfico
plt.show()
