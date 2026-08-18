#Xyra i2
#python


candidates = [
    {"name": "Xyra Shannel", "votes": 7},
    {"name": "Mitchie Mae", "votes": 18},
    {"name": "Raymart John", "votes": 27}
]


def get_votes(candidate):
    return candidate["votes"]


def view_results():
    if not candidates:
        print("No candidates available.")
        return

    print("\n------- VOTING RESULTS -------")
    print("Candidates              Votes")
    print("--------------------------------")

    sorted_candidates = sorted(
        candidates,
        key=get_votes,
        reverse=True
    )

    for candidate in sorted_candidates:
        print(f"{candidate['name']:<20} {candidate['votes']} vote(s)")

    total = sum(candidate["votes"] for candidate in candidates)

    winner = sorted_candidates[0]

    print("--------------------------------")
    print(f"Total Votes: {total}")
    print(f"\nWinner: {winner['name']} with {winner['votes']} votes!")


view_results()