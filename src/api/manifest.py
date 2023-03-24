from main import app
import os
import json

@app.get('/v1/manifest')
def get_manifest():
    try:
        with open(os.environ['MANIFEST_FILE_PATH']) as manifest_file:
            manifest = json.load(manifest_file)
            return manifest
    except IOError as err:
        return 500, {'status': 'error', 'reason': err}
