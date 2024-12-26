import sys
import traceback

from flask import jsonify, make_response, render_template
from client import app

from server import glossary



app.route('/get', methods=['GET'])
def get_glossary():
    try:
        render_template(
            "index.html",
            data = glossary
        )
    except:
        tb = sys.exc_info()[2]
        handler_name = traceback.format_tb(tb)[0]
        app.logger.exception(handler_name)
        return render_template("index.html")