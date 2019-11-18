from mkdocs.plugins import BasePlugin
from .snippet import webmsx_snippet


class WebMSXPlugin(BasePlugin):
    """
    This class is derived from mkdocs.plugins.BasePlugin
    """

    def on_page_content(self, html, page, **kwargs):
        """
        This will be invoked each time a page has just finished rendering from markdown to HTML

        Args:
            html: the HTML code
            page:

        Returns:
            the HTML code, eventually modified
        """

        # Search for {% msx "title.rom" %}

        # markdown = re.sub(r"\{\%(\s)*msx(.*?)\%\}",
        #                   webmsx_snippet(),
        #                   markdown,
        #                   flags=re.IGNORECASE)

        try:
            game_data = page.meta.get("MSX") or page.meta.get("msx")
            # breakpoint()
            if game_data:
                game = ""
                machine = "MSX1"
                if "game" in game_data:
                    game = game_data["game"].replace(chr(34), "").replace(chr(39), "")
                if "machine" in game_data:
                    machine = game_data["machine"].upper().replace(chr(34), "").replace(chr(39), "")

                # breakpoint()
                html = webmsx_snippet(game=game, machine=machine) + html

        except KeyError:
            pass

        return html

    def on_post_page(self, out, **kwargs):
        """
        This will be invoked each time the page in HTML format
        is ready to be sent to jinja2

        Args:
            out: output-formatted HTML code
            **kwargs:

        Returns:
            output-formatted HTML code, eventually modified
        """

        # Inject jQuery in the header
        out = out.replace("</head>", "<script src='http://code.jquery.com/jquery-3.3.1.min.js' "
                          + "integrity='sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=' "
                          + "crossorigin='anonymous'></script></head>")

        return out
