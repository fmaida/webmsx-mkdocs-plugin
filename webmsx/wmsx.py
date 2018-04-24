import re
from mkdocs.plugins import BasePlugin
from .snippet import wmsx_snippet


class WMSXPlugin(BasePlugin):

    def on_page_markdown(self, markdown, page, config, site_navigation):

        # Search for {% msx "title.rom" %}

        markdown = re.sub(r"\{\%(\s)*msx(.*?)\%\}",
                          wmsx_snippet(),
                          markdown,
                          flags=re.IGNORECASE)

        return markdown
