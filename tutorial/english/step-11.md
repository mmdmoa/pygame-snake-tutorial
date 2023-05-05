in this step we'll improve the visual aspects of our snake,
grid table, and game in general.

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/6572ff00b8098aa7e9b1aa77ae5b26695fd1eb77


# changes at `core.event_holder`
### changes at `__init__` method
```python
# addition
self.should_render_debug = False
```

# changes at `core.game`
### changes at `__init__` method
```python
# adjustment
self.grid_system = GridSystem(self.rect,Vector2(12*4,10*4))
```

# changes at `core.grid_system`
### changes at `render_cells` method
```python
# adjustment
pg.draw.rect(cr.screen,color,FRect(x,y,self.x_step+1,self.y_step+1))
```
### new `render_debug` method
```python
def render_debug( self ):
    """
    grid table rendering code is migrated from `render` 
    method, into here.
    """
    for x in range(int(self.grid_size.x)):
        x *= self.x_step
        x += self.rect.x
        pg.draw.line(cr.screen,"black",(x,self.rect.y),(x,self.rect.y+self.rect.h))
    
    for y in range(int(self.grid_size.y)):
        y *= self.y_step
        y += self.rect.y
        pg.draw.line(cr.screen,"black",(self.rect.x,y),(self.rect.x+self.rect.w,y))
```

### changes at `render` method
```python
def render( self ):
    # addition
    if cr.event_holder.should_render_debug:
        # addition
        self.render_debug()
        
    self.render_cells()
```

# changes at `core.snake`

### changes at `__init__` mehotd
```python
# rename refactor from `color`
self.body_color: Optional[Color] = None
# new attribute
self.head_color: Optional[Color] = None
```

### changes at `colored_body` method
```python
def colored_body( self ):
    # change
    return [(i,self.body_color) for i in self.body[:-1]] + \
           [(self.body[-1], self.head_color)]
```

### changes at `reset` method
```python
# rename refactor from `color`
self.body_color = Color("red").lerp("black",0.5)
# new attribute
self.head_color = Color("red").lerp("black",0.65)
```
# changes at `main`
### changes in the main loop

```python
if K_ESCAPE in cr.event_holder.released_keys:
    cr.event_holder.should_quit = True
    
# addition
if K_F3 in cr.event_holder.pressed_keys:
    cr.event_holder.should_render_debug = not cr.event_holder.should_render_debug

cr.event_holder.get_events()
```