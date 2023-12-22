questions = [
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 2],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 1],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 2],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
    ["What is your Country name?", "Nepal", "China", "Indian", "USA", 3],
]

levels = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 1000000]
money = 0
for i in range(0, len(questions)):
  print("\n\n", questions[i][0])
  question = questions[i]
  print(
      f"                                                Question for rupees  {levels[i]}"
  )
  print(f"a. {question[1]}              b. {question[2]}")
  print(f"c. {question[3]}              d. {question[4]}")
  reply = int(input("Enter your option between (1-4): "))
  if reply == question[5]:
    print("Correct Answer and your Cash priz is ", levels[i])
    if (i == 4):
      money = 5000
    elif (i == 8):
      money = 10000

  else:
    print("Wrong Answeer")
    break

print(f"Your take home money is {money}")
