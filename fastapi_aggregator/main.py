from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def aggregate_data():
    data_from_ip1 = {"data": "from IP 1"}
    data_from_ip2 = {"data": "from IP 2"}
    data_from_ip3 = {"data": "from IP 3"}

    aggregated_data = {
        "ip1": data_from_ip1,
        "ip2": data_from_ip2,
        "ip3": data_from_ip3
    }
    
    return aggregated_data
