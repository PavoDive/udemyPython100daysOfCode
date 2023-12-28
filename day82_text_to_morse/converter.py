import pandas as pd
from unidecode import unidecode

data = pd.read_csv("data/morse.csv", sep = "|")
data = pd.concat([data, pd.DataFrame({"character": " ", "code": "    "}, index = [1])], ignore_index = True)

# an accessory function that mirrors R's menu:
def menu(choices, prompt):
    valid_choices = [str(i) for i in range(1, len(choices) + 1)]

    while True:
        print(prompt)
        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")

        user_input = input("Enter the number corresponding to your choice: ")

        if user_input in valid_choices:
            return choices[int(user_input) - 1]
        else:
            print("Invalid choice. Please enter a valid number.")

# This is the work horse
def converter(string):
    string = unidecode(string.replace('"', "*").replace("'", "*").lower())
    new_df = pd.DataFrame({"character": list(string), "id": range(len(string))})
    output_string = pd.merge(data, new_df, on = "character").sort_values("id")["code"].str.cat(sep = " ")
    return output_string

choices = ["Yes", "No"]
user_choice = "Yes"

while user_choice == "Yes":
    text_to_convert = input("Welcome to our text to morse converter. Please input your string:\n")
    text_to_output = converter(text_to_convert)
    print(f"Your converted text is:\n{text_to_output}\n")
    user_choice = menu(choices, prompt = "Do you want to convert another string?")
