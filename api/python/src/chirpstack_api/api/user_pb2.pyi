"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class User(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    IS_ADMIN_FIELD_NUMBER: builtins.int
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    NOTE_FIELD_NUMBER: builtins.int
    # User ID (UUID).
    # Will be set automatically on create.
    id: typing.Text = ...
    # Set to true to make the user a global administrator.
    is_admin: builtins.bool = ...
    # Set to false to disable the user.
    is_active: builtins.bool = ...
    # E-mail of the user.
    email: typing.Text = ...
    # Optional note to store with the user.
    note: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        is_admin : builtins.bool = ...,
        is_active : builtins.bool = ...,
        email : typing.Text = ...,
        note : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"email",b"email",u"id",b"id",u"is_active",b"is_active",u"is_admin",b"is_admin",u"note",b"note"]) -> None: ...
global___User = User

class UserListItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    IS_ADMIN_FIELD_NUMBER: builtins.int
    IS_ACTIVE_FIELD_NUMBER: builtins.int
    # User ID (UUID).
    id: typing.Text = ...
    # Created at timestamp.
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last update timestamp.
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Email of the user.
    email: typing.Text = ...
    # Set to true to make the user a global administrator.
    is_admin: builtins.bool = ...
    # Set to false to disable the user.
    is_active: builtins.bool = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        email : typing.Text = ...,
        is_admin : builtins.bool = ...,
        is_active : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"updated_at",b"updated_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"email",b"email",u"id",b"id",u"is_active",b"is_active",u"is_admin",b"is_admin",u"updated_at",b"updated_at"]) -> None: ...
global___UserListItem = UserListItem

class UserTenant(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TENANT_ID_FIELD_NUMBER: builtins.int
    IS_ADMIN_FIELD_NUMBER: builtins.int
    IS_DEVICE_ADMIN_FIELD_NUMBER: builtins.int
    IS_GATEWAY_ADMIN_FIELD_NUMBER: builtins.int
    # Tenant ID.
    tenant_id: typing.Text = ...
    # User is admin within the context of the tenant.
    # There is no need to set the is_device_admin and is_gateway_admin flags.
    is_admin: builtins.bool = ...
    # User is able to modify device related resources (applications,
    # device-profiles, devices, multicast-groups).
    is_device_admin: builtins.bool = ...
    # User is able to modify gateways.
    is_gateway_admin: builtins.bool = ...
    def __init__(self,
        *,
        tenant_id : typing.Text = ...,
        is_admin : builtins.bool = ...,
        is_device_admin : builtins.bool = ...,
        is_gateway_admin : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"is_admin",b"is_admin",u"is_device_admin",b"is_device_admin",u"is_gateway_admin",b"is_gateway_admin",u"tenant_id",b"tenant_id"]) -> None: ...
global___UserTenant = UserTenant

class CreateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    TENANTS_FIELD_NUMBER: builtins.int
    # User object to create.
    @property
    def user(self) -> global___User: ...
    # Password to set for the user.
    password: typing.Text = ...
    # Add the user to the following tenants.
    @property
    def tenants(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserTenant]: ...
    def __init__(self,
        *,
        user : typing.Optional[global___User] = ...,
        password : typing.Text = ...,
        tenants : typing.Optional[typing.Iterable[global___UserTenant]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"password",b"password",u"tenants",b"tenants",u"user",b"user"]) -> None: ...
global___CreateUserRequest = CreateUserRequest

class CreateUserResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    # User ID.
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___CreateUserResponse = CreateUserResponse

class GetUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    # User ID.
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___GetUserRequest = GetUserRequest

class GetUserResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    UPDATED_AT_FIELD_NUMBER: builtins.int
    # User object.
    @property
    def user(self) -> global___User: ...
    # Created at timestamp.
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    # Last update timestamp.
    @property
    def updated_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        user : typing.Optional[global___User] = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        updated_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"updated_at",b"updated_at",u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"updated_at",b"updated_at",u"user",b"user"]) -> None: ...
global___GetUserResponse = GetUserResponse

class UpdateUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_FIELD_NUMBER: builtins.int
    # User object.
    @property
    def user(self) -> global___User: ...
    def __init__(self,
        *,
        user : typing.Optional[global___User] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"user",b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"user",b"user"]) -> None: ...
global___UpdateUserRequest = UpdateUserRequest

class DeleteUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    # User ID.
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___DeleteUserRequest = DeleteUserRequest

class ListUsersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LIMIT_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    # Max number of tenants to return in the result-set.
    limit: builtins.int = ...
    # Offset in the result-set (for pagination).
    offset: builtins.int = ...
    def __init__(self,
        *,
        limit : builtins.int = ...,
        offset : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"limit",b"limit",u"offset",b"offset"]) -> None: ...
global___ListUsersRequest = ListUsersRequest

class ListUsersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    # Total number of users.
    total_count: builtins.int = ...
    # Result-set.
    @property
    def result(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserListItem]: ...
    def __init__(self,
        *,
        total_count : builtins.int = ...,
        result : typing.Optional[typing.Iterable[global___UserListItem]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"result",b"result",u"total_count",b"total_count"]) -> None: ...
global___ListUsersResponse = ListUsersResponse

class UpdateUserPasswordRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_ID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    # User ID.
    user_id: typing.Text = ...
    # Password to set.
    password: typing.Text = ...
    def __init__(self,
        *,
        user_id : typing.Text = ...,
        password : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"password",b"password",u"user_id",b"user_id"]) -> None: ...
global___UpdateUserPasswordRequest = UpdateUserPasswordRequest