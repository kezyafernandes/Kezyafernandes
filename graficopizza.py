import matplotlib.pyplot as plt
# Dados
rotulos = ['Maçãs', 'Laranjas', 'Bananas', 'Uvas', 'Figos']
tamanhos = [25, 30, 20, 25, 27]
cores = ['red', 'orange', 'yellow', 'blue', 'purple']
# Criar figura e eixos
fig, ax = plt.subplots()
# Criar um gráfico de pizza
ax.pie(tamanhos, labels=rotulos, colors=cores, 
autopct='%1.1f%%')
# Adicionar título
ax.set_title('Distribuição das Frutas')
# Mostrar o gráfico plotado
plt.show()
