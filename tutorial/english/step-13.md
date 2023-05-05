In this step we will restart the game if the snake has bitten/eaten itself.

# changes at `core.snake`

### new `has_eaten_self` method
```python
def has_eaten_self( self ):
    return self.body[-1] in self.body[:-1]
```

### changes at `move` method
```python
# addition *
if self.has_eaten_self():
    self.reset()
    cr.game.food.spawn()
```