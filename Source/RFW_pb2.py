# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RFW.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RFW.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\tRFW.proto\"w\n\x0bProtoBufRFW\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x62m_type\x18\x02 \x01(\t\x12\x11\n\twl_metric\x18\x03 \x01(\t\x12\x12\n\nbatch_unit\x18\x04 \x01(\x05\x12\x10\n\x08\x62\x61tch_id\x18\x05 \x01(\x05\x12\x12\n\nbatch_size\x18\x06 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROTOBUFRFW = _descriptor.Descriptor(
  name='ProtoBufRFW',
  full_name='ProtoBufRFW',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ProtoBufRFW.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bm_type', full_name='ProtoBufRFW.bm_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wl_metric', full_name='ProtoBufRFW.wl_metric', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_unit', full_name='ProtoBufRFW.batch_unit', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_id', full_name='ProtoBufRFW.batch_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='ProtoBufRFW.batch_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['ProtoBufRFW'] = _PROTOBUFRFW

ProtoBufRFW = _reflection.GeneratedProtocolMessageType('ProtoBufRFW', (_message.Message,), dict(
  DESCRIPTOR = _PROTOBUFRFW,
  __module__ = 'RFW_pb2'
  # @@protoc_insertion_point(class_scope:ProtoBufRFW)
  ))
_sym_db.RegisterMessage(ProtoBufRFW)


# @@protoc_insertion_point(module_scope)
