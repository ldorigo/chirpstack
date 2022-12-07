"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import google.protobuf.empty_pb2
import grpc

from .gateway_pb2 import *
# GatewayService is the service providing API methods for managing gateways.
class GatewayServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # Create creates the given gateway.
    Create:grpc.UnaryUnaryMultiCallable[
        global___CreateGatewayRequest,
        google.protobuf.empty_pb2.Empty] = ...

    # Get returns the gateway for the given Gateway ID.
    Get:grpc.UnaryUnaryMultiCallable[
        global___GetGatewayRequest,
        global___GetGatewayResponse] = ...

    # Update updates the given gateway.
    Update:grpc.UnaryUnaryMultiCallable[
        global___UpdateGatewayRequest,
        google.protobuf.empty_pb2.Empty] = ...

    # Delete deletes the gateway matching the given Gateway ID.
    Delete:grpc.UnaryUnaryMultiCallable[
        global___DeleteGatewayRequest,
        google.protobuf.empty_pb2.Empty] = ...

    # Get the list of gateways.
    List:grpc.UnaryUnaryMultiCallable[
        global___ListGatewaysRequest,
        global___ListGatewaysResponse] = ...

    # Generate client-certificate for the gateway.
    GenerateClientCertificate:grpc.UnaryUnaryMultiCallable[
        global___GenerateGatewayClientCertificateRequest,
        global___GenerateGatewayClientCertificateResponse] = ...

    # GetMetrics returns the gateway metrics.
    GetMetrics:grpc.UnaryUnaryMultiCallable[
        global___GetGatewayMetricsRequest,
        global___GetGatewayMetricsResponse] = ...


# GatewayService is the service providing API methods for managing gateways.
class GatewayServiceServicer(metaclass=abc.ABCMeta):
    # Create creates the given gateway.
    @abc.abstractmethod
    def Create(self,
        request: global___CreateGatewayRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...

    # Get returns the gateway for the given Gateway ID.
    @abc.abstractmethod
    def Get(self,
        request: global___GetGatewayRequest,
        context: grpc.ServicerContext,
    ) -> global___GetGatewayResponse: ...

    # Update updates the given gateway.
    @abc.abstractmethod
    def Update(self,
        request: global___UpdateGatewayRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...

    # Delete deletes the gateway matching the given Gateway ID.
    @abc.abstractmethod
    def Delete(self,
        request: global___DeleteGatewayRequest,
        context: grpc.ServicerContext,
    ) -> google.protobuf.empty_pb2.Empty: ...

    # Get the list of gateways.
    @abc.abstractmethod
    def List(self,
        request: global___ListGatewaysRequest,
        context: grpc.ServicerContext,
    ) -> global___ListGatewaysResponse: ...

    # Generate client-certificate for the gateway.
    @abc.abstractmethod
    def GenerateClientCertificate(self,
        request: global___GenerateGatewayClientCertificateRequest,
        context: grpc.ServicerContext,
    ) -> global___GenerateGatewayClientCertificateResponse: ...

    # GetMetrics returns the gateway metrics.
    @abc.abstractmethod
    def GetMetrics(self,
        request: global___GetGatewayMetricsRequest,
        context: grpc.ServicerContext,
    ) -> global___GetGatewayMetricsResponse: ...


def add_GatewayServiceServicer_to_server(servicer: GatewayServiceServicer, server: grpc.Server) -> None: ...