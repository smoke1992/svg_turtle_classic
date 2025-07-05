"""
SVG Turtle Classic - A wrapper for svg-turtle to mimic the classic Python turtle module's interface.

This module provides three modes of use:
1. `from svg_turtle_classic import *`: Procedural style (e.g., forward(100))
2. `import svg_turtle_classic`: Module style (e.g., svg_turtle_classic.forward(100))
3. `t = Turtle()`: Object-oriented style (e.g., t.forward(100))

The done() function handles the final SVG generation and display.

Version: 0.1.0
Author: Based on svg-turtle by Don Kirkby
License: MIT
"""

# Import all the main functionality from the svg_turtle_classic module
from .svg_turtle_classic import *

# Version information
__version__ = "0.1.0"
__author__ = "smoke1992,Based on svg-turtle by Don Kirkby"
__license__ = "MIT"

# Make sure all the important functions and classes are available
__all__ = [
    'Turtle',
    'setup',
    'done',
    'speed',
    'stamp_size',
    # All the turtle methods
    'forward', 'fd', 'backward', 'bk', 'back', 'right', 'rt', 'left', 'lt',
    'goto', 'setpos', 'setposition', 'setx', 'sety', 'setheading', 'seth',
    'home', 'circle', 'dot', 'stamp', 'clearstamp', 'clearstamps', 'undo',
    'position', 'pos', 'towards', 'xcor', 'ycor', 'heading', 'distance',
    'degrees', 'radians', 'penup', 'pu', 'up', 'pendown', 'pd', 'down',
    'pensize', 'width', 'pencolor', 'fillcolor', 'color', 'isdown',
    'begin_fill', 'end_fill', 'reset', 'clear', 'write', 'hideturtle', 'ht',
    'showturtle', 'st', 'isvisible', 'shape', 'shapesize', 'turtlesize'
] 