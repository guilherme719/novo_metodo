print("Bem Vindo ao Sistema de Cadastro de Notas")


notas = []

for i in range(1, 5):
    nota = float(input(f" nota {i}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"A média das notas é: {media:.2f}")

if media >= 6:
    print("***Aprovado Parabens!!!!!*****")
else:
    print("____Reprovado seu Burro____ .!.")