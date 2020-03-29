import os 
import requests
import json

url_api = os.environ.get('API_URL') or "http://localhost:5555/api/v1/"

def api_authentication(basic_auth,expiration):
    url = url_api + "authentication/tokens/" + expiration
    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + basic_auth
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    result = json.loads(response.text)
    token = result['token']
    return token

#API_USER
def api_get_users(token):
    url = url_api + "users"

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result

#API_CUSTOMER
def check_customer(token,user_name,password):
    url = url_api + "customers/" + user_name + "/" + password.decode('utf-8')

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']


def api_get_customer(token,id):
    url = url_api + "customers/" + str(id)

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']


def api_get_list_customer(token):
    url = url_api + "customers"

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']

def api_create_customer(token,name,email,address,phone,username,password):
    url = url_api + "customers"

    payload = {
        "name":name,
        "email":email,
        "address":address,
        "phone":phone,
        "username":username,
        "password":password
    }
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("POST", url, headers=headers, json = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['status']

#API_PRODUCT
def api_get_list_category(token):
    url = url_api + "products/categories"

    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()
    return result['result']
def api_get_category(token,id):
    url = url_api + "products/categories/" + str(id)
    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    result = response.json()
    return result['result']


def api_get_list_products(token):
    url = url_api + "products"

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']

def api_get_product(token,id):
    url = url_api + "products/" + str(id)

    payload  = {}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    result = json.loads(response.text.encode("utf-8"))
    return result['result']


def api_create_product(token,product_name,product_category,price,stock_price,quantity, description):
    url = url_api + "products"

    payload = {"product_name":product_name,
        "product_category":product_category,
        "price":price,
        "stock_price":stock_price,
        "quantity":quantity,
        "description":description}
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
    }

    response = requests.request("POST", url, headers=headers, json = payload)
    result = response.json()
    
    return result['status']

#API_ORDER
#API_ORDER'S DETAIL