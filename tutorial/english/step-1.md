
in this step we achieve basic functionality for our screen, and are preparing our 
structures for the next steps

## changes at core/commons/names

this class imports every name that I'm sure of I'm going to need in most of my 
classes. by just importing everything from `core.common.names` I will have access
to all of those names, it's a fast and clean method to import things.

```python
# Optional helps the linters, it's not a necessary component for our project
from typing import Optional

import pygame as pg
from pygame.locals import *
# I always use these classes in my project's, it's helpful to directly import them
from pygame import Vector2,FRect,Surface,Color
```

## changes at core/commons/resources

screen is the main window that is created by pygame through `pg.display.set_mode` command.
by storing it in `core.common.resources` it's possible to access it from any class, anywhere.
( unless it causes a circular import )

EventHolder is helps to store every event in a proper format, and easily 
manage them.

```python
from core.common.names import *
from core.event_holder import EventHolder

"""
by doing `Optional[type]` the linters will always assume 
the value of the variable is the same as the specified type in `Optional`.
so it helps to fix the behaviour of linters while initializing a variable with `None`.
again, this is not necessary
"""
screen: Optional[Surface] = None
event_holder: Optional[EventHolder] = None
```

## changes at core/event_holder
for now, I'm just creating an empty class names `EventHolder` so our import
doesn't fail in `core.common.resources`

```python
from core.common.names import *

class EventHolder :
    def __init__( self ) :
        ...

```
## changes at core/main.py

this code is like any pygame code. the only difference is the import system.
instead of directly importing what I precisely need, I import everything that I'm most likely
to need in the current file.

also instead of assigning the window to a variable in `main`, I assign it to
a variable in `core.common.resources`, so I can have access to it from anywhere!

I didn't add anything to `EventHolder` class, so I obviously can't use it. in the next step
we'll actually make `EventHolder`, and replace its functionalities with anything commented
as temporary in this code.

```python

from core.common.names import *
import core.common.resources as cr

pg.init()
cr.screen = pg.display.set_mode([800,640])


# temporary 
running = True
while running:
    # temporary
    for i in pg.event.get():
        if i.type == QUIT or i.type == KEYDOWN and i.key == K_ESCAPE:
            running = False
```