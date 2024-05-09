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
        
        return {'statusCode': 200, 'message': 'Hello from Lambda'}

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return {'statusCode': 200, 'message': 'Hello from Lambda'}
