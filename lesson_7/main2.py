# Expressões condicionais

num = input("Digite um número -> ")
num = (float(num) if str(num).isdigit() or str(num).lstrip("-").isdigit() else print("Número invalido") or exit())
is_odd = True if num % 2 == 0 else False

print(f"{num} é par? -> {"Sim" if is_odd else "Não"}")