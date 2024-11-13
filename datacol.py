from prometheus_api_client import PrometheusConnect
import datetime
import pandas as pd

prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)

metric_query = "container_cpu_usage_seconds_total"  
start_time = datetime.datetime(2024, 11, 3)  
end_time = datetime.datetime(2024, 11, 4)   
step = "300s"  

metric_data = prom.custom_query_range(
    query=metric_query,
    start_time=start_time,
    end_time=end_time,
    step=step
)

rows = []
for result in metric_data:
    metric = result["metric"]
    for value in result["values"]:
        timestamp = datetime.datetime.fromtimestamp(float(value[0]))
        rows.append({
            "timestamp": timestamp,
            **metric,
            "value": float(value[1])
        })

df = pd.DataFrame(rows)
df.to_csv("prometheus_metrics.csv", index=False)

print("CSV imported")