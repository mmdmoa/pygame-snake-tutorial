In this step we'll create and implement our `core.grid_system`.
it is responsible to provide a grid table that makes collision calculations easier.

commit link https://github.com/mmdmoa/pygame-snake-tutorial/commit/a6bef14c699fce2a103275025ad57979dfca40a6

# changes at `core.grid_system`

The `GridSystem` class is designed to divide a given rectangle into a grid of equally-sized cells,
as specified by a `Vector2` named `grid_size`. This is achieved
by dividing the `width` of the rectangle by `grid_size.x` and the `height` 
of the rectangle by `grid_size.y`.

The resulting values are stored in multiple attributes within `self`, 
specifically `x_step` and `y_step`. These attributes can be used conveniently 
while looping through the `grid_size` components to render our grid table. 
By leveraging these attributes, we can ensure that each cell in the grid has an equal size and 
that our grid is visually consistent throughout.

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
def render( self ) :
    for x in range(int(self.grid_size.x)) :
        x *= self.x_step
        x += self.rect.x
        pg.draw.line(cr.screen, "black", (x, self.rect.y), (x, self.rect.y + self.rect.h))

    for y in range(int(self.grid_size.y)) :
        y *= self.y_step
        y += self.rect.y
        pg.draw.line(cr.screen, "black", (self.rect.x, y), (self.rect.x + self.rect.w, y))
```

# changes at `core.game`

With the `GridSystem` class now complete, it's time to create an instance of it within the `Game` class. 
This can be achieved by passing `Game.rect` and an additional `Vector2` parameter 
that determines how we want to divide the rectangle into equally-sized cells.

By instantiating `GridSystem` within the `Game` class, 
we gain access to the functionality provided by the `GridSystem` class, 
allowing us to create and render a grid of cells within our game.

To render the grid system within our game, 
we simply call its `GridSystem.render` method from within the `Game.render` method. 
This method call results in the grid system 
being rendered alongside other components in the `Game` class that will be added later on in our project.

### changes at `__init__` method

```python

# change: I converted it to an FRect since GridSystem only accepts FRects as parameters
self.rect = FRect(cr.screen.get_rect())
# addition
self.grid_system = GridSystem(self.rect, Vector2(12 * 5, 10 * 5))
```

### changes at `render` method

```python
# addition
self.grid_system.render()
```

