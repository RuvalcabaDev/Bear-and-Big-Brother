# Challenge 1 developed in python


def validate_weight_rules(limak_weight, bob_weight):
    if limak_weight <= bob_weight and limak_weight != 0:
        return overcome_weight(limak_weight, bob_weight)
    else:
        print("No se cumplen las reglas de peso de Limak y Bob")


def overcome_weight(limak_weight, bob_weight):
    year = 0
    while bob_weight >= limak_weight:
        limak_weight = limak_weight * 3
        bob_weight = bob_weight * 2
        year = year + 1
        print("Año: ", year)
        print("El peso de Limak es: ", limak_weight)
        print("El peso de Bob es: ", bob_weight)
    print("Limak ahora es más grande")
    print("Peso Limak: ", limak_weight)
    print("Peso Bob: ", bob_weight)
    return print("Resultado: ", year)


try:
    limak_weight = int(input("Peso Limak: "))
    bob_weight = int(input("Peso Bob: "))
    validate_weight_rules(limak_weight, bob_weight)
except Exception as e:
    print("Error de argumentos: ", e)