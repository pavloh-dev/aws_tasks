from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('SqsHandler-handler')


class SqsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        import json

        for record in event['Records']:
            message_body = record['body']

            print(f'SQS Message Body: {message_body}')

        return {
            'statusCode': 200,
            'body': json.dumps('SQS Handler executed successfully!')
        }
    

HANDLER = SqsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
