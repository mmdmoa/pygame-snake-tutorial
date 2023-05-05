In this step we'll create and implement our `core.grid_system`.
it is responsible to provide a grid table that makes collision calculations easier.

commit link https://github.com/mmdmoa/pygame-snake-tutorial/commit/a6bef14c699fce2a103275025ad57979dfca40a6

# changes at `core.game`


### changes at `__init__` method

```python

# change: I converted it to an FRect since GridSystem only accepts FRects as parameters
self.rect = FRect(cr.screen.get_rect())
# addition
self.grid_system = GridSystem(self.rect,Vector2(12*5,10*5))
```

### changes at `render` method

```python
# addition
self.grid_system.render()
```

# changes at `core.grid_system`

### changes at `__init__` method

```python
# addition *
self.rect = rect
self.grid_size = grid_size
self.x_step = self.rect.w / grid_size.x
self.y_step = self.rect.h / grid_size.y
```

### new `render` method

```python
def render( self ):
    for x in range(int(self.grid_size.x)):
        x *= self.x_step
        x += self.rect.x
        pg.draw.line(cr.screen,"black",(x,self.rect.y),(x,self.rect.y+self.rect.h))

    for y in range(int(self.grid_size.y)):
        y *= self.y_step
        y += self.rect.y
        pg.draw.line(cr.screen,"black",(self.rect.x,y),(self.rect.x+self.rect.w,y))
```