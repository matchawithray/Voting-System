from add import candidates
from Votings import voters, cast_vote
from result import view_results


def main():
    while True:
        print("\n==============================")
        print("        VOTING SYSTEM")
        print("==============================")
        print("1. Cast Vote")
        print("2. View Results")
        print("3. Exit")
        print("==============================")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            cast_vote(voters, candidates)

        elif choice == "2":
            view_results(candidates)

        elif choice == "3":
            print("\nThank you for using the Voting System!")
            break

        else:
            print("\nInvalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
