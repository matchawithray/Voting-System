candidates = [
    "BAYLON, REYNEIL BAEZ",
    "CALUAG, VILMA BALLE",
    "MANALO, CHERRY DIZON",
    "HALILI, CHRISTIAN CASTRO"
]

votes = [0, 0, 0, 0]

for i, name in enumerate(candidates, 1):
    print(i, name)

choice = int(input("Choose the candidates you want to vote: "))
if 1 <= choice <= len(candidates):
    votes[choice - 1] += 1
    print("You voted for:", candidates[choice - 1])
else:
    print("Invalid choice.")



 