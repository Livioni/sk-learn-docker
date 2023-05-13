import requests

def invoke(url, method, data=None, headers=None):
    if method == 'GET':
        return requests.get(url, headers=headers)
    elif method == 'POST':
        return requests.post(url, data=data, headers=headers)
    elif method == 'PUT':
        return requests.put(url, data=data, headers=headers)
    elif method == 'DELETE':
        return requests.delete(url, headers=headers)
    else:
        raise Exception('Unsupported method: {}'.format(method))
    
if __name__ == "__main__":
    url = 'http://127.0.0.1:8010'
    method = 'GET'
    response = invoke(url, method)
    print(response.text)




