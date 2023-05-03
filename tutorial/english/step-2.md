in this step we are going to complete our `EventHolder` class.

it's essential purpose is to fetch the events using `pg.event.get` and convert them
to a more digestible format.

# changes at core/event_holder

here we add four attributes to our `EventHolder` class.
I made multiple lists that are going to contain any keys that are in pressed, released or held states.
also , `should_quit` attribute is responsible to determine if the quit button was pressed.

```python
def __init__( self ) :
    self.pressed_keys = []
    self.released_keys = []
    self.held_keys = []
    self.should_quit = False
```

here we simply fetch every key event and add them to their respective lists.

keep in note that checking if a key value is inside `held_keys` before trying
to remove it is important, as sometimes there can be exceptions duo to unexpected behaviours of
the operating system.

```python
def get_events( self ) :
    self.pressed_keys.clear()
    self.released_keys.clear()

    for i in pg.event.get() :
        if i.type == QUIT :
            self.should_quit = True

        if i.type == KEYDOWN :
            self.pressed_keys.append(i.key)
            self.held_keys.append(i.key)

        if i.type == KEYUP :
            self.released_keys.append(i.key)
            if i.key in self.held_keys :
                self.held_keys.remove(i.key)
```


# changes at main
now that our `EventHolder` class is complete, all left to do is to create
an instance of it and run `EventHolder.get_events` in every iteration of the main loop!

a bonus feature of making a class that fetches the events, is that we can simply create it like
we did the screen in `core.common.resources`,
and then have access to the events from any class, anywhere!

```python
cr.event_holder = EventHolder()

while not cr.event_holder.should_quit:

    if K_ESCAPE in cr.event_holder.released_keys:
        cr.event_holder.should_quit = True

    cr.event_holder.get_events()
```