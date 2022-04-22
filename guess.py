import pandas as pd
import turtle
df = pd.read_csv('50_states.csv')
ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")
class Guess:

    def __init__(self):
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        self.right_answers = []
        self.missed = []
        self.all_states = df.state.to_list()

    def draw(self):
        self.turtle.penup()
        self.turtle.goto(int(self.answer.x), int(self.answer.y))
        self.turtle.hideturtle()
        self.turtle.write(self.guess, align=ALIGNMENT, font=FONT)


    def is_correct(self, answer_state):
        self.guess = answer_state
        right = True
        if (df.state == self.guess).any() == True and self.guess not in self.right_answers:
            self.answer = df.loc[df['state'] == self.guess,:]
            self.right_answers.append(self.guess)
            self.draw()
            return right
        else:
            right = False
            return right
    
    def states_not_guessed(self):
        self.missed = [state for state in self.all_states if state not in self.right_answers]
        missed_states = pd.DataFrame(self.missed, columns=['States Missed'])
        return missed_states

            

    