Candidate_name = input ("Choose candidate: ")
print("1.) LAZATIN, CARMELO II BAUTISTA")
print("2.) GONZALES, AURELIO JR. DUEÑAS")

choice = input("Enter Choice: ")

while Candidate_name not in ["1", "2"]:
    print("Invalid choice. Please choose again")
    Candidate_name = input("Choose your candidate: \n1. Lazatin\n2. Gonzales")

if Candidate_name == "1":
    Candidate_name = "Lazatin"

elif Candidate_name == "2":
    Candidate_name = "Gonzales"

candidate = Candidate_name(Candidate_name, Candidate_name)