class HTMLText:

    def __init__(self):
        self.html = ""

    def add(self, p_text):
        self.html += p_text + "\n"

    def addn(self, p_text):
        self.html += p_text

    def __str__(self):
        return self.html


def webmsx_snippet(p_game, p_system):
    html = HTMLText()

    html.add("<div id='wmsx-control'>")
    html.add("</div>")

    html.add("<a id='playmsx' href='#'>Play this game</a>")

    html.add("<script type='text/javascript'>")
    html.add("  $(document).ready(function() {")
    html.add("    WMSX.AUTO_START_DELAY = -1;")
    html.add("    WMSX.CARTRIDGE1_URL = '/_roms/{}';".format(p_game))
    html.add("    WMSX.SYSTEM = '{}';".format(p_system))
    html.add("    $('#playmsx').click(function() {")
    html.addn("      $('#wmsx-control').append('")

    html.addn("        <div id=\"wmsx\" style=\"text-align: center; margin: 20px auto 0;\" \\ >")
    html.addn("          <div id=\"wmsx-screen\" style=\"box-shadow: 2px 2px 10px rgba(0, 0, 0, .7);\" \\ >")
    html.addn("          </div> \\")
    html.addn("        </div> \\")

    # html.addn("        <script src=\"/_js/wmsx.js\"></script> \\")

    html.add("      ');")
    html.add("    });")
    html.add("  });")

    html.add("</script>")

    return str(html)
