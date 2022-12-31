import requests

# params = {
#         "id":1
# }

# Get method with single data
id = 1

responseget = requests.get('http://127.0.0.1:8000/product/' + f'{id}')
print(responseget.url)

res_json = responseget.json()
print(res_json)

# Get method with Multiple data

responsegetmultiple = requests.get('http://127.0.0.1:8000/products/')
print(responsegetmultiple.url)

res_jsonmul = responsegetmultiple.json()
print(res_jsonmul)


# Post request call 

payloads = {
        'name':'Table',
        'original_price':1500
}

responsepost = requests.post('http://127.0.0.1:8000/products/',data=payloads)
print(responsepost.url)

res_jsonpost = responsepost.json()
print(res_jsonpost)

# print(responsepost.text)


# responsestcode = requests.get('https://httpbin.org/status/200')
# print(responsestcode.text)

