In this step we will implement the basic behaviour of our `core.game` class.

commit link https://github.com/mmdmoa/pygame-snake-tutorial/commit/221f86ea41efb02306e97b56bf843c131ee89e7a

# changes at `core.common.resources`

```python
game = None
```

# changes at `core.game`


```python
from core.common.names import *
import core.common.resources as cr

from core.grid_system import GridSystem

class Game:
    def __init__( self ):
        self.rect = cr.screen.get_rect()
        self.rect.y += self.rect.h * 0.1

    def check_events( self ):
        ...

    def render( self ):
        cr.screen.fill("gray")
        pg.draw.rect(cr.screen,Color("gray").lerp("black",0.5),self.rect)
```

# changes at `core.grid_system`

```python
from core.common.names import *
import core.common.resources as cr

class GridSystem:
    def __init__(self):
        ...
```

# changes at `main`

new import 

```python
from core.game import Game 
```

new screen size

```python
cr.screen = pg.display.set_mode([900,740])
```

new statements in the main loop
```python
cr.event_holder.get_events()
cr.game.check_events()
cr.game.render()
pg.display.update()
```

