from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from prometheus_client.exposition import basic_auth_handler
from prometheus_client import start_http_server, core


'''
def my_auth_handler(url, method, timeout, headers, data):
    username = 'dell'
    password = 'dell123'
    return basic_auth_handler(url, method, timeout, headers, data, username, password)
'''

registry = CollectorRegistry()

print dir(registry)

start_http_server(82)

g = Gauge('job_last_success_unixtime', 'Last time a batch job successfully finished', registry=registry)


while True:
        g.set_to_current_time()

        print registry.__dict__


        push_to_gateway('<push_gateway_ip>:9091', job='batchA', registry=registry)
