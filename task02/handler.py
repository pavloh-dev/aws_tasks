from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json 

_LOG = get_logger('HelloWorld-handler')


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        response = {
            "statusCode": 200,
            "body": json.dumps({"statusCode": 200, "message": "Hello from Lambda!"}),
            "headers": {
                "Content-Type": "application/json"
            }
        }
        return response
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
