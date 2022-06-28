import os
from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = "s3cr3t"
app.debug = False
app._static_folder = os.path.abspath("templates/static/")


@app.route("/", methods=["GET"])
def index():
    """
        Creates the index page with all of its attributes.

        Parameters
        ----------
        title : title of the image

        Returns
        -------
        The index page rendered
    """
    # Creates the input image
    #title = "Create the input image"
    return render_template("/layouts/[NRC_6275]_LeopoldoCastro_Lab1Unidad2.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)