scores = []
for i in range(3):
    player = int(input("Enter your score: "))
    scores.append(player)

average = sum(scores) / len(scores)
print(f"Average: {average}")