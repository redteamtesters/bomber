# Importing the arcade library
import arcade

# Defining the constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
BOMB_SPEED = 5

# Defining the classes

class Bomb(arcade.Sprite):
    def update(self):
        self.center_y -= BOMB_SPEED
        if self.top < 0:
            self.kill()

class BomberManGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Bomber Man Game")
        self.bombs_list = arcade.SpriteList()
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        self.bombs_list.draw()

    def on_update(self, delta_time):
        self.bombs_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            bomb = Bomb(
                ":resources:images/items/bomb.png",
                center_x=self.width / 2,
                center_y=self.height,
            )
            self.bombs_list.append(bomb)

# Running the game
if __name__ == "__main__":
    game = BomberManGame()
    arcade.run()

