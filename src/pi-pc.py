#!/usr/bin/env python3

import click
import RPi.GPIO as GPIO

power_btn_pin = 17
GPIO.setmode(GPIO.BCM)

@click.group()
def cli():
    pass

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
        
if __name__ == "__main__":
  cli()