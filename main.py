def on_pin_pressed_p0():
    global mark
    # p0
    mark += 1
    basic.show_number(mark)
    music.start_melody(music.built_in_melody(Melodies.RINGTONE), MelodyOptions.ONCE)
    for index in range(5):
        light2(10)
    strip.clear()
    strip.show()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    control.reset()
input.on_button_pressed(Button.A, on_button_pressed_a)

def light3(num: number):
    # light
    light22.show_rainbow(1, 360)
    light22.rotate(num)
    basic.pause(num)
    strip.show()
def start(a: str, num2: number, list2: List[any], sprite: game.LedSprite, bool2: bool, image: Image):
    global strip, light22, mark
    # start
    strip = neopixel.create(DigitalPin.P2, 50, NeoPixelMode.RGB)
    light22 = neopixel.create(DigitalPin.P1, 34, NeoPixelMode.RGB)
    mark = 0
    basic.show_number(mark)
def light2(light_number: number):
    # light
    strip.show_rainbow(1, 360)
    for index2 in range(50):
        strip.rotate(1)
        basic.pause(light_number)
        strip.show()
light22: neopixel.Strip = None
strip: neopixel.Strip = None
mark = 0
image2: Image = None
sprite2: game.LedSprite = None
list3: List[number] = []
# start
start("abc", 1, list3, sprite2, True, image2)

def on_forever():
    light3(100)
basic.forever(on_forever)
