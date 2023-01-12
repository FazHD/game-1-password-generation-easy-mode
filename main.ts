input.onButtonPressed(Button.B, function () {
    Alphabet = randint(0, 25)
    if (Alphabet == 0) {
        basic.showLeds(`
            . # # . .
            # . . # .
            # # # # .
            # . . # .
            # . . # .
            `)
    } else if (Alphabet == 1) {
        basic.showLeds(`
            # # # . .
            # . . # .
            # # # . .
            # . . # .
            # # # . .
            `)
    } else if (Alphabet == 2) {
        basic.showLeds(`
            # # # # .
            # . . . .
            # . . . .
            # . . . .
            # # # # .
            `)
    } else if (Alphabet == 3) {
        basic.showLeds(`
            # # # . .
            # . . # .
            # . . # .
            # . . # .
            # # # . .
            `)
    } else if (Alphabet == 4) {
        basic.showLeds(`
            # # # # .
            # . . . .
            # # # . .
            # . . . .
            # # # # .
            `)
    } else if (Alphabet == 5) {
        basic.showLeds(`
            # # # # .
            # . . . .
            # # # . .
            # . . . .
            # . . . .
            `)
    } else if (Alphabet == 6) {
        basic.showLeds(`
            . # # # .
            # . . . .
            # . . # #
            # . . . #
            . # # # .
            `)
    } else if (Alphabet == 7) {
        basic.showLeds(`
            # . . # .
            # . . # .
            # # # # .
            # . . # .
            # . . # .
            `)
    } else if (Alphabet == 8) {
        basic.showLeds(`
            # # # . .
            . # . . .
            . # . . .
            . # . . .
            # # # . .
            `)
    } else if (Alphabet == 9) {
        basic.showLeds(`
            # # # # #
            . . . # .
            . . . # .
            # . . # .
            . # # . .
            `)
    } else if (Alphabet == 10) {
        basic.showLeds(`
            # . . # .
            # . # . .
            # # . . .
            # . # . .
            # . . # .
            `)
    } else if (Alphabet == 11) {
        basic.showLeds(`
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # # # # .
            `)
    } else if (Alphabet == 12) {
        basic.showLeds(`
            # . . . #
            # # . # #
            # . # . #
            # . . . #
            # . . . #
            `)
    } else if (Alphabet == 13) {
        basic.showLeds(`
            # . . . #
            # # . . #
            # . # . #
            # . . # #
            # . . . #
            `)
    } else if (Alphabet == 14) {
        basic.showLeds(`
            . # # . .
            # . . # .
            # . . # .
            # . . # .
            . # # . .
            `)
    } else if (Alphabet == 15) {
        basic.showLeds(`
            # # # . .
            # . . # .
            # # # . .
            # . . . .
            # . . . .
            `)
    } else if (Alphabet == 16) {
        basic.showLeds(`
            . # # . .
            # . . # .
            # . . # .
            . # # . .
            . . # # .
            `)
    } else if (Alphabet == 17) {
        basic.showLeds(`
            # # # . .
            # . . # .
            # # # . .
            # . . # .
            # . . . #
            `)
    } else if (Alphabet == 18) {
        basic.showLeds(`
            . # # # .
            # . . . .
            . # # . .
            . . . # .
            . # # . .
            `)
    } else if (Alphabet == 19) {
        basic.showLeds(`
            # # # # #
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            `)
    } else if (Alphabet == 20) {
        basic.showLeds(`
            # . . # .
            # . . # .
            # . . # .
            # . . # .
            . # # . .
            `)
    } else if (Alphabet == 21) {
        basic.showLeds(`
            # . . . #
            # . . . #
            # . . . #
            . # . # .
            . . # . .
            `)
    } else if (Alphabet == 22) {
        basic.showLeds(`
            # . . . #
            # . . . #
            # . # . #
            # # . # #
            # . . . #
            `)
    } else if (Alphabet == 23) {
        basic.showLeds(`
            # . . # .
            # . . # .
            . # # . .
            # . . # .
            # . . # .
            `)
    } else if (Alphabet == 24) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . . # . .
            . . # . .
            `)
    } else if (Alphabet == 25) {
        basic.showLeds(`
            # # # # .
            . . # . .
            . # . . .
            # . . . .
            # # # # .
            `)
    } else {
    	
    }
})
let Alphabet = 0
basic.showString("Welcome To The Password Generating Game Easy Mode")
basic.clearScreen()
