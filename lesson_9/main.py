# String indexing (como ler valores especificos em uma sequência)
# Para isso, usamos o operador [] e dentro deles especificamos os indíces de ínicio, fim, e step que queremos os dados
# [índice_inicial : índice_final : step]

credit_card = "1234-5678-9012-3456"

start_index = 0
end_index = 4
step = 0

print(f"Na string {credit_card}, o valor do índice {start_index} é {credit_card[start_index]}")
print(f"Na string {credit_card}, o valor do índice {-1} é {credit_card[-1]} (neste caso, obtém o primeira valor no final da sequência)")

start_index = 5; end_index = 9
print(f"Na string {credit_card}, o valor do índice {start_index} até {end_index} é {credit_card[start_index:end_index]}")
print(f"Na string {credit_card}, o valor do índice final {end_index} é {credit_card[:end_index]} (neste caso, ao se omitir o índice incial, ele é considerado 0)")
print(f"Na string {credit_card}, o valor do índice final {start_index} é {credit_card[start_index:]} (neste caso, ao se omitir o índice final, ele é considerado como último índice)")

step = 3
print(f"Na string {credit_card}, com um step de {step} é {credit_card[::step]} (neste caso, ao se informar somente o step, obtém somente os caracteres a cada {step} indices, do início ao fim.")
start_index = 3; step = 4
print(f"Na string {credit_card}, com um step de {step} a partir do índice {start_index} é {credit_card[start_index::step]} (neste caso, obtém somente os caracteres a cada {step} indices, do índice {start_index} ao fim.)")
step = -1
print(f"Na string {credit_card}, com um step de {step} é {credit_card[::step]} (neste caso, o {step} faz com que a string seja lida ao contrário a cada {abs(step)} caracteres)")
step = -2
print(f"Na string {credit_card}, com um step de {step} é {credit_card[::step]} (neste caso, o {step} faz com que a string seja lida ao contrário a cada {abs(step)} caracteres)")