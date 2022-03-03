import xml.etree.ElementTree as ET

from flask import Flask, jsonify, request


tree = ET.parse('sample/marines.cat')
root = tree.getroot()


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    items = []
    for child in root:
        items.append((child.tag, child.attrib))
    return str(items)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)