import requests
import json

def api():
    pet_id = str(input('\nВведите ID питомца: '))
    response = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
    resp = response.text
    data = json.loads(resp)
    print("\n")
    for key, value in data.items():
        print(f'{key}: {value}')
    print("\n")
    print((json.dumps(data, indent=2, ensure_ascii=False)))

api()
