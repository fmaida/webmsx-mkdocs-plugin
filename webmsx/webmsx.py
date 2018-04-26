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
            if page.meta["msx"] != "":
                values = page.meta["msx"].split(" ")
                if "game:" in values:
                    try:
                        pos = values.index("game:")
                        game = values[pos + 1].replace(chr(34), "").replace("'", "")
                    except KeyError:
                        game = ""
                if "machine:" in values:
                    try:
                        pos = values.index("machine:")
                        machine = values[pos + 1].upper().replace(chr(34), "").replace("'", "")
                    except KeyError:
                        machine = "MSX1"
                else:
                    machine = "MSX1"

                html = webmsx_snippet(game, machine) + html

        except KeyError:
            pass

        return html

    def on_post_page(self, out, **kwargs):

        # Inject jQuery in the header
        out = out.replace("</head>", "<script src='http://code.jquery.com/jquery-3.3.1.min.js' "
                          + "integrity='sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=' "
                          + "crossorigin='anonymous'></script></head>")

        return out
