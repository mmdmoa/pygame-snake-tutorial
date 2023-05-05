In this step we will add a new method to our `core.grid_system.GridSystem` class
that is responsible to render the occupied cells inside our grid table.

commit link https://github.com/mmdmoa/pygame-snake-tutorial/commit/a6247048b390d1db162a7d28b71509f9b2bb0e2b

# changes at `core.grid_system`

### changes at `__init__` method

```python
# addition
self.cell_list: list[list[tuple[Vector2,Color]]] = []
```

### new `render_cells` method
```python
# addition *
def render_cells( self ):
    for list_ in self.cell_list:
        for pos,color in list_:
            x,y = int(pos.x),int(pos.y)

            x *= self.x_step
            x += self.rect.x
            y *= self.y_step
            y += self.rect.y

            pg.draw.rect(cr.screen,color,FRect(x,y,self.x_step,self.y_step))
```

### changes at `render` method

```python
# addition
self.render_cells()
```