"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import chirpstack_api.common.common_pb2
import chirpstack_api.gw.gw_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class UplinkFrameLog(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PHY_PAYLOAD_FIELD_NUMBER: builtins.int
    TX_INFO_FIELD_NUMBER: builtins.int
    RX_INFO_FIELD_NUMBER: builtins.int
    M_TYPE_FIELD_NUMBER: builtins.int
    DEV_ADDR_FIELD_NUMBER: builtins.int
    DEV_EUI_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    PLAINTEXT_MAC_COMMANDS_FIELD_NUMBER: builtins.int
    # PHYPayload.
    phy_payload: builtins.bytes = ...
    # TX meta-data.
    @property
    def tx_info(self) -> chirpstack_api.gw.gw_pb2.UplinkTxInfo: ...
    # RX meta-data.
    @property
    def rx_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[chirpstack_api.gw.gw_pb2.UplinkRxInfo]: ...
    # Message type.
    m_type: chirpstack_api.common.common_pb2.MType.V = ...
    # Device address (optional).
    dev_addr: typing.Text = ...
    # Device EUI (optional).
    dev_eui: typing.Text = ...
    # Time.
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Plaintext mac-commands.
    plaintext_mac_commands: builtins.bool = ...
    def __init__(self,
        *,
        phy_payload : builtins.bytes = ...,
        tx_info : typing.Optional[chirpstack_api.gw.gw_pb2.UplinkTxInfo] = ...,
        rx_info : typing.Optional[typing.Iterable[chirpstack_api.gw.gw_pb2.UplinkRxInfo]] = ...,
        m_type : chirpstack_api.common.common_pb2.MType.V = ...,
        dev_addr : typing.Text = ...,
        dev_eui : typing.Text = ...,
        time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        plaintext_mac_commands : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"time",b"time",u"tx_info",b"tx_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_addr",b"dev_addr",u"dev_eui",b"dev_eui",u"m_type",b"m_type",u"phy_payload",b"phy_payload",u"plaintext_mac_commands",b"plaintext_mac_commands",u"rx_info",b"rx_info",u"time",b"time",u"tx_info",b"tx_info"]) -> None: ...
global___UplinkFrameLog = UplinkFrameLog

class DownlinkFrameLog(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TIME_FIELD_NUMBER: builtins.int
    PHY_PAYLOAD_FIELD_NUMBER: builtins.int
    TX_INFO_FIELD_NUMBER: builtins.int
    DOWNLINK_ID_FIELD_NUMBER: builtins.int
    GATEWAY_ID_FIELD_NUMBER: builtins.int
    M_TYPE_FIELD_NUMBER: builtins.int
    DEV_ADDR_FIELD_NUMBER: builtins.int
    DEV_EUI_FIELD_NUMBER: builtins.int
    PLAINTEXT_MAC_COMMANDS_FIELD_NUMBER: builtins.int
    # Time.
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # PHYPayload.
    phy_payload: builtins.bytes = ...
    # TX meta-data.
    @property
    def tx_info(self) -> chirpstack_api.gw.gw_pb2.DownlinkTxInfo: ...
    # Downlink ID.
    downlink_id: builtins.int = ...
    # Gateway ID (EUI64).
    gateway_id: typing.Text = ...
    # Message type.
    m_type: chirpstack_api.common.common_pb2.MType.V = ...
    # Device address (optional).
    dev_addr: typing.Text = ...
    # Device EUI (optional).
    dev_eui: typing.Text = ...
    # Plaintext mac-commands.
    plaintext_mac_commands: builtins.bool = ...
    def __init__(self,
        *,
        time : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        phy_payload : builtins.bytes = ...,
        tx_info : typing.Optional[chirpstack_api.gw.gw_pb2.DownlinkTxInfo] = ...,
        downlink_id : builtins.int = ...,
        gateway_id : typing.Text = ...,
        m_type : chirpstack_api.common.common_pb2.MType.V = ...,
        dev_addr : typing.Text = ...,
        dev_eui : typing.Text = ...,
        plaintext_mac_commands : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"time",b"time",u"tx_info",b"tx_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_addr",b"dev_addr",u"dev_eui",b"dev_eui",u"downlink_id",b"downlink_id",u"gateway_id",b"gateway_id",u"m_type",b"m_type",u"phy_payload",b"phy_payload",u"plaintext_mac_commands",b"plaintext_mac_commands",u"time",b"time",u"tx_info",b"tx_info"]) -> None: ...
global___DownlinkFrameLog = DownlinkFrameLog