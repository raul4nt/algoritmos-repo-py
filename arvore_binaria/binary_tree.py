class PatientNode:
    def __init__(self, name, age, registration):
        self.name = name  # Nome do paciente
        self.age = age  # Idade do paciente (chave de ordenação na árvore)
        self.registration = registration  # Número de registro médico do paciente
        self.left = None  # Referência ao filho à esquerda na árvore
        self.right = None  # Referência ao filho à direita na árvore

class PatientTree:
    def __init__(self):
        self.root = None  # Inicializa a árvore sem raiz

    def insertPatient(self, name, age, registration):
        """Insere um novo paciente na árvore."""
        new_node = PatientNode(name, age, registration)
        if self.root is None:
            self.root = new_node  # Se a árvore está vazia, o novo nó se torna a raiz
        else:
            current_node = self.root
            while True:
                if age <= current_node.age:
                    if current_node.left is None:
                        current_node.left = new_node  # Insere à esquerda se não houver filho à esquerda
                        break
                    else:
                        current_node = current_node.left  # Move para o filho à esquerda
                else:
                    if current_node.right is None:
                        current_node.right = new_node  # Insere à direita se não houver filho à direita
                        break
                    else:
                        current_node = current_node.right  # Move para o filho à direita

    def removePatient(self, age):
        """Remove um paciente com a idade especificada."""
        current_node = self.root
        parent_node = None
        while current_node is not None:
            if age < current_node.age:
                parent_node = current_node
                current_node = current_node.left  # Move para o filho à esquerda
            elif age > current_node.age:
                parent_node = current_node
                current_node = current_node.right  # Move para o filho à direita
            else:
                # Casos de remoção baseados nos filhos do nó a ser removido
                if current_node.left is None and current_node.right is None:
                    # Caso 1: Nó sem filhos
                    if parent_node is None:
                        self.root = None  # O nó é a raiz
                    elif parent_node.left == current_node:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                elif current_node.left is None:
                    # Caso 2: Nó com apenas um filho à direita
                    if parent_node is None:
                        self.root = current_node.right  # O nó é a raiz
                    elif parent_node.left == current_node:
                        parent_node.left = current_node.right
                    else:
                        parent_node.right = current_node.right
                elif current_node.right is None:
                    # Caso 3: Nó com apenas um filho à esquerda
                    if parent_node is None:
                        self.root = current_node.left  # O nó é a raiz
                    elif parent_node.left == current_node:
                        parent_node.left = current_node.left
                    else:
                        parent_node.right = current_node.left
                else:
                    # Caso 4: Nó com dois filhos
                    temp = current_node.right
                    while temp.left is not None:
                        temp = temp.left  # Encontra o nó mais à esquerda na subárvore à direita
                    # Substitui os dados do nó atual pelos do nó mais à esquerda encontrado
                    current_node.name = temp.name
                    current_node.age = temp.age
                    current_node.registration = temp.registration
                    # Remove o nó mais à esquerda da subárvore à direita
                    current_node.right = self.removeMin(current_node.right, temp.age)
                break

    def removeMin(self, node, age):
        """Remove o nó com a menor idade na subárvore."""
        if node is None:
            return None

        if node.age == age:
            if node.left is None:
                return node.right
            else:
                node.left = self.removeMin(node.left, age)
                return node

        node.right = self.removeMin(node.right, age)
        return node

    def preOrder(self):
        """Executa a travessia em pré-ordem na árvore."""
        if self.root is None:
            return []

        result = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.name)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result

    def printPreOrder(self):
        """Imprime a travessia em pré-ordem da árvore."""
        elements = self.preOrder()
        for element in elements:
            print(element, end=' ')
        print()


# Exemplo de uso da árvore de pacientes
patient_tree = PatientTree()
patient_tree.insertPatient("Carlos", 30, "12345")
patient_tree.insertPatient("Ana", 25, "67890")
patient_tree.insertPatient("Pedro", 35, "54321")
patient_tree.insertPatient("Mariana", 40, "98765")


patient_tree.printPreOrder()

patient_tree.insertPatient("Beatriz", 32, "97531")
patient_tree.printPreOrder()


patient_tree.removePatient(25)
patient_tree.printPreOrder()
