def on_button_pressed_a():
    global frente, trás
    if trás == 0:
        frente = 0
        trás = 1
    else:
        frente = 1
        trás = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

velocidade = 0
trás = 0
frente = 0
frente = 1
trás = 0

def on_forever():
    global velocidade
    velocidade = pins.map(pins.analog_read_pin(AnalogPin.P3), 0, 1023, 200, 1023)
    pins.analog_write_pin(AnalogPin.P0, velocidade)
    pins.digital_write_pin(DigitalPin.P1, frente)
    pins.digital_write_pin(DigitalPin.P2, trás)
basic.forever(on_forever)
