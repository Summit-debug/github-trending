# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.cwp.v20180228 import models


class CwpClient(AbstractClient):
    _apiVersion = '2018-02-28'
    _endpoint = 'cwp.tencentcloudapi.com'
    _service = 'cwp'


    def CancelIgnoreVul(self, request):
        """取消漏洞忽略

        :param request: Request instance for CancelIgnoreVul.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CancelIgnoreVulRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CancelIgnoreVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelIgnoreVul", params, headers=headers)
            response = json.loads(body)
            model = models.CancelIgnoreVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeRuleEventsIgnoreStatus(self, request):
        """根据检测项id或事件id批量忽略事件或取消忽略

        :param request: Request instance for ChangeRuleEventsIgnoreStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ChangeRuleEventsIgnoreStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ChangeRuleEventsIgnoreStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeRuleEventsIgnoreStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeRuleEventsIgnoreStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckBashRuleParams(self, request):
        """校验高危命令用户规则新增和编辑时的参数。

        :param request: Request instance for CheckBashRuleParams.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CheckBashRuleParamsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CheckBashRuleParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckBashRuleParams", params, headers=headers)
            response = json.loads(body)
            model = models.CheckBashRuleParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBaselineStrategy(self, request):
        """根据策略信息创建基线策略

        :param request: Request instance for CreateBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEmergencyVulScan(self, request):
        """创建应急漏洞扫描任务

        :param request: Request instance for CreateEmergencyVulScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateEmergencyVulScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateEmergencyVulScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEmergencyVulScan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEmergencyVulScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLicenseOrder(self, request):
        """CreateLicenseOrder 该接口可以创建专业版/旗舰版订单
        支持预付费后付费创建
        后付费订单直接创建成功
        预付费订单仅下单不支付,需要调用计费支付接口进行支付

        :param request: Request instance for CreateLicenseOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateLicenseOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateLicenseOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLicenseOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLicenseOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProtectServer(self, request):
        """添加网站防护服务器

        :param request: Request instance for CreateProtectServer.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateProtectServerRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateProtectServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProtectServer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProtectServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateScanMalwareSetting(self, request):
        """该接口可以对入侵检测-文件查杀扫描检测

        :param request: Request instance for CreateScanMalwareSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateScanMalwareSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateScanMalwareSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScanMalwareSetting", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScanMalwareSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSearchLog(self, request):
        """添加历史搜索记录

        :param request: Request instance for CreateSearchLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateSearchLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateSearchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSearchLog", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSearchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSearchTemplate(self, request):
        """添加检索模板

        :param request: Request instance for CreateSearchTemplate.
        :type request: :class:`tencentcloud.cwp.v20180228.models.CreateSearchTemplateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.CreateSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSearchTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSearchTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAttackLogs(self, request):
        """删除网络攻击日志

        :param request: Request instance for DeleteAttackLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteAttackLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteAttackLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAttackLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAttackLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselinePolicy(self, request):
        """删除基线策略配置

        :param request: Request instance for DeleteBaselinePolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineRule(self, request):
        """删除基线规则

        :param request: Request instance for DeleteBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineRuleIgnore(self, request):
        """删除基线忽略规则

        :param request: Request instance for DeleteBaselineRuleIgnore.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineRuleIgnoreRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineRuleIgnoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineRuleIgnore", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineRuleIgnoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineStrategy(self, request):
        """根据基线策略id删除策略

        :param request: Request instance for DeleteBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBaselineWeakPassword(self, request):
        """删除基线弱口令

        :param request: Request instance for DeleteBaselineWeakPassword.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineWeakPasswordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBaselineWeakPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaselineWeakPassword", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaselineWeakPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashEvents(self, request):
        """根据Ids删除高危命令事件

        :param request: Request instance for DeleteBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBashRules(self, request):
        """删除高危命令规则

        :param request: Request instance for DeleteBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBruteAttacks(self, request):
        """本接口 (DeleteBruteAttacks) 用于删除暴力破解记录。

        :param request: Request instance for DeleteBruteAttacks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteBruteAttacksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLicenseRecord(self, request):
        """对授权管理-订单列表内已过期的订单进行删除.(删除后的订单不在统计范畴内)

        :param request: Request instance for DeleteLicenseRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLicenseRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLicenseRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLicenseRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLoginWhiteList(self, request):
        """本接口用于删除异地登录白名单规则。

        :param request: Request instance for DeleteLoginWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachine(self, request):
        """本接口（DeleteMachine）用于卸载主机安全客户端。

        :param request: Request instance for DeleteMachine.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMachineTag(self, request):
        """删除服务器关联的标签

        :param request: Request instance for DeleteMachineTag.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineTagRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMachineTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMachineTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMachineTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMaliciousRequests(self, request):
        """本接口 (DeleteMaliciousRequests) 用于删除恶意请求记录。

        :param request: Request instance for DeleteMaliciousRequests.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwareScanTask(self, request):
        """入侵管理-终止扫描任务

        :param request: Request instance for DeleteMalwareScanTask.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareScanTaskRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwareScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwareScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwareScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMalwares(self, request):
        """本接口 (DeleteMalwares) 用于删除木马记录。

        :param request: Request instance for DeleteMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNonlocalLoginPlaces(self, request):
        """本接口 (DeleteNonlocalLoginPlaces) 用于删除异地登录记录。

        :param request: Request instance for DeleteNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivilegeEvents(self, request):
        """根据Ids删除本地提权

        :param request: Request instance for DeletePrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivilegeRules(self, request):
        """删除本地提权规则

        :param request: Request instance for DeletePrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeletePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProtectDir(self, request):
        """删除防护网站

        :param request: Request instance for DeleteProtectDir.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteProtectDirRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteProtectDirResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProtectDir", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProtectDirResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellEvents(self, request):
        """根据Ids删除反弹Shell事件

        :param request: Request instance for DeleteReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReverseShellRules(self, request):
        """删除反弹Shell规则

        :param request: Request instance for DeleteReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScanTask(self, request):
        """DeleteScanTask 该接口可以对指定类型的扫描任务进行停止扫描;

        :param request: Request instance for DeleteScanTask.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteScanTaskRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteScanTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScanTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScanTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSearchTemplate(self, request):
        """删除检索模板

        :param request: Request instance for DeleteSearchTemplate.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteSearchTemplateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteSearchTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSearchTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSearchTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTags(self, request):
        """删除标签

        :param request: Request instance for DeleteTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTags", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWebPageEventLog(self, request):
        """网站防篡改-删除事件记录

        :param request: Request instance for DeleteWebPageEventLog.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DeleteWebPageEventLogRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DeleteWebPageEventLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWebPageEventLog", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWebPageEventLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountStatistics(self, request):
        """本接口 (DescribeAccountStatistics) 用于获取帐号统计列表数据。

        :param request: Request instance for DescribeAccountStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAccountStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAgentInstallCommand(self, request):
        """获取agent安装命令

        :param request: Request instance for DescribeAgentInstallCommand.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallCommandRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAgentInstallCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAgentInstallCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAgentInstallCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmIncidentNodes(self, request):
        """获取告警点所在事件的所有节点信息

        :param request: Request instance for DescribeAlarmIncidentNodes.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmIncidentNodesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmIncidentNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmIncidentNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmIncidentNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlarmVertexId(self, request):
        """查询告警点id列表

        :param request: Request instance for DescribeAlarmVertexId.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmVertexIdRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmVertexIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmVertexId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmVertexIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppList(self, request):
        """查询应用列表

        :param request: Request instance for DescribeAssetAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetAppProcessList(self, request):
        """获取软件关联进程列表

        :param request: Request instance for DescribeAssetAppProcessList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppProcessListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetAppProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetAppProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetCoreModuleInfo(self, request):
        """获取内核模块详情

        :param request: Request instance for DescribeAssetCoreModuleInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetCoreModuleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetCoreModuleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetCoreModuleList(self, request):
        """查询资产管理内核模块列表

        :param request: Request instance for DescribeAssetCoreModuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetCoreModuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetCoreModuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetCoreModuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDatabaseInfo(self, request):
        """获取资产管理数据库详情

        :param request: Request instance for DescribeAssetDatabaseInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDatabaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDatabaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetDatabaseList(self, request):
        """查询资产管理数据库列表

        :param request: Request instance for DescribeAssetDatabaseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetDatabaseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetDatabaseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetDatabaseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetEnvList(self, request):
        """查询资产管理环境变量列表

        :param request: Request instance for DescribeAssetEnvList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetEnvListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetEnvListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetEnvList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetEnvListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetHostTotalCount(self, request):
        """获取主机所有资源数量

        :param request: Request instance for DescribeAssetHostTotalCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetHostTotalCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetHostTotalCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetHostTotalCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetHostTotalCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetInfo(self, request):
        """获取资产数量： 主机数、账号数、端口数、进程数、软件数、数据库数、Web应用数、Web框架数、Web服务数、Web站点数

        :param request: Request instance for DescribeAssetInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetInitServiceList(self, request):
        """查询资产管理启动服务列表

        :param request: Request instance for DescribeAssetInitServiceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInitServiceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetInitServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetInitServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetInitServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetJarInfo(self, request):
        """获取Jar包详情

        :param request: Request instance for DescribeAssetJarInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetJarInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetJarInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetJarList(self, request):
        """查询Jar包列表

        :param request: Request instance for DescribeAssetJarList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetJarListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetJarList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetJarListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetMachineDetail(self, request):
        """获取资产管理主机资源详细信息

        :param request: Request instance for DescribeAssetMachineDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetMachineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetMachineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetMachineList(self, request):
        """获取资产指纹页面的资源监控列表

        :param request: Request instance for DescribeAssetMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPlanTaskList(self, request):
        """查询资产管理计划任务列表

        :param request: Request instance for DescribeAssetPlanTaskList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPlanTaskListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPlanTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPlanTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPlanTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetPortInfoList(self, request):
        """获取资产管理端口列表

        :param request: Request instance for DescribeAssetPortInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetPortInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetPortInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetPortInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetProcessInfoList(self, request):
        """获取资产管理进程列表

        :param request: Request instance for DescribeAssetProcessInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetProcessInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetProcessInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetProcessInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetRecentMachineInfo(self, request):
        """获取主机最近趋势情况

        :param request: Request instance for DescribeAssetRecentMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetRecentMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetRecentMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetRecentMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetRecentMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSystemPackageList(self, request):
        """获取资产管理系统安装包列表

        :param request: Request instance for DescribeAssetSystemPackageList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetSystemPackageListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetSystemPackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSystemPackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSystemPackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserInfo(self, request):
        """获取主机账号详情

        :param request: Request instance for DescribeAssetUserInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetUserList(self, request):
        """获取账号列表

        :param request: Request instance for DescribeAssetUserList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebAppList(self, request):
        """获取资产管理Web应用列表

        :param request: Request instance for DescribeAssetWebAppList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebAppList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebAppListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebAppPluginList(self, request):
        """获取资产管理Web应用插件列表

        :param request: Request instance for DescribeAssetWebAppPluginList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppPluginListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebAppPluginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebAppPluginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebAppPluginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebFrameList(self, request):
        """获取资产管理Web框架列表

        :param request: Request instance for DescribeAssetWebFrameList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebFrameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebFrameList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebFrameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationInfo(self, request):
        """获取Web站点详情

        :param request: Request instance for DescribeAssetWebLocationInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebLocationList(self, request):
        """获取Web站点列表

        :param request: Request instance for DescribeAssetWebLocationList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebLocationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebLocationList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebLocationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceInfoList(self, request):
        """查询资产管理Web服务列表

        :param request: Request instance for DescribeAssetWebServiceInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetWebServiceProcessList(self, request):
        """获取Web服务关联进程列表

        :param request: Request instance for DescribeAssetWebServiceProcessList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceProcessListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetWebServiceProcessListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetWebServiceProcessList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetWebServiceProcessListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackEvents(self, request):
        """按分页形式展示网络攻击检测事件列表

        :param request: Request instance for DescribeAttackEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackLogInfo(self, request):
        """网络攻击日志详情

        :param request: Request instance for DescribeAttackLogInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackLogInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackLogInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackLogs(self, request):
        """按分页形式展示网络攻击日志列表

        :param request: Request instance for DescribeAttackLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAttackVulTypeList(self, request):
        """获取网络攻击威胁类型列表

        :param request: Request instance for DescribeAttackVulTypeList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackVulTypeListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAttackVulTypeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAttackVulTypeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAttackVulTypeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableExpertServiceDetail(self, request):
        """专家服务-可用订单详情

        :param request: Request instance for DescribeAvailableExpertServiceDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAvailableExpertServiceDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAvailableExpertServiceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableExpertServiceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableExpertServiceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanMode(self, request):
        """获取爆破阻断模式

        :param request: Request instance for DescribeBanMode.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanModeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanRegions(self, request):
        """获取阻断地域

        :param request: Request instance for DescribeBanRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanStatus(self, request):
        """获取阻断按钮状态

        :param request: Request instance for DescribeBanStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBanWhiteList(self, request):
        """获取阻断白名单列表

        :param request: Request instance for DescribeBanWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBanWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBanWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBanWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBanWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineAnalysisData(self, request):
        """根据基线策略id查询基线策略数据概览统计

        :param request: Request instance for DescribeBaselineAnalysisData.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineAnalysisDataRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineAnalysisDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineAnalysisData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineAnalysisDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineBasicInfo(self, request):
        """查询基线基础信息列表

        :param request: Request instance for DescribeBaselineBasicInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineBasicInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineBasicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineBasicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineBasicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDetail(self, request):
        """根据基线id查询基线详情接口

        :param request: Request instance for DescribeBaselineDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDetectList(self, request):
        """获取基线检测详情记录

        :param request: Request instance for DescribeBaselineDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDetectOverview(self, request):
        """获取基线检测概览

        :param request: Request instance for DescribeBaselineDetectOverview.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetectOverviewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDetectOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDetectOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDetectOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineDownloadList(self, request):
        """获取基线下载列表

        :param request: Request instance for DescribeBaselineDownloadList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDownloadListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineDownloadListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineDownloadList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineDownloadListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineEffectHostList(self, request):
        """根据基线id查询基线影响主机列表

        :param request: Request instance for DescribeBaselineEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineFixList(self, request):
        """获取基线修复列表

        :param request: Request instance for DescribeBaselineFixList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineFixListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineFixListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineFixList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineFixListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostDetectList(self, request):
        """获取基线检测主机列表

        :param request: Request instance for DescribeBaselineHostDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostIgnoreList(self, request):
        """获取忽略规则主机列表

        :param request: Request instance for DescribeBaselineHostIgnoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostIgnoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostRiskTop(self, request):
        """获取基线服务器风险TOP5

        :param request: Request instance for DescribeBaselineHostRiskTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostRiskTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostRiskTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostRiskTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostRiskTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineHostTop(self, request):
        """接口返回TopN的风险服务器

        :param request: Request instance for DescribeBaselineHostTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineHostTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineHostTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineHostTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemDetectList(self, request):
        """获取基线检测项的列表

        :param request: Request instance for DescribeBaselineItemDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemIgnoreList(self, request):
        """获取忽略规则项列表

        :param request: Request instance for DescribeBaselineItemIgnoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemIgnoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemInfo(self, request):
        """获取基线检测项信息

        :param request: Request instance for DescribeBaselineItemInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemList(self, request):
        """获取基线项检测结果列表

        :param request: Request instance for DescribeBaselineItemList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineItemRiskTop(self, request):
        """获取基线检测项TOP5

        :param request: Request instance for DescribeBaselineItemRiskTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemRiskTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineItemRiskTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineItemRiskTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineItemRiskTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineList(self, request):
        """查询基线列表信息

        :param request: Request instance for DescribeBaselineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselinePolicyList(self, request):
        """获取基线策略列表

        :param request: Request instance for DescribeBaselinePolicyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselinePolicyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselinePolicyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselinePolicyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselinePolicyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRule(self, request):
        """根据基线id查询下属检测项信息

        :param request: Request instance for DescribeBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRuleCategoryList(self, request):
        """获取基线分类列表

        :param request: Request instance for DescribeBaselineRuleCategoryList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleCategoryListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleCategoryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRuleCategoryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleCategoryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRuleDetectList(self, request):
        """获取基线规则检测列表

        :param request: Request instance for DescribeBaselineRuleDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRuleDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRuleIgnoreList(self, request):
        """获取基线忽略规则列表

        :param request: Request instance for DescribeBaselineRuleIgnoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleIgnoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleIgnoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRuleIgnoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleIgnoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineRuleList(self, request):
        """获取基线规则列表

        :param request: Request instance for DescribeBaselineRuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineRuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineRuleList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineRuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineScanSchedule(self, request):
        """根据任务id查询基线检测进度

        :param request: Request instance for DescribeBaselineScanSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineScanScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineScanScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineScanSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineScanScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineStrategyDetail(self, request):
        """根据基线策略id查询策略详情

        :param request: Request instance for DescribeBaselineStrategyDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineStrategyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineStrategyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineStrategyList(self, request):
        """查询一个用户下的基线策略信息

        :param request: Request instance for DescribeBaselineStrategyList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineTop(self, request):
        """根据策略id查询基线检测项TOP

        :param request: Request instance for DescribeBaselineTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaselineWeakPasswordList(self, request):
        """获取基线弱口令列表

        :param request: Request instance for DescribeBaselineWeakPasswordList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineWeakPasswordListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBaselineWeakPasswordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaselineWeakPasswordList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaselineWeakPasswordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEvents(self, request):
        """获取高危命令列表

        :param request: Request instance for DescribeBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEventsInfoNew(self, request):
        """查询高危命令事件详情(新)

        :param request: Request instance for DescribeBashEventsInfoNew.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoNewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsInfoNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEventsInfoNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsInfoNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashEventsNew(self, request):
        """获取高危命令列表(新)

        :param request: Request instance for DescribeBashEventsNew.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsNewRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashEventsNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashEventsNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashEventsNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBashRules(self, request):
        """获取高危命令规则列表

        :param request: Request instance for DescribeBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBruteAttackList(self, request):
        """获取密码破解列表

        :param request: Request instance for DescribeBruteAttackList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttackList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBruteAttackRules(self, request):
        """获取爆破破解规则

        :param request: Request instance for DescribeBruteAttackRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeBruteAttackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBruteAttackRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBruteAttackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientException(self, request):
        """获取客户端异常事件

        :param request: Request instance for DescribeClientException.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeClientExceptionRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeClientExceptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientException", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientExceptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeComponentStatistics(self, request):
        """本接口 (DescribeComponentStatistics) 用于获取组件统计列表数据。

        :param request: Request instance for DescribeComponentStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeComponentStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeComponentStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeComponentStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeComponentStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeESAggregations(self, request):
        """获取ES字段聚合结果

        :param request: Request instance for DescribeESAggregations.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeESAggregationsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeESAggregationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeESAggregations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeESAggregationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmergencyResponseList(self, request):
        """专家服务-应急响应列表

        :param request: Request instance for DescribeEmergencyResponseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyResponseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyResponseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmergencyResponseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmergencyResponseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmergencyVulList(self, request):
        """获取应急漏洞列表

        :param request: Request instance for DescribeEmergencyVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEmergencyVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmergencyVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmergencyVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEventByTable(self, request):
        """根据事件表名和id查询告警事件详情

        :param request: Request instance for DescribeEventByTable.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEventByTableRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEventByTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEventByTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEventByTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExpertServiceList(self, request):
        """专家服务-安全管家列表

        :param request: Request instance for DescribeExpertServiceList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExpertServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExpertServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExpertServiceOrderList(self, request):
        """专家服务-专家服务订单列表

        :param request: Request instance for DescribeExpertServiceOrderList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceOrderListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceOrderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExpertServiceOrderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExpertServiceOrderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExportMachines(self, request):
        """本接口 (DescribeExportMachines) 用于导出区域主机列表。

        :param request: Request instance for DescribeExportMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExportMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExportMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExportMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExportMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileTamperEvents(self, request):
        """核心文件监控事件列表

        :param request: Request instance for DescribeFileTamperEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeFileTamperEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileTamperEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileTamperEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralStat(self, request):
        """获取主机相关统计

        :param request: Request instance for DescribeGeneralStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeGeneralStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeGeneralStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistoryAccounts(self, request):
        """本接口 (DescribeHistoryAccounts) 用于获取帐号变更历史列表数据。

        :param request: Request instance for DescribeHistoryAccounts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryAccountsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHistoryService(self, request):
        """查询日志检索服务信息

        :param request: Request instance for DescribeHistoryService.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryServiceRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHistoryServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHistoryService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHistoryServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostLoginList(self, request):
        """获取登录审计列表

        :param request: Request instance for DescribeHostLoginList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeHostLoginListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeHostLoginListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostLoginList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostLoginListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreBaselineRule(self, request):
        """查询已经忽略的检测项信息

        :param request: Request instance for DescribeIgnoreBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreHostAndItemConfig(self, request):
        """获取一键忽略受影响的检测项和主机信息

        :param request: Request instance for DescribeIgnoreHostAndItemConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreHostAndItemConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreHostAndItemConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreHostAndItemConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreHostAndItemConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIgnoreRuleEffectHostList(self, request):
        """根据检测项id与筛选条件查询忽略检测项影响主机列表信息

        :param request: Request instance for DescribeIgnoreRuleEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreRuleEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIgnoreRuleEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIgnoreRuleEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIgnoreRuleEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImportMachineInfo(self, request):
        """查询批量导入机器信息

        :param request: Request instance for DescribeImportMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeImportMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeImportMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImportMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImportMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIndexList(self, request):
        """获取索引列表

        :param request: Request instance for DescribeIndexList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeIndexListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeIndexListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIndexList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIndexListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJavaMemShellList(self, request):
        """查询java内存马事件列表

        :param request: Request instance for DescribeJavaMemShellList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeJavaMemShellListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJavaMemShellList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJavaMemShellListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseBindList(self, request):
        """该接口可以获取设置中心-授权管理,某个授权下已绑定的授权机器列表

        :param request: Request instance for DescribeLicenseBindList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseBindList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseBindListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseBindSchedule(self, request):
        """查询授权绑定任务的进度

        :param request: Request instance for DescribeLicenseBindSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseBindScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseBindSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseBindScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseGeneral(self, request):
        """授权管理-授权概览信息

        :param request: Request instance for DescribeLicenseGeneral.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseGeneralRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseGeneralResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseGeneral", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseGeneralResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLicenseList(self, request):
        """获取用户所有授权订单信息

        :param request: Request instance for DescribeLicenseList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLicenseListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLicenseList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLicenseListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageConfig(self, request):
        """获取日志存储配置

        :param request: Request instance for DescribeLogStorageConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageRecord(self, request):
        """获取日志存储量记录

        :param request: Request instance for DescribeLogStorageRecord.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageRecordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogStorageStatistic(self, request):
        """获取日志检索容量使用统计

        :param request: Request instance for DescribeLogStorageStatistic.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageStatisticRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLogStorageStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogStorageStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogStorageStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteCombinedList(self, request):
        """获取异地登录白名单合并后列表

        :param request: Request instance for DescribeLoginWhiteCombinedList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteCombinedListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteCombinedListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteCombinedList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteCombinedListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLoginWhiteList(self, request):
        """获取异地登录白名单列表

        :param request: Request instance for DescribeLoginWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeLoginWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoginWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoginWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineInfo(self, request):
        """本接口（DescribeMachineInfo）用于获取机器详细信息。

        :param request: Request instance for DescribeMachineInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineList(self, request):
        """用于网页防篡改获取区域主机列表。

        :param request: Request instance for DescribeMachineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineOsList(self, request):
        """查询可筛选操作系统列表.

        :param request: Request instance for DescribeMachineOsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineOsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineOsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineOsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineOsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineRegions(self, request):
        """获取机器地域列表

        :param request: Request instance for DescribeMachineRegions.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachineRiskCnt(self, request):
        """查询主机入侵检测事件统计

        :param request: Request instance for DescribeMachineRiskCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRiskCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachineRiskCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachineRiskCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineRiskCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachines(self, request):
        """本接口 (DescribeMachines) 用于获取区域主机列表。

        :param request: Request instance for DescribeMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalWareList(self, request):
        """入侵检测获取木马列表

        :param request: Request instance for DescribeMalWareList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalWareListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalWareListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalWareList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalWareListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaliciousRequestWhiteList(self, request):
        """查询恶意请求白名单列表

        :param request: Request instance for DescribeMaliciousRequestWhiteList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMaliciousRequestWhiteListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMaliciousRequestWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaliciousRequestWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaliciousRequestWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareFile(self, request):
        """获取木马文件下载地址

        :param request: Request instance for DescribeMalwareFile.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareFileRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareInfo(self, request):
        """查看恶意文件详情

        :param request: Request instance for DescribeMalwareInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareRiskWarning(self, request):
        """打开入侵检测-恶意文件检测,弹出风险预警内容

        :param request: Request instance for DescribeMalwareRiskWarning.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskWarningRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareRiskWarningResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareRiskWarning", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareRiskWarningResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMalwareTimingScanSetting(self, request):
        """查询定时扫描配置

        :param request: Request instance for DescribeMalwareTimingScanSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareTimingScanSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMalwareTimingScanSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMalwareTimingScanSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMalwareTimingScanSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonthInspectionReport(self, request):
        """专家服务-安全管家月巡检报告下载

        :param request: Request instance for DescribeMonthInspectionReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeMonthInspectionReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeMonthInspectionReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonthInspectionReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonthInspectionReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOpenPortStatistics(self, request):
        """本接口 (DescribeOpenPortStatistics) 用于获取端口统计列表。

        :param request: Request instance for DescribeOpenPortStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeOpenPortStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeOpenPortStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOpenPortStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOpenPortStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOverviewStatistics(self, request):
        """获取概览统计数据。

        :param request: Request instance for DescribeOverviewStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeOverviewStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeOverviewStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOverviewStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOverviewStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeEventInfo(self, request):
        """本地提权信息详情

        :param request: Request instance for DescribePrivilegeEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeEvents(self, request):
        """获取本地提权事件列表

        :param request: Request instance for DescribePrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivilegeRules(self, request):
        """获取本地提权规则列表

        :param request: Request instance for DescribePrivilegeRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivilegeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivilegeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProVersionInfo(self, request):
        """用于获取专业版概览信息。

        :param request: Request instance for DescribeProVersionInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProVersionInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProVersionStatus(self, request):
        """用于获取单台主机或所有主机是否开通专业版状态。

        :param request: Request instance for DescribeProVersionStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProVersionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProVersionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProVersionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProcessStatistics(self, request):
        """本接口 (DescribeProcessStatistics) 用于获取进程统计列表数据。

        :param request: Request instance for DescribeProcessStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProcessStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProcessStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProcessStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProcessStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectDirList(self, request):
        """网页防篡改防护目录列表

        :param request: Request instance for DescribeProtectDirList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectDirListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectDirListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectDirList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectDirListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectDirRelatedServer(self, request):
        """查询防护目录关联服务器列表信息

        :param request: Request instance for DescribeProtectDirRelatedServer.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectDirRelatedServerRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectDirRelatedServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectDirRelatedServer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectDirRelatedServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectNetList(self, request):
        """专家服务-旗舰重保列表

        :param request: Request instance for DescribeProtectNetList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectNetListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeProtectNetListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectNetList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectNetListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEventInfo(self, request):
        """反弹shell信息详情

        :param request: Request instance for DescribeReverseShellEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellEvents(self, request):
        """获取反弹Shell列表

        :param request: Request instance for DescribeReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReverseShellRules(self, request):
        """获取反弹Shell规则列表

        :param request: Request instance for DescribeReverseShellRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReverseShellRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReverseShellRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsEventInfo(self, request):
        """查询恶意请求事件详情

        :param request: Request instance for DescribeRiskDnsEventInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsEventInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsEventInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsEventList(self, request):
        """获取恶意请求事件列表

        :param request: Request instance for DescribeRiskDnsEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRiskDnsList(self, request):
        """入侵检测，获取恶意请求列表

        :param request: Request instance for DescribeRiskDnsList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRiskDnsList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRiskDnsListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanMalwareSchedule(self, request):
        """查询木马扫描进度

        :param request: Request instance for DescribeScanMalwareSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanMalwareScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanMalwareScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanMalwareSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanMalwareScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanSchedule(self, request):
        """根据taskid查询检测进度

        :param request: Request instance for DescribeScanSchedule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanScheduleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanState(self, request):
        """DescribeScanState 该接口能查询对应模块正在进行的扫描任务状态

        :param request: Request instance for DescribeScanState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskDetails(self, request):
        """DescribeScanTaskDetails 查询扫描任务详情 , 可以查询扫描进度信息/异常;

        :param request: Request instance for DescribeScanTaskDetails.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskDetailsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanTaskStatus(self, request):
        """DescribeScanTaskStatus 查询机器扫描状态列表用于过滤筛选

        :param request: Request instance for DescribeScanTaskStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScanVulSetting(self, request):
        """查询定期检测的配置

        :param request: Request instance for DescribeScanVulSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeScanVulSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeScanVulSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScanVulSetting", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScanVulSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchLogs(self, request):
        """获取历史搜索记录

        :param request: Request instance for DescribeSearchLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSearchTemplates(self, request):
        """获取快速检索列表

        :param request: Request instance for DescribeSearchTemplates.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchTemplatesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSearchTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSearchTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSearchTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityBroadcasts(self, request):
        """安全播报列表页

        :param request: Request instance for DescribeSecurityBroadcasts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityBroadcastsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityBroadcasts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityBroadcastsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityDynamics(self, request):
        """本接口 (DescribeSecurityDynamics) 用于获取安全事件动态消息数据。

        :param request: Request instance for DescribeSecurityDynamics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityDynamicsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityDynamicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityDynamics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityDynamicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityEventStat(self, request):
        """获取安全事件统计

        :param request: Request instance for DescribeSecurityEventStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityEventStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityEventStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityEventsCnt(self, request):
        """获取安全概览相关事件统计数据接口

        :param request: Request instance for DescribeSecurityEventsCnt.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventsCntRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityEventsCntResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityEventsCnt", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityEventsCntResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityTrends(self, request):
        """本接口 (DescribeSecurityTrends) 用于获取安全事件统计数据。

        :param request: Request instance for DescribeSecurityTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityTrends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServerRelatedDirInfo(self, request):
        """查询服务区关联目录详情

        :param request: Request instance for DescribeServerRelatedDirInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeServerRelatedDirInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeServerRelatedDirInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerRelatedDirInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerRelatedDirInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServersAndRiskAndFirstInfo(self, request):
        """获取待处理风险文件数+影响服务器数+是否试用检测+最近检测时间

        :param request: Request instance for DescribeServersAndRiskAndFirstInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeServersAndRiskAndFirstInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeServersAndRiskAndFirstInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServersAndRiskAndFirstInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServersAndRiskAndFirstInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategyExist(self, request):
        """根据策略名查询策略是否存在

        :param request: Request instance for DescribeStrategyExist.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeStrategyExistRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeStrategyExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategyExist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategyExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagMachines(self, request):
        """获取指定标签关联的服务器信息

        :param request: Request instance for DescribeTagMachines.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTagMachinesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTagMachinesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagMachines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagMachinesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTags(self, request):
        """获取所有主机标签

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUndoVulCounts(self, request):
        """获取漏洞管理模块指定类型的待处理漏洞数、主机数和非专业版主机数量

        :param request: Request instance for DescribeUndoVulCounts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUndoVulCountsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUndoVulCountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUndoVulCounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUndoVulCountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsualLoginPlaces(self, request):
        """此接口（DescribeUsualLoginPlaces）用于查询常用登录地。

        :param request: Request instance for DescribeUsualLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeUsualLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeUsualLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsualLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsualLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVersionStatistics(self, request):
        """用于统计专业版和基础版机器数。

        :param request: Request instance for DescribeVersionStatistics.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionStatisticsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVersionStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVersionStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVersionStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVertexDetail(self, request):
        """获取指定点属性信息

        :param request: Request instance for DescribeVertexDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVertexDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVertexDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVertexDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVertexDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulCountByDates(self, request):
        """漏洞管理模块，获取近日指定类型的漏洞数量和主机数量

        :param request: Request instance for DescribeVulCountByDates.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCountByDatesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCountByDatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulCountByDates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulCountByDatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulEffectHostList(self, request):
        """漏洞影响主机列表

        :param request: Request instance for DescribeVulEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulHostCountScanTime(self, request):
        """获取待处理漏洞数+影响主机数

        :param request: Request instance for DescribeVulHostCountScanTime.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostCountScanTimeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostCountScanTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulHostCountScanTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulHostCountScanTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulHostTop(self, request):
        """获取服务器风险top列表

        :param request: Request instance for DescribeVulHostTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulHostTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulHostTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulHostTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulInfoCvss(self, request):
        """漏洞详情，带CVSS版本

        :param request: Request instance for DescribeVulInfoCvss.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulInfoCvssRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulInfoCvssResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulInfoCvss", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulInfoCvssResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulLevelCount(self, request):
        """漏洞数量等级分布统计

        :param request: Request instance for DescribeVulLevelCount.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLevelCountRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulLevelCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulLevelCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulLevelCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulList(self, request):
        """获取漏洞列表数据

        :param request: Request instance for DescribeVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulStoreList(self, request):
        """获取漏洞库列表

        :param request: Request instance for DescribeVulStoreList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulStoreListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulStoreListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulStoreList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulStoreListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVulTop(self, request):
        """漏洞top统计

        :param request: Request instance for DescribeVulTop.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTopRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVulTopResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulTop", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulTopResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWarningList(self, request):
        """获取当前用户告警列表

        :param request: Request instance for DescribeWarningList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWarningListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWarningList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWarningListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebPageEventList(self, request):
        """查询篡改事件列表

        :param request: Request instance for DescribeWebPageEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebPageEventList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebPageEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebPageGeneralize(self, request):
        """查询网站防篡改概览信息

        :param request: Request instance for DescribeWebPageGeneralize.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageGeneralizeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageGeneralizeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebPageGeneralize", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebPageGeneralizeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebPageProtectStat(self, request):
        """网站防篡改-查询动态防护信息

        :param request: Request instance for DescribeWebPageProtectStat.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageProtectStatRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageProtectStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebPageProtectStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebPageProtectStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWebPageServiceInfo(self, request):
        """网站防篡改-查询网页防篡改服务器购买信息及服务器信息

        :param request: Request instance for DescribeWebPageServiceInfo.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageServiceInfoRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeWebPageServiceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWebPageServiceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWebPageServiceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyOrder(self, request):
        """DestroyOrder  该接口可以对资源销毁.

        :param request: Request instance for DestroyOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.DestroyOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.DestroyOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyOrder", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditBashRules(self, request):
        """新增或修改高危命令规则

        :param request: Request instance for EditBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.EditBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditTags(self, request):
        """新增或编辑标签

        :param request: Request instance for EditTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.EditTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.EditTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditTags", params, headers=headers)
            response = json.loads(body)
            model = models.EditTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetCoreModuleList(self, request):
        """导出资产管理内核模块列表

        :param request: Request instance for ExportAssetCoreModuleList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetCoreModuleListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetCoreModuleListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetCoreModuleList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetCoreModuleListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAssetWebServiceInfoList(self, request):
        """导出资产管理Web服务列表

        :param request: Request instance for ExportAssetWebServiceInfoList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebServiceInfoListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAssetWebServiceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAssetWebServiceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAssetWebServiceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportAttackLogs(self, request):
        """导出网络攻击日志

        :param request: Request instance for ExportAttackLogs.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportAttackLogsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportAttackLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportAttackLogs", params, headers=headers)
            response = json.loads(body)
            model = models.ExportAttackLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineEffectHostList(self, request):
        """导出基线影响主机列表

        :param request: Request instance for ExportBaselineEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineFixList(self, request):
        """导出修复列表

        :param request: Request instance for ExportBaselineFixList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineFixListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineFixListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineFixList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineFixListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineHostDetectList(self, request):
        """导出基线主机检测

        :param request: Request instance for ExportBaselineHostDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineHostDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineHostDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineHostDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineHostDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineItemDetectList(self, request):
        """导出基线检测项

        :param request: Request instance for ExportBaselineItemDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineItemDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineItemDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineItemList(self, request):
        """导出检测项结果列表

        :param request: Request instance for ExportBaselineItemList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineItemListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineItemList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineItemListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineList(self, request):
        """导出基线列表

        :param request: Request instance for ExportBaselineList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineRuleDetectList(self, request):
        """导出基线检测规则

        :param request: Request instance for ExportBaselineRuleDetectList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineRuleDetectListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineRuleDetectListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineRuleDetectList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineRuleDetectListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBaselineWeakPasswordList(self, request):
        """导出弱口令配置列表

        :param request: Request instance for ExportBaselineWeakPasswordList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineWeakPasswordListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBaselineWeakPasswordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBaselineWeakPasswordList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBaselineWeakPasswordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBashEvents(self, request):
        """导出高危命令事件

        :param request: Request instance for ExportBashEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBashEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBashEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBashEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportBruteAttacks(self, request):
        """本接口 (ExportBruteAttacks) 用于导出密码破解记录成CSV文件。

        :param request: Request instance for ExportBruteAttacks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportBruteAttacksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportBruteAttacksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBruteAttacks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBruteAttacksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportIgnoreBaselineRule(self, request):
        """导出已忽略基线检测项信息

        :param request: Request instance for ExportIgnoreBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportIgnoreBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.ExportIgnoreBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportIgnoreRuleEffectHostList(self, request):
        """根据检测项id导出忽略检测项影响主机列表

        :param request: Request instance for ExportIgnoreRuleEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreRuleEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportIgnoreRuleEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportIgnoreRuleEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportIgnoreRuleEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportLicenseDetail(self, request):
        """导出授权列表对应的绑定信息

        :param request: Request instance for ExportLicenseDetail.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportLicenseDetailRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportLicenseDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportLicenseDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ExportLicenseDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportMaliciousRequests(self, request):
        """本接口 (ExportMaliciousRequests) 用于导出下载恶意请求文件。

        :param request: Request instance for ExportMaliciousRequests.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportMaliciousRequestsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportMaliciousRequestsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMaliciousRequests", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMaliciousRequestsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportMalwares(self, request):
        """本接口 (ExportMalwares) 用于导出木马记录CSV文件。

        :param request: Request instance for ExportMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.ExportMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportNonlocalLoginPlaces(self, request):
        """本接口 (ExportNonlocalLoginPlaces) 用于导出异地登录事件记录CSV文件。

        :param request: Request instance for ExportNonlocalLoginPlaces.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportNonlocalLoginPlacesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportNonlocalLoginPlacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportNonlocalLoginPlaces", params, headers=headers)
            response = json.loads(body)
            model = models.ExportNonlocalLoginPlacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportPrivilegeEvents(self, request):
        """导出本地提权事件

        :param request: Request instance for ExportPrivilegeEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportPrivilegeEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportPrivilegeEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportPrivilegeEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportPrivilegeEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportProtectDirList(self, request):
        """导出网页防篡改防护目录列表

        :param request: Request instance for ExportProtectDirList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportProtectDirListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportProtectDirListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportProtectDirList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportProtectDirListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportReverseShellEvents(self, request):
        """导出反弹Shell事件

        :param request: Request instance for ExportReverseShellEvents.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportReverseShellEventsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportReverseShellEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportReverseShellEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ExportReverseShellEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportScanTaskDetails(self, request):
        """根据任务id导出指定扫描任务详情

        :param request: Request instance for ExportScanTaskDetails.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportScanTaskDetailsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportScanTaskDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportScanTaskDetails", params, headers=headers)
            response = json.loads(body)
            model = models.ExportScanTaskDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportSecurityTrends(self, request):
        """导出风险趋势

        :param request: Request instance for ExportSecurityTrends.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportSecurityTrendsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportSecurityTrendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportSecurityTrends", params, headers=headers)
            response = json.loads(body)
            model = models.ExportSecurityTrendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportTasks(self, request):
        """用于异步导出数据量大的日志文件

        :param request: Request instance for ExportTasks.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportTasksRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ExportTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDetectionExcel(self, request):
        """导出本次漏洞检测Excel

        :param request: Request instance for ExportVulDetectionExcel.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionExcelRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionExcelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDetectionExcel", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDetectionExcelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulDetectionReport(self, request):
        """导出漏洞检测报告。

        :param request: Request instance for ExportVulDetectionReport.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionReportRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulDetectionReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulDetectionReport", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulDetectionReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulEffectHostList(self, request):
        """导出漏洞影响主机列表

        :param request: Request instance for ExportVulEffectHostList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulEffectHostListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulEffectHostListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulEffectHostList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulEffectHostListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportVulList(self, request):
        """漏洞管理-导出漏洞列表

        :param request: Request instance for ExportVulList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportVulListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportVulListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportVulList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportVulListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportWebPageEventList(self, request):
        """导出篡改事件列表

        :param request: Request instance for ExportWebPageEventList.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ExportWebPageEventListRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ExportWebPageEventListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportWebPageEventList", params, headers=headers)
            response = json.loads(body)
            model = models.ExportWebPageEventListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FixBaselineDetect(self, request):
        """修复基线检测

        :param request: Request instance for FixBaselineDetect.
        :type request: :class:`tencentcloud.cwp.v20180228.models.FixBaselineDetectRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.FixBaselineDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FixBaselineDetect", params, headers=headers)
            response = json.loads(body)
            model = models.FixBaselineDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IgnoreImpactedHosts(self, request):
        """本接口 (IgnoreImpactedHosts) 用于忽略漏洞。

        :param request: Request instance for IgnoreImpactedHosts.
        :type request: :class:`tencentcloud.cwp.v20180228.models.IgnoreImpactedHostsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.IgnoreImpactedHostsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnoreImpactedHosts", params, headers=headers)
            response = json.loads(body)
            model = models.IgnoreImpactedHostsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoOpenProVersionConfig(self, request):
        """用于设置新增主机自动开通专业防护配置。

        :param request: Request instance for ModifyAutoOpenProVersionConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyAutoOpenProVersionConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyAutoOpenProVersionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoOpenProVersionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoOpenProVersionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanMode(self, request):
        """修改爆破阻断模式

        :param request: Request instance for ModifyBanMode.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBanModeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBanModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBanStatus(self, request):
        """设置阻断开关状态

        :param request: Request instance for ModifyBanStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBanStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselinePolicy(self, request):
        """更改基线策略设置

        :param request: Request instance for ModifyBaselinePolicy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselinePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselinePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselinePolicyState(self, request):
        """更改基线策略状态

        :param request: Request instance for ModifyBaselinePolicyState.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyStateRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselinePolicyStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselinePolicyState", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselinePolicyStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineRule(self, request):
        """更改基线检测规则

        :param request: Request instance for ModifyBaselineRule.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineRuleRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineRuleIgnore(self, request):
        """更改基线忽略规则

        :param request: Request instance for ModifyBaselineRuleIgnore.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineRuleIgnoreRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineRuleIgnoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineRuleIgnore", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineRuleIgnoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaselineWeakPassword(self, request):
        """更改或新增弱口令

        :param request: Request instance for ModifyBaselineWeakPassword.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineWeakPasswordRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBaselineWeakPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaselineWeakPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaselineWeakPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBruteAttackRules(self, request):
        """修改暴力破解规则

        :param request: Request instance for ModifyBruteAttackRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyBruteAttackRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyBruteAttackRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBruteAttackRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBruteAttackRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicenseBinds(self, request):
        """设置中心-授权管理 对某个授权批量绑定机器

        :param request: Request instance for ModifyLicenseBinds.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseBindsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicenseBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicenseOrder(self, request):
        """编辑《主机安全-按量计费》授权订单

        :param request: Request instance for ModifyLicenseOrder.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseOrderRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicenseOrder", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLicenseUnBinds(self, request):
        """设置中心-授权管理 对某个授权批量解绑机器

        :param request: Request instance for ModifyLicenseUnBinds.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseUnBindsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLicenseUnBindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLicenseUnBinds", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLicenseUnBindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogStorageConfig(self, request):
        """修改日志存储配置

        :param request: Request instance for ModifyLogStorageConfig.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyLogStorageConfigRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyLogStorageConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogStorageConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogStorageConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMachineRemark(self, request):
        """修改主机备注信息

        :param request: Request instance for ModifyMachineRemark.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMachineRemarkRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMachineRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMachineRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMachineRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMalwareTimingScanSettings(self, request):
        """定时扫描设置

        :param request: Request instance for ModifyMalwareTimingScanSettings.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareTimingScanSettingsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyMalwareTimingScanSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMalwareTimingScanSettings", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMalwareTimingScanSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOrderAttribute(self, request):
        """对订单属性编辑

        :param request: Request instance for ModifyOrderAttribute.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyOrderAttributeRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyOrderAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOrderAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOrderAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWarningSetting(self, request):
        """修改告警设置

        :param request: Request instance for ModifyWarningSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWarningSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWarningSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWarningSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebPageProtectDir(self, request):
        """创建/修改网站防护目录

        :param request: Request instance for ModifyWebPageProtectDir.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectDirRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectDirResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebPageProtectDir", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebPageProtectDirResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebPageProtectSetting(self, request):
        """修改网站防护设置

        :param request: Request instance for ModifyWebPageProtectSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebPageProtectSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebPageProtectSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWebPageProtectSwitch(self, request):
        """网站防篡改防护设置开关

        :param request: Request instance for ModifyWebPageProtectSwitch.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSwitchRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ModifyWebPageProtectSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWebPageProtectSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWebPageProtectSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverMalwares(self, request):
        """本接口（RecoverMalwares）用于批量恢复已经被隔离的木马文件。

        :param request: Request instance for RecoverMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.RecoverMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.RecoverMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanAsset(self, request):
        """资产指纹启动扫描

        :param request: Request instance for ScanAsset.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanAssetRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanAsset", params, headers=headers)
            response = json.loads(body)
            model = models.ScanAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVul(self, request):
        """一键检测

        :param request: Request instance for ScanVul.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVul", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVulAgain(self, request):
        """漏洞管理-重新检测接口

        :param request: Request instance for ScanVulAgain.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulAgainRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulAgainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVulAgain", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulAgainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScanVulSetting(self, request):
        """定期扫描漏洞设置

        :param request: Request instance for ScanVulSetting.
        :type request: :class:`tencentcloud.cwp.v20180228.models.ScanVulSettingRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.ScanVulSettingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScanVulSetting", params, headers=headers)
            response = json.loads(body)
            model = models.ScanVulSettingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SeparateMalwares(self, request):
        """本接口（SeparateMalwares）用于隔离木马。

        :param request: Request instance for SeparateMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SeparateMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SeparateMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SeparateMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.SeparateMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetBashEventsStatus(self, request):
        """设置高危命令事件状态

        :param request: Request instance for SetBashEventsStatus.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SetBashEventsStatusRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SetBashEventsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetBashEventsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.SetBashEventsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBaselineDetect(self, request):
        """检测基线

        :param request: Request instance for StartBaselineDetect.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StartBaselineDetectRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StartBaselineDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBaselineDetect", params, headers=headers)
            response = json.loads(body)
            model = models.StartBaselineDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBaselineDetect(self, request):
        """停止基线检测

        :param request: Request instance for StopBaselineDetect.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StopBaselineDetectRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StopBaselineDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBaselineDetect", params, headers=headers)
            response = json.loads(body)
            model = models.StopBaselineDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopNoticeBanTips(self, request):
        """不再提醒爆破阻断提示弹窗

        :param request: Request instance for StopNoticeBanTips.
        :type request: :class:`tencentcloud.cwp.v20180228.models.StopNoticeBanTipsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.StopNoticeBanTipsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopNoticeBanTips", params, headers=headers)
            response = json.loads(body)
            model = models.StopNoticeBanTipsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchBashRules(self, request):
        """切换高危命令规则状态

        :param request: Request instance for SwitchBashRules.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SwitchBashRulesRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SwitchBashRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchBashRules", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchBashRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncAssetScan(self, request):
        """同步资产扫描信息

        :param request: Request instance for SyncAssetScan.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncAssetScanRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncAssetScanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncAssetScan", params, headers=headers)
            response = json.loads(body)
            model = models.SyncAssetScanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncBaselineDetectSummary(self, request):
        """同步基线检测进度概要

        :param request: Request instance for SyncBaselineDetectSummary.
        :type request: :class:`tencentcloud.cwp.v20180228.models.SyncBaselineDetectSummaryRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.SyncBaselineDetectSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncBaselineDetectSummary", params, headers=headers)
            response = json.loads(body)
            model = models.SyncBaselineDetectSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TrustMalwares(self, request):
        """本接口(TrustMalwares)将被识别木马文件设为信任。

        :param request: Request instance for TrustMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.TrustMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.TrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.TrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UntrustMalwares(self, request):
        """本接口（UntrustMalwares）用于取消信任木马文件。

        :param request: Request instance for UntrustMalwares.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UntrustMalwaresRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UntrustMalwaresResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UntrustMalwares", params, headers=headers)
            response = json.loads(body)
            model = models.UntrustMalwaresResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBaselineStrategy(self, request):
        """根据基线策略id更新策略信息

        :param request: Request instance for UpdateBaselineStrategy.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UpdateBaselineStrategyRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UpdateBaselineStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBaselineStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBaselineStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateMachineTags(self, request):
        """关联机器标签列表

        :param request: Request instance for UpdateMachineTags.
        :type request: :class:`tencentcloud.cwp.v20180228.models.UpdateMachineTagsRequest`
        :rtype: :class:`tencentcloud.cwp.v20180228.models.UpdateMachineTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateMachineTags", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateMachineTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))