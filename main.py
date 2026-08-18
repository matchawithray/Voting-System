candidates = [
  {"name": "Xyra Shannel", "votes": 7},
  {"name": "Mitchie Mae", "votes": 18},
  {"name": "Raymart John", "votes": 27}
]

def view_results():
  if len(candidates) == 0:
    print("No candidates available.")
    return

  print("\n------VOTING RESULTS------")
  print("Candidates       Votes")
  print("-------------------------")

  for candidate in candidates:
    print(candidate['name'], '-', candidate['votes'], 'vote(s)')

view_results()