In this step we'll make our snake move!

commit link: https://github.com/mmdmoa/pygame-snake-tutorial/commit/8eae2f3f38d9bc4d95016f772347d54f3d31fc3a


# changes at `core.snake`

In this step, we will implement the movement of our snake using the enums we created earlier.
We can achieve this by checking the direction of the snake and calculating the new position
relative to its current position. We add a new element to the snake's body as its new head,
and remove the first element of its body if it has not eaten food.

Additionally, we want to ensure that our snake can travel across the game board or, 
alternatively, teleport to the other side if it tries to leave the board. 
For example, if the snake is moving to the right edge of the board, 
it should appear on the left edge of the board instead of leaving the game.


### new `has_eaten_food` method
```python
def has_eaten_food( self ):
    return False
```

### new `move` method
```python
def move( self ):
    grid_size = cr.game.grid_system.grid_size
    head = self.body[-1]
    movement = Vector2(0,0)

    if self.direction == SnakeDirection.up:
        movement.y -= 1
    elif self.direction == SnakeDirection.down:
        movement.y += 1
    elif self.direction == SnakeDirection.right:
        movement.x += 1
    elif self.direction == SnakeDirection.left:
        movement.x -= 1

    new_head = Vector2(head.x+movement.x,head.y+movement.y)

    if new_head.x <= 0:
        new_head.x = grid_size.x -1
    if new_head.y <= 0:
        new_head.y = grid_size.y -1

    if new_head.x > grid_size.x -1:
        new_head.x = 0
    if new_head.y > grid_size.y -1:
        new_head.y = 0

    self.body.append(new_head)

    if not self.has_eaten_food():
        self.body.pop(0)
```
# changes at `main`
### adjusting the fps
```python
# change
fps = 30
```