Quickfind plugin
================

Works similarly to TextMate's `ctrl+s`.  But if text is already selected, it will be the default search.  Keep pressing `ctrl+s` to search for the next instance.

Installation
------------

Using Package Control, install "Quickfind" or clone this repo in your packages folder.

I recommended you add key bindings for the commands. I've included my preferred bindings below.
Copy them to your key bindings file (⌘⇧,).

Commands
--------

`quickfind`: Displays an input panel where you can enter a quick search.

If text is selected, it will search for that text if the previous command was 'quickfind'.

If `extend` option is true, the selection will be extended *up to* (but not including) the search.

Default search settings are:

* `wrap`: True
* `case_insensitive`: True
* `use_regex`: False
* `look_backwards`: False
* `extend`: False

Key Bindings
------------

Copy these to your user key bindings file.

<!-- keybindings start -->
    { "keys": ["ctrl+s"], "command": "quickfind" },
    { "keys": ["ctrl+shift+s"], "command": "quickfind", "args": { "extend": true } },
    { "keys": ["alt+s"], "command": "quickfind", "args": { "look_backwards": true } },
    { "keys": ["alt+shift+s"], "command": "quickfind", "args": { "look_backwards": true, "extend": true } },
    { "keys": ["ctrl+alt+s"], "command": "quickfind", "args": { "use_regex": true } },
<!-- keybindings stop -->
