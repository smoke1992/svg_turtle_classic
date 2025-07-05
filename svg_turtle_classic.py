"""
A wrapper for svg-turtle to mimic the classic Python turtle module's interface.
Version 0.1.0 supports three modes of use:
1. `from svg_turtle_classic import *`: Procedural style (e.g., forward(100))
2. `import svg_turtle_classic`: Module style (e.g., svg_turtle_classic.forward(100))
3. `t = Turtle()`: Object-oriented style (e.g., t.forward(100))

The done() function handles the final SVG generation and display.
"""

from svg_turtle import SvgTurtle
from IPython.display import SVG, display

# --- Global State for the Module ---

# Default canvas dimensions
_canvas_width = 800
_canvas_height = 600

# The single, global turtle instance for the procedural/module-level style
_the_turtle = SvgTurtle(_canvas_width, _canvas_height)

# Store the desired size for the final stamp
_stamp_size_params = (1, 1, 1)

# --- The Turtle Class (for OO style) ---

class Turtle(SvgTurtle):
    """
    Creates a new turtle object that draws on its own canvas.
    Mimics the behavior of `t = turtle.Turtle()`.
    """
    def __init__(self, shape='classic', undobuffersize=1000, visible=True):
        # Initialize the parent SvgTurtle with the current global canvas dimensions
        super().__init__(_canvas_width, _canvas_height)
        # These parameters are for compatibility with the standard turtle constructor
        self.shape(shape)
        if not visible:
            self.hideturtle()

# --- Public API Functions ---

def setup(width=800, height=600):
    """
    Sets the dimensions for ALL subsequent canvases (both procedural and OO).
    This will reset the current procedural drawing.
    
    :param width: Canvas width in pixels.
    :param height: Canvas height in pixels.
    """
    global _the_turtle, _canvas_width, _canvas_height
    _canvas_width = width
    _canvas_height = height
    # Re-initialize the global turtle with new dimensions
    _the_turtle = SvgTurtle(_canvas_width, _canvas_height)

def stamp_size(stretch_wid=1, stretch_len=None, outline=None):
    """
    Sets the size of the turtle stamp that will be drawn by done().
    """
    global _stamp_size_params
    if stretch_len is None:
        stretch_len = stretch_wid
    _stamp_size_params = (stretch_wid, stretch_len, outline)

def done(turtle_instance=None):
    """
    Finalizes and displays the drawing with a final stamp.

    - If called as `done()`, it finalizes the procedural/module-level drawing.
    - If called as `done(t)`, it finalizes the drawing of the turtle object `t`.
    """
    target_turtle = turtle_instance if turtle_instance is not None else _the_turtle
    
    if target_turtle:
        target_turtle.shapesize(*_stamp_size_params)
        target_turtle.stamp()
        display(SVG(target_turtle.to_svg()))
        # Reset the turtle for the next run
        target_turtle.reset()

def speed(*args, **kwargs):
    """Placeholder for compatibility. Does nothing."""
    pass

# --- Dynamic Function Wrapping for Procedural/Module Style ---

_METHODS_TO_WRAP = [
    'forward', 'fd', 'backward', 'bk', 'back', 'right', 'rt', 'left', 'lt',
    'goto', 'setpos', 'setposition', 'setx', 'sety', 'setheading', 'seth',
    'home', 'circle', 'dot', 'stamp', 'clearstamp', 'clearstamps', 'undo',
    'position', 'pos', 'towards', 'xcor', 'ycor', 'heading', 'distance',
    'degrees', 'radians', 'penup', 'pu', 'up', 'pendown', 'pd', 'down',
    'pensize', 'width', 'pencolor', 'fillcolor', 'color', 'isdown',
    'begin_fill', 'end_fill', 'reset', 'clear', 'write', 'hideturtle', 'ht',
    'showturtle', 'st', 'isvisible', 'shape', 'shapesize', 'turtlesize'
]

def create_wrapper(name):
    def wrapper(*args, **kwargs):
        method = getattr(_the_turtle, name)
        return method(*args, **kwargs)
    wrapper.__doc__ = getattr(_the_turtle, name).__doc__
    return wrapper

for method_name in _METHODS_TO_WRAP:
    globals()[method_name] = create_wrapper(method_name)

# --- Controlling `from svg_turtle_classic import *` ---
__all__ = _METHODS_TO_WRAP + ['setup', 'done', 'speed', 'stamp_size', 'Turtle']