input.onPinPressed(TouchPin.P0, function () {
    // p0
    mark += 1
    basic.showNumber(mark)
    music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Once)
    for (let index = 0; index < 5; index++) {
        light2(10)
    }
    strip.clear()
    strip.show()
})
input.onButtonPressed(Button.A, function () {
    control.reset()
})
function light3 (num: number) {
    // light
    light22.showRainbow(1, 360)
    for (let index = 0; index < 50; index++) {
        light22.rotate(num)
        basic.pause(num)
        light22.show()
    }
}
function light2 (light_number: number) {
    // light
    strip.showRainbow(1, 360)
    for (let index = 0; index < 50; index++) {
        strip.rotate(1)
        basic.pause(light_number)
        strip.show()
    }
}
let mark = 0
let light22: neopixel.Strip = null
let strip: neopixel.Strip = null
music.setVolume(127)
music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.OnceInBackground)
// start
strip = neopixel.create(DigitalPin.P2, 50, NeoPixelMode.RGB)
light22 = neopixel.create(DigitalPin.P1, 34, NeoPixelMode.RGB_RGB)
light22.setBrightness(6)
mark = 0
basic.showNumber(mark)
loops.everyInterval(1000, function () {
    light3(300)
})
