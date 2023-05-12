In this step, we will achieve basic functionality for our screen 
and prepare our structures for the next steps.

## changes at core/commons/names

This class enables us to import all the necessary names 
that we are likely to require in most of our classes. 
By utilizing the `core.common.names` module and importing everything, 
we can easily access all the required names in a fast and efficient manner. 

This streamlined approach to importing allows us to maintain a clean and organized codebase.

```python
# Optional helps the linters, it's not a necessary component for our project
from typing import Optional

import pygame as pg
from pygame.locals import *
# I always use these classes in my project's, it's helpful to directly import them
from pygame import Vector2,FRect,Surface,Color
```

## changes at core/commons/resources

The screen is the primary window that Pygame creates using the `pg.display.set_mode` command. 
By storing it in `core.common.resources`, we can access it from any class, anywhere within our project, 
except in cases where circular imports occur.

The `EventHolder` class is designed to store every event in a well-formatted manner 
and manage them with ease, 
thereby simplifying event handling across our project.

```python
from core.common.names import *
from core.event_holder import EventHolder

"""
By defining a variable as Optional[type], we can inform linters 
that the value of the variable can either be of the specified type or None. 
This helps to avoid issues that may arise from initializing a variable with None and makes 
it easier for linters to correctly identify the type of the variable. 
It is important to note that while this step is not necessary, 
it can help ensure the correctness of our code and make it more robust.
"""
screen: Optional[Surface] = None
event_holder: Optional[EventHolder] = None
```

## changes at core/event_holder
For now, I'm just creating an empty class names `EventHolder` so our import
doesn't fail in `core.common.resources`

```python
from core.common.names import *

class EventHolder :
    def __init__( self ) :
        ...

```
## changes at core/main.py

The codebase follows the standard structure for Pygame projects. 
The primary difference lies in the import system. 
Rather than importing specific modules, 
we import everything we are likely to need in the current file, through the `core.common.names` module.

Furthermore, we store the window in the `core.common.resources` module rather than in main. 
This enables us to access the window from anywhere within our project.

At present, the `EventHolder` class is empty and has no functionality. Hence, 
it is not being used. However, in the upcoming step,
we will create and implement the `EventHolder` class, 
and replace any temporary code with its functionalities.

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