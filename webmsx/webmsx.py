import re
from mkdocs.plugins import BasePlugin
from .snippet import webmsx_snippet


class WebMSXPlugin(BasePlugin):

    def on_page_content(self, html, page, config, site_navigation):

        # Search for {% msx "title.rom" %}

        # markdown = re.sub(r"\{\%(\s)*msx(.*?)\%\}",
        #                   webmsx_snippet(),
        #                   markdown,
        #                   flags=re.IGNORECASE)

        try:
            if page.meta["msx_game"] != "":
                game = page.meta["msx_game"].replace(chr(34), "").replace("'", "")
                try:
                    system = page.meta["msx_system"].upper().replace(chr(34), "").replace("'", "")
                except KeyError:
                    system = "MSX1"
                html += webmsx_snippet(game, system)
        except KeyError:
            pass

        return html
