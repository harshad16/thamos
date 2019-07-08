# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from thamos.swagger_client.api_client import ApiClient


class BuildAnalysisApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def post_build(self, body, **kwargs):  # noqa: E501
        """Analyze the given build imagestream and log.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_build(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Log body: Build log to be stored. (required)
        :param str base_image: Name of base image - can also specify remote registry to pull image from. 
        :param str image: Name of image - can also specify remote registry to pull image from. 
        :param str registry_user: Registry user to be used for pulling images from registry. 
        :param str registry_password: Registry password or token to be used for pulling images from registry. 
        :param str environment_type: Type of environment (runtime or buildtime) which is being analyzed. 
        :param str origin: A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available. 
        :param bool debug: Run the given analyzer in a verbose mode so developers can debug analyzer. 
        :param bool verify_tls: Verify TLS certificates of registry from where images are pulled from. 
        :param bool force: Do not use cached results, always run analysis. 
        :return: AnalysisResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_build_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_build_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_build_with_http_info(self, body, **kwargs):  # noqa: E501
        """Analyze the given build imagestream and log.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_build_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Log body: Build log to be stored. (required)
        :param str base_image: Name of base image - can also specify remote registry to pull image from. 
        :param str image: Name of image - can also specify remote registry to pull image from. 
        :param str registry_user: Registry user to be used for pulling images from registry. 
        :param str registry_password: Registry password or token to be used for pulling images from registry. 
        :param str environment_type: Type of environment (runtime or buildtime) which is being analyzed. 
        :param str origin: A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available. 
        :param bool debug: Run the given analyzer in a verbose mode so developers can debug analyzer. 
        :param bool verify_tls: Verify TLS certificates of registry from where images are pulled from. 
        :param bool force: Do not use cached results, always run analysis. 
        :return: AnalysisResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'base_image', 'image', 'registry_user', 'registry_password', 'environment_type', 'origin', 'debug', 'verify_tls', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_build" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_build`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'base_image' in params:
            query_params.append(('base_image', params['base_image']))  # noqa: E501
        if 'image' in params:
            query_params.append(('image', params['image']))  # noqa: E501
        if 'registry_user' in params:
            query_params.append(('registry_user', params['registry_user']))  # noqa: E501
        if 'registry_password' in params:
            query_params.append(('registry_password', params['registry_password']))  # noqa: E501
        if 'environment_type' in params:
            query_params.append(('environment_type', params['environment_type']))  # noqa: E501
        if 'origin' in params:
            query_params.append(('origin', params['origin']))  # noqa: E501
        if 'debug' in params:
            query_params.append(('debug', params['debug']))  # noqa: E501
        if 'verify_tls' in params:
            query_params.append(('verify_tls', params['verify_tls']))  # noqa: E501
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/build-analysis', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalysisResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)