from flask import Flask
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client.core import CollectorRegistry

ServerB = Flask(__name__)

# Creazione di un registro di metriche Prometheus
registry = CollectorRegistry()

# Creazione di metriche personalizzate
http_requests_total = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint"], registry=registry)
http_request_latency_seconds = Histogram("http_request_latency_seconds", "HTTP request latency", ["method", "endpoint"], registry=registry)

# Definizione di una rotta per esporre le metriche di Prometheus
@ServerB.route("/metrics")
def metrics():
    return generate_latest(registry), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@ServerB.route("/")
def getData():
    # Registrazione di una richiesta HTTP
    http_requests_total.labels(method="GET", endpoint="/").inc()

    # Misurazione della latenza di una richiesta HTTP
    with http_request_latency_seconds.labels(method="GET", endpoint="/").time():
        # Codice per gestire la richiesta
        print("Gestisco la richiesta")

    return "Gestisco la richiesta dal server B"

if __name__ == "__main__":
    ServerB.run(debug=True,
            host='0.0.0.0',
            port=9001)
    
