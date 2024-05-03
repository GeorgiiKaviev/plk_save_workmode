from model import Mode
from fastapi import FastAPI
from service import get_data, error_report

app = FastAPI()

@app.post("/workmode")
def get_work_mode(mode: Mode):
    place = mode.place
    program = mode.program
    data = mode.data
    try:
        get_data(place, program, data)
    except:
        error_report()
    return place
    
