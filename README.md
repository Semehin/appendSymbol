# appendSymbol
Sublime text 2 &amp; 3 package allows you to append any symbol at the end of a line by pressing a hotkey. 
Also it can jump to EOL or add new line after appending symbol.

## hotkeys

### linux & windows
+ <kbd>Ctrl</kbd>+<kbd>;</kbd> - appends ";" at EOL
+ <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>;</kbd> - appends ";" to EOL and jumps there
+ <kbd>Ctrl</kbd>+<kbd>shift</kbd>+<kbd>;</kbd> - appends ";" to EOL and adds new line below and jumps there

### mac
Same as linux & windows but <kbd>Super</kbd> instead of <kbd>Ctrl</kbd>.

### symbols
There are three predefined symbols which you can use with default hotkeys above: 
+ "."
+ ";"
+ ","

## config
###symbols
You can configure any symbol what you need via "args" key in key bindings:

`{ "keys": ["ctrl+#"], "command": "append_symbol", "args": {"symb": "#"} }`

Where are "#" - any symbol you need.

###callbacks
To use callbacks define one of them at "args" key

`{ "keys": ["ctrl+#"], "command": "append_symbol", "args": {"symb": "#", "callback": "*"} }`

Where are "*" one of two callbacks:
+ "jumpToEOL"
+ "addLine"

Inspired by: [AppendSemiColon](https://github.com/MauriceZ/AppendSemiColon)