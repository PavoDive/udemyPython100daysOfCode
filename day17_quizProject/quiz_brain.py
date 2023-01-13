class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}. (True/False)?: ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, r_answer):
        if u_answer.lower() == r_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer is: {r_answer}.")
        print(f"Your current score is {self.score}/{self.question_number + 1}\n")
