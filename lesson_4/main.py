name = input("Qual o seu nome? ")
age = input("Quantos anos você tem? ")

print(f"Olá, {name}, prazer em lhe conhecer!")
print(f"Você tem {age} anos de idade.")

if type(age) == str and str.isnumeric(age):
    age = int(age) + 1
    print(f"Ano que vem você terá {age} anos de idade.")
