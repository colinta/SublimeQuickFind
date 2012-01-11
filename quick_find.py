import sublime
import sublime_plugin


class QuickfindCommand(sublime_plugin.TextCommand):
    def run(self, edit, look_backwards=False, use_regex=None, wrap=True, case_insensitive=True):
        region = self.view.sel()[0]

        def on_change(search):
            if not len(search):
                return

            if use_regex:
                flags = 0
            else:
                flags = sublime.LITERAL

            if case_insensitive:
                flags |= sublime.IGNORECASE

            if look_backwards:
                start = region.begin()
                point = start - 1
                while point >= 0:
                    found = self.view.find(search, point, flags)
                    if found and found.end() < start:
                        break
                    else:
                        found = None
                    point -= 1
                    # if we get to the beginning, and wrap is enabled, start at the end and keep searching
                    # unless we already tried that
                    if point < 0 and wrap and start < self.view.size():
                        start = point = self.view.size()
                        point -= 1
            else:
                start = region.end()
                found = self.view.find(search, start, flags)
                if not found and wrap:
                    found = self.view.find(search, 0, flags)

            if found:
                selection = self.view.sel()
                selection.clear()
                selection.add(found)
                sublime.status_message('Found "%s"' % search)
                self.view.show_at_center(found)
            else:
                sublime.status_message('Could not find "%s"' % search)

        cmd, _, _ = self.view.command_history(0, True)
        if not region.empty() and cmd == 'quickfind':
            on_change(self.view.substr(region))
        else:
            prompt = 'Search' if not use_regex else "Regex Search"
            self.view.window().show_input_panel(prompt, self.view.substr(region), None, on_change, None)
