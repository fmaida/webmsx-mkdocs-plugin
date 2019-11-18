from mkdocs.plugins import BasePlugin
from .snippet import webmsx_snippet


class WebMSXPlugin(BasePlugin):
    """
    This class is derived from mkdocs.plugins.BasePlugin
    """
    def __init__(self, **kwargs):
        super().__init__()
        self.message = "Play this game online"
        self.background = "#333"
        self.color = "#aaa"
        self.height = 64

    def on_pre_build(self, config):
        if self.config.get("message"):
            self.message = self.config["message"]
        if self.config.get("background-color"):
            self.background = self.config["background-color"]
        if self.config.get("color"):
            self.color = self.config["color"]
        if self.config.get("height"):
            self.height = self.config["height"]

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
            if game_data:
                game = ""
                machine = "MSX1"
                if "game" in game_data:
                    game = game_data["game"].replace(chr(34), "").replace(chr(39), "")
                if "machine" in game_data:
                    machine = game_data["machine"].upper().replace(chr(34), "").replace(chr(39), "")

                # breakpoint()
                html = webmsx_snippet(game=game, machine=machine,
                                      message=self.message,
                                      background=self.background,
                                      color=self.color,
                                      height=self.height) + html

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
        jquery = "https://code.jquery.com/jquery-3.4.1.min.js"
        out = out.replace("</head>", 
                "<script src=\"{}\">".format(jquery) 
                + "</script></head>")

        return out
