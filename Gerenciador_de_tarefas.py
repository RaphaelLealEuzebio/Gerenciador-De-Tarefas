#Gerenciador de Tarefas
tarefas = []
# adicionando tarefas
def add_tarefa (tarefa): 
    tarefas.append(tarefa)
    print('Tarefa Adicionada !')
    return tarefa
def lista_tarefas():
    if len(tarefas) >= 1:
        print('Lista de Terefas !!')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa}')
    else:
        print('Nenhuma tarefa na lista !!')
#marcando como concluida
def tarefa_completa (tarefa_index):
    if 1 <= tarefa_index <= len(tarefas):
        tarefas.pop (tarefa_index - 1)
        print('Tarefa concluida e removida da lista')
    else:
        print('Indice de tarefa invalido')
#menu
def main(): 
    while True:
        print('Menu Lista de Tarefas')
        print('[1] Adcionar uma Tarefa')
        print('[2] Lista de Tarefas')
        print('[3] Marcar como concluida')
        print('[4] Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            tarefa = input('Digite uma nova tarefa: ')
            add_tarefa(tarefa)
        elif escolha == '2':
            lista_tarefas()
        elif escolha == '3':
            tarefa_index = int(input('Digite o numero da tarefa concluida: '))
            tarefa_completa (tarefa_index)
        elif escolha == '4':
            print('Saindo .....')
            break
        else:
            print('Opção invalida !!!')

main()