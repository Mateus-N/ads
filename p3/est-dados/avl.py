class Node:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1  # A altura de um nó folha é 1

class AVLTree:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if not self.raiz:
            self.raiz = Node(chave)
        else:
            self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, node, chave):
        if not node:
            return Node(chave)
        
        if chave < node.chave:
            node.esquerda = self._inserir(node.esquerda, chave)
        else:
            node.direita = self._inserir(node.direita, chave)
        
        node.altura = 1 + max(self._get_altura(node.esquerda), self._get_altura(node.direita))

        balance = self._get_balance(node)

        # Rotações para manter a propriedade AVL
        if balance > 1:
            if chave < node.esquerda.chave:
                return self._rotacao_direita(node)
            else:
                node.esquerda = self._rotacao_esquerda(node.esquerda)
                return self._rotacao_direita(node)
        if balance < -1:
            if chave > node.direita.chave:
                return self._rotacao_esquerda(node)
            else:
                node.direita = self._rotacao_direita(node.direita)
                return self._rotacao_esquerda(node)

        return node

    def _get_altura(self, node):
        if not node:
            return 0
        return node.altura

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_altura(node.esquerda) - self._get_altura(node.direita)

    def _rotacao_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def _rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))
        x.altura = 1 + max(self._get_altura(x.esquerda), self._get_altura(x.direita))

        return x

    def search(self, chave):
        return self._search(self.raiz, chave)

    def _search(self, node, chave):
        if not node:
            return None
        if chave == node.chave:
            return node
        elif chave < node.chave:
            return self._search(node.esquerda, chave)
        else:
            return self._search(node.direita, chave)

    def depth_first_search(self):
        result = []
        self._dfs(self.raiz, result)
        return result

    def _dfs(self, node, result):
        if node:
            result.append(node.chave)
            self._dfs(node.esquerda, result)
            self._dfs(node.direita, result)

    def busca_em_profundidade(self, chave):
        return self._busca_em_profundidade(self.raiz, chave)
    
    def _busca_em_profundidade(self, node, chave):
        if not node:
            return
        if node.chave == chave:
            return node.chave
        result = self._busca_em_profundidade(node.esquerda, chave)
        if not result:
            result = self._busca_em_profundidade(node.direita, chave)
        return result
    

# Exemplo de uso:
tree = AVLTree()
chaves = [30, 20, 40, 10, 25, 35, 50, 55, 99]

for chave in chaves:
    tree.inserir(chave)

print("Árvore AVL:")
print(tree.depth_first_search())  # Saída esperada: [30, 20, 10, 25, 40, 35, 50]

search_chave = 255
result = tree.busca_em_profundidade(search_chave)
if result:
    print(f"\nA chave {search_chave} foi encontrada na árvore.")
else:
    print(f"\nA chave {search_chave} não foi encontrada na árvore.")
