import sublime
import sublime_plugin


class GotoCharsCommand(sublime_plugin.TextCommand):
    def run(self, edit, look_backwards=False, use_regex=False):
        # this is a silly way to assign region to the first in RegionSet
        for region in self.view.sel():
            break

        def on_change(text):
            if not len(text):
                return

            if look_backwards:
                start = region.begin()
                point = start - 1
                while point > 0:
                    found = self.view.find(text, point, sublime.LITERAL)
                    if found and found.end() < start:
                        break
                    else:
                        found = None
                    point -= 1
                sublime.status_message('Could not find "%s"' % text)
            else:
                start = region.end()
                if use_regex:
                    flags = None
                else:
                    flags = sublime.LITERAL
                found = self.view.find(text, start, flags)

            if found:
                selection = self.view.sel()
                selection.clear()
                selection.add(found)
                sublime.status_message('Found "%s"' % text)
                self.view.show_at_center(found)
            else:
                sublime.status_message('Could not find "%s"' % text)

        if region.empty():
            self.view.window().show_input_panel('Search', '', None, on_change, None)
        else:
            search = self.view.substr(region)
            on_change(search)
