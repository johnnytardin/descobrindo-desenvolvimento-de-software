import random

min, max = 1, 6

sortear = "sim"

while sortear in ["sim", "s"]:
    print(f"Rolando os dados...")

    dado1 = random.randint(min, max)
    dado2 = random.randint(min, max)

    print(f"Os números sorteados foram: {dado1} e {dado2}")

    sortear = input("Sortear novamente?")

    print("-"*60)
    