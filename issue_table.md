| Issue Type                            | Tool            | Line(s)  | Description                                      | Fix Applied                                            |
| ------------------------------------- | --------------- | -------- | ------------------------------------------------ | ------------------------------------------------------ |
| Mutable default argument              | Pylint          | 8        | Function used `logs=[]`, causing shared state    | Changed to `logs=None` and initialized inside function |
| Bare `except:`                        | Bandit / Pylint | 19       | Exception hides all errors                       | Replaced with `except KeyError:` and added message     |
| Use of `eval()`                       | Bandit          | 59       | Dangerous and insecure                           | Removed and replaced with direct print statement       |
| Unused `logging` import               | Flake8 / Pylint | 2        | Import not used anywhere                         | Removed unused import                                  |
| File handling without context manager | Pylint          | 26, 32   | `open()` used without `with`                     | Replaced with `with open(..., encoding="utf-8")`       |
| Non–snake_case function names         | Pylint          | Multiple | Functions not following Python naming convention | Renamed to `add_item`, `remove_item`, etc.             |
