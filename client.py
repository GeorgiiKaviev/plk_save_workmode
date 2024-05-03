import requests as r
a = r.post('http://localhost:8000/workmode', json={"place": "place", "program": "program", "data": None})
