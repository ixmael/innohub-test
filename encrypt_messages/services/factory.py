from .restapi_service import RestAPIService

def get_service(service_name):
    services_allowed = ['restapi']

    if service_name in services_allowed:
        elif service_name == 'restapi':
            return RestAPIService()
    else:
        raise Exception('The service "{}" is not allowed.'.format(service_name))
