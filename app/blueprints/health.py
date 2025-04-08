from . import healthpage

@healthpage.route("/")
def health():
    return "all right i guess?"