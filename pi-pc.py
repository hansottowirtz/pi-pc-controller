#!/usr/bin/env python3

import click
import RPi.GPIO as GPIO

power_btn_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(power_btn_pin, GPIO.OUT)

@click.command()
@click.argument('turn-on')
def turn_on():
    GPIO.output(power_btn_pin, GPIO.LOW)
    GPIO.cleanup(power_btn_pin)
