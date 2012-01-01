import sublime
import sublime_plugin


class QuickfindCommand(sublime_plugin.TextCommand):
    def run(self, edit, look_backwards=False, use_regex=False):
        # this is a silly way to assign region to the first in RegionSet
        for region in self.view.sel():
            break

        def on_change(search):
            if not len(search):
                return

            if look_backwards:
                start = region.begin()
                point = start - 1
                while point > 0:
                    found = self.view.find(search, point, sublime.LITERAL)
                    if found and found.end() < start:
                        break
                    else:
                        found = None
                    point -= 1
                sublime.status_message('Could not find "%s"' % search)
            else:
                start = region.end()
                if use_regex:
                    flags = None
                else:
                    flags = sublime.LITERAL
                found = self.view.find(search, start, flags)

            if found:
                selection = self.view.sel()
                selection.clear()
                selection.add(found)
                sublime.status_message('Found "%s"' % search)
                self.view.show_at_center(found)
            else:
                sublime.status_message('Could not find "%s"' % search)

        if not region.empty():
            on_change(self.view.substr(region))
        else:
            self.view.window().show_input_panel('Search', '', None, on_change, None)
