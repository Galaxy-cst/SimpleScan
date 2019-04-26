import os
from os.path import join
import json

basefilepath = os.path.dirname(__file__)
payloads_path = join(basefilepath, 'Payloads')


def payloads_iter():
    payloads = os.listdir(payloads_path)
    for payload in payloads:
        if payload.endswith('.json'):
            with open(join(payloads_path, payload)) as f:
                try:
                    payload_obj = json.load(f)
                    if payload_obj['name'] is None:
                        raise Exception("Not a Payload!")
                except:
                    pass
                else:
                    yield payload_obj
