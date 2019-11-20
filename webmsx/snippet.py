from os.path import join, dirname
import jinja2
# from os import getcwd


class HTMLText:
    """
    Creates the HTML Snippet that will be injected
    """

    def __init__(self, config):
        file_path = join(dirname(__file__), "partials")
        templateLoader = jinja2.FileSystemLoader(searchpath=file_path)
        templateEnv = jinja2.Environment(loader=templateLoader)
        template = templateEnv.get_template("code.inc.html")
        temp = ""
        game = config["game"]
        if game.endswith(".rom") \
                or game.endswith(".mx1") \
                or game.endswith(".mx2"):
            temp = "WMSX.CARTRIDGE1_URL = '{}/roms/{}';".format(
                    config["path"], game)
        elif game.endswith(".dsk"):
            temp = "WMSX.DISKA_URL = '{}/disks/{}';".format(
                    config["path"], game)
        elif game.endswith(".cas"):
            temp = "WMSX.TAPE_URL = '{}/tapes/{}';".format(
                    config["path"], game)
        
        config["game"] = temp
        self.html = template.render(**config)

    def __str__(self):
        return self.html


def webmsx_snippet(config):
    html = HTMLText(config)
    return str(html)

