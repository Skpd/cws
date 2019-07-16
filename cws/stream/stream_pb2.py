# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream/stream.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cws.client import client_pb2 as client_dot_client__pb2
from cws.markets import market_pb2 as markets_dot_market__pb2
from cws.markets import index_pb2 as markets_dot_index__pb2
from cws.markets import pair_pb2 as markets_dot_pair__pb2
from cws.markets import asset_pb2 as markets_dot_asset__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stream/stream.proto',
  package='ProtobufStream',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13stream/stream.proto\x12\x0eProtobufStream\x1a\x13\x63lient/client.proto\x1a\x14markets/market.proto\x1a\x13markets/index.proto\x1a\x12markets/pair.proto\x1a\x13markets/asset.proto\"\xcb\x04\n\rStreamMessage\x12\x44\n\x14\x61uthenticationResult\x18\x01 \x01(\x0b\x32$.ProtobufStream.AuthenticationResultH\x00\x12@\n\x12subscriptionResult\x18\x05 \x01(\x0b\x32\".ProtobufStream.SubscriptionResultH\x00\x12\x44\n\x14unsubscriptionResult\x18\x06 \x01(\x0b\x32$.ProtobufStream.UnsubscriptionResultH\x00\x12\x38\n\x0emissedMessages\x18\x07 \x01(\x0b\x32\x1e.ProtobufStream.MissedMessagesH\x00\x12<\n\x0cmarketUpdate\x18\x02 \x01(\x0b\x32$.ProtobufMarkets.MarketUpdateMessageH\x00\x12\x38\n\npairUpdate\x18\x03 \x01(\x0b\x32\".ProtobufMarkets.PairUpdateMessageH\x00\x12:\n\x0b\x61ssetUpdate\x18\x04 \x01(\x0b\x32#.ProtobufMarkets.AssetUpdateMessageH\x00\x12:\n\x0bindexUpdate\x18\x08 \x01(\x0b\x32#.ProtobufMarkets.IndexUpdateMessageH\x00\x12:\n\x0f\x62\x61ndwidthUpdate\x18\t \x01(\x0b\x32\x1f.ProtobufStream.BandwidthUpdateH\x00\x42\x06\n\x04\x62ody\"\xd3\x01\n\x14\x41uthenticationResult\x12;\n\x06status\x18\x01 \x01(\x0e\x32+.ProtobufStream.AuthenticationResult.Status\"~\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x11\n\rAUTHENTICATED\x10\x01\x12\r\n\tBAD_NONCE\x10\x02\x12\r\n\tBAD_TOKEN\x10\x03\x12\x11\n\rTOKEN_EXPIRED\x10\x04\x12\x10\n\x0cREADONLY_KEY\x10\x05\x12\x11\n\rACCESS_DENIED\x10\x06\"\xcb\x01\n\x12SubscriptionResult\x12\x16\n\nsubscribed\x18\x01 \x03(\tB\x02\x18\x01\x12.\n\x06\x66\x61iled\x18\x02 \x03(\x0b\x32\x1e.ProtobufStream.SubscribeError\x12\x32\n\x06status\x18\x03 \x01(\x0b\x32\".ProtobufStream.SubscriptionStatus\x12\x39\n\rsubscriptions\x18\x04 \x03(\x0b\x32\".ProtobufClient.ClientSubscription\"\xd1\x01\n\x14UnsubscriptionResult\x12\x18\n\x0cunsubscribed\x18\x01 \x03(\tB\x02\x18\x01\x12\x30\n\x06\x66\x61iled\x18\x02 \x03(\x0b\x32 .ProtobufStream.UnsubscribeError\x12\x32\n\x06status\x18\x03 \x01(\x0b\x32\".ProtobufStream.SubscriptionStatus\x12\x39\n\rsubscriptions\x18\x04 \x03(\x0b\x32\".ProtobufClient.ClientSubscription\"j\n\x0eSubscribeError\x12\x0f\n\x03key\x18\x01 \x01(\tB\x02\x18\x01\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x38\n\x0csubscription\x18\x03 \x01(\x0b\x32\".ProtobufClient.ClientSubscription\"l\n\x10UnsubscribeError\x12\x0f\n\x03key\x18\x01 \x01(\tB\x02\x18\x01\x12\r\n\x05\x65rror\x18\x02 \x01(\t\x12\x38\n\x0csubscription\x18\x03 \x01(\x0b\x32\".ProtobufClient.ClientSubscription\"a\n\x12SubscriptionStatus\x12\x10\n\x04keys\x18\x01 \x03(\tB\x02\x18\x01\x12\x39\n\rsubscriptions\x18\x02 \x03(\x0b\x32\".ProtobufClient.ClientSubscription\"+\n\x0eMissedMessages\x12\x19\n\x11numMissedMessages\x18\x01 \x01(\x03\"H\n\x0f\x42\x61ndwidthUpdate\x12\n\n\x02ok\x18\x01 \x01(\x08\x12\x16\n\x0e\x62ytesRemaining\x18\x02 \x01(\x03\x12\x11\n\tbytesUsed\x18\x03 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[client_dot_client__pb2.DESCRIPTOR,markets_dot_market__pb2.DESCRIPTOR,markets_dot_index__pb2.DESCRIPTOR,markets_dot_pair__pb2.DESCRIPTOR,markets_dot_asset__pb2.DESCRIPTOR,])



_AUTHENTICATIONRESULT_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ProtobufStream.AuthenticationResult.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTHENTICATED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_NONCE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_TOKEN', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOKEN_EXPIRED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READONLY_KEY', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_DENIED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=820,
  serialized_end=946,
)
_sym_db.RegisterEnumDescriptor(_AUTHENTICATIONRESULT_STATUS)


_STREAMMESSAGE = _descriptor.Descriptor(
  name='StreamMessage',
  full_name='ProtobufStream.StreamMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authenticationResult', full_name='ProtobufStream.StreamMessage.authenticationResult', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptionResult', full_name='ProtobufStream.StreamMessage.subscriptionResult', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unsubscriptionResult', full_name='ProtobufStream.StreamMessage.unsubscriptionResult', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='missedMessages', full_name='ProtobufStream.StreamMessage.missedMessages', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marketUpdate', full_name='ProtobufStream.StreamMessage.marketUpdate', index=4,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pairUpdate', full_name='ProtobufStream.StreamMessage.pairUpdate', index=5,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assetUpdate', full_name='ProtobufStream.StreamMessage.assetUpdate', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indexUpdate', full_name='ProtobufStream.StreamMessage.indexUpdate', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bandwidthUpdate', full_name='ProtobufStream.StreamMessage.bandwidthUpdate', index=8,
      number=9, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='body', full_name='ProtobufStream.StreamMessage.body',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=145,
  serialized_end=732,
)


_AUTHENTICATIONRESULT = _descriptor.Descriptor(
  name='AuthenticationResult',
  full_name='ProtobufStream.AuthenticationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ProtobufStream.AuthenticationResult.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AUTHENTICATIONRESULT_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=735,
  serialized_end=946,
)


_SUBSCRIPTIONRESULT = _descriptor.Descriptor(
  name='SubscriptionResult',
  full_name='ProtobufStream.SubscriptionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='subscribed', full_name='ProtobufStream.SubscriptionResult.subscribed', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failed', full_name='ProtobufStream.SubscriptionResult.failed', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ProtobufStream.SubscriptionResult.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptions', full_name='ProtobufStream.SubscriptionResult.subscriptions', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=949,
  serialized_end=1152,
)


_UNSUBSCRIPTIONRESULT = _descriptor.Descriptor(
  name='UnsubscriptionResult',
  full_name='ProtobufStream.UnsubscriptionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unsubscribed', full_name='ProtobufStream.UnsubscriptionResult.unsubscribed', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failed', full_name='ProtobufStream.UnsubscriptionResult.failed', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ProtobufStream.UnsubscriptionResult.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptions', full_name='ProtobufStream.UnsubscriptionResult.subscriptions', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=1155,
  serialized_end=1364,
)


_SUBSCRIBEERROR = _descriptor.Descriptor(
  name='SubscribeError',
  full_name='ProtobufStream.SubscribeError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ProtobufStream.SubscribeError.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='ProtobufStream.SubscribeError.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscription', full_name='ProtobufStream.SubscribeError.subscription', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1366,
  serialized_end=1472,
)


_UNSUBSCRIBEERROR = _descriptor.Descriptor(
  name='UnsubscribeError',
  full_name='ProtobufStream.UnsubscribeError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ProtobufStream.UnsubscribeError.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='ProtobufStream.UnsubscribeError.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscription', full_name='ProtobufStream.UnsubscribeError.subscription', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1474,
  serialized_end=1582,
)


_SUBSCRIPTIONSTATUS = _descriptor.Descriptor(
  name='SubscriptionStatus',
  full_name='ProtobufStream.SubscriptionStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='ProtobufStream.SubscriptionStatus.keys', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptions', full_name='ProtobufStream.SubscriptionStatus.subscriptions', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1584,
  serialized_end=1681,
)


_MISSEDMESSAGES = _descriptor.Descriptor(
  name='MissedMessages',
  full_name='ProtobufStream.MissedMessages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numMissedMessages', full_name='ProtobufStream.MissedMessages.numMissedMessages', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=1683,
  serialized_end=1726,
)


_BANDWIDTHUPDATE = _descriptor.Descriptor(
  name='BandwidthUpdate',
  full_name='ProtobufStream.BandwidthUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ok', full_name='ProtobufStream.BandwidthUpdate.ok', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytesRemaining', full_name='ProtobufStream.BandwidthUpdate.bytesRemaining', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytesUsed', full_name='ProtobufStream.BandwidthUpdate.bytesUsed', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=1728,
  serialized_end=1800,
)

_STREAMMESSAGE.fields_by_name['authenticationResult'].message_type = _AUTHENTICATIONRESULT
_STREAMMESSAGE.fields_by_name['subscriptionResult'].message_type = _SUBSCRIPTIONRESULT
_STREAMMESSAGE.fields_by_name['unsubscriptionResult'].message_type = _UNSUBSCRIPTIONRESULT
_STREAMMESSAGE.fields_by_name['missedMessages'].message_type = _MISSEDMESSAGES
_STREAMMESSAGE.fields_by_name['marketUpdate'].message_type = markets_dot_market__pb2._MARKETUPDATEMESSAGE
_STREAMMESSAGE.fields_by_name['pairUpdate'].message_type = markets_dot_pair__pb2._PAIRUPDATEMESSAGE
_STREAMMESSAGE.fields_by_name['assetUpdate'].message_type = markets_dot_asset__pb2._ASSETUPDATEMESSAGE
_STREAMMESSAGE.fields_by_name['indexUpdate'].message_type = markets_dot_index__pb2._INDEXUPDATEMESSAGE
_STREAMMESSAGE.fields_by_name['bandwidthUpdate'].message_type = _BANDWIDTHUPDATE
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['authenticationResult'])
_STREAMMESSAGE.fields_by_name['authenticationResult'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['subscriptionResult'])
_STREAMMESSAGE.fields_by_name['subscriptionResult'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['unsubscriptionResult'])
_STREAMMESSAGE.fields_by_name['unsubscriptionResult'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['missedMessages'])
_STREAMMESSAGE.fields_by_name['missedMessages'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['marketUpdate'])
_STREAMMESSAGE.fields_by_name['marketUpdate'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['pairUpdate'])
_STREAMMESSAGE.fields_by_name['pairUpdate'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['assetUpdate'])
_STREAMMESSAGE.fields_by_name['assetUpdate'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['indexUpdate'])
_STREAMMESSAGE.fields_by_name['indexUpdate'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_STREAMMESSAGE.oneofs_by_name['body'].fields.append(
  _STREAMMESSAGE.fields_by_name['bandwidthUpdate'])
_STREAMMESSAGE.fields_by_name['bandwidthUpdate'].containing_oneof = _STREAMMESSAGE.oneofs_by_name['body']
_AUTHENTICATIONRESULT.fields_by_name['status'].enum_type = _AUTHENTICATIONRESULT_STATUS
_AUTHENTICATIONRESULT_STATUS.containing_type = _AUTHENTICATIONRESULT
_SUBSCRIPTIONRESULT.fields_by_name['failed'].message_type = _SUBSCRIBEERROR
_SUBSCRIPTIONRESULT.fields_by_name['status'].message_type = _SUBSCRIPTIONSTATUS
_SUBSCRIPTIONRESULT.fields_by_name['subscriptions'].message_type = client_dot_client__pb2._CLIENTSUBSCRIPTION
_UNSUBSCRIPTIONRESULT.fields_by_name['failed'].message_type = _UNSUBSCRIBEERROR
_UNSUBSCRIPTIONRESULT.fields_by_name['status'].message_type = _SUBSCRIPTIONSTATUS
_UNSUBSCRIPTIONRESULT.fields_by_name['subscriptions'].message_type = client_dot_client__pb2._CLIENTSUBSCRIPTION
_SUBSCRIBEERROR.fields_by_name['subscription'].message_type = client_dot_client__pb2._CLIENTSUBSCRIPTION
_UNSUBSCRIBEERROR.fields_by_name['subscription'].message_type = client_dot_client__pb2._CLIENTSUBSCRIPTION
_SUBSCRIPTIONSTATUS.fields_by_name['subscriptions'].message_type = client_dot_client__pb2._CLIENTSUBSCRIPTION
DESCRIPTOR.message_types_by_name['StreamMessage'] = _STREAMMESSAGE
DESCRIPTOR.message_types_by_name['AuthenticationResult'] = _AUTHENTICATIONRESULT
DESCRIPTOR.message_types_by_name['SubscriptionResult'] = _SUBSCRIPTIONRESULT
DESCRIPTOR.message_types_by_name['UnsubscriptionResult'] = _UNSUBSCRIPTIONRESULT
DESCRIPTOR.message_types_by_name['SubscribeError'] = _SUBSCRIBEERROR
DESCRIPTOR.message_types_by_name['UnsubscribeError'] = _UNSUBSCRIBEERROR
DESCRIPTOR.message_types_by_name['SubscriptionStatus'] = _SUBSCRIPTIONSTATUS
DESCRIPTOR.message_types_by_name['MissedMessages'] = _MISSEDMESSAGES
DESCRIPTOR.message_types_by_name['BandwidthUpdate'] = _BANDWIDTHUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamMessage = _reflection.GeneratedProtocolMessageType('StreamMessage', (_message.Message,), dict(
  DESCRIPTOR = _STREAMMESSAGE,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.StreamMessage)
  ))
_sym_db.RegisterMessage(StreamMessage)

AuthenticationResult = _reflection.GeneratedProtocolMessageType('AuthenticationResult', (_message.Message,), dict(
  DESCRIPTOR = _AUTHENTICATIONRESULT,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.AuthenticationResult)
  ))
_sym_db.RegisterMessage(AuthenticationResult)

SubscriptionResult = _reflection.GeneratedProtocolMessageType('SubscriptionResult', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIPTIONRESULT,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.SubscriptionResult)
  ))
_sym_db.RegisterMessage(SubscriptionResult)

UnsubscriptionResult = _reflection.GeneratedProtocolMessageType('UnsubscriptionResult', (_message.Message,), dict(
  DESCRIPTOR = _UNSUBSCRIPTIONRESULT,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.UnsubscriptionResult)
  ))
_sym_db.RegisterMessage(UnsubscriptionResult)

SubscribeError = _reflection.GeneratedProtocolMessageType('SubscribeError', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIBEERROR,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.SubscribeError)
  ))
_sym_db.RegisterMessage(SubscribeError)

UnsubscribeError = _reflection.GeneratedProtocolMessageType('UnsubscribeError', (_message.Message,), dict(
  DESCRIPTOR = _UNSUBSCRIBEERROR,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.UnsubscribeError)
  ))
_sym_db.RegisterMessage(UnsubscribeError)

SubscriptionStatus = _reflection.GeneratedProtocolMessageType('SubscriptionStatus', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIPTIONSTATUS,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.SubscriptionStatus)
  ))
_sym_db.RegisterMessage(SubscriptionStatus)

MissedMessages = _reflection.GeneratedProtocolMessageType('MissedMessages', (_message.Message,), dict(
  DESCRIPTOR = _MISSEDMESSAGES,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.MissedMessages)
  ))
_sym_db.RegisterMessage(MissedMessages)

BandwidthUpdate = _reflection.GeneratedProtocolMessageType('BandwidthUpdate', (_message.Message,), dict(
  DESCRIPTOR = _BANDWIDTHUPDATE,
  __module__ = 'stream.stream_pb2'
  # @@protoc_insertion_point(class_scope:ProtobufStream.BandwidthUpdate)
  ))
_sym_db.RegisterMessage(BandwidthUpdate)


_SUBSCRIPTIONRESULT.fields_by_name['subscribed']._options = None
_UNSUBSCRIPTIONRESULT.fields_by_name['unsubscribed']._options = None
_SUBSCRIBEERROR.fields_by_name['key']._options = None
_UNSUBSCRIBEERROR.fields_by_name['key']._options = None
_SUBSCRIPTIONSTATUS.fields_by_name['keys']._options = None
# @@protoc_insertion_point(module_scope)
