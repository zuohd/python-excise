# import autopy
# autopy.key.type_string("Hello, world!") # Prints out "Hello, world!" as quickly as OS will allow.
# autopy.key.type_string("Hello, world!", wpm=60) # Prints out "Hello, world!" at 60 WPM.
# autopy.key.tap(autopy.key.Code.RETURN)Hello, world!He
# autopy.key.tap(autopy.key.Code.F1)
# autopy.key.tap(autopy.key.Code.LEFT_ARROW)

import autopy
def hello_world():
    # autopy.alert.alert("Hello, world")
    autopy.key.tap("f",[autopy.key.Modifier.CONTROL])
    # help(autopy.key.toggle)
hello_world()