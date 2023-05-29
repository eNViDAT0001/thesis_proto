# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import recommender_pb2 as recommender__pb2


class RecommenderBaseCommentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddComment = channel.unary_unary(
                '/recommender.RecommenderBaseComment/AddComment',
                request_serializer=recommender__pb2.CommentReq.SerializeToString,
                response_deserializer=recommender__pb2.NonQueryResponse.FromString,
                )
        self.UpdateComment = channel.unary_unary(
                '/recommender.RecommenderBaseComment/UpdateComment',
                request_serializer=recommender__pb2.CommentReq.SerializeToString,
                response_deserializer=recommender__pb2.NonQueryResponse.FromString,
                )
        self.DeleteComment = channel.unary_unary(
                '/recommender.RecommenderBaseComment/DeleteComment',
                request_serializer=recommender__pb2.DeleteCommentReq.SerializeToString,
                response_deserializer=recommender__pb2.NonQueryResponse.FromString,
                )
        self.LisRecommendedProductIDsByUserID = channel.unary_unary(
                '/recommender.RecommenderBaseComment/LisRecommendedProductIDsByUserID',
                request_serializer=recommender__pb2.RecommentReq.SerializeToString,
                response_deserializer=recommender__pb2.RecommentRes.FromString,
                )


class RecommenderBaseCommentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteComment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LisRecommendedProductIDsByUserID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommenderBaseCommentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddComment': grpc.unary_unary_rpc_method_handler(
                    servicer.AddComment,
                    request_deserializer=recommender__pb2.CommentReq.FromString,
                    response_serializer=recommender__pb2.NonQueryResponse.SerializeToString,
            ),
            'UpdateComment': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateComment,
                    request_deserializer=recommender__pb2.CommentReq.FromString,
                    response_serializer=recommender__pb2.NonQueryResponse.SerializeToString,
            ),
            'DeleteComment': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteComment,
                    request_deserializer=recommender__pb2.DeleteCommentReq.FromString,
                    response_serializer=recommender__pb2.NonQueryResponse.SerializeToString,
            ),
            'LisRecommendedProductIDsByUserID': grpc.unary_unary_rpc_method_handler(
                    servicer.LisRecommendedProductIDsByUserID,
                    request_deserializer=recommender__pb2.RecommentReq.FromString,
                    response_serializer=recommender__pb2.RecommentRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'recommender.RecommenderBaseComment', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RecommenderBaseComment(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recommender.RecommenderBaseComment/AddComment',
            recommender__pb2.CommentReq.SerializeToString,
            recommender__pb2.NonQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recommender.RecommenderBaseComment/UpdateComment',
            recommender__pb2.CommentReq.SerializeToString,
            recommender__pb2.NonQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteComment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recommender.RecommenderBaseComment/DeleteComment',
            recommender__pb2.DeleteCommentReq.SerializeToString,
            recommender__pb2.NonQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LisRecommendedProductIDsByUserID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/recommender.RecommenderBaseComment/LisRecommendedProductIDsByUserID',
            recommender__pb2.RecommentReq.SerializeToString,
            recommender__pb2.RecommentRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
