from kafka import KafkaConsumer
from const import *
from concurrent import futures
import threading
import datetime

import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc

history = []

class TemperatureServer(TemperatureService_pb2_grpc.TemperatureServiceServicer):

    def GetLatest(self, request, context):
        if len(history) == 0:
            return TemperatureService_pb2.TemperatureReply(average=0.0, timestamp='No data yet')
        last = history[-1]
        return TemperatureService_pb2.TemperatureReply(average=last['average'], timestamp=last['timestamp'])

    def GetHistory(self, request, context):
        result = TemperatureService_pb2.TemperatureList()
        for entry in history:
            result.entries.append(TemperatureService_pb2.TemperatureReply(average=entry['average'], timestamp=entry['timestamp']))
        return result

def consume():
    consumer = KafkaConsumer(bootstrap_servers=[BROKER_ADDR + ':' + BROKER_PORT])
    consumer.subscribe(['topic-average'])

    print('Listening on topic-average...')

    for msg in consumer:
        average = float(msg.value.decode())
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        history.append({'average': average, 'timestamp': timestamp})
        print('Stored average: ' + str(average) + ' at ' + timestamp)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    TemperatureService_pb2_grpc.add_TemperatureServiceServicer_to_server(TemperatureServer(), server)
    server.add_insecure_port(GRPC_HOST + ':' + GRPC_PORT)
    server.start()
    print('gRPC server started on port ' + GRPC_PORT)
    server.wait_for_termination()

if __name__ == '__main__':
    t = threading.Thread(target=consume)
    t.daemon = True
    t.start()
    serve()
