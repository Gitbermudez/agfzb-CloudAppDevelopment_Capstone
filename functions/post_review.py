import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def main(dict):
    authenticator = IAMAuthenticator("IygMQ7rjuOiKDjgLijuXb-HXE2kE8ATeqh6KqZxJ3zFA")
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("https://5a0c237f-53dc-42b7-a8f5-fc814248c94a-bluemix.cloudantnosqldb.appdomain.cloud")
    response = service.post_document(db='reviews', document={'review': dict['review']}).get_result()
    try:
        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return result
    except:
        return {
        'statusCode': 404,
        'message': 'Something went wrong'
        }