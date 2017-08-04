from backend import backend_pb2
from backend import backend_pb2_grpc
from backend.server import BackendServicer
from concurrent import futures
import grpc
import time
import threading

def background():
    while True:
        time.sleep(1)

threading.Thread(target=background).start()

print("starting server")
server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
backend_pb2_grpc.add_BackendServicer_to_server(
    BackendServicer(),
    server
)
server.add_insecure_port('[::]:50051')
server.start()
