import grpc
import TemperatureService_pb2
import TemperatureService_pb2_grpc
from const import *

with grpc.insecure_channel(GRPC_HOST + ':' + GRPC_PORT) as channel:
    stub = TemperatureService_pb2_grpc.TemperatureServiceStub(channel)

    response = stub.GetLatest(TemperatureService_pb2.EmptyMessage())
    print('Latest average: ' + str(response.average) + ' at ' + response.timestamp)

    response = stub.GetHistory(TemperatureService_pb2.EmptyMessage())
    print('History:')
    for entry in response.entries:
        print('  ' + str(entry.average) + ' at ' + entry.timestamp)
