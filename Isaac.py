
perros = {'pequeños': ['chihuahua', 'pomerania', 'yorkshire'],
          'medianos': ['bulldog', 'beagle', 'cocker'],
          'grande': ['pastor alemán', 'labrador', 'dogo']}

def validar_perro(tamaño, raza):
    if tamaño in perros:
        if raza in perros[tamaño]:
            return True
        else:
            return False
    else:
        return False

print(validar_perro('medianos', 'beagle'))
print(validar_perro('grande', 'chihuahua'))
