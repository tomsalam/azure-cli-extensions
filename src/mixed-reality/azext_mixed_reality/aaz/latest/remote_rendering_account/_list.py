# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "remote-rendering-account list",
    is_preview=True,
)
class List(AAZCommand):
    """List Remote Rendering Accounts by Subscription

    :example: List remote rendering accounts by resource group
        az remote-rendering-account list --resource-group "MyResourceGroup"

    :example: List remote rendering accounts by subscription
        az remote-rendering-account list
    """

    _aaz_info = {
        "version": "2021-03-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.mixedreality/remoterenderingaccounts", "2021-03-01-preview"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.mixedreality/remoterenderingaccounts", "2021-03-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.RemoteRenderingAccountsListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.RemoteRenderingAccountsListBySubscription(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class RemoteRenderingAccountsListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MixedReality/remoteRenderingAccounts",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-03-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _ListHelper._build_schema_identity_read(_element.identity)
            _element.kind = AAZObjectType()
            _ListHelper._build_schema_sku_read(_element.kind)
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.plan = AAZObjectType()
            _ListHelper._build_schema_identity_read(_element.plan)
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _ListHelper._build_schema_sku_read(_element.sku)
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.account_domain = AAZStrType(
                serialized_name="accountDomain",
                flags={"read_only": True},
            )
            properties.account_id = AAZStrType(
                serialized_name="accountId",
                flags={"read_only": True},
            )
            properties.storage_account_name = AAZStrType(
                serialized_name="storageAccountName",
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class RemoteRenderingAccountsListBySubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.MixedReality/remoteRenderingAccounts",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-03-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _ListHelper._build_schema_identity_read(_element.identity)
            _element.kind = AAZObjectType()
            _ListHelper._build_schema_sku_read(_element.kind)
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.plan = AAZObjectType()
            _ListHelper._build_schema_identity_read(_element.plan)
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.sku = AAZObjectType()
            _ListHelper._build_schema_sku_read(_element.sku)
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.account_domain = AAZStrType(
                serialized_name="accountDomain",
                flags={"read_only": True},
            )
            properties.account_id = AAZStrType(
                serialized_name="accountId",
                flags={"read_only": True},
            )
            properties.storage_account_name = AAZStrType(
                serialized_name="storageAccountName",
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_identity_read = None

    @classmethod
    def _build_schema_identity_read(cls, _schema):
        if cls._schema_identity_read is not None:
            _schema.principal_id = cls._schema_identity_read.principal_id
            _schema.tenant_id = cls._schema_identity_read.tenant_id
            _schema.type = cls._schema_identity_read.type
            return

        cls._schema_identity_read = _schema_identity_read = AAZObjectType()

        identity_read = _schema_identity_read
        identity_read.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity_read.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity_read.type = AAZStrType()

        _schema.principal_id = cls._schema_identity_read.principal_id
        _schema.tenant_id = cls._schema_identity_read.tenant_id
        _schema.type = cls._schema_identity_read.type

    _schema_sku_read = None

    @classmethod
    def _build_schema_sku_read(cls, _schema):
        if cls._schema_sku_read is not None:
            _schema.capacity = cls._schema_sku_read.capacity
            _schema.family = cls._schema_sku_read.family
            _schema.name = cls._schema_sku_read.name
            _schema.size = cls._schema_sku_read.size
            _schema.tier = cls._schema_sku_read.tier
            return

        cls._schema_sku_read = _schema_sku_read = AAZObjectType()

        sku_read = _schema_sku_read
        sku_read.capacity = AAZIntType()
        sku_read.family = AAZStrType()
        sku_read.name = AAZStrType(
            flags={"required": True},
        )
        sku_read.size = AAZStrType()
        sku_read.tier = AAZStrType()

        _schema.capacity = cls._schema_sku_read.capacity
        _schema.family = cls._schema_sku_read.family
        _schema.name = cls._schema_sku_read.name
        _schema.size = cls._schema_sku_read.size
        _schema.tier = cls._schema_sku_read.tier


__all__ = ["List"]