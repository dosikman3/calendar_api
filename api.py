import logic
import model
from flask import Flask
from flask import request


app = Flask(__name__)

_calendar_logic = logic.CalendarLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_calendar: str) -> model.Calendar:
    parts = raw_calendar.split('|')
    if len(parts) == 3:
        calendar = model.Calendar()
        calendar.id = None
        calendar.date = str(parts[0])
        calendar.title = str(parts[1])
        calendar.text = str(parts[2])
        return calendar
    elif len(parts) == 4:
        calendar = model.Calendar()
        calendar.id = str(parts[0])
        calendar.date = str(parts[1])
        calendar.title = str(parts[2])
        calendar.text = str(parts[3])
        return calendar
    else:
        raise ApiException(f"Invalid RAW calendar data {raw_calendar}")


def _to_raw(calendar: model.Calendar) -> str:
    if calendar.id is None:
        return f"{calendar.date}|{calendar.title}|{calendar.text}"
    else:
        return f"{calendar.id}|{calendar.date}|{calendar.title}|{calendar.text}"


API_ROOT = "/api/v1"

CALENDAR_API_ROOT = API_ROOT + "/calendar"


@app.route(CALENDAR_API_ROOT + "/", methods=["POST"])
def create():
    try:
        data = str(request.get_data())
        calendar = _from_raw(data)
        _id = _calendar_logic.create(calendar)
        return f"new id: {_id}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/", methods=["GET"])
def list():
    try:
        calendars = _calendar_logic.list()
        raw_calendars = ""
        for calendar in calendars:
            raw_calendars += _to_raw(calendar) + '\n'
        return raw_calendars, 200
    except Exception as ex:
        return f"dailed to LIST with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        calendar = _calendar_logic.read(_id)
        raw_calendar = _to_raw(calendar)
        return raw_calendar, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        data = str(request.get_data())
        calendar = _from_raw(data)
        _calendar_logic.update(_id, calendar)
        return "update", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _calendar_logic.delete(_id)
        return "delete", 200
    except Exception as ex:
        return f"failed ro DELETE with: {ex}", 404
