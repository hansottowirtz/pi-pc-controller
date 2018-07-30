#!/usr/bin/env python3

import click
import time
import RPi.GPIO as GPIO

pwr_btn_pin = 17
pwr_led_pin = 27
on_btn_pin = 22

GPIO.setmode(GPIO.BCM)

@click.group()
def cli():
    pass

@cli.command()
def toggle():
    try:
        GPIO.setup(pwr_btn_pin, GPIO.OUT)
        GPIO.output(pwr_btn_pin, GPIO.LOW)
        time.sleep(.2)
        # GPIO.cleanup(power_btn_pin)           
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

@cli.command()
def status():
    try:
        GPIO.setup(pwr_led_pin, GPIO.IN)
        status = GPIO.input(pwr_led_pin)
        print('on' if status else 'off')
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

@cli.command('force-quit')
def force_quit():
    try:
        GPIO.setup(pwr_btn_pin, GPIO.OUT)
        GPIO.output(pwr_btn_pin, GPIO.LOW)
        time.sleep(8)
        # GPIO.cleanup(power_btn_pin)           
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
  cli()
