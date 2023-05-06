In this step we will add a new method to our `core.grid_system.GridSystem` class
that is responsible to render the occupied cells inside our grid table.

commit link https://github.com/mmdmoa/pygame-snake-tutorial/commit/a6247048b390d1db162a7d28b71509f9b2bb0e2b

# changes at `core.grid_system`

In order to customize the appearance of our grid, 
we can create a method that fills specific cells in the table with determined colors. 
This can be achieved by zipping the coordinates 
of each cell with its corresponding color in a `tuple` format.

To support the functionality of filling specific cells with predetermined colors, 
we've added a new attribute to the `GridSystem` class called `cell_list`. 
This attribute is a list that contains sub-lists of tuples, 
with each `tuple` containing a `Vector2` and `Color`. These sub-lists represent the data 
of each cell that needs to be filled and the color that it should be filled with.

By utilizing this approach to render our game components, 
we can avoid writing redundant code and achieve a more consistent way of rendering our 
`Snake` and `Food` elements.

By encapsulating the rendering logic within the `GridSystem` class, 
we can easily integrate new game elements into our project without having 
to write additional rendering code. 
This results in a more efficient and organized codebase that is easier to maintain and update.

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