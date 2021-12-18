let Tie_Control = 0
let AI_ROCK_PAPER_SCISSORS_DECISIONS_CONTROL = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showString("WELCOME!")
    basic.showString("[AI] Ready? Start!")
    basic.pause(500)
    basic.showString("[AI Player] I pick:")
    basic.showNumber(randint(1, 3))
    basic.showString("[Player (You)] I pick:")
    basic.showNumber(randint(1, 3))
    Tie_Control = randint(1, 3)
    AI_ROCK_PAPER_SCISSORS_DECISIONS_CONTROL += 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString("Game Logs (All):")
    basic.showNumber(AI_ROCK_PAPER_SCISSORS_DECISIONS_CONTROL)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("The last game was a:")
    basic.showString("[Debug] :")
    basic.showNumber(Tie_Control)
})
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    basic.showString("[Debug Console] :")
})
