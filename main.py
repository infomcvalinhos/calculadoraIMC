#IMC = 

print("Academia MC Valinhos")
print("............................")
print("Seja bem-vindo(a)")

nome = input("me diga por favor, o seu nome: ")
idade = int(input("agora precisoque você me informa a sua idade :"))
altura = float(input("informe a sua altura"))
nacimento = 2024 - idade 
peso = float(input("informe o seu peso: "))
IMC = peso / (altura * altura)

print("olá. senhor ", nome")
print("sua idade é: ", idade " anos")
print("voce naceu em: ", nacimento")
print("sua altura é de:", altura, "metros.")
print("seu peso é: ", peso")
print("seu IMC é: {: 2f} kg/m²".format(IMC)")