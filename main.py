

import tcod as t
import emoji

screen_width = 39
screen_height = 12
damfortrap = 0
health = 100 - damfortrap
key = t.Key()
mouse = t.Mouse()
enemy = "X"
exit = "█"


class Player:
    x = 1
    y = 10
    def move(self,x,y):
        if not obstacle(x,y):
            self.x=x
            self.y =y

map = [
    "#######################################",
    "#            |     |_______|          #",
    f"#            |___  |         |-----|  {exit}",
    "#  ________        | ________|_____|__#",
    "# |____    |_______|                  #",
    "#      |  |        |_______  _________#",
    "#      |  | |---| |       | |         #",
    "#      |  | |___| | |---| | |_________#",
    "# |--| |  | |     | |     |           #",
    "# |  | |__| | ----| | ____|__________ #",
    "# |  |      |       |                 #",
    "########################################"
]
def obstacle(x,y):

    if y > len(map) or y <0:
        return True
    if x > len(map[0]) or x < 0:
        return True
    el = map[y][x]
    if el == " " or el == "\t" or el == ".":
        return False
    if el == exit:
        damfortrap.append(100)
        return False
    if el == enemy:
        health -= 25
        return False
    else:
        return True

def map_draw():
    for y in range(len(map)):
        for x in range(len(map[0])):
            cchar(x,y,map[y][x])

def game():
    player = Player()


    t.console_init_root(screen_width, screen_height, "LABIRINT")
    while not t.console_is_window_closed():
        t.console_set_default_foreground(0, t.white)
        t.sys_check_for_event(t.EVENT_KEY_PRESS,key,mouse)
        map_draw()

        cchar(player.x, player.y, "▲")

        t.console_flush()
        cclear()

        if health == 0:
            return
        if key.vk == t.KEY_ESCAPE:
            return
        if key.vk == t.KEY_UP:
            player.move(player.x, player.y-1)

        elif key.vk == t.KEY_DOWN:
            player.move(player.x, player.y+1)

        if key.vk == t.KEY_LEFT:
            player.move(player.x-1, player.y)

        elif key.vk == t.KEY_RIGHT:
            player.move(player.x+1, player.y)

def cchar(x, y, c):
    t.console_put_char(0, x, y, ord(c))
def cprint(x, y, txt):
    t.console_print(0, x, y, txt)
def cclear():
    t.console_clear(0)

if __name__ == "__main__":
    game()