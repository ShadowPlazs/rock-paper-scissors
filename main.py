Tie_Control = 0
AI_ROCK_PAPER_SCISSORS_DECISIONS_CONTROL = 0

def on_button_pressed_a():
    global Tie_Control, AI_ROCK_PAPER_SCISSORS_DECISIONS_CONTROL
    basic.show_string("WELCOME!")
    basic.show_string("[AI] Ready? Start!")
    basic.pause(500)
    basic.show_string("[AI Player] I pick:")
    basic.show_number(randint(1, 3))
    basic.show_string("[Player (You)] I pick:")
    basic.show_number(randint(1, 3))
    Tie_Control = randint(1, 3)
    AI_ROCK_PAPER_SCISSORS_DECISIONS_CONTROL += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Game Logs (All):")
    basic.show_number(AI_ROCK_PAPER_SCISSORS_DECISIONS_CONTROL)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("The last game was a:")
    basic.show_string("[Debug] :")
    basic.show_number(Tie_Control)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_string("[Debug Console] :")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
