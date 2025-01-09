# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eyetask.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='eyetask.proto',
  package='EyeTask',
  syntax='proto3',
  serialized_options=b'\n io.grpc.custom.neuromeka.EyeTaskB\014EyeTaskProtoP\001\242\002\004FDDO',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\reyetask.proto\x12\x07\x45yeTask\"(\n\x0cImageRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\"\x90\x01\n\rImageResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x0e\n\x06height\x18\x04 \x01(\x05\x12\r\n\x05\x63olor\x18\x05 \x01(\x0c\x12\r\n\x05\x64\x65pth\x18\x06 \x01(\x0c\x12\x13\n\x0b\x64\x65pth_scale\x18\x07 \x01(\x02\x12\x13\n\x0b\x65rror_state\x18\x08 \x01(\x08\"\x15\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\x05\"A\n\tClassList\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0b\x63lass_names\x18\x02 \x03(\t\x12\x13\n\x0b\x65rror_state\x18\x08 \x01(\x08\"L\n\rDetectRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ls\x18\x02 \x01(\x05\x12\x10\n\x08pose_cmd\x18\x03 \x03(\x02\x12\x10\n\x08robot_ip\x18\x04 \x01(\t\"*\n\x0fRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ls\x18\x02 \x01(\x05\"\xca\x01\n\x0e\x44\x65tectResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08\x64\x65tected\x18\x02 \x01(\x08\x12\x0e\n\x06passed\x18\x03 \x01(\x08\x12\x0b\n\x03\x63ls\x18\x04 \x01(\x05\x12\x13\n\x0btar_ee_pose\x18\x05 \x03(\x02\x12\x15\n\rtar_tool_pose\x18\x06 \x03(\x02\x12\x14\n\x0ctar_obj_pose\x18\x07 \x03(\x02\x12\x10\n\x08tool_idx\x18\x08 \x01(\x05\x12\x13\n\x0b\x65rror_state\x18\t \x01(\x08\x12\x14\n\x0c\x65rror_module\x18\n \x01(\t2\xfc\x01\n\x07\x45yeTask\x12;\n\x08GetImage\x12\x15.EyeTask.ImageRequest\x1a\x16.EyeTask.ImageResponse\"\x00\x12\x36\n\x0cGetClassList\x12\x10.EyeTask.Request\x1a\x12.EyeTask.ClassList\"\x00\x12;\n\x06\x44\x65tect\x12\x16.EyeTask.DetectRequest\x1a\x17.EyeTask.DetectResponse\"\x00\x12?\n\x08Retrieve\x12\x18.EyeTask.RetrieveRequest\x1a\x17.EyeTask.DetectResponse\"\x00\x42\x39\n io.grpc.custom.neuromeka.EyeTaskB\x0c\x45yeTaskProtoP\x01\xa2\x02\x04\x46\x44\x44Ob\x06proto3'
)




_IMAGEREQUEST = _descriptor.Descriptor(
  name='ImageRequest',
  full_name='EyeTask.ImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EyeTask.ImageRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='EyeTask.ImageRequest.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=66,
)


_IMAGERESPONSE = _descriptor.Descriptor(
  name='ImageResponse',
  full_name='EyeTask.ImageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EyeTask.ImageResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='EyeTask.ImageResponse.type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='EyeTask.ImageResponse.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='EyeTask.ImageResponse.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='EyeTask.ImageResponse.color', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depth', full_name='EyeTask.ImageResponse.depth', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='depth_scale', full_name='EyeTask.ImageResponse.depth_scale', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_state', full_name='EyeTask.ImageResponse.error_state', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=213,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='EyeTask.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EyeTask.Request.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=236,
)


_CLASSLIST = _descriptor.Descriptor(
  name='ClassList',
  full_name='EyeTask.ClassList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EyeTask.ClassList.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='class_names', full_name='EyeTask.ClassList.class_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_state', full_name='EyeTask.ClassList.error_state', index=2,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=238,
  serialized_end=303,
)


_DETECTREQUEST = _descriptor.Descriptor(
  name='DetectRequest',
  full_name='EyeTask.DetectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EyeTask.DetectRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cls', full_name='EyeTask.DetectRequest.cls', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pose_cmd', full_name='EyeTask.DetectRequest.pose_cmd', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='robot_ip', full_name='EyeTask.DetectRequest.robot_ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=305,
  serialized_end=381,
)


_RETRIEVEREQUEST = _descriptor.Descriptor(
  name='RetrieveRequest',
  full_name='EyeTask.RetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EyeTask.RetrieveRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cls', full_name='EyeTask.RetrieveRequest.cls', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=425,
)


_DETECTRESPONSE = _descriptor.Descriptor(
  name='DetectResponse',
  full_name='EyeTask.DetectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EyeTask.DetectResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detected', full_name='EyeTask.DetectResponse.detected', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='passed', full_name='EyeTask.DetectResponse.passed', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cls', full_name='EyeTask.DetectResponse.cls', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tar_ee_pose', full_name='EyeTask.DetectResponse.tar_ee_pose', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tar_tool_pose', full_name='EyeTask.DetectResponse.tar_tool_pose', index=5,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tar_obj_pose', full_name='EyeTask.DetectResponse.tar_obj_pose', index=6,
      number=7, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tool_idx', full_name='EyeTask.DetectResponse.tool_idx', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_state', full_name='EyeTask.DetectResponse.error_state', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_module', full_name='EyeTask.DetectResponse.error_module', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=630,
)

DESCRIPTOR.message_types_by_name['ImageRequest'] = _IMAGEREQUEST
DESCRIPTOR.message_types_by_name['ImageResponse'] = _IMAGERESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['ClassList'] = _CLASSLIST
DESCRIPTOR.message_types_by_name['DetectRequest'] = _DETECTREQUEST
DESCRIPTOR.message_types_by_name['RetrieveRequest'] = _RETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['DetectResponse'] = _DETECTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageRequest = _reflection.GeneratedProtocolMessageType('ImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREQUEST,
  '__module__' : 'eyetask_pb2'
  # @@protoc_insertion_point(class_scope:EyeTask.ImageRequest)
  })
_sym_db.RegisterMessage(ImageRequest)

ImageResponse = _reflection.GeneratedProtocolMessageType('ImageResponse', (_message.Message,), {
  'DESCRIPTOR' : _IMAGERESPONSE,
  '__module__' : 'eyetask_pb2'
  # @@protoc_insertion_point(class_scope:EyeTask.ImageResponse)
  })
_sym_db.RegisterMessage(ImageResponse)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'eyetask_pb2'
  # @@protoc_insertion_point(class_scope:EyeTask.Request)
  })
_sym_db.RegisterMessage(Request)

ClassList = _reflection.GeneratedProtocolMessageType('ClassList', (_message.Message,), {
  'DESCRIPTOR' : _CLASSLIST,
  '__module__' : 'eyetask_pb2'
  # @@protoc_insertion_point(class_scope:EyeTask.ClassList)
  })
_sym_db.RegisterMessage(ClassList)

DetectRequest = _reflection.GeneratedProtocolMessageType('DetectRequest', (_message.Message,), {
  'DESCRIPTOR' : _DETECTREQUEST,
  '__module__' : 'eyetask_pb2'
  # @@protoc_insertion_point(class_scope:EyeTask.DetectRequest)
  })
_sym_db.RegisterMessage(DetectRequest)

RetrieveRequest = _reflection.GeneratedProtocolMessageType('RetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEREQUEST,
  '__module__' : 'eyetask_pb2'
  # @@protoc_insertion_point(class_scope:EyeTask.RetrieveRequest)
  })
_sym_db.RegisterMessage(RetrieveRequest)

DetectResponse = _reflection.GeneratedProtocolMessageType('DetectResponse', (_message.Message,), {
  'DESCRIPTOR' : _DETECTRESPONSE,
  '__module__' : 'eyetask_pb2'
  # @@protoc_insertion_point(class_scope:EyeTask.DetectResponse)
  })
_sym_db.RegisterMessage(DetectResponse)


DESCRIPTOR._options = None

_EYETASK = _descriptor.ServiceDescriptor(
  name='EyeTask',
  full_name='EyeTask.EyeTask',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=633,
  serialized_end=885,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetImage',
    full_name='EyeTask.EyeTask.GetImage',
    index=0,
    containing_service=None,
    input_type=_IMAGEREQUEST,
    output_type=_IMAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetClassList',
    full_name='EyeTask.EyeTask.GetClassList',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_CLASSLIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Detect',
    full_name='EyeTask.EyeTask.Detect',
    index=2,
    containing_service=None,
    input_type=_DETECTREQUEST,
    output_type=_DETECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='EyeTask.EyeTask.Retrieve',
    index=3,
    containing_service=None,
    input_type=_RETRIEVEREQUEST,
    output_type=_DETECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EYETASK)

DESCRIPTOR.services_by_name['EyeTask'] = _EYETASK

# @@protoc_insertion_point(module_scope)
