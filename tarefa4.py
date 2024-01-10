#Criar um programa para clocar tres numeros em ordem crescente e identificar se há
num1=int(input("Digite o primeiro número: "))

num2=int(input("Digite o segundo número: "))

num3=int(input("Digite o terceiro número: "))

lista_crescente = [num1,num2,num3]
if (num1==num2==num3):
    print("Nao é permitido numeros repetidos! Digite um numero diferente: ")
else :
    print(num1,num2,num3)
    

lista_crescente.sort()

print(lista_crescente)
