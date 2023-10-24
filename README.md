# TODO list in Python / Rust

Simple command line application which allows to store and keep track of a todo-list. Currently it is implemented in Python and in the futur hopefully in Rust as well.  
I actually use the Pyton version quite a bit as it is really handy to just quickly write down something you have to do. I also recommend creating a shortcut to the program and placing it somewhere accessible, like the desktop.

## Content
- [Python version](#python-version)
- [Rust version](#rust-version)

## Python version
__This code is very old and badly written. I am very sorry. Please don't look at it.__   
It also probably only works on Windows.

### Storage
The todo's are stored in the JSON file `todo.json` in the same directory as `todo.py`.  
With some important todo's it looks like this:
```json
{
    "todo": [
        "pet cat",
        "pet cat again"
    ],
    "done": [
        "cuddle with cat"
    ]
}
```

### Commands

The program has 6 simple commands:  
| command(s) + argument(s) | Function |
|--------------------------|----------|
| `list` or `l` | Clears the screen and lists all unfinished todo's (by index) and finished todo's. |
| `add` or `a` + `todo` | Adds a new todo to the list. The value added to the list is the value passed as the `todo` argument. <br> For example `add pet cat` would add the todo "pet cat" to the list. |
| `remove` or `r` + `todo` or `index` | Removes the specified todo from the list entirely, meaning either from the list of finished todo's or from the list of unfinished todo's. <br> The todo can either be specified via the argument `todo` with its name, or via the argument `index` with its index in the list of unfinished todo's. <br> For example `remove 1` would remove the first todo from the list of unfinished todo's. |
| `finish` or `f` + `todo` or `index` | Moves the specified todo from the list of unfished todo's to the list of finished todo's. <br> The todo can either be specified via the argument `todo` with its name, or via the argument `index` with its index in the list of unfinished todo's. <br> For example `finish pet cat` would finish the todo `pet cat`. |
| `delete` or `del` | Deletes the whole todo list. __This is not reversable!__  |
| `quit` or `q` | Saves all changes (if any) and quits the program. You need to press `Enter` again after the program quits to close the terminal. |

There is also another "secret" command: `open` or `o` which opens the the JSON file  where all the todo's are stored in Notepad. There you could modify the list yourself, for example if you mistyped a todo or if you want to change the order.  
__This should only be done if you know JSON, as you could corrupt your whole list.__

## Rust version
As the program gets implemented in Rust i will update this section.

## Licensing
This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)