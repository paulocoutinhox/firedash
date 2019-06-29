def success(message=None, data=None):
    """
    Get a web response with success, message and data
    """
    response = {'success': True}

    if message:
        response['message'] = message

    if data:
        response['data'] = data

    return response


def not_success(message=None, data=None):
    """
    Get a web response with not success, message and data
    """
    response = {'success': False}

    if message:
        response['message'] = message

    if data:
        response['data'] = data

    return response


def from_form(form):
    """
    Get a web response from WTForm
    :wtforms.Form form:
    """
    response = {
        'success': False,
        'message': 'validate',
        'data': {
            'errors': [

            ]
        }
    }

    errors = []

    for fieldName, errorMessages in form.errors.items():
        messages = []

        for errorMessage in errorMessages:
            messages.append(getattr(form, fieldName).label.text + ': ' + errorMessage)

        errors.append({'field': fieldName, 'messages': messages})

    response['data']['errors'] = errors

    return response


def with_validate_error(field, errors):
    """
    Get a web response with field and errors filled
    :string form:
    :array errors:
    """
    response = {
        'success': False,
        'message': 'validate',
        'data': {
            'errors': [

            ]
        }
    }

    response_errors = [{'field': field, 'messages': errors}]
    response['data']['errors'] = response_errors

    return response


def unauthorized():
    """
    Get a web response with unauthorized fields
    """
    return {'success': False, 'message': 'unauthorized'}, 401
