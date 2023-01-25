from datetime import * #bibliotecas usadas

dataEHoraAtuais = datetime.now()#pegar a hora exata de agora junto com a data
diferenca = timedelta(hours=-3) #ajustando fusio horario da diferenca de 3 horas
fuso_horario = timezone(diferenca)
dataBrasil = dataEHoraAtuais.astimezone(fuso_horario) #ajustando o fusio horario com a hora exata
dataEHoraEmTexto = dataBrasil.strftime("%d/%m/%Y %H:%M") #ajustando a data e hora. A data para ficar como a tradicional e nao Ano/Mes/Dias
horario = [] #Fiz uma lista para ajudar a colocar as adicionais nas Entradas e Saidas


print(input("Empresario: "))
print(f"Data/Hora: {dataBrasil}")
print("---------------------------")

while True:

    print('''
        1- Bater Ponto Entrada
        2- Bater Ponto Saida 
        3- Bater Ponto Entrada Tarde
        4- Bater Ponto Saida Noite

        0- Encerrar
        ''')#Fiz um Menu de acesso para apertar qual entrada ira entrar ou saida.

    escolha = int(input('Qual a funcao a ser executada?: '))#botei a variavel escolha dentro do loop para que nao rode so uma vez e fique sem parar

    if  escolha == 1: 
        horario.append(datetime.now())#Ja que a variavel horario estava adicionada como vazia, fui adicionando a data e hora no codigo
        print(f"Entrada: {horario[0]}")
    
    elif escolha == 2:
        horario.append(datetime.now())
        print(f"Saida: {horario[1]}")

    elif  escolha == 3: 
        horario.append(datetime.now())
        print(f"Entrada 2: {horario[2]}")
    
    elif escolha == 4:
        horario.append(datetime.now())
        print(f"Saida 2: {horario[3]}")

    elif escolha == 0:
        break


print(f"A Hora Total De Trabalho Diurno Foi De: {horario[1] - horario[0]}") #Aqui ele recebe o tempo trabalhado pela manha
print(f"A Hora Total De Trabalho Vespertino Foi De: {horario[3] - horario[2]}")#Aqui ele recebe o tempo trabalhado pela tarde