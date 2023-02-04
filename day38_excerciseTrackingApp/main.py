from nutrition import Exercise, Nutrients
from sheety import Sheety

# ----------------- set the objects -----------------

exercise = Exercise()
nutrients = Nutrients()
sheety = Sheety()

# ----------------- What is user recording? -----------------

recording_type = input("What do you want to register? food / exercise: ").lower()

# ----------------- Workhorse -----------------
if recording_type == "exercise":
    exercise_input = input("Please input what exercise you did:\n")
    exercises = exercise.query_exercise(exercise_input)
    sheety.post_exercise(exercises)
elif recording_type == "food":
    food_input = input("What did you eat?:\n")
    foods = nutrients.query_food(food_input)
    sheety.post_food(foods)
else:
    print("Sorry, I don't recognize that input")

