from faker import Faker

fake = Faker()

def gerador_nomes_fake(quantidade_nomes: int) -> list:
    nomes = set()
    while len(nomes) < quantidade_nomes:
        nomes.add(fake.name())
    return nomes