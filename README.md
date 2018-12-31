# pollite

A python module to allow for polling in a lightweight manner. poll + lite = pollite!

## Usage
Sometimes when dealing with external services not under your control with no way of subscribing to notifications, you're forced to check on them on a periodic basis, and required to rate-limit your code as it does so. This often leads to code that looks something like this:
```
#!/usr/bin/env python3
import time

if __name__ == "__main__":
    most_recent_tick = time.time()
    frequency = 1
    end_time = most_recent_tick + 10
    while most_recent_tick < end_time:
        elapsed = time.time() - most_recent_tick
        if elapsed < frequency:
            time.sleep(frequency - elapsed)
        print(most_recent_tick)
        most_recent_tick = time.time()
```

Replace the print statement with literally any code that has to do some task once every second for 10 seconds (for this example) or whatever period of time. Because you must update the value of `most_recent_tick` after the code that depends on it runs, you wind up copying and pasting this in other parts of your code if you want different things to happen for different periods and different frequencies. This is how pollite solves that issue:

```
#!/usr/bin/env python3
import pollite

if __name__ == "__main__":
    for i in pollite.TimeRange(frequency=1, duration=10):
        print(i)
```

Look at how cute and tiny it is! No weird time shenanigans, just a simple iterator interface. Oh? You want to poll forever too? That's covered by setting `forever=True` in the constructor:

```
#!/usr/bin/env python3
import pollite

if __name__ == "__main__":
    for i in pollite.TimeRange(1, forever=True):
        print(i)
```
Life (of a program at least) is short. Use pollite-ness where you can. :)
