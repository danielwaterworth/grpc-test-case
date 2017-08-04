from backend import backend_pb2
from backend import backend_pb2_grpc
from concurrent import futures
import grpc

class BackendServicer(backend_pb2_grpc.BackendServicer):
    def Upscale(self, image, context):
        return backend_pb2.Image(data=image.data)
