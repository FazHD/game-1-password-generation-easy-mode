def on_button_pressed_a():
    basic.show_number(randint(0, 9))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Alphabet
    Alphabet = randint(0, 25)
    if Alphabet == 0:
        basic.show_leds("""
            . # # . .
                        # . . # .
                        # # # # .
                        # . . # .
                        # . . # .
        """)
    elif Alphabet == 1:
        basic.show_leds("""
            # # # . .
                        # . . # .
                        # # # . .
                        # . . # .
                        # # # . .
        """)
    elif Alphabet == 2:
        basic.show_leds("""
            # # # # .
                        # . . . .
                        # . . . .
                        # . . . .
                        # # # # .
        """)
    elif Alphabet == 3:
        basic.show_leds("""
            # # # . .
                        # . . # .
                        # . . # .
                        # . . # .
                        # # # . .
        """)
    elif Alphabet == 4:
        basic.show_leds("""
            # # # # .
                        # . . . .
                        # # # . .
                        # . . . .
                        # # # # .
        """)
    elif Alphabet == 5:
        basic.show_leds("""
            # # # # .
                        # . . . .
                        # # # . .
                        # . . . .
                        # . . . .
        """)
    elif Alphabet == 6:
        basic.show_leds("""
            . # # # .
                        # . . . .
                        # . . # #
                        # . . . #
                        . # # # .
        """)
    elif Alphabet == 7:
        basic.show_leds("""
            # . . # .
                        # . . # .
                        # # # # .
                        # . . # .
                        # . . # .
        """)
    elif Alphabet == 8:
        basic.show_leds("""
            # # # . .
                        . # . . .
                        . # . . .
                        . # . . .
                        # # # . .
        """)
    elif Alphabet == 9:
        basic.show_leds("""
            # # # # #
                        . . . # .
                        . . . # .
                        # . . # .
                        . # # . .
        """)
    elif Alphabet == 10:
        basic.show_leds("""
            # . . # .
                        # . # . .
                        # # . . .
                        # . # . .
                        # . . # .
        """)
    elif Alphabet == 11:
        basic.show_leds("""
            # . . . .
                        # . . . .
                        # . . . .
                        # . . . .
                        # # # # .
        """)
    elif Alphabet == 12:
        basic.show_leds("""
            # . . . #
                        # # . # #
                        # . # . #
                        # . . . #
                        # . . . #
        """)
    elif Alphabet == 13:
        basic.show_leds("""
            # . . . #
                        # # . . #
                        # . # . #
                        # . . # #
                        # . . . #
        """)
    elif Alphabet == 14:
        basic.show_leds("""
            . # # . .
                        # . . # .
                        # . . # .
                        # . . # .
                        . # # . .
        """)
    elif Alphabet == 15:
        basic.show_leds("""
            # # # . .
                        # . . # .
                        # # # . .
                        # . . . .
                        # . . . .
        """)
    elif Alphabet == 16:
        basic.show_leds("""
            . # # . .
                        # . . # .
                        # . . # .
                        . # # . .
                        . . # # .
        """)
    elif Alphabet == 17:
        basic.show_leds("""
            # # # . .
                        # . . # .
                        # # # . .
                        # . . # .
                        # . . . #
        """)
    elif Alphabet == 18:
        basic.show_leds("""
            . # # # .
                        # . . . .
                        . # # . .
                        . . . # .
                        . # # . .
        """)
    elif Alphabet == 19:
        basic.show_leds("""
            # # # # #
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
        """)
    elif Alphabet == 20:
        basic.show_leds("""
            # . . # .
                        # . . # .
                        # . . # .
                        # . . # .
                        . # # . .
        """)
    elif Alphabet == 21:
        basic.show_leds("""
            # . . . #
                        # . . . #
                        # . . . #
                        . # . # .
                        . . # . .
        """)
    elif Alphabet == 22:
        basic.show_leds("""
            # . . . #
                        # . . . #
                        # . # . #
                        # # . # #
                        # . . . #
        """)
    elif Alphabet == 23:
        basic.show_leds("""
            # . . # .
                        # . . # .
                        . # # . .
                        # . . # .
                        # . . # .
        """)
    elif Alphabet == 24:
        basic.show_leds("""
            # . . . #
                        . # . # .
                        . . # . .
                        . . # . .
                        . . # . .
        """)
    elif Alphabet == 25:
        basic.show_leds("""
            # # # # .
                        . . # . .
                        . # . . .
                        # . . . .
                        # # # # .
        """)
    else:
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

Alphabet = 0
basic.show_string("Welcome To The Password Generating Game")
basic.clear_screen()