#!/usr/bin/python3

import requests
from dotenv import dotenv_values


def get_json(word):
    url = "https://dictionaryapi.com/api/v3/references/collegiate/json/{0}?key={1}".format(word.lower(),
                                                                                           dotenv_values()["API_KEY"])
    result = requests.get(url)
    if result.status_code == 200:
        data = result.json()
        datastr = "{0} ({1}): {2}".format(data["hwi"]["hw"], data["fl"], data["def"]["sseq"]["dt"]["text"])
        print(datastr)
    else:
        print("We got an error, code {}".format(result.status_code))


get_json(input("Enter a word: "))
