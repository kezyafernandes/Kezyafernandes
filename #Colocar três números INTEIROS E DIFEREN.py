 #Colocar três números INTEIROS E DIFERENTES em ordem decrescente
 a=input("Digite o primeiro número: ")
 b=input("Digite o segundo número: ")
 c=input("Digite o terceiro número: ")
 if(a>b)&(b>c):
     print(a, b, c)
 elif(a>c)&(c>b):
     print(a, c, b)
 elif(b>a)&(a>c):
     print(b, a, c)
 elif(b>c)&(c>a):
     print(b, c, a)
 else:
     print(c, b, a)