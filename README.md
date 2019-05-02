# ValueCrossingEvents
A DRF project to return the sum of value crossing events in an array of real numbers. 


### Prerequisites

Create a virtual environment and activate it

```
python3 -m venv env
```

```
source env/bin/activate
```

### Installing Requirements

Make sure you are in the main directory. Install the requirements.txt using pip install.

```
pip install -r requirements.txt
```
### Create a superuser

You will need a superuser account for administration purposes.

```
python manage.py createsuperuser
```

### Run the server & login


```
python manage.py runserver
```

## API Access
Have used TDD approach so some use cases for the API are listed in tests.py
Go to the following URL.
```
http://127.0.0.1/api/
```
This is a post request which takes in the following data
```
Sample Request:
        headers = { 'Authorization': 'Token {}'.format(token),
                    'Content-Type': 'application/json; charset=utf-8'
                  }
        data = {"signal":[1,2,3,3,3,7,8,5,4,3,7,2], "value":3}
        resp = requests.post('http://localhost:8000/api/',data=json.dumps(data), headers=headers)
        print(resp.status_code, resp.text)
```

I have used Content Headers to provide authorisation token for authentication, 
the use case for generating the token using DRF is also listed in tests.py
```
Response Obtained
{"sum_value_crossing_events":2}

```
Tornado App for Asynchronous Networking
Have added tornado webapp for asynchronous networking for scalability.
Need to start it using python tornadoapp.py
```
Request is 

http://localhost:8888/?value=3&signal=1,2,3,3,3,7,8,5,4,3,7,2

Response Obtained
{"sum_value_crossing_events":2}
```


##  Notes

I have used Django Rest Framwork creating the API and have used Token Based Authrntication.
Django Rest provides a Powerful serialization engine compatible with both ORM and non-ORM data sources.
Apache benchmark can be used for load testing of the API. Throttling has also been applied to API and 
can be seen in settings.py
```
Tornado App
ab -n 500 -c 10 "http://localhost:8888/?value=4&signal=3,4,5,1,6,4,4,6,2,4,4,6
Time per request:       4.002 [ms] (mean)
Time per request:       0.400 [ms] (mean, across all concurrent requests)

Djago Restframe
Time per request:       3.248 [ms] (mean)
Time per request:       0.949 [ms] (mean, across all concurrent requests)
```
