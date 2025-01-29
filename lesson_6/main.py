age = input("Qual a sua idade?: ")

valid_age = str(age).isdigit() or str(age).lstrip("-").isdigit()

if valid_age:
    age = int(age)
    if age >= 18:
        print("Você é um adulto.")
    elif age < 0:
        print("Você nasceu no reverso...")
    else:
        print("Você é um jovem.")
else:
    print("Idade inválida.")
    exit()
