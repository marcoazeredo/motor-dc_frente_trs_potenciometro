input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (trás == 0) {
        frente = 0
        trás = 1
    } else {
        frente = 1
        trás = 0
    }
    
})
let velocidade = 0
let trás = 0
let frente = 0
frente = 1
trás = 0
basic.forever(function on_forever() {
    
    velocidade = pins.map(pins.analogReadPin(AnalogPin.P3), 0, 1023, 200, 1023)
    pins.analogWritePin(AnalogPin.P0, velocidade)
    pins.digitalWritePin(DigitalPin.P1, frente)
    pins.digitalWritePin(DigitalPin.P2, trás)
})
