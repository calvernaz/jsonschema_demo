import jsonschema

if __name__ == "__main__":
    data = {
        "actor": {
            "objectType": "Agent",
            "name": None,
            "mbox": "mailto:xapi@adlnet.gov"
        },
        "verb": {
            "id": "http://adlnet.gov/expapi/verbs/attended",
            "display": {
                "en-GB": "attended",
                "en-US": "attended"
            }
        },
        "object": {
            "objectType": "Activity",
            "id": "http://www.example.com/meetings/occurances/34534"
        }
    }

    # TODO: validate "data" against the "statement" schema"
    # jsonschema.validate(data, schema)
