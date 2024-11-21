class PatientNode:
    def __init__(self, name, age, registration):
        self.name = name  
        self.age = age  # chave de ordenacao na arvore avl
        self.registration = registration  
        self.left = None  # referencia ao filho a esquerda na arvore
        self.right = None  # referencia ao filho a direita na arvore
        self.height = 1  # inicializa a altura do no como 1


class AVLTree:
    def __init__(self):
        self.root = None  # inicializa a arvore sem raiz

    def insert(self, name, age, registration):
        self.root = self._insert(self.root, name, age, registration)

    def _insert(self, node, name, age, registration):
        # funcao auxiliar para insercao recursiva na arvore AVL
        # caso base: se o no atual for None, cria um novo no com os dados fornecidos
        if not node:
            return PatientNode(name, age, registration)

        # insere a esquerda se a idade for menor ou igual a idade do no atual
        if age < node.age:
            node.left = self._insert(node.left, name, age, registration)
        else:
            # insere a direita se a idade for maior que a idade do no atual
            node.right = self._insert(node.right, name, age, registration)

        # atualiza a altura do no atual
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # calcula o fator de balanceamento do no atual
        balance = self._get_balance(node)

        # casos de rotacao para balanceamento da arvore AVL
        if balance > 1 and age < node.left.age:
            return self._rotate_right(node)

        if balance < -1 and age > node.right.age:
            return self._rotate_left(node)

        if balance > 1 and age > node.left.age:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and age < node.right.age:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, z):
        # realiza uma rotacao para a esquerda no no dado
        y = z.right
        T2 = y.left

        # realiza a rotacao
        y.left = z
        z.right = T2

        # atualiza as alturas dos nos
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        # realiza uma rotacao para a direita no no dado
        y = z.left
        T3 = y.right

        # realiza a rotacao
        y.right = z
        z.left = T3

        # atualiza as alturas dos nos
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, node):
        # retorna a altura do no dado
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        # retorna o fator de balanceamento do no dado
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def print_in_order(self):
        # visita primeiro o filho a esquerda, depois o no atual e por ultimo o filho a direita
        self._print_in_order(self.root)
        print()

    def _print_in_order(self, node):
        # funcao auxiliar pra printar em ordem de maneira mais recursiva
        if node:
            self._print_in_order(node.left)
            print(f"Name: {node.name}, Age: {node.age}, Registration: {node.registration}")
            self._print_in_order(node.right)


# alguns exemplinhos de uso e testes

avl_tree = AVLTree()
avl_tree.insert("Carlos", 30, "12345")
avl_tree.insert("Ana", 25, "67890")
avl_tree.insert("Pedro", 35, "54321")
avl_tree.insert("Mariana", 40, "98765")

print("Arvore AVL apos insercoes:")
avl_tree.print_in_order()

avl_tree.insert("Beatriz", 32, "97531")
print("\nArvore AVL apos insercao de Beatriz:")
avl_tree.print_in_order()

avl_tree.insert("Luisa", 20, "13579")
print("\nArvore AVL apos insercao de Luisa:")
avl_tree.print_in_order()

avl_tree.insert("Joao", 38, "24680")
print("\nArvore AVL apos insercao de Joao:")
avl_tree.print_in_order()
