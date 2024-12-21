from prometheus_api_client import PrometheusConnect
import datetime
import pandas as pd

prom = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)

metric_query = "container_cpu_usage_seconds_total"  # PromQL query
start_time = datetime.datetime(2024, 11, 3)    # start of time-period to scrape metrics from
end_time = datetime.datetime(2024, 11, 4)    # end of time-period
step = "300s"    # timestep between scraped metrics (minimum 10s)

# Execute the query
metric_data = prom.custom_query_range(
    query=metric_query,
    start_time=start_time,
    end_time=end_time,
    step=step
)

# Convert scraped metrics into a data frame
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

# Filer results for vulnerable program container ID
container_ID_regex = "2f1a5"    # container ID is found in Docker desktop app
df = df[df["id"].str.contains(container_ID_regex)]

# Export scraped metrics to CSV
df.to_csv("prometheus_metrics.csv", index=False)

print("CSV imported")
