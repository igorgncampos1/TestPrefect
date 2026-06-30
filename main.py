from prefect import flow, task
from datetime import datetime

@flow(name="TestPrefect", flow_run_name=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"), log_prints=True)
def hello():
    print("Hello, Prefect!")

if __name__ == "__main__":
    hello()
