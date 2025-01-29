# Funções matemáticas nátivas do Python

x = 3.14
y = -4
z = 5

# arredonda o número
print(f"{x} arredondado é {round(x, 1)}")
print(f"É possível definir o número de casas decimais -> {x} arredondado é {round(x, 1)} (1 casa)")

# valor absoluto
print(f"O valor absoluto de {y} é {abs(y)}")

# potência
print(f"{z} elevado a 3 é {pow(z, 3)}")

# valor máximo
print(f"O maior valor entre {x}, {y} e {z} é {max(x, y, z)}")

# valor mínimo
print(f"O menor valor entre {x}, {y} e {z} é {min(x, y, z)}")