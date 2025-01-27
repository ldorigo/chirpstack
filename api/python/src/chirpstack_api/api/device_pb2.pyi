"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import chirpstack_api.common.common_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Device(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class VariablesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class TagsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        value: typing.Text = ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    DEV_EUI_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    APPLICATION_ID_FIELD_NUMBER: builtins.int
    DEVICE_PROFILE_ID_FIELD_NUMBER: builtins.int
    SKIP_FCNT_CHECK_FIELD_NUMBER: builtins.int
    IS_DISABLED_FIELD_NUMBER: builtins.int
    VARIABLES_FIELD_NUMBER: builtins.int
    TAGS_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    # Name.
    name: typing.Text = ...
    # Description.
    description: typing.Text = ...
    # Application ID (UUID).
    application_id: typing.Text = ...
    # Device-profile ID (UUID).
    device_profile_id: typing.Text = ...
    # Skip frame-counter checks (this is insecure, but could be helpful for debugging).
    skip_fcnt_check: builtins.bool = ...
    # Device is disabled.
    is_disabled: builtins.bool = ...
    # Variables (user defined).
    # These variables can be used together with integrations to store tokens /
    # secrets that must be configured per device. These variables are not
    # exposed in the event payloads.
    @property
    def variables(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    # Tags (user defined).
    # These tags are exposed in the event payloads or to integration. Tags are
    # intended for aggregation and filtering.
    @property
    def tags(self) -> google.protobuf.internal.containers.ScalarMap[typing.Text, typing.Text]: ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        name : typing.Text = ...,
        description : typing.Text = ...,
        application_id : typing.Text = ...,
        device_profile_id : typing.Text = ...,
        skip_fcnt_check : builtins.bool = ...,
        is_disabled : builtins.bool = ...,
        variables : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        tags : typing.Optional[typing.Mapping[typing.Text, typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"application_id",b"application_id",u"description",b"description",u"dev_eui",b"dev_eui",u"device_profile_id",b"device_profile_id",u"is_disabled",b"is_disabled",u"name",b"name",u"skip_fcnt_check",b"skip_fcnt_check",u"tags",b"tags",u"variables",b"variables"]) -> None: ...
global___Device = Device

class DeviceStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MARGIN_FIELD_NUMBER: builtins.int
    EXTERNAL_POWER_SOURCE_FIELD_NUMBER: builtins.int
    BATTERY_LEVEL_FIELD_NUMBER: builtins.int
    # The device margin status
    # -32..32: The demodulation SNR ration in dB
    margin: builtins.int = ...
    # Device is connected to an external power source.
    external_power_source: builtins.bool = ...
    # Device battery level as a percentage.
    # -1 when the battery level is not available.
    battery_level: builtins.float = ...
    def __init__(self,
        *,
        margin : builtins.int = ...,
        external_power_source : builtins.bool = ...,
        battery_level : builtins.float = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"battery_level",b"battery_level",u"external_power_source",b"external_power_source",u"margin",b"margin"]) -> None: ...
global___DeviceStatus = DeviceStatus

class DeviceListItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    LAST_SEEN_AT_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DEVICE_PROFILE_ID_FIELD_NUMBER: builtins.int
    DEVICE_PROFILE_NAME_FIELD_NUMBER: builtins.int
    DEVICE_STATUS_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    # Created at timestamp.
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last update timestamp.
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last seen at timestamp.
    @property
    def last_seen_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Name.
    name: typing.Text = ...
    # Description.
    description: typing.Text = ...
    # Device-profile ID (UUID).
    device_profile_id: typing.Text = ...
    # Device-profile name.
    device_profile_name: typing.Text = ...
    # Device status.
    @property
    def device_status(self) -> global___DeviceStatus: ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_seen_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        name : typing.Text = ...,
        description : typing.Text = ...,
        device_profile_id : typing.Text = ...,
        device_profile_name : typing.Text = ...,
        device_status : typing.Optional[global___DeviceStatus] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"device_status",b"device_status",u"last_seen_at",b"last_seen_at",u"updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"description",b"description",u"dev_eui",b"dev_eui",u"device_profile_id",b"device_profile_id",u"device_profile_name",b"device_profile_name",u"device_status",b"device_status",u"last_seen_at",b"last_seen_at",u"name",b"name",u"updated_at",b"updated_at"]) -> None: ...
global___DeviceListItem = DeviceListItem

class DeviceKeys(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    NWK_KEY_FIELD_NUMBER: builtins.int
    APP_KEY_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    # Network root key (128 bit).
    # Note: For LoRaWAN 1.0.x, use this field for the LoRaWAN 1.0.x 'AppKey`!
    nwk_key: typing.Text = ...
    # Application root key (128 bit).
    # Note: This field only needs to be set for LoRaWAN 1.1.x devices!
    app_key: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        nwk_key : typing.Text = ...,
        app_key : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"app_key",b"app_key",u"dev_eui",b"dev_eui",u"nwk_key",b"nwk_key"]) -> None: ...
global___DeviceKeys = DeviceKeys

class CreateDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_FIELD_NUMBER: builtins.int
    # Device object.
    @property
    def device(self) -> global___Device: ...
    def __init__(self,
        *,
        device : typing.Optional[global___Device] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device",b"device"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device",b"device"]) -> None: ...
global___CreateDeviceRequest = CreateDeviceRequest

class GetDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___GetDeviceRequest = GetDeviceRequest

class GetDeviceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    LAST_SEEN_AT_FIELD_NUMBER: builtins.int
    DEVICE_STATUS_FIELD_NUMBER: builtins.int
    # Device object.
    @property
    def device(self) -> global___Device: ...
    # Created at timestamp.
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last update timestamp.
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last seen at timestamp.
    @property
    def last_seen_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Device status.
    @property
    def device_status(self) -> global___DeviceStatus: ...
    def __init__(self,
        *,
        device : typing.Optional[global___Device] = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_seen_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        device_status : typing.Optional[global___DeviceStatus] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"device",b"device",u"device_status",b"device_status",u"last_seen_at",b"last_seen_at",u"updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"device",b"device",u"device_status",b"device_status",u"last_seen_at",b"last_seen_at",u"updated_at",b"updated_at"]) -> None: ...
global___GetDeviceResponse = GetDeviceResponse

class UpdateDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_FIELD_NUMBER: builtins.int
    # Device object.
    @property
    def device(self) -> global___Device: ...
    def __init__(self,
        *,
        device : typing.Optional[global___Device] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device",b"device"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device",b"device"]) -> None: ...
global___UpdateDeviceRequest = UpdateDeviceRequest

class DeleteDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___DeleteDeviceRequest = DeleteDeviceRequest

class ListDevicesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LIMIT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    SEARCH_FIELD_NUMBER: builtins.int
    APPLICATION_ID_FIELD_NUMBER: builtins.int
    MULTICAST_GROUP_ID_FIELD_NUMBER: builtins.int
    # Max number of devices to return in the result-set.
    limit: builtins.int = ...
    # Offset in the result-set (for pagination).
    offset: builtins.int = ...
    # If set, the given string will be used to search on name (optional).
    search: typing.Text = ...
    # Application ID (UUID) to filter devices on.
    application_id: typing.Text = ...
    # Multicst-group ID (UUID) to filter devices on.
    multicast_group_id: typing.Text = ...
    def __init__(self,
        *,
        limit : builtins.int = ...,
        offset : builtins.int = ...,
        search : typing.Text = ...,
        application_id : typing.Text = ...,
        multicast_group_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"application_id",b"application_id",u"limit",b"limit",u"multicast_group_id",b"multicast_group_id",u"offset",b"offset",u"search",b"search"]) -> None: ...
global___ListDevicesRequest = ListDevicesRequest

class ListDevicesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    # Total number of devices.
    total_count: builtins.int = ...
    # Result-set.
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeviceListItem]: ...
    def __init__(self,
        *,
        total_count : builtins.int = ...,
        result : typing.Optional[typing.Iterable[global___DeviceListItem]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"result",b"result",u"total_count",b"total_count"]) -> None: ...
global___ListDevicesResponse = ListDevicesResponse

class CreateDeviceKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_KEYS_FIELD_NUMBER: builtins.int
    # Device-keys object.
    @property
    def device_keys(self) -> global___DeviceKeys: ...
    def __init__(self,
        *,
        device_keys : typing.Optional[global___DeviceKeys] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device_keys",b"device_keys"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device_keys",b"device_keys"]) -> None: ...
global___CreateDeviceKeysRequest = CreateDeviceKeysRequest

class GetDeviceKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___GetDeviceKeysRequest = GetDeviceKeysRequest

class GetDeviceKeysResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_KEYS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    # Device-keys object.
    @property
    def device_keys(self) -> global___DeviceKeys: ...
    # Created at timestamp.
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last update timestamp.
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        device_keys : typing.Optional[global___DeviceKeys] = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"device_keys",b"device_keys",u"updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"device_keys",b"device_keys",u"updated_at",b"updated_at"]) -> None: ...
global___GetDeviceKeysResponse = GetDeviceKeysResponse

class UpdateDeviceKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_KEYS_FIELD_NUMBER: builtins.int
    # Device-keys object.
    @property
    def device_keys(self) -> global___DeviceKeys: ...
    def __init__(self,
        *,
        device_keys : typing.Optional[global___DeviceKeys] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device_keys",b"device_keys"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device_keys",b"device_keys"]) -> None: ...
global___UpdateDeviceKeysRequest = UpdateDeviceKeysRequest

class DeleteDeviceKeysRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___DeleteDeviceKeysRequest = DeleteDeviceKeysRequest

class DeviceActivation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    DEV_ADDR_FIELD_NUMBER: builtins.int
    APP_S_KEY_FIELD_NUMBER: builtins.int
    NWK_S_ENC_KEY_FIELD_NUMBER: builtins.int
    S_NWK_S_INT_KEY_FIELD_NUMBER: builtins.int
    F_NWK_S_INT_KEY_FIELD_NUMBER: builtins.int
    F_CNT_UP_FIELD_NUMBER: builtins.int
    N_F_CNT_DOWN_FIELD_NUMBER: builtins.int
    A_F_CNT_DOWN_FIELD_NUMBER: builtins.int
    # Device EUI (EUI64).
    dev_eui: typing.Text = ...
    # Device address (HEX encoded).
    dev_addr: typing.Text = ...
    # Application session key (HEX encoded).
    app_s_key: typing.Text = ...
    # Network session encryption key (HEX encoded).
    nwk_s_enc_key: typing.Text = ...
    # Serving network session integrity key (HEX encoded).
    s_nwk_s_int_key: typing.Text = ...
    # Forwarding network session integrity key (HEX encoded).
    f_nwk_s_int_key: typing.Text = ...
    # Uplink frame-counter.
    f_cnt_up: builtins.int = ...
    # Downlink network frame-counter.
    n_f_cnt_down: builtins.int = ...
    # Downlink application frame-counter.
    a_f_cnt_down: builtins.int = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        dev_addr : typing.Text = ...,
        app_s_key : typing.Text = ...,
        nwk_s_enc_key : typing.Text = ...,
        s_nwk_s_int_key : typing.Text = ...,
        f_nwk_s_int_key : typing.Text = ...,
        f_cnt_up : builtins.int = ...,
        n_f_cnt_down : builtins.int = ...,
        a_f_cnt_down : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"a_f_cnt_down",b"a_f_cnt_down",u"app_s_key",b"app_s_key",u"dev_addr",b"dev_addr",u"dev_eui",b"dev_eui",u"f_cnt_up",b"f_cnt_up",u"f_nwk_s_int_key",b"f_nwk_s_int_key",u"n_f_cnt_down",b"n_f_cnt_down",u"nwk_s_enc_key",b"nwk_s_enc_key",u"s_nwk_s_int_key",b"s_nwk_s_int_key"]) -> None: ...
global___DeviceActivation = DeviceActivation

class ActivateDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_ACTIVATION_FIELD_NUMBER: builtins.int
    # Device activation object.
    @property
    def device_activation(self) -> global___DeviceActivation: ...
    def __init__(self,
        *,
        device_activation : typing.Optional[global___DeviceActivation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device_activation",b"device_activation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device_activation",b"device_activation"]) -> None: ...
global___ActivateDeviceRequest = ActivateDeviceRequest

class DeactivateDeviceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___DeactivateDeviceRequest = DeactivateDeviceRequest

class GetDeviceActivationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___GetDeviceActivationRequest = GetDeviceActivationRequest

class GetDeviceActivationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEVICE_ACTIVATION_FIELD_NUMBER: builtins.int
    # Device activation object.
    @property
    def device_activation(self) -> global___DeviceActivation: ...
    def __init__(self,
        *,
        device_activation : typing.Optional[global___DeviceActivation] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"device_activation",b"device_activation"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"device_activation",b"device_activation"]) -> None: ...
global___GetDeviceActivationResponse = GetDeviceActivationResponse

class GetRandomDevAddrRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___GetRandomDevAddrRequest = GetRandomDevAddrRequest

class GetRandomDevAddrResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_ADDR_FIELD_NUMBER: builtins.int
    # DevAddr.
    dev_addr: typing.Text = ...
    def __init__(self,
        *,
        dev_addr : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_addr",b"dev_addr"]) -> None: ...
global___GetRandomDevAddrResponse = GetRandomDevAddrResponse

class GetDeviceMetricsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    AGGREGATION_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    # Interval start timestamp.
    @property
    def start(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Interval end timestamp.
    @property
    def end(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Aggregation.
    aggregation: chirpstack_api.common.common_pb2.Aggregation.V = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        start : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        aggregation : chirpstack_api.common.common_pb2.Aggregation.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"end",b"end",u"start",b"start"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"aggregation",b"aggregation",u"dev_eui",b"dev_eui",u"end",b"end",u"start",b"start"]) -> None: ...
global___GetDeviceMetricsRequest = GetDeviceMetricsRequest

class GetDeviceMetricsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class MetricsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> chirpstack_api.common.common_pb2.Metric: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[chirpstack_api.common.common_pb2.Metric] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class StatesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___DeviceState: ...
        def __init__(self,
            *,
            key : typing.Text = ...,
            value : typing.Optional[global___DeviceState] = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    METRICS_FIELD_NUMBER: builtins.int
    STATES_FIELD_NUMBER: builtins.int
    @property
    def metrics(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, chirpstack_api.common.common_pb2.Metric]: ...
    @property
    def states(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, global___DeviceState]: ...
    def __init__(self,
        *,
        metrics : typing.Optional[typing.Mapping[typing.Text, chirpstack_api.common.common_pb2.Metric]] = ...,
        states : typing.Optional[typing.Mapping[typing.Text, global___DeviceState]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"metrics",b"metrics",u"states",b"states"]) -> None: ...
global___GetDeviceMetricsResponse = GetDeviceMetricsResponse

class DeviceState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    # Name.
    name: typing.Text = ...
    # Value.
    value: typing.Text = ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        value : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"value",b"value"]) -> None: ...
global___DeviceState = DeviceState

class GetDeviceLinkMetricsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    AGGREGATION_FIELD_NUMBER: builtins.int
    # DevEUI (EUI64).
    dev_eui: typing.Text = ...
    # Interval start timestamp.
    @property
    def start(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Interval end timestamp.
    @property
    def end(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Aggregation.
    aggregation: chirpstack_api.common.common_pb2.Aggregation.V = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        start : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        end : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        aggregation : chirpstack_api.common.common_pb2.Aggregation.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"end",b"end",u"start",b"start"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"aggregation",b"aggregation",u"dev_eui",b"dev_eui",u"end",b"end",u"start",b"start"]) -> None: ...
global___GetDeviceLinkMetricsRequest = GetDeviceLinkMetricsRequest

class GetDeviceLinkMetricsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RX_PACKETS_FIELD_NUMBER: builtins.int
    GW_RSSI_FIELD_NUMBER: builtins.int
    GW_SNR_FIELD_NUMBER: builtins.int
    RX_PACKETS_PER_FREQ_FIELD_NUMBER: builtins.int
    RX_PACKETS_PER_DR_FIELD_NUMBER: builtins.int
    ERRORS_FIELD_NUMBER: builtins.int
    # Packets received from the device.
    @property
    def rx_packets(self) -> chirpstack_api.common.common_pb2.Metric: ...
    # RSSI (as reported by the gateway(s)).
    @property
    def gw_rssi(self) -> chirpstack_api.common.common_pb2.Metric: ...
    # SNR (as reported by the gateway(s)).
    @property
    def gw_snr(self) -> chirpstack_api.common.common_pb2.Metric: ...
    # Packets received by frequency.
    @property
    def rx_packets_per_freq(self) -> chirpstack_api.common.common_pb2.Metric: ...
    # Packets received by DR.
    @property
    def rx_packets_per_dr(self) -> chirpstack_api.common.common_pb2.Metric: ...
    # Errors.
    @property
    def errors(self) -> chirpstack_api.common.common_pb2.Metric: ...
    def __init__(self,
        *,
        rx_packets : typing.Optional[chirpstack_api.common.common_pb2.Metric] = ...,
        gw_rssi : typing.Optional[chirpstack_api.common.common_pb2.Metric] = ...,
        gw_snr : typing.Optional[chirpstack_api.common.common_pb2.Metric] = ...,
        rx_packets_per_freq : typing.Optional[chirpstack_api.common.common_pb2.Metric] = ...,
        rx_packets_per_dr : typing.Optional[chirpstack_api.common.common_pb2.Metric] = ...,
        errors : typing.Optional[chirpstack_api.common.common_pb2.Metric] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"errors",b"errors",u"gw_rssi",b"gw_rssi",u"gw_snr",b"gw_snr",u"rx_packets",b"rx_packets",u"rx_packets_per_dr",b"rx_packets_per_dr",u"rx_packets_per_freq",b"rx_packets_per_freq"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"errors",b"errors",u"gw_rssi",b"gw_rssi",u"gw_snr",b"gw_snr",u"rx_packets",b"rx_packets",u"rx_packets_per_dr",b"rx_packets_per_dr",u"rx_packets_per_freq",b"rx_packets_per_freq"]) -> None: ...
global___GetDeviceLinkMetricsResponse = GetDeviceLinkMetricsResponse

class DeviceQueueItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    DEV_EUI_FIELD_NUMBER: builtins.int
    CONFIRMED_FIELD_NUMBER: builtins.int
    F_PORT_FIELD_NUMBER: builtins.int
    DATA_FIELD_NUMBER: builtins.int
    OBJECT_FIELD_NUMBER: builtins.int
    IS_PENDING_FIELD_NUMBER: builtins.int
    F_CNT_DOWN_FIELD_NUMBER: builtins.int
    # ID (UUID).
    # This is automatically generated on enqueue.
    id: typing.Text = ...
    # Device EUI (EUI64).
    dev_eui: typing.Text = ...
    # Confirmed.
    confirmed: builtins.bool = ...
    # FPort (must be > 0).
    f_port: builtins.int = ...
    # Data.
    # Or use the json_object field when a codec has been configured.
    data: builtins.bytes = ...
    # Only use this when a codec has been configured that can encode this
    # object to bytes.
    @property
    def object(self) -> google.protobuf.struct_pb2.Struct: ...
    # Is pending.
    # This is set to true when the downlink is pending.
    is_pending: builtins.bool = ...
    # Downlink frame-counter.
    # This is set when the payload has been sent as downlink.
    f_cnt_down: builtins.int = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        dev_eui : typing.Text = ...,
        confirmed : builtins.bool = ...,
        f_port : builtins.int = ...,
        data : builtins.bytes = ...,
        object : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        is_pending : builtins.bool = ...,
        f_cnt_down : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"object",b"object"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"confirmed",b"confirmed",u"data",b"data",u"dev_eui",b"dev_eui",u"f_cnt_down",b"f_cnt_down",u"f_port",b"f_port",u"id",b"id",u"is_pending",b"is_pending",u"object",b"object"]) -> None: ...
global___DeviceQueueItem = DeviceQueueItem

class EnqueueDeviceQueueItemRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    QUEUE_ITEM_FIELD_NUMBER: builtins.int
    @property
    def queue_item(self) -> global___DeviceQueueItem: ...
    def __init__(self,
        *,
        queue_item : typing.Optional[global___DeviceQueueItem] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"queue_item",b"queue_item"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"queue_item",b"queue_item"]) -> None: ...
global___EnqueueDeviceQueueItemRequest = EnqueueDeviceQueueItemRequest

class EnqueueDeviceQueueItemResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    # ID (UUID).
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___EnqueueDeviceQueueItemResponse = EnqueueDeviceQueueItemResponse

class FlushDeviceQueueRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # Device EUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___FlushDeviceQueueRequest = FlushDeviceQueueRequest

class GetDeviceQueueItemsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    COUNT_ONLY_FIELD_NUMBER: builtins.int
    # Device EUI (EUI64).
    dev_eui: typing.Text = ...
    # Return only the count, not the result-set.
    count_only: builtins.bool = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        count_only : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"count_only",b"count_only",u"dev_eui",b"dev_eui"]) -> None: ...
global___GetDeviceQueueItemsRequest = GetDeviceQueueItemsRequest

class GetDeviceQueueItemsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    # Total number of queue items.
    total_count: builtins.int = ...
    # Result-set.
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeviceQueueItem]: ...
    def __init__(self,
        *,
        total_count : builtins.int = ...,
        result : typing.Optional[typing.Iterable[global___DeviceQueueItem]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"result",b"result",u"total_count",b"total_count"]) -> None: ...
global___GetDeviceQueueItemsResponse = GetDeviceQueueItemsResponse

class FlushDevNoncesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DEV_EUI_FIELD_NUMBER: builtins.int
    # Device EUI (EUI64).
    dev_eui: typing.Text = ...
    def __init__(self,
        *,
        dev_eui : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dev_eui",b"dev_eui"]) -> None: ...
global___FlushDevNoncesRequest = FlushDevNoncesRequest
