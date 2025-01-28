# strings
first_name = "Rodrigo"
middle_name = "Martins"
last_name = "Azevedo"

print(first_name)
print(f"{first_name} {last_name}, mas agora usando uma formatted string (string formatada)")
print(f"""
Meu nome é {first_name} {middle_name} {last_name}, 
Mas agora usando uma string em várias linhas
""")

# integers
age = 32
quantity = 0

print(f"Eu tenho {age} anos")
print(f"Eu tenho {quantity} filhos")

# floats
height = 1.80
weight = 91.2

print(f"Eu tenho {height} de altura")
print(f"Eu peso {weight} kg")

# boolean
is_student = True
is_studying_python = True
print(f"Eu sou estudante? {'sim' if is_student else 'não'}")

if is_studying_python:
    print("Eu estou estudando Python")
else:
    print("Eu não estou estudando Python")