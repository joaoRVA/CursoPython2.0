# Métodos úteis em dicionários

pessoa = {
    'nome': 'Joca',
    'sobrenome': 'Martins',
}

# print(pessoa.__len__()) retorna o numero de chaves
# print(len(pessoa)) mais usado

print(pessoa.keys()) # retorna as chaves
print(list(pessoa.keys())) # conversão

print(tuple(pessoa.values())) # retorna valores


print(list(pessoa.items())) # .items() retorna as chaves e os valores

for chaves, valor in pessoa.items():
    print(chaves, valor)

pessoa.setdefault('idade', 0) # estabelece um valor padrão a uma chave específica

print(pessoa['idade'])