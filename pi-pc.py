#!/usr/bin/env python3

import click
import RPi.GPIO as GPIO

power_btn_pin = 17
GPIO.setmode(GPIO.BCM)

cli = click.Group()

@cli.command()
def main():
    print("Usage: toggle, on, off, status")

@cli.command()
def toggle():
    try:
        GPIO.setup(power_btn_pin, GPIO.OUT)
        GPIO.output(power_btn_pin, GPIO.LOW)
        GPIO.cleanup(power_btn_pin)           
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()