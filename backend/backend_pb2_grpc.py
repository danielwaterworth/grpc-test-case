# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from backend import backend_pb2 as backend_dot_backend__pb2


class BackendStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Upscale = channel.unary_unary(
        '/backend.Backend/Upscale',
        request_serializer=backend_dot_backend__pb2.Image.SerializeToString,
        response_deserializer=backend_dot_backend__pb2.Image.FromString,
        )


class BackendServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Upscale(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BackendServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Upscale': grpc.unary_unary_rpc_method_handler(
          servicer.Upscale,
          request_deserializer=backend_dot_backend__pb2.Image.FromString,
          response_serializer=backend_dot_backend__pb2.Image.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'backend.Backend', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))