import time
from turtle import Screen
from player import Player, STARTING_POSITION, FINISH_LINE_Y
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)


def level_up():
    player.goto(STARTING_POSITION)
    car_manager.level_up()
    score.update_level()


player = Player()
car_manager = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkeypress(key="Up", fun=player.move)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    score.display_level()
    car_manager.make_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_on = False

    # Detect if player has reached the top edge of the screen
    if player.ycor() >= FINISH_LINE_Y:
        level_up()

    print(car_manager.upper_range)
screen.exitonclick()
