from os.path import join, dirname
# from os import getcwd


class HTMLText:

    def __init__(self, p_game, p_machine):
        self.html = ""
        f = open(join(dirname(__file__), "partials", "./code.inc.html"), "r")
        self.html = f.read()
        self.html = self.html.replace("{% GAME %}", p_game)
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

