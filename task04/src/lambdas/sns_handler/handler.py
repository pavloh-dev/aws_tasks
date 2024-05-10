from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda

_LOG = get_logger('SnsHandler-handler')


class SnsHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        import json


        for record in event['Records']:
            # Each record is a dictionary containing details about the message
            # The 'Sns' key in the record dictionary contains the SNS message details
            sns_message = record['Sns']['Message']
            
            # Print the SNS message to CloudWatch Logs
            print(f'SNS Message: {sns_message}')
            
        return {
            'statusCode': 200,
            'body': json.dumps('SNS Handler executed successfully!')
        }
    

HANDLER = SnsHandler()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
