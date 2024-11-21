import random
from gerador_nomes import *

class Paciente:
    def __init__(self, nome, idade, registro_medico):
        self.nome = nome
        self.idade = idade
        self.registro_medico = registro_medico
        self.proximo = None

class ListaPaciente:
    def __init__(self):
        self.primeiro = None

    def tamanho(self):
        qt = 0
        paciente = self.primeiro
        while paciente is not None:
            paciente = paciente.proximo
            qt += 1
        return qt

    def add_paciente(self, nome, idade, registro_medico):
        novo_paciente = Paciente(nome, idade, registro_medico)

        if self.primeiro is None:
            self.primeiro = novo_paciente
        else:
            paciente_atual = self.primeiro
            while paciente_atual.proximo is not None:
                paciente_atual = paciente_atual.proximo
            paciente_atual.proximo = novo_paciente

    def busca_paciente(self, registro_medico):
        paciente_atual = self.primeiro

        while paciente_atual is not None:
            if paciente_atual.registro_medico == registro_medico:
                return paciente_atual
            paciente_atual = paciente_atual.proximo

        return None

    def lista_pacientes(self):
        if self.primeiro is None:
            print("A lista de pacientes está vazia.")
        else:
            paciente_atual = self.primeiro
            while paciente_atual is not None:
                print(f"Nome: {paciente_atual.nome}, Idade: {paciente_atual.idade}, Prontuário: {paciente_atual.registro_medico}")
                paciente_atual = paciente_atual.proximo


def counting_sort(info):
    count_dict = {}
    for nome in info:
        count_dict[nome] = count_dict.get(nome, 0) + 1

    info_corrigida = []
    for nome in sorted(count_dict.keys()):
        info_corrigida.extend([nome] * count_dict[nome])

    return info_corrigida


def ordenar_counting(lista_pacientes):
    if lista_pacientes.primeiro is None:
        return

    nomes = []

    paciente_atual = lista_pacientes.primeiro
    while paciente_atual is not None:
        nomes.append(paciente_atual.nome)
        paciente_atual = paciente_atual.proximo

    nomes_ordenados = counting_sort(nomes)

    paciente_atual = lista_pacientes.primeiro
    for nome in nomes_ordenados:
        paciente_atual.nome = nome
        paciente_atual = paciente_atual.proximo

    return lista_pacientes


pacientes = ListaPaciente()

lista_nomes = list(gerador_nomes_fake(10))
lista_idades = [random.randint(1,100) for _ in range(10)]
numero_registro = 202400001

for i in range(10):
    pacientes.add_paciente(lista_nomes[i], lista_idades[i], numero_registro)
    numero_registro += 1

print("Pacientes desordenados:")
pacientes.lista_pacientes()
input()

ordenar_counting(pacientes)

print("Pacientes ordenados por nome:")
pacientes.lista_pacientes()
print("fim")
