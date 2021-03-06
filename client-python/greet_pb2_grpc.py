# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import greet_pb2 as greet__pb2


class GreetServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/github.com.sevendollar.grpc.greet.GreetService/Ping',
                request_serializer=greet__pb2.PingRequest.SerializeToString,
                response_deserializer=greet__pb2.PingResponse.FromString,
                )
        self.Hello = channel.unary_unary(
                '/github.com.sevendollar.grpc.greet.GreetService/Hello',
                request_serializer=greet__pb2.HelloRequest.SerializeToString,
                response_deserializer=greet__pb2.HelloResponse.FromString,
                )


class GreetServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Hello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=greet__pb2.PingRequest.FromString,
                    response_serializer=greet__pb2.PingResponse.SerializeToString,
            ),
            'Hello': grpc.unary_unary_rpc_method_handler(
                    servicer.Hello,
                    request_deserializer=greet__pb2.HelloRequest.FromString,
                    response_serializer=greet__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'github.com.sevendollar.grpc.greet.GreetService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.sevendollar.grpc.greet.GreetService/Ping',
            greet__pb2.PingRequest.SerializeToString,
            greet__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Hello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/github.com.sevendollar.grpc.greet.GreetService/Hello',
            greet__pb2.HelloRequest.SerializeToString,
            greet__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
