music.playMelody("C5 G A B A G B B ", 120)
music.playMelody("F G A B B B A G ", 120)
basic.forever(function on_forever() {
    basic.showLeds(`
        # . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . #
        `)
    basic.showString("Mustafa")
    basic.showLeds(`
        . . . . #
        . . . # .
        . . # . .
        . # . . .
        # . . . .
        `)
    basic.showArrow(ArrowNames.North)
    basic.pause(200)
    basic.showArrow(ArrowNames.South)
    basic.pause(200)
    basic.showArrow(ArrowNames.West)
    basic.pause(200)
    basic.showArrow(ArrowNames.East)
})
