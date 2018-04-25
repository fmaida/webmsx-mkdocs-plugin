def webmsx_snippet(p_game, p_system):
    temp = ""

    temp += "<script type=\"text/javascript\">"
    # temp += "console.log(\"Ciao a tutti belli e brutti.\");"
    temp += "WMSX.CARTRIDGE1_URL = \"/_roms/{}\";".format(p_game)
    temp += "WMSX.SYSTEM = \"{}\";".format(p_system)
    temp += "</script>"

    temp += "<div id=\"wmsx-control\">"
    temp += "<div id=\"wmsx\" style=\"text-align: center; margin: 20px auto 0;\">"
    temp += "<div id=\"wmsx-screen\" style=\"box-shadow: 2px 2px 10px rgba(0, 0, 0, .7);\">"
    temp += "</div>"
    temp += "</div>"
    temp += "</div>"

    # temp += "<script src=\"/_js/wmsx.js\"></script>"

    return temp
