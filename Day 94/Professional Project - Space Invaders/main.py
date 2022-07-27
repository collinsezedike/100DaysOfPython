import time
from turtle import Screen

from blockers import Blockers
from invaders import Invaders
from player import Player
from writer import Writer

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=600)
screen.title("Turtle Invaders")
screen.tracer(0)

player = Player((0, -250))

screen.listen()
screen.onkeypress(key="Right", fun=player.move_right)
screen.onkeypress(key="Left", fun=player.move_left)
screen.onkeyrelease(key="space", fun=player.shoot)
# it is onkeyrelease not onkeypress so that 
# holding on the spacebar does not increase the bullet speed

blockers = Blockers((-220, 50))

invaders = Invaders()
invaders.create_army((-140, 260))

lives_writer = Writer((-200, -280))
levels_writer = Writer((200, -280))

lives = 3
level = 0

while lives:
    screen.update()
    time.sleep(0.01)

    player.bullet.fire()  # so that the fired bullet keeps moving

    if invaders.soldiers:

        if invaders.soldiers[0].ycor() <= player.ycor():  # if invaders have overtaken player's territory
            time.sleep(2)
            player.bullet.goto(1000, 1000)
            lives -= 1
            for soldier in invaders.soldiers:
                soldier.goto(1000, -1000)
                soldier.bullet.goto(-1000, -1000)
            invaders.create_army((-140, 260))
            blockers.refresh((-220, 50))

        invaders.shoot(-500)
        invaders.move()

        for block in blockers.blocks:
            if player.bullet.distance(block) <= 20:  # if player shoots at block
                player.bullet.goto(1000, 1000)

        for soldier in invaders.soldiers:
            if soldier.ycor() <= -250:
                soldier.hideturtle()

            if player.bullet.distance(soldier.bullet) <= 20:  # if player bullet collides with soldier bullet
                player.bullet.goto(1000, 1000)
                soldier.bullet.goto(-1000, -1000)

            if soldier.distance(player) <= 10:  # if soldier touches player
                time.sleep(2)
                player.bullet.goto(1000, 1000)
                lives -= 1
                for invader in invaders.soldiers:  # using invader instead to avoid ambiguity
                    invader.goto(1000, -1000)
                    invader.bullet.goto(-1000, -1000)
                invaders.create_army((-140, 260))
                blockers.refresh((-220, 50))

            if player.bullet.distance(soldier) <= 20:  # if player shoots at soldier
                player.bullet.goto(1000, 1000)
                soldier.goto(1000, -1000)
                soldier.bullet.goto(-1000, -1000)
                soldier.clear()
                invaders.soldiers.remove(soldier)

            if soldier.bullet.distance(player) <= 10:  # if soldier shoots at player
                time.sleep(2)
                lives -= 1
                player.bullet.goto(1000, 1000)
                soldier.bullet.goto(-1000, -1000)

            for block in blockers.blocks:
                if soldier.bullet.distance(block) <= 20:  # if soldier shoots at block
                    soldier.bullet.goto(-1000, -1000)
                    block.goto(1000, -1000)
                    block.clear()
                if soldier.distance(block) <= 20:  # if soldier touches block
                    block.goto(1000, -1000)
                    block.clear()

    else:  # if player has shot all the invaders
        invaders.level_up((-140, 260))
        blockers.refresh((-220, 50))
        level += 1
        lives += 1

    lives_writer.write_lives(lives)
    levels_writer.write_level(level)

time.sleep(2)
Writer((0, -10)).write_gameover()
screen.exitonclick()
