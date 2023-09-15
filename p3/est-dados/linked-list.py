class Node:
    def __init__(self, content):
        self.content = content
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserirNoInicio(self, content):
        newNode = Node(content)
        if not self.head:
            self.head = newNode
            self.tail = newNode
            return
        newNode.nextNode = self.head
        self.head = newNode

    def inserirNoFinal(self, content):
        if not self.head:
            self.inserirNoInicio(content)
            return
        newNode = Node(content)
        self.tail.nextNode = newNode
        self.tail = newNode

    def imprimirLista(self):
        if not self.head:
            print('Lista vazia')
            return
        currentNode = self.head
        while currentNode:
            print(currentNode.content, end=' -> ')
            currentNode = currentNode.nextNode

    def inserirNoMeio(self, content, posicao):
        if (not self.head) or posicao == 1:
            self.inserirNoInicio(content)
            return
        
        currentNode = self.head
        contador = 2
        while contador < posicao and currentNode.nextNode:
            currentNode = currentNode.nextNode
            contador += 1
            
        if currentNode.nextNode:
            newNode = Node(content)
            newNode.nextNode = currentNode.nextNode
            currentNode.nextNode = newNode
            return
        
        self.inserirNoFinal(content)


linkedList = LinkedList()

while True:
    content = input('\ndigite o conteúdo: ')
    opcao = int(input('Deseja inserir no inicio(1) ou no final(2) ou no meio(3)? '))
    if opcao == 1:
        linkedList.inserirNoInicio(content)
    elif opcao == 2:
        linkedList.inserirNoFinal(content)
    elif opcao == 3:
        posicao = int(input('Qual a posição? '))
        linkedList.inserirNoMeio(content, posicao)
    linkedList.imprimirLista()
