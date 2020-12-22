# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='robot.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0brobot.proto\"\t\n\x07Request\"\x18\n\x08RequestI\x12\x0c\n\x04\x61rg1\x18\x01 \x01(\x12\"\'\n\tRequestII\x12\x0c\n\x04\x61rg1\x18\x01 \x01(\x12\x12\x0c\n\x04\x61rg2\x18\x02 \x01(\x12\"\x18\n\x08RequestS\x12\x0c\n\x04\x61rg1\x18\x01 \x01(\t\"\x18\n\x08RequestD\x12\x0c\n\x04\x61rg1\x18\x01 \x01(\x01\"\n\n\x08Response\"\x1a\n\tResponseS\x12\r\n\x05\x64\x61ta1\x18\x01 \x01(\t\"\x1a\n\tResponseI\x12\r\n\x05\x64\x61ta1\x18\x01 \x01(\x12\"\x1a\n\tResponseD\x12\r\n\x05\x64\x61ta1\x18\x01 \x01(\x01\"\x1b\n\nResponseRD\x12\r\n\x05\x64\x61ta1\x18\x01 \x03(\x01\x32\xd8\t\n\x0cRobotService\x12#\n\nHelloWorld\x12\t.RequestI\x1a\n.ResponseS\x12$\n\rGetSDKVersion\x12\x08.Request\x1a\t.RequestS\x12&\n\rTeachSetIndex\x12\t.RequestI\x1a\n.ResponseI\x12%\n\rTeachGetIndex\x12\x08.Request\x1a\n.ResponseI\x12%\n\x0cTeachSetTool\x12\t.RequestS\x1a\n.ResponseI\x12$\n\x0cTeachGetTool\x12\x08.Request\x1a\n.ResponseS\x12%\n\x0cTeachSetWobj\x12\t.RequestS\x1a\n.ResponseI\x12$\n\x0cTeachGetWobj\x12\x08.Request\x1a\n.ResponseS\x12+\n\x12TeachSetCoordinate\x12\t.RequestI\x1a\n.ResponseI\x12*\n\x12TeachGetCoordinate\x12\x08.Request\x1a\n.ResponseI\x12#\n\x0bTeachGetNum\x12\x08.Request\x1a\n.ResponseI\x12#\n\x0bTeachGetDof\x12\x08.Request\x1a\n.ResponseI\x12&\n\rTeachGetJoint\x12\x08.Request\x1a\x0b.ResponseRD\x12.\n\x13TeachStreamGetJoint\x12\x08.Request\x1a\x0b.ResponseRD0\x01\x12*\n\x11TeachGetCartesian\x12\x08.Request\x1a\x0b.ResponseRD\x12\x32\n\x17TeachStreamGetCartesian\x12\x08.Request\x1a\x0b.ResponseRD0\x01\x12(\n\x10TeachSetVelocity\x12\t.RequestD\x1a\t.Response\x12(\n\x10TeachGetVelocity\x12\x08.Request\x1a\n.ResponseD\x12\'\n\x0fTeachSetRunType\x12\t.RequestI\x1a\t.Response\x12\'\n\x0fTeachGetRunType\x12\x08.Request\x1a\n.ResponseI\x12*\n\x13TeachClearMoveError\x12\x08.Request\x1a\t.Response\x12*\n\x11TeachStartProject\x12\t.RequestS\x1a\n.ResponseI\x12(\n\x10TeachStopProject\x12\x08.Request\x1a\n.ResponseI\x12&\n\x0eTeachMoveStart\x12\x08.Request\x1a\n.ResponseI\x12%\n\rTeachMoveStop\x12\x08.Request\x1a\n.ResponseI\x12%\n\rTeachMoveHome\x12\x08.Request\x1a\n.ResponseI\x12#\n\tTeachMove\x12\n.RequestII\x1a\n.ResponseI\x12!\n\tTeachStop\x12\x08.Request\x1a\n.ResponseI\x12+\n\x12TeachCalibrateAxis\x12\t.RequestI\x1a\n.ResponseI\x12&\n\x0eTeachCalibrate\x12\x08.Request\x1a\n.ResponseIb\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=15,
  serialized_end=24,
)


_REQUESTI = _descriptor.Descriptor(
  name='RequestI',
  full_name='RequestI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg1', full_name='RequestI.arg1', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_end=50,
)


_REQUESTII = _descriptor.Descriptor(
  name='RequestII',
  full_name='RequestII',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg1', full_name='RequestII.arg1', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arg2', full_name='RequestII.arg2', index=1,
      number=2, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=52,
  serialized_end=91,
)


_REQUESTS = _descriptor.Descriptor(
  name='RequestS',
  full_name='RequestS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg1', full_name='RequestS.arg1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=93,
  serialized_end=117,
)


_REQUESTD = _descriptor.Descriptor(
  name='RequestD',
  full_name='RequestD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg1', full_name='RequestD.arg1', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=119,
  serialized_end=143,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=145,
  serialized_end=155,
)


_RESPONSES = _descriptor.Descriptor(
  name='ResponseS',
  full_name='ResponseS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data1', full_name='ResponseS.data1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=157,
  serialized_end=183,
)


_RESPONSEI = _descriptor.Descriptor(
  name='ResponseI',
  full_name='ResponseI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data1', full_name='ResponseI.data1', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=185,
  serialized_end=211,
)


_RESPONSED = _descriptor.Descriptor(
  name='ResponseD',
  full_name='ResponseD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data1', full_name='ResponseD.data1', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=213,
  serialized_end=239,
)


_RESPONSERD = _descriptor.Descriptor(
  name='ResponseRD',
  full_name='ResponseRD',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data1', full_name='ResponseRD.data1', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=241,
  serialized_end=268,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['RequestI'] = _REQUESTI
DESCRIPTOR.message_types_by_name['RequestII'] = _REQUESTII
DESCRIPTOR.message_types_by_name['RequestS'] = _REQUESTS
DESCRIPTOR.message_types_by_name['RequestD'] = _REQUESTD
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['ResponseS'] = _RESPONSES
DESCRIPTOR.message_types_by_name['ResponseI'] = _RESPONSEI
DESCRIPTOR.message_types_by_name['ResponseD'] = _RESPONSED
DESCRIPTOR.message_types_by_name['ResponseRD'] = _RESPONSERD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

RequestI = _reflection.GeneratedProtocolMessageType('RequestI', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTI,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:RequestI)
  })
_sym_db.RegisterMessage(RequestI)

RequestII = _reflection.GeneratedProtocolMessageType('RequestII', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTII,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:RequestII)
  })
_sym_db.RegisterMessage(RequestII)

RequestS = _reflection.GeneratedProtocolMessageType('RequestS', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTS,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:RequestS)
  })
_sym_db.RegisterMessage(RequestS)

RequestD = _reflection.GeneratedProtocolMessageType('RequestD', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTD,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:RequestD)
  })
_sym_db.RegisterMessage(RequestD)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

ResponseS = _reflection.GeneratedProtocolMessageType('ResponseS', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSES,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:ResponseS)
  })
_sym_db.RegisterMessage(ResponseS)

ResponseI = _reflection.GeneratedProtocolMessageType('ResponseI', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEI,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:ResponseI)
  })
_sym_db.RegisterMessage(ResponseI)

ResponseD = _reflection.GeneratedProtocolMessageType('ResponseD', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSED,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:ResponseD)
  })
_sym_db.RegisterMessage(ResponseD)

ResponseRD = _reflection.GeneratedProtocolMessageType('ResponseRD', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSERD,
  '__module__' : 'robot_pb2'
  # @@protoc_insertion_point(class_scope:ResponseRD)
  })
_sym_db.RegisterMessage(ResponseRD)



_ROBOTSERVICE = _descriptor.ServiceDescriptor(
  name='RobotService',
  full_name='RobotService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=271,
  serialized_end=1511,
  methods=[
  _descriptor.MethodDescriptor(
    name='HelloWorld',
    full_name='RobotService.HelloWorld',
    index=0,
    containing_service=None,
    input_type=_REQUESTI,
    output_type=_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetSDKVersion',
    full_name='RobotService.GetSDKVersion',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REQUESTS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachSetIndex',
    full_name='RobotService.TeachSetIndex',
    index=2,
    containing_service=None,
    input_type=_REQUESTI,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetIndex',
    full_name='RobotService.TeachGetIndex',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachSetTool',
    full_name='RobotService.TeachSetTool',
    index=4,
    containing_service=None,
    input_type=_REQUESTS,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetTool',
    full_name='RobotService.TeachGetTool',
    index=5,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachSetWobj',
    full_name='RobotService.TeachSetWobj',
    index=6,
    containing_service=None,
    input_type=_REQUESTS,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetWobj',
    full_name='RobotService.TeachGetWobj',
    index=7,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachSetCoordinate',
    full_name='RobotService.TeachSetCoordinate',
    index=8,
    containing_service=None,
    input_type=_REQUESTI,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetCoordinate',
    full_name='RobotService.TeachGetCoordinate',
    index=9,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetNum',
    full_name='RobotService.TeachGetNum',
    index=10,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetDof',
    full_name='RobotService.TeachGetDof',
    index=11,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetJoint',
    full_name='RobotService.TeachGetJoint',
    index=12,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSERD,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachStreamGetJoint',
    full_name='RobotService.TeachStreamGetJoint',
    index=13,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSERD,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetCartesian',
    full_name='RobotService.TeachGetCartesian',
    index=14,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSERD,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachStreamGetCartesian',
    full_name='RobotService.TeachStreamGetCartesian',
    index=15,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSERD,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachSetVelocity',
    full_name='RobotService.TeachSetVelocity',
    index=16,
    containing_service=None,
    input_type=_REQUESTD,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetVelocity',
    full_name='RobotService.TeachGetVelocity',
    index=17,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSED,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachSetRunType',
    full_name='RobotService.TeachSetRunType',
    index=18,
    containing_service=None,
    input_type=_REQUESTI,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachGetRunType',
    full_name='RobotService.TeachGetRunType',
    index=19,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachClearMoveError',
    full_name='RobotService.TeachClearMoveError',
    index=20,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachStartProject',
    full_name='RobotService.TeachStartProject',
    index=21,
    containing_service=None,
    input_type=_REQUESTS,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachStopProject',
    full_name='RobotService.TeachStopProject',
    index=22,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachMoveStart',
    full_name='RobotService.TeachMoveStart',
    index=23,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachMoveStop',
    full_name='RobotService.TeachMoveStop',
    index=24,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachMoveHome',
    full_name='RobotService.TeachMoveHome',
    index=25,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachMove',
    full_name='RobotService.TeachMove',
    index=26,
    containing_service=None,
    input_type=_REQUESTII,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachStop',
    full_name='RobotService.TeachStop',
    index=27,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachCalibrateAxis',
    full_name='RobotService.TeachCalibrateAxis',
    index=28,
    containing_service=None,
    input_type=_REQUESTI,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='TeachCalibrate',
    full_name='RobotService.TeachCalibrate',
    index=29,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSEI,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROBOTSERVICE)

DESCRIPTOR.services_by_name['RobotService'] = _ROBOTSERVICE

# @@protoc_insertion_point(module_scope)
