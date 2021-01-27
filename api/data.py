import json
def read_json_mockdata():
    data = {}
    with open('test/aviationstack_realtime_fligth.json') as json_file:
        data = json.load(json_file)
    return data