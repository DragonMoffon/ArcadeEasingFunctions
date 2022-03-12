import arcade

import easing_util


class TestWindow(arcade.Window):

    def __init__(self):
        super().__init__(900, 900, "Easing Tests")
        arcade.set_background_color(arcade.color.WHITE)

        self.func_index = 0
        self.animate = True
        self.time = 0
        self.speed = 0.5

        self.start = False
        self.tick_timer = 0

    def on_update(self, delta_time):
        if self.start:
            if self.animate:
                self.time = (self.time + delta_time * self.speed) % 1

            self.tick_timer += delta_time * self.speed
            if self.tick_timer >= self.animate + 1:
                self.func_index = (self.func_index + 1) % len(easing_util.functions)
                self.tick_timer = self.time = 0

    def on_draw(self):
        offset = 150
        self.clear()
        arcade.draw_line(offset, offset, offset, offset + 570, arcade.color.BLACK, 2)
        arcade.draw_line(offset, offset, offset + 570, offset, arcade.color.BLACK, 2)
        for n in range(1, 11):
            arcade.draw_line(offset, offset + 57 * n, offset + 570, offset + 57 * n, arcade.color.LIGHT_GRAY, 1)
            arcade.draw_line(offset, offset+57*n, offset + 10, offset+57*n, arcade.color.BLACK, 2)

            arcade.draw_line(offset+57*n, offset, offset + 57*n, offset + 570, arcade.color.LIGHT_GRAY, 1)
            arcade.draw_line(offset+57*n, offset, offset + 57*n, offset + 10, arcade.color.BLACK, 2)

        arcade.draw_text("0", offset, offset, arcade.color.BLACK, anchor_x="right", anchor_y="top")
        arcade.draw_text("1", offset, offset + 570, arcade.color.BLACK, anchor_x="right", anchor_y="top")
        arcade.draw_text("1", offset + 570, offset, arcade.color.BLACK, anchor_x="right", anchor_y="top")

        for n in range(0, 41):
            percent = n/40
            x = offset + percent*570
            y = offset + easing_util.functions[self.func_index](percent)*570

            arcade.draw_point(x, y, arcade.color.SEA_BLUE, 10)

        if self.animate and self.start:
            percent = self.time
            func = easing_util.functions[self.func_index](percent)
            arcade.draw_point(offset + percent*570, offset + func*570,
                              arcade.color.RADICAL_RED, 15)

            arcade.draw_point(offset/2, offset + func*570,
                              arcade.color.RADICAL_RED, 15)

            x = (900 - 570 - offset) / 2
            arcade.draw_rectangle_filled(900-x, 450, offset, 15, arcade.color.RADICAL_RED, 180*func)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.func_index = (self.func_index + 1) % len(easing_util.functions)
            self.time = 0
        elif symbol == arcade.key.A:
            self.func_index = (self.func_index - 1) % len(easing_util.functions)
            self.time = 0
        elif symbol == arcade.key.SPACE:
            self.start = True


def main():
    window = TestWindow()
    window.run()


if __name__ == '__main__':
    main()
