def on_button_pressed_a():
    basic.show_leds("""
        . # # # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global myImage
    basic.clear_screen()
    myImage = images.create_big_image("""
        # . . . . . # . . . . . . . . . . . . .
        . # # . # # . # . . # . . # . . . . . .
        . # # . # # . # # . # # . # # . . . . .
        . . . # . . . # # . # # . # # . . . . .
        . . # # # . . # # . # # . # # . . . . .
        """)
    myImage.scroll_image(0, 200)
input.on_button_pressed(Button.B, on_button_pressed_b)

myImage: Image = None