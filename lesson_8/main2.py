# Exercício -> validando o input de um usuário

username = input("Digite um nome para o seu usuário: ")

if username == "":
    print("O nome do usuário não pode ser vazio!")
elif username.__len__() > 12:
    print("O nome do usuário não pode ter mais de 12 caracteres!")
elif not username.count(" ") == 0:
    print("O nome do usuário não pode possuir espaços!")
elif username.isalnum():
    print("O nome do usuário não pode possuir digitos!")
else:
    print(f"USUÁRIO PODE SER CADASTRADO COM SUCESSO! BEM VINDO {username}")