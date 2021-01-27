"""This module just provide data for data flow testing."""

import json
from sys import version_info
from typing import Optional
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse

from fastapi import FastAPI, Query
from fastapi import __version__


app = FastAPI()
version = f"{version_info.major}.{version_info.minor}"

@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message, "fastApi_version": __version__}


def read_json_mockdata():
    data = {}
    with open('mockdata/aviationstack_realtime_fligth.json') as json_file:
        data = json.load(json_file)
    return data

@app.get("/v1/flights", response_class=JSONResponse)
async def avistionstack(access_key: str = Query(None, title="Access Key of AviationStak"),
     limit: int = 100, flight_status: Optional[str] = Query("",
     title=" Filter your results by flight status. Available values: scheduled, active, landed, cancelled, incident, diverted")):
    results = {'access_key': access_key, "limit": limit, "flight_status": flight_status}
    results.update( read_json_mockdata())
    results['data'] = results['data'][:limit]
    return results
