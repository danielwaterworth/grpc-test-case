import backend
from backend import backend_pb2
from backend import backend_pb2_grpc
import grpc

channel = grpc.insecure_channel('localhost:50051')
stub = backend_pb2_grpc.BackendStub(channel)

def upscale(data):
    return stub.Upscale(backend_pb2.Image(data=data)).data

if __name__ == '__main__':
    upscale(b'foo')
