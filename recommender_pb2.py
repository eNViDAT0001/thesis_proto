# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommender.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11recommender.proto\x12\x04main\"\x1f\n\x0cRecommentReq\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"\"\n\x0cRecommentRes\x12\x12\n\nproduct_id\x18\x01 \x03(\x05\"A\n\nCommentReq\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x12\n\nproduct_id\x18\x02 \x01(\x05\x12\x0e\n\x06rating\x18\x03 \x01(\x05\"7\n\x10\x44\x65leteCommentReq\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x12\n\nproduct_id\x18\x02 \x01(\x05\"#\n\x10NonQueryResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\x98\x02\n\x16RecommenderBaseComment\x12\x36\n\nAddComment\x12\x10.main.CommentReq\x1a\x16.main.NonQueryResponse\x12\x39\n\rUpdateComment\x12\x10.main.CommentReq\x1a\x16.main.NonQueryResponse\x12?\n\rDeleteComment\x12\x16.main.DeleteCommentReq\x1a\x16.main.NonQueryResponse\x12J\n LisRecommendedProductIDsByUserID\x12\x12.main.RecommentReq\x1a\x12.main.RecommentResB\x04Z\x02/.b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recommender_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\002/.'
  _RECOMMENTREQ._serialized_start=27
  _RECOMMENTREQ._serialized_end=58
  _RECOMMENTRES._serialized_start=60
  _RECOMMENTRES._serialized_end=94
  _COMMENTREQ._serialized_start=96
  _COMMENTREQ._serialized_end=161
  _DELETECOMMENTREQ._serialized_start=163
  _DELETECOMMENTREQ._serialized_end=218
  _NONQUERYRESPONSE._serialized_start=220
  _NONQUERYRESPONSE._serialized_end=255
  _RECOMMENDERBASECOMMENT._serialized_start=258
  _RECOMMENDERBASECOMMENT._serialized_end=538
# @@protoc_insertion_point(module_scope)