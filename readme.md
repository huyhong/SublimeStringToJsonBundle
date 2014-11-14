# String to JSON Bundle
Converts a string (or line) to a JSON message bundle key. Does the following:
- Generates a key: takes first 7 words of string, uppercases it, removes punctuation, replaces spaces with underscores
- Escapes double quotes from value
- Wraps in double quotes, adds a colon after the key, appends a comma

## Keybindings
- `"ctrl+alt+j"`

## Install
#### Git Clone
Clone this repository in to the Sublime Text 3 "Packages" directory, which is located where ever the 
"Preferences" -> "Browse Packages" option in sublime takes you.

#### Package Control
Will add this when it's more flushed out, maybe.

## Contributors
- Huy Hong (@huy)
