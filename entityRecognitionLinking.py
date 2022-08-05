# Takes entity/relation as input and links it to DBpedia.
# Need to add additional code to rank the DBpedia results based on context and choose the best matching entity.


import requests
import json


class EntityRecognitionLinking:

    class APIError(Exception):

        def __init__(self, status):
            self.status = status

        def __str__(self):
            return "APIError: status={}".format(self.status)

    def entityRecogLink(self, text):

        # Base URL for Spotlight API
        base_url = "http://api.dbpedia-spotlight.org/en/annotate"
        # Parameters
        # 'text' - text to be annotated
        # 'confidence' -   confidence score for linking
        params = {"text": text, "confidence": 0.1}
        # Response content type
        #headers = {'accept': 'text/html'}
        headers = {'accept': 'application/json'}
        # GET Request
        res = requests.get(base_url, params=params, headers=headers)
        if res.status_code != 200:
            # Something went wrong
            raise APIError(res.status_code)
        print(json.dumps(json.loads(res.text), sort_keys=True, indent=4))
        return json.loads(res.text)
