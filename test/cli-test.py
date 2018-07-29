#!/usr/bin/env python3

import click

@click.group()
def cli():
  pass

@cli.command()
def lol():
  print('haha')

@cli.command()
def lel():
  print('hehe')

if __name__ == "__main__":
  cli()