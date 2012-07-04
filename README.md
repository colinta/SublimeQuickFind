Quickfind plugin for Sublime Text 2
===================================

Works similarly to TextMate's `ctrl+s`.  But if text is already selected, it will be the default search.  Keep pressing `ctrl+s` to search for the next instance.


Installation
------------

1. Using Package Control, install "Quickfind"

Or:

1. Open the Sublime Text 2 Packages folder

    - OS X: ~/Library/Application Support/Sublime Text 2/Packages/
    - Windows: %APPDATA%/Sublime Text 2/Packages/
    - Linux: ~/.Sublime Text 2/Packages/

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

Commands
--------

`quickfind`: Displays an input panel where you can enter a quick search.

If text is selected, it will search for that text if the previous command was
'quickfind'.  This is incredibly inconsistent, but [it’s not my fault][last_command_bug]!

If `extend` option is true, the selection will be extended *up to* (but not including) the search.

Default search settings are:

* `wrap`: True
* `case_insensitive`: True
* `use_regex`: False
* `look_backwards`: False
* `extend`: False

[last_command_bug]: http://sublimetext.userecho.com/topic/93699-command_history-does-not-help-determine-last-command/ "bug submission at sublimetext.userecho.com"
