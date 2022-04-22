from guess import Guess
import turtle

screen = turtle.Screen()
screen.title('U.S. States Game')
image = ('blank_states_img.gif')
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

guess = Guess()

score = 0
while score < 50:

    answer_state = screen.textinput(title=f'{score}/50 States Correct', prompt="What's another state name").title()
    if answer_state == "Exit":
        break
    if guess.is_correct(answer_state) == True:
        score+=1
    
not_guessed = guess.states_not_guessed()
not_guessed.to_csv('missed_list.csv', index = False)

turtle.mainloop()