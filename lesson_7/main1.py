# Expressões condicionais

num = input("Digite um número para checar se ele é positivo ou negativo -> ")
num = (float(num) if str(num).isdigit() or str(num).lstrip("-").isdigit() else print("Número invalido") or exit())
is_positive = True if num > 0 else 0

print(f"{num} é positivo? -> {"Sim" if is_positive else "Não"}")