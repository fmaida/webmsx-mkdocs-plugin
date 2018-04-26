from os.path import join, dirname
# from os import getcwd


class HTMLText:

    def __init__(self, p_game, p_machine):
        self.html = ""
        f = open(join(dirname(__file__), "partials", "./code.inc.html"), "r")
        self.html = f.read()
        if p_game.endswith(".rom") \
                or p_game.endswith(".mx1") \
                or p_game.endswith(".mx2"):
            temp = "WMSX.CARTRIDGE1_URL = '/_roms/{}';".format(p_game)
        elif p_game.endswith(".dsk"):
            temp = "WMSX.DISKA_URL = '/_disks/{}';".format(p_game)
        elif p_game.endswith(".cas"):
            temp = "WMSX.TAPE_URL = '/_tapes/{}';".format(p_game)
        self.html = self.html.replace("{% GAME %}", temp)
        self.html = self.html.replace("{% MACHINE %}", p_machine)
        f.close()

    def add(self, p_text):
        self.html += p_text + "\n"

    def adn(self, p_text):
        self.html += p_text.strip()

    def __str__(self):
        return self.html


def webmsx_snippet(p_game, p_machine):
    html = HTMLText(p_game, p_machine)

    return str(html)

