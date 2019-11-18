from os.path import join, dirname
# from os import getcwd


class HTMLText:
    """
    Creates the HTML Snippet that will be injected
    """

    def __init__(self, game, machine, message, background, color, height):
        self.html = ""
        f = open(join(dirname(__file__), "partials", "./code.inc.html"), "r")
        self.html = f.read()
        f.close()

        temp = ""
        if game.endswith(".rom") \
                or game.endswith(".mx1") \
                or game.endswith(".mx2"):
            temp = "WMSX.CARTRIDGE1_URL = '/_roms/{}';".format(game)
        elif game.endswith(".dsk"):
            temp = "WMSX.DISKA_URL = '/_disks/{}';".format(game)
        elif game.endswith(".cas"):
            temp = "WMSX.TAPE_URL = '/_tapes/{}';".format(game)

        self.html = self.html.replace("{% GAME %}", temp)
        self.html = self.html.replace("{% MACHINE %}", machine)
        self.html = self.html.replace("{% MESSAGE %}", message)
        self.html = self.html.replace("{% BACKGROUND %}", background)
        self.html = self.html.replace("{% COLOR %}", color)
        self.html = self.html.replace("{% HEIGHT %}", height)

    def __str__(self):
        return self.html


def webmsx_snippet(**kwargs):
    html = HTMLText(**kwargs)

    return str(html)

