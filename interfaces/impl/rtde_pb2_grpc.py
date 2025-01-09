# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import common_msgs_pb2 as common__msgs__pb2
import rtde_msgs_pb2 as rtde__msgs__pb2


class RTDataExchangeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMotionData = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetMotionData',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.MotionData.FromString,
                )
        self.GetControlData = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetControlData',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.ControlData.FromString,
                )
        self.GetControlState = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetControlState',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.ControlData2.FromString,
                )
        self.GetIOData = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetIOData',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.IOData.FromString,
                )
        self.GetServoData = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetServoData',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.ServoData.FromString,
                )
        self.GetViolationData = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetViolationData',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.ViolationData.FromString,
                )
        self.GetViolationMessageQueue = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetViolationMessageQueue',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.ViolationMessageQueue.FromString,
                )
        self.GetProgramData = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetProgramData',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.ProgramData.FromString,
                )
        self.GetStopState = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/GetStopState',
                request_serializer=common__msgs__pb2.Empty.SerializeToString,
                response_deserializer=rtde__msgs__pb2.StopState.FromString,
                )
        self.TestFunction = channel.unary_unary(
                '/Nrmk.IndyFramework.RTDataExchange/TestFunction',
                request_serializer=rtde__msgs__pb2.TestRequest.SerializeToString,
                response_deserializer=rtde__msgs__pb2.TestResponse.FromString,
                )


class RTDataExchangeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetMotionData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetControlData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetControlState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIOData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServoData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetViolationData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetViolationMessageQueue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProgramData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStopState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestFunction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RTDataExchangeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMotionData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMotionData,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.MotionData.SerializeToString,
            ),
            'GetControlData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetControlData,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.ControlData.SerializeToString,
            ),
            'GetControlState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetControlState,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.ControlData2.SerializeToString,
            ),
            'GetIOData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIOData,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.IOData.SerializeToString,
            ),
            'GetServoData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServoData,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.ServoData.SerializeToString,
            ),
            'GetViolationData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetViolationData,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.ViolationData.SerializeToString,
            ),
            'GetViolationMessageQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.GetViolationMessageQueue,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.ViolationMessageQueue.SerializeToString,
            ),
            'GetProgramData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProgramData,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.ProgramData.SerializeToString,
            ),
            'GetStopState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStopState,
                    request_deserializer=common__msgs__pb2.Empty.FromString,
                    response_serializer=rtde__msgs__pb2.StopState.SerializeToString,
            ),
            'TestFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.TestFunction,
                    request_deserializer=rtde__msgs__pb2.TestRequest.FromString,
                    response_serializer=rtde__msgs__pb2.TestResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Nrmk.IndyFramework.RTDataExchange', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RTDataExchange(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetMotionData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetMotionData',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.MotionData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetControlData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetControlData',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.ControlData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetControlState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetControlState',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.ControlData2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIOData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetIOData',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.IOData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServoData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetServoData',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.ServoData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetViolationData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetViolationData',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.ViolationData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetViolationMessageQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetViolationMessageQueue',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.ViolationMessageQueue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProgramData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetProgramData',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.ProgramData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStopState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/GetStopState',
            common__msgs__pb2.Empty.SerializeToString,
            rtde__msgs__pb2.StopState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Nrmk.IndyFramework.RTDataExchange/TestFunction',
            rtde__msgs__pb2.TestRequest.SerializeToString,
            rtde__msgs__pb2.TestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
