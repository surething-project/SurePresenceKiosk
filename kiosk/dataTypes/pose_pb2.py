# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pose.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pose.proto',
  package='pt.ulisboa.tecnico.surething.pose',
  syntax='proto3',
  serialized_options=b'\n!pt.ulisboa.tecnico.surething.poseB\004poseP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\npose.proto\x12!pt.ulisboa.tecnico.surething.pose\"x\n\x0cPoseEncrypt0\x12\x11\n\tprotected\x18\x01 \x01(\x0c\x12\x41\n\x0bunprotected\x18\x02 \x01(\x0b\x32,.pt.ulisboa.tecnico.surething.pose.HeaderMap\x12\x12\n\nciphertext\x18\x03 \x01(\x0c\"O\n\x05Value\x12\r\n\x03int\x18\x01 \x01(\x05H\x00\x12\x0e\n\x04tstr\x18\x02 \x01(\tH\x00\x12\x0e\n\x04uint\x18\x03 \x01(\rH\x00\x12\x0e\n\x04\x62str\x18\x04 \x01(\x0cH\x00\x42\x07\n\x05Value\"\xa5\x01\n\tHeaderMap\x12\x42\n\x03map\x18\x01 \x03(\x0b\x32\x35.pt.ulisboa.tecnico.surething.pose.HeaderMap.MapEntry\x1aT\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x37\n\x05value\x18\x02 \x01(\x0b\x32(.pt.ulisboa.tecnico.surething.pose.Value:\x02\x38\x01\"r\n\rEnc_Structure\x12\x0f\n\x07\x63ontext\x18\x01 \x01(\t\x12=\n\x04\x62ody\x18\x02 \x01(\x0b\x32/.pt.ulisboa.tecnico.surething.pose.PoseEncrypt0\x12\x11\n\tprotected\x18\x03 \x01(\x0c\"\xb8\x01\n\nPose_Sign1\x12\x11\n\tprotected\x18\x01 \x01(\x0c\x12\x41\n\x0bunprotected\x18\x02 \x01(\x0b\x32,.pt.ulisboa.tecnico.surething.pose.HeaderMap\x12\x41\n\x07payload\x18\x03 \x01(\x0b\x32\x30.pt.ulisboa.tecnico.surething.pose.Enc_Structure\x12\x11\n\tsignature\x18\x04 \x01(\x0c\"u\n\rSig_Structure\x12\x0f\n\x07\x63ontext\x18\x01 \x01(\t\x12;\n\x04\x62ody\x18\x02 \x01(\x0b\x32-.pt.ulisboa.tecnico.surething.pose.Pose_Sign1\x12\x16\n\x0e\x62ody_protected\x18\x03 \x01(\x0c\x42+\n!pt.ulisboa.tecnico.surething.poseB\x04poseP\x01\x62\x06proto3'
)




_POSEENCRYPT0 = _descriptor.Descriptor(
  name='PoseEncrypt0',
  full_name='pt.ulisboa.tecnico.surething.pose.PoseEncrypt0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protected', full_name='pt.ulisboa.tecnico.surething.pose.PoseEncrypt0.protected', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unprotected', full_name='pt.ulisboa.tecnico.surething.pose.PoseEncrypt0.unprotected', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ciphertext', full_name='pt.ulisboa.tecnico.surething.pose.PoseEncrypt0.ciphertext', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=49,
  serialized_end=169,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='pt.ulisboa.tecnico.surething.pose.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='int', full_name='pt.ulisboa.tecnico.surething.pose.Value.int', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tstr', full_name='pt.ulisboa.tecnico.surething.pose.Value.tstr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uint', full_name='pt.ulisboa.tecnico.surething.pose.Value.uint', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bstr', full_name='pt.ulisboa.tecnico.surething.pose.Value.bstr', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
    _descriptor.OneofDescriptor(
      name='Value', full_name='pt.ulisboa.tecnico.surething.pose.Value.Value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=171,
  serialized_end=250,
)


_HEADERMAP_MAPENTRY = _descriptor.Descriptor(
  name='MapEntry',
  full_name='pt.ulisboa.tecnico.surething.pose.HeaderMap.MapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pt.ulisboa.tecnico.surething.pose.HeaderMap.MapEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='pt.ulisboa.tecnico.surething.pose.HeaderMap.MapEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=418,
)

_HEADERMAP = _descriptor.Descriptor(
  name='HeaderMap',
  full_name='pt.ulisboa.tecnico.surething.pose.HeaderMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='map', full_name='pt.ulisboa.tecnico.surething.pose.HeaderMap.map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HEADERMAP_MAPENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=418,
)


_ENC_STRUCTURE = _descriptor.Descriptor(
  name='Enc_Structure',
  full_name='pt.ulisboa.tecnico.surething.pose.Enc_Structure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='pt.ulisboa.tecnico.surething.pose.Enc_Structure.context', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='pt.ulisboa.tecnico.surething.pose.Enc_Structure.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='protected', full_name='pt.ulisboa.tecnico.surething.pose.Enc_Structure.protected', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=420,
  serialized_end=534,
)


_POSE_SIGN1 = _descriptor.Descriptor(
  name='Pose_Sign1',
  full_name='pt.ulisboa.tecnico.surething.pose.Pose_Sign1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protected', full_name='pt.ulisboa.tecnico.surething.pose.Pose_Sign1.protected', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unprotected', full_name='pt.ulisboa.tecnico.surething.pose.Pose_Sign1.unprotected', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='pt.ulisboa.tecnico.surething.pose.Pose_Sign1.payload', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='pt.ulisboa.tecnico.surething.pose.Pose_Sign1.signature', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=537,
  serialized_end=721,
)


_SIG_STRUCTURE = _descriptor.Descriptor(
  name='Sig_Structure',
  full_name='pt.ulisboa.tecnico.surething.pose.Sig_Structure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='pt.ulisboa.tecnico.surething.pose.Sig_Structure.context', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='pt.ulisboa.tecnico.surething.pose.Sig_Structure.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body_protected', full_name='pt.ulisboa.tecnico.surething.pose.Sig_Structure.body_protected', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=723,
  serialized_end=840,
)

_POSEENCRYPT0.fields_by_name['unprotected'].message_type = _HEADERMAP
_VALUE.oneofs_by_name['Value'].fields.append(
  _VALUE.fields_by_name['int'])
_VALUE.fields_by_name['int'].containing_oneof = _VALUE.oneofs_by_name['Value']
_VALUE.oneofs_by_name['Value'].fields.append(
  _VALUE.fields_by_name['tstr'])
_VALUE.fields_by_name['tstr'].containing_oneof = _VALUE.oneofs_by_name['Value']
_VALUE.oneofs_by_name['Value'].fields.append(
  _VALUE.fields_by_name['uint'])
_VALUE.fields_by_name['uint'].containing_oneof = _VALUE.oneofs_by_name['Value']
_VALUE.oneofs_by_name['Value'].fields.append(
  _VALUE.fields_by_name['bstr'])
_VALUE.fields_by_name['bstr'].containing_oneof = _VALUE.oneofs_by_name['Value']
_HEADERMAP_MAPENTRY.fields_by_name['value'].message_type = _VALUE
_HEADERMAP_MAPENTRY.containing_type = _HEADERMAP
_HEADERMAP.fields_by_name['map'].message_type = _HEADERMAP_MAPENTRY
_ENC_STRUCTURE.fields_by_name['body'].message_type = _POSEENCRYPT0
_POSE_SIGN1.fields_by_name['unprotected'].message_type = _HEADERMAP
_POSE_SIGN1.fields_by_name['payload'].message_type = _ENC_STRUCTURE
_SIG_STRUCTURE.fields_by_name['body'].message_type = _POSE_SIGN1
DESCRIPTOR.message_types_by_name['PoseEncrypt0'] = _POSEENCRYPT0
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['HeaderMap'] = _HEADERMAP
DESCRIPTOR.message_types_by_name['Enc_Structure'] = _ENC_STRUCTURE
DESCRIPTOR.message_types_by_name['Pose_Sign1'] = _POSE_SIGN1
DESCRIPTOR.message_types_by_name['Sig_Structure'] = _SIG_STRUCTURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PoseEncrypt0 = _reflection.GeneratedProtocolMessageType('PoseEncrypt0', (_message.Message,), {
  'DESCRIPTOR' : _POSEENCRYPT0,
  '__module__' : 'pose_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surething.pose.PoseEncrypt0)
  })
_sym_db.RegisterMessage(PoseEncrypt0)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'pose_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surething.pose.Value)
  })
_sym_db.RegisterMessage(Value)

HeaderMap = _reflection.GeneratedProtocolMessageType('HeaderMap', (_message.Message,), {

  'MapEntry' : _reflection.GeneratedProtocolMessageType('MapEntry', (_message.Message,), {
    'DESCRIPTOR' : _HEADERMAP_MAPENTRY,
    '__module__' : 'pose_pb2'
    # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surething.pose.HeaderMap.MapEntry)
    })
  ,
  'DESCRIPTOR' : _HEADERMAP,
  '__module__' : 'pose_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surething.pose.HeaderMap)
  })
_sym_db.RegisterMessage(HeaderMap)
_sym_db.RegisterMessage(HeaderMap.MapEntry)

Enc_Structure = _reflection.GeneratedProtocolMessageType('Enc_Structure', (_message.Message,), {
  'DESCRIPTOR' : _ENC_STRUCTURE,
  '__module__' : 'pose_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surething.pose.Enc_Structure)
  })
_sym_db.RegisterMessage(Enc_Structure)

Pose_Sign1 = _reflection.GeneratedProtocolMessageType('Pose_Sign1', (_message.Message,), {
  'DESCRIPTOR' : _POSE_SIGN1,
  '__module__' : 'pose_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surething.pose.Pose_Sign1)
  })
_sym_db.RegisterMessage(Pose_Sign1)

Sig_Structure = _reflection.GeneratedProtocolMessageType('Sig_Structure', (_message.Message,), {
  'DESCRIPTOR' : _SIG_STRUCTURE,
  '__module__' : 'pose_pb2'
  # @@protoc_insertion_point(class_scope:pt.ulisboa.tecnico.surething.pose.Sig_Structure)
  })
_sym_db.RegisterMessage(Sig_Structure)


DESCRIPTOR._options = None
_HEADERMAP_MAPENTRY._options = None
# @@protoc_insertion_point(module_scope)
