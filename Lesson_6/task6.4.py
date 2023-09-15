import guessing_module

attempt_number = guessing_module.guess_riddle("Что может в одно и то же время стоять и ходить?", ["часы"], 3)
if attempt_number:
    print(f"Отгадано с попытки {attempt_number}!")
else:
    print("Загадка не была отгадана.")
