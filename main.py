music.play_melody("C5 G A B A G B B ", 120)
music.play_melody("F G A B B B A G ", 120)

def on_forever():
    basic.show_leds("""
        # . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . #
        """)
    basic.show_string("Mustafa")
    basic.show_leds("""
        . . . . #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
        """)
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(200)
    basic.show_arrow(ArrowNames.SOUTH)
    basic.pause(200)
    basic.show_arrow(ArrowNames.WEST)
    basic.pause(200)
    basic.show_arrow(ArrowNames.EAST)
basic.forever(on_forever)
