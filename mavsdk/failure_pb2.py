# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: failure/failure.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='failure/failure.proto',
  package='mavsdk.rpc.failure',
  syntax='proto3',
  serialized_options=b'\n\021io.mavsdk.failureB\014FailureProto',
  serialized_pb=b'\n\x15\x66\x61ilure/failure.proto\x12\x12mavsdk.rpc.failure\x1a\x14mavsdk_options.proto\"\x8f\x01\n\rInjectRequest\x12\x35\n\x0c\x66\x61ilure_unit\x18\x01 \x01(\x0e\x32\x1f.mavsdk.rpc.failure.FailureUnit\x12\x35\n\x0c\x66\x61ilure_type\x18\x02 \x01(\x0e\x32\x1f.mavsdk.rpc.failure.FailureType\x12\x10\n\x08instance\x18\x03 \x01(\x05\"K\n\x0eInjectResponse\x12\x39\n\x0e\x66\x61ilure_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.failure.FailureResult\"\x97\x02\n\rFailureResult\x12\x38\n\x06result\x18\x01 \x01(\x0e\x32(.mavsdk.rpc.failure.FailureResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xb7\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x04\x12\x11\n\rRESULT_DENIED\x10\x05\x12\x13\n\x0fRESULT_DISABLED\x10\x06\x12\x12\n\x0eRESULT_TIMEOUT\x10\x07*\xfd\x03\n\x0b\x46\x61ilureUnit\x12\x1c\n\x18\x46\x41ILURE_UNIT_SENSOR_GYRO\x10\x00\x12\x1d\n\x19\x46\x41ILURE_UNIT_SENSOR_ACCEL\x10\x01\x12\x1b\n\x17\x46\x41ILURE_UNIT_SENSOR_MAG\x10\x02\x12\x1c\n\x18\x46\x41ILURE_UNIT_SENSOR_BARO\x10\x03\x12\x1b\n\x17\x46\x41ILURE_UNIT_SENSOR_GPS\x10\x04\x12$\n FAILURE_UNIT_SENSOR_OPTICAL_FLOW\x10\x05\x12\x1b\n\x17\x46\x41ILURE_UNIT_SENSOR_VIO\x10\x06\x12\'\n#FAILURE_UNIT_SENSOR_DISTANCE_SENSOR\x10\x07\x12 \n\x1c\x46\x41ILURE_UNIT_SENSOR_AIRSPEED\x10\x08\x12\x1f\n\x1b\x46\x41ILURE_UNIT_SYSTEM_BATTERY\x10\x64\x12\x1d\n\x19\x46\x41ILURE_UNIT_SYSTEM_MOTOR\x10\x65\x12\x1d\n\x19\x46\x41ILURE_UNIT_SYSTEM_SERVO\x10\x66\x12!\n\x1d\x46\x41ILURE_UNIT_SYSTEM_AVOIDANCE\x10g\x12!\n\x1d\x46\x41ILURE_UNIT_SYSTEM_RC_SIGNAL\x10h\x12&\n\"FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL\x10i*\xd2\x01\n\x0b\x46\x61ilureType\x12\x13\n\x0f\x46\x41ILURE_TYPE_OK\x10\x00\x12\x14\n\x10\x46\x41ILURE_TYPE_OFF\x10\x01\x12\x16\n\x12\x46\x41ILURE_TYPE_STUCK\x10\x02\x12\x18\n\x14\x46\x41ILURE_TYPE_GARBAGE\x10\x03\x12\x16\n\x12\x46\x41ILURE_TYPE_WRONG\x10\x04\x12\x15\n\x11\x46\x41ILURE_TYPE_SLOW\x10\x05\x12\x18\n\x14\x46\x41ILURE_TYPE_DELAYED\x10\x06\x12\x1d\n\x19\x46\x41ILURE_TYPE_INTERMITTENT\x10\x07\x32g\n\x0e\x46\x61ilureService\x12U\n\x06Inject\x12!.mavsdk.rpc.failure.InjectRequest\x1a\".mavsdk.rpc.failure.InjectResponse\"\x04\x80\xb5\x18\x01\x42!\n\x11io.mavsdk.failureB\x0c\x46\x61ilureProtob\x06proto3'
  ,
  dependencies=[mavsdk__options__pb2.DESCRIPTOR,])

_FAILUREUNIT = _descriptor.EnumDescriptor(
  name='FailureUnit',
  full_name='mavsdk.rpc.failure.FailureUnit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_GYRO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_ACCEL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_MAG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_BARO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_GPS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_OPTICAL_FLOW', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_VIO', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_DISTANCE_SENSOR', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SENSOR_AIRSPEED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SYSTEM_BATTERY', index=9, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SYSTEM_MOTOR', index=10, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SYSTEM_SERVO', index=11, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SYSTEM_AVOIDANCE', index=12, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SYSTEM_RC_SIGNAL', index=13, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL', index=14, number=105,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=573,
  serialized_end=1082,
)
_sym_db.RegisterEnumDescriptor(_FAILUREUNIT)

FailureUnit = enum_type_wrapper.EnumTypeWrapper(_FAILUREUNIT)
_FAILURETYPE = _descriptor.EnumDescriptor(
  name='FailureType',
  full_name='mavsdk.rpc.failure.FailureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FAILURE_TYPE_OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_TYPE_OFF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_TYPE_STUCK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_TYPE_GARBAGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_TYPE_WRONG', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_TYPE_SLOW', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_TYPE_DELAYED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_TYPE_INTERMITTENT', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1085,
  serialized_end=1295,
)
_sym_db.RegisterEnumDescriptor(_FAILURETYPE)

FailureType = enum_type_wrapper.EnumTypeWrapper(_FAILURETYPE)
FAILURE_UNIT_SENSOR_GYRO = 0
FAILURE_UNIT_SENSOR_ACCEL = 1
FAILURE_UNIT_SENSOR_MAG = 2
FAILURE_UNIT_SENSOR_BARO = 3
FAILURE_UNIT_SENSOR_GPS = 4
FAILURE_UNIT_SENSOR_OPTICAL_FLOW = 5
FAILURE_UNIT_SENSOR_VIO = 6
FAILURE_UNIT_SENSOR_DISTANCE_SENSOR = 7
FAILURE_UNIT_SENSOR_AIRSPEED = 8
FAILURE_UNIT_SYSTEM_BATTERY = 100
FAILURE_UNIT_SYSTEM_MOTOR = 101
FAILURE_UNIT_SYSTEM_SERVO = 102
FAILURE_UNIT_SYSTEM_AVOIDANCE = 103
FAILURE_UNIT_SYSTEM_RC_SIGNAL = 104
FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL = 105
FAILURE_TYPE_OK = 0
FAILURE_TYPE_OFF = 1
FAILURE_TYPE_STUCK = 2
FAILURE_TYPE_GARBAGE = 3
FAILURE_TYPE_WRONG = 4
FAILURE_TYPE_SLOW = 5
FAILURE_TYPE_DELAYED = 6
FAILURE_TYPE_INTERMITTENT = 7


_FAILURERESULT_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='mavsdk.rpc.failure.FailureResult.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_NO_SYSTEM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_CONNECTION_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_UNSUPPORTED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_DENIED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_DISABLED', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULT_TIMEOUT', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=387,
  serialized_end=570,
)
_sym_db.RegisterEnumDescriptor(_FAILURERESULT_RESULT)


_INJECTREQUEST = _descriptor.Descriptor(
  name='InjectRequest',
  full_name='mavsdk.rpc.failure.InjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failure_unit', full_name='mavsdk.rpc.failure.InjectRequest.failure_unit', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failure_type', full_name='mavsdk.rpc.failure.InjectRequest.failure_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instance', full_name='mavsdk.rpc.failure.InjectRequest.instance', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=68,
  serialized_end=211,
)


_INJECTRESPONSE = _descriptor.Descriptor(
  name='InjectResponse',
  full_name='mavsdk.rpc.failure.InjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='failure_result', full_name='mavsdk.rpc.failure.InjectResponse.failure_result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_end=288,
)


_FAILURERESULT = _descriptor.Descriptor(
  name='FailureResult',
  full_name='mavsdk.rpc.failure.FailureResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='mavsdk.rpc.failure.FailureResult.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='result_str', full_name='mavsdk.rpc.failure.FailureResult.result_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FAILURERESULT_RESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=570,
)

_INJECTREQUEST.fields_by_name['failure_unit'].enum_type = _FAILUREUNIT
_INJECTREQUEST.fields_by_name['failure_type'].enum_type = _FAILURETYPE
_INJECTRESPONSE.fields_by_name['failure_result'].message_type = _FAILURERESULT
_FAILURERESULT.fields_by_name['result'].enum_type = _FAILURERESULT_RESULT
_FAILURERESULT_RESULT.containing_type = _FAILURERESULT
DESCRIPTOR.message_types_by_name['InjectRequest'] = _INJECTREQUEST
DESCRIPTOR.message_types_by_name['InjectResponse'] = _INJECTRESPONSE
DESCRIPTOR.message_types_by_name['FailureResult'] = _FAILURERESULT
DESCRIPTOR.enum_types_by_name['FailureUnit'] = _FAILUREUNIT
DESCRIPTOR.enum_types_by_name['FailureType'] = _FAILURETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InjectRequest = _reflection.GeneratedProtocolMessageType('InjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _INJECTREQUEST,
  '__module__' : 'failure.failure_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.failure.InjectRequest)
  })
_sym_db.RegisterMessage(InjectRequest)

InjectResponse = _reflection.GeneratedProtocolMessageType('InjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _INJECTRESPONSE,
  '__module__' : 'failure.failure_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.failure.InjectResponse)
  })
_sym_db.RegisterMessage(InjectResponse)

FailureResult = _reflection.GeneratedProtocolMessageType('FailureResult', (_message.Message,), {
  'DESCRIPTOR' : _FAILURERESULT,
  '__module__' : 'failure.failure_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.failure.FailureResult)
  })
_sym_db.RegisterMessage(FailureResult)


DESCRIPTOR._options = None

_FAILURESERVICE = _descriptor.ServiceDescriptor(
  name='FailureService',
  full_name='mavsdk.rpc.failure.FailureService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1297,
  serialized_end=1400,
  methods=[
  _descriptor.MethodDescriptor(
    name='Inject',
    full_name='mavsdk.rpc.failure.FailureService.Inject',
    index=0,
    containing_service=None,
    input_type=_INJECTREQUEST,
    output_type=_INJECTRESPONSE,
    serialized_options=b'\200\265\030\001',
  ),
])
_sym_db.RegisterServiceDescriptor(_FAILURESERVICE)

DESCRIPTOR.services_by_name['FailureService'] = _FAILURESERVICE

# @@protoc_insertion_point(module_scope)
