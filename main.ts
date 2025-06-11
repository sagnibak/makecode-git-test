input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        . # # # .
        # . . . #
        # # # # #
        # . . . #
        # . . . #
        `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    basic.clearScreen()
    myImage = images.createBigImage(`
        # . . . . . # . . . . . . . . . . . . .
        . # # . # # . # . . # . . # . . . . . .
        . # # . # # . # # . # # . # # . . . . .
        . . . # . . . # # . # # . # # . . . . .
        . . # # # . . # # . # # . # # . . . . .
        `)
    myImage.scrollImage(0, 200)
})
let myImage : Image = null
