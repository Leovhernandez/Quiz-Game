import pgzrun

WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)

timer_box = Rect(0, 0, 240, 240)

answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)

timer_box.move_ip(990, 40)

answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 538)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0

time_left = 10

q1 = ["What year was Apple founded?",
      "1976", "1972", "1974", "1973", 1]

q2 = ["As of 2021, how many playoff points has Lebron scored in his career?",
      "7,589", "7,631", "7,604", "7,752", 2]

q3 = ["What game engine does Fortnite use to run?",
      "GameMaker", "Unity","Godot","Unreal",4]

q4 = ["What color is the Sun?",
      "Yellow", "White", "Red", "Orange", 2]

q5 = ["What was the average salary of a game developer in the US in 2021?",
      "$101,000", "$92,000", "$83,000", "$75,000", 1]

questions = [q1, q2, q3, q4, q5]
question = questions.pop(0)

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "light cyan")
    screen.draw.filled_rect(timer_box, "light cyan")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "sky blue")

    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))

    index = 1

    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index += 1

def game_over():
    global question, time_left
    message = "Game over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left

    score += 1
    if questions:
        question = questions.pop(0)
        time_left = 10
    else:
        print("End of questions")
        game_over()

def on_mouse_down(pos):
    global score
    index = 1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print("Clicked on answer " + str(index))
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                print("Wrong answer.")
                score -= 1
                correct_answer()
        index += 1

def update_time_left():
    global time_left

    if time_left:
        time_left -= 1
    else:
        game_over()

def on_key_up(key):
    global score
    if key == keys.SPACE:
        score -= 1
        correct_answer()


clock.schedule_interval(update_time_left, 1.0)


pgzrun.go()
