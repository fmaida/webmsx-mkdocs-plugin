from mkdocs import config, utils
from mkdocs.plugins import BasePlugin
from .snippet import webmsx_snippet


class WebMSXPlugin(BasePlugin):
    """
    This class is derived from mkdocs.plugins.BasePlugin
    """

    config_scheme = (
        ('path', config.config_options.Type(
            utils.string_types, default='/msx')),
        ('message', config.config_options.Type(
            utils.string_types, default='Play this game online')),
        ('loadingmessage', config.config_options.Type(
            utils.string_types, default='( Hold on.. )')),
        ('color', config.config_options.Type(
            utils.string_types, default="#aaa")),
        ('backgroundcolor', config.config_options.Type(
            utils.string_types, default="#333")),
        ("height", config.config_options.Type(int, default=64)),
    )
    
    def __init__(self, **kwargs):
        super().__init__()
    
    def on_config(self, config):
        return config

    def on_page_content(self, html, page, **kwargs):
        """
        This will be invoked each time a page has just 
        finished rendering from markdown to HTML

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
                    game = game_data["game"]
                    game = game.replace(chr(34), "")
                    game = game.replace(chr(39), "")
                    self.config["game"] = game
                if "machine" in game_data:
                    machine = game_data["machine"].upper()
                    machine = machine.replace(chr(34), "")
                    machine = machine.replace(chr(39), "")
                    self.config["machine"] = machine
                
                # breakpoint()
                html = webmsx_snippet(self.config) + html

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
