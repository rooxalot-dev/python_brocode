name = "Rodrigo"
last_name = ""
age = 32
height = 1.78
is_student = True

name_var_type = type(name)
age_var_type = type(age)
height_var_type = type(height)
is_student_var_type = type(is_student)

print(f"""
    O tipo da variável 'name' é {name_var_type}, 
    Da variável 'age' é {age_var_type}
    Da variável 'height' é {height_var_type}
    Da variável 'is_student' é {is_student_var_type}
""")

converted_height = int(height)
print(f"O valor de 'height' convertido para inteiro é {converted_height} (já que perdeu seus decimais)")

converted_age = float(age)
print(f"O valor de 'age' convertido para float é {converted_age} (já que ganhou decimais)")

converted_string_height = str(height)
print(f"O valor de 'height' convertido para string é '{converted_string_height}' (virou um texto como podemos ver pelo seu type: {type(converted_string_height)})")

converted_name = bool(name)
converted_last_name = bool(last_name)
print(f"O valor de 'name' convertido para boolean é {converted_name} (já que é uma string e strings são consideradas True,)")
print(f"O valor de 'last_name' convertido para boolean é {converted_last_name} (já que é uma string vazia e strings assim são consideradas False)")