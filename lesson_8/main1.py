# string methods

fullname = input("Qual o seu nome completo? ")
fullname_length = len(fullname)
print(f"O nome {fullname} possuí {fullname_length} caracteres")

index_R_position = fullname.find("R")
index_A_position = fullname.find("A")
last_index_o_position = fullname.rfind("o")
print(f"""No nome {fullname}...
A primeira posição da letra R é {index_R_position}
A primeira posição da letra A é {index_A_position}
A ultima posição da letra o é {last_index_o_position}
""")

other_name = "patricia tamires de sousa"
print(f"O nome {other_name} pode ser ajustado para iniciar com letras maíusculas com o método capitalize: {other_name.capitalize()}")
print(f"É possível também substituir caracteres na string, como os espaços no nome {other_name}: {other_name.replace(" ", "[ERA UM ESPAÇO AQUI]")}")

capitilized_string_list = list(map((lambda name_part: name_part.capitalize()), other_name.split(" ")))
capitilized_string = " ".join(capitilized_string_list)
print(f"O nome {other_name} completamente ajustado fica: {capitilized_string}")

