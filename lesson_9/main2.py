email = input("Digite o seu melhor email: ")

at_index = email.index("@")
username = email[:at_index]
domain = email[at_index + 1:]

print(f"Seu usuário é {username} e seu dominio é {domain}")