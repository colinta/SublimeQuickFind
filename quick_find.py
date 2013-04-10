from functools import cmp_to_key

import sublime
import sublime_plugin


class QuickfindCommand(sublime_plugin.TextCommand):
    def quickfind(self, search, region,
            look_backwards=False,
            use_regex=None,
            wrap=True,
            case_insensitive=True,
            extend=False,
            ):
        if not len(search):
            return

        flags = 0
        if not use_regex:
            flags |= sublime.LITERAL

        if case_insensitive:
            flags |= sublime.IGNORECASE

        if look_backwards:
            start = region.begin()
            point = start
            while point >= 0:
                found = self.view.find(search, point, flags)
                if found and found.end() < start:
                    break
                else:
                    found = None
                if use_regex:
                    point -= 1
                elif point > len(search):
                    point -= len(search)
                else:
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

        if found and extend:
            if look_backwards:
                found = sublime.Region(region.end(), found.end())
            else:
                found = sublime.Region(region.begin(), found.begin())
        return found

    def run(self, edit, **kwargs):
        regions = [region for region in self.view.sel()]

        if kwargs.get('extend'):
            # change default 'wrap' when extend is true.
            kwargs.setdefault('wrap', False)

        # any edits that are performed will happen in reverse; this makes it
        # easy to keep region.a and region.b pointing to the correct locations
        def get_end(region):
            return region.end()
        regions.sort(key=get_end, reverse=True)
        first_region = regions[0]

        def on_change_each(search):
            new_regions = filter(bool, (self.quickfind(search, region, **kwargs) for region in regions))

            if new_regions:
                if len(new_regions) > 1:
                    sublime.status_message('Found %i instances of "%s"' % (len(new_regions), search))
                else:
                    sublime.status_message('Found "%s"' % search)

                selection = self.view.sel()
                selection.clear()
                for region in new_regions:
                    selection.add(region)

                pos = self.view.viewport_position()
                self.view.show_at_center(region)
                new_pos = self.view.viewport_position()
                if abs(new_pos[0] - pos[0]) <= 1.0 and abs(new_pos[1] - pos[1]) <= 1.0:
                    self.view.set_viewport_position((new_pos[0], new_pos[1] + 1))
                    self.view.set_viewport_position((new_pos[0], new_pos[1]))
            else:
                sublime.status_message('Could not find "%s"' % search)

        if kwargs.get('use_regex') or kwargs.get('extend'):
            selection = ''
        else:
            selection = self.view.substr(first_region)
            cmd, _, _ = self.view.command_history(0, True)
            if selection and any([selection != self.view.substr(region) for region in regions]):
                cmd = None

        if selection and cmd == 'quickfind':
            on_change_each(selection)
        else:
            if kwargs.get('use_regex'):
                prompt = "Regex Search"
            else:
                prompt = "Search"

            if kwargs.get('look_backwards'):
                prompt += ' Backwards'

            if kwargs.get('extend'):
                prompt += ' and Extend'
            self.view.window().show_input_panel(prompt, selection, None, on_change_each, None)
