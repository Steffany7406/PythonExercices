import time #Importando a função tempo

print("Contagem") 
for i in range(5):
    print(5 - i)
    #print(5 -i end='\r') #Para não imprimir a linha inteira
    time.sleep(1) #pausa de um segundo
    
print("Fim")

# O \r imprime os valores em cima da mesma linha. O end='\r' faz com que o valor seja impresso na mesma linha. 
# O time.sleep(1) faz com que a contagem seja feita de forma lenta. Ou seja, ele espera um segundo antes de imprimir o próximo valor.