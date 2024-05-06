import json


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "apiversion": "1",
            "author": "",
            "color": "#888888",  # TODO: Choose color
            "head": "default",  # TODO: Choose head
            "tail": "default",  # TODO: Choose tail
        }),
    }


