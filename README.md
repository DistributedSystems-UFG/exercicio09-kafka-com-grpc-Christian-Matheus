[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/A6uVSc3Y)

# Exercício 09 — Kafka + gRPC

## 1) Install PIP

$:> sudo apt install python3-pip

## 2) Upgrade PIP

$:> python3 -m pip install --upgrade pip

## 3) Install Kafka client

$:> python3 -m pip install kafka-python

## 4) Install gRPC runtime

$:> python3 -m pip install grpcio

## 5) Install gRPC tools

$:> python3 -m pip install grpcio-tools

## 6) Clone this repo

## 7) Compile interface specification (Protocol Buffers .proto file)

$:> cd python

$:> python3 -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/TemperatureService.proto

## 8) Run the example (using four different machines)

### Machine 1 — Temperature sensor (producer):

$:> python3 producer.py

### Machine 2 — Average calculator (consumer/producer):

$:> python3 consumer_producer.py

### Machine 3 — Storage + gRPC server (consumer/web service):

$:> python3 consumer_service.py

### Machine 4 — gRPC client:

$:> python3 client.py

### Note: open ports 9092 (Kafka) and 50051 (gRPC) on the firewall at EC2 (security group)
