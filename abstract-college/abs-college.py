from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self._telefone = telefone

    def matricular(self):
        pass

    @abstractmethod
    def marcarPresenca(self):
        pass

class AlunoGraduacao(Pessoa):
    def __init__(self, id, nome, telefone, matricula, presencas):
        super().__init__(id, nome, telefone)
        self.__matricula = matricula
        self.__presencas = presencas

    def matricular(self):
        return f"Aluno {self.nome} matriculado com sucesso!"

    def acessarMatricula(self):
        return self.__matricula

    def modificarMatricula(self, matriculaNova):
        self.__matricula = matriculaNova
        return self.__matricula

    def marcarPresenca(self, qtPresencas):
        self.__presencas += qtPresencas
        return f"Presença marcada! Total de presenças: {self.__presencas}"

# exemplos de uso!

if __name__ == "__main__":
    # cria uma instância de AlunoGraduacao
    aluno = AlunoGraduacao(id=1, nome="João Silva", telefone="(11) 99999-8888", matricula="2024001", presencas=0)

    # exibe informações basicas do aluno
    print(f"Nome: {aluno.nome}")
    print(f"Telefone: {aluno._telefone}")
    print(f"Matrícula: {aluno.acessarMatricula()}")

    # modifica a matrícula do aluno
    nova_matricula = "2024002"
    print(f"Nova matrícula: {aluno.modificarMatricula(nova_matricula)}")

    # marca a  presença do aluno
    print(aluno.marcarPresenca(1))

    # matricula o aluno
    print(aluno.matricular())
