Quickfind plugin
================

Works similarly to TextMate's `ctrl+s`.  But if text is already selected, it will be the default search.  Keep pressing `ctrl+s` to search for the next instance.

Installation
------------

1. Using Package Control, install "Quickfind"

Or:

1. Open the Sublime Text Packages folder
    - OS X: ~/Library/Application Support/Sublime Text 3/Packages/
    - Windows: %APPDATA%/Sublime Text 3/Packages/
    - Linux: ~/.Sublime Text 3/Packages/ or ~/.config/sublime-text-3/Packages

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

### Sublime Text 2

1. Open the Sublime Text 2 Packages folder
2. clone this repo, but use the `st2` branch

       git clone -b st2 git@github.com:colinta/SublimeQuickFind

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
