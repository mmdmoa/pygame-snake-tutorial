In this step, we will complete the implementation of our `EventHolder` class. 
Its primary objective is to retrieve events using the `pg.event.get` method 
and convert them into a more easily processable format.

By doing so, we can simplify the process of event handling 
and make it more straightforward for us to manage events across our entire project. 
The `EventHolder` class will play a crucial role in our codebase, 
allowing us to easily manage and process events in a well-organized manner.

# changes at core/event_holder

In this step, we are adding four attributes to our `EventHolder` class. These attributes are:

* `pressed_keys`: A list containing all keys that are currently in the pressed state.
* `released_keys`: A list containing all keys that were released in the last frame.
* `held_keys`: A list containing all keys that are currently in the held state.
+ `should_quit`: A boolean attribute responsible for determining whether the quit button was pressed.

By using these attributes, we can keep track of the state 
of various keys and events in a well-organized manner, 
thereby simplifying our code and making it more maintainable.

```python
def __init__( self ) :
    self.pressed_keys = []
    self.released_keys = []
    self.held_keys = []
    self.should_quit = False
```

In this step, we are fetching every key event using 
`pg.event.get()` and adding them to their respective lists 
(`pressed_keys`, `released_keys`, and `held_keys`).

It is important to note that we check whether a key value is present 
in `held_keys` before trying to remove it. This is crucial as unexpected behaviors 
from the operating system can sometimes cause exceptions to be raised. 
By performing this check, 
we can avoid such exceptions and ensure that our code remains stable and reliable.

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
With the completion of our `EventHolder` class, all that remains to be done is 
to create an instance of it and call its `get_events` method in every iteration of the main loop.

One of the benefits of creating a class that fetches events is that 
we can easily create an instance of it and then access the events from any class, 
anywhere. We can store this instance in `core.common.resources`, just like we did with the screen, 
and then access it whenever we need to retrieve events. This approach 
makes our code more modular and flexible, allowing us to handle events more efficiently and effectively.

```python
cr.event_holder = EventHolder()

while not cr.event_holder.should_quit:

    if K_ESCAPE in cr.event_holder.released_keys:
        cr.event_holder.should_quit = True

    cr.event_holder.get_events()
```