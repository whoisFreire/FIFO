tam = int(input('Digite o tamanho da fila: '))
option = 0
processos = []

def insert(processos):
    if tam <= len(processos):
        print('Fila Cheia')
    else:
        task_name = input('Nome do processo: ')
        time = int(input('Tempo de processador: '))
        processo = {
            'task_name': task_name,
            'time': time
        }
        processos.append(processo)
        print(len(processos))


def show():

    if len(processos) == 0:
        print('\nFila vazia')
    else:
        for processo in processos:
            print('\nNome do Processo: {}'.format(processo['task_name']))
            print('\nTempo de Processamento: {}'.format(processo['time']))
            print("\n-----------------------------")
    input('')


def fifo():
    wait = 0
    response = 0
    tme = 0
    tmr = 0

    for processo in processos:
        processo['wait_time'] = wait 
        processo['response_time'] = response + processo['time']
        tme += processo['wait_time']
        tmr += processo['response_time']
        wait += processo['time']
        response += processo['time']
    
    print("\n-----------------------------")
    
    for processo in processos:
        print('Processo: {}'.format(processo['task_name']))
        print('Tempo de espera: {}'.format(processo['wait_time']))
        print('Tempo de resposta: {}'.format(processo['response_time']))
        print("\n-----------------------------")
        input('')


while option <= 3:
    print("\n\n1 - Inserir")
    print("2 - Mostrar")
    print("3 - FIFO")
    print("4 - Sair")
    option = int(input("Escolha sua opcao: "))

    if option == 1:
        insert(processos)
        continue
    elif option ==2:
        show()
        continue
    elif option == 3:
        fifo()
        continue
    else:
        break