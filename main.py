import json
from topia.termextract import extract

from flask import Flask, Response, request

extractor = extract.TermExtractor()
# extractor.filter = extract.permissiveFilter

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def tag():
    payload = (request.json or {}).get('text') or request.args.get('text')
    return Response(json.dumps(get_tags(payload)), 200)


def get_tags(text):
    return extractor(text)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
