# thamos.swagger_client.BuildlogsAnalysisApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buildlog_analyze**](BuildlogsAnalysisApi.md#get_buildlog_analyze) | **GET** /buildlog-analyse/{analysis_id} | Retrieve an build analyzer result.
[**list_buildlog_analyze**](BuildlogsAnalysisApi.md#list_buildlog_analyze) | **GET** /buildlog-analyze | Retrieve a list of document ids for build analyzer results.
[**post_buildlog_analyze**](BuildlogsAnalysisApi.md#post_buildlog_analyze) | **POST** /buildlog-analyze | Analyze the given build log.

# **get_buildlog_analyze**
> AnalysisResultResponse get_buildlog_analyze(analysis_id)

Retrieve an build analyzer result.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsAnalysisApi()
analysis_id = 'analysis_id_example' # str | Id of analysis that results should be retrieved.

try:
    # Retrieve an build analyzer result.
    api_response = api_instance.get_buildlog_analyze(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildlogsAnalysisApi->get_buildlog_analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Id of analysis that results should be retrieved. | 

### Return type

[**AnalysisResultResponse**](AnalysisResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_buildlog_analyze**
> AnalysisListingResponse list_buildlog_analyze(page=page)

Retrieve a list of document ids for build analyzer results.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsAnalysisApi()
page = 56 # int | Page offset in pagination. (optional)

try:
    # Retrieve a list of document ids for build analyzer results.
    api_response = api_instance.list_buildlog_analyze(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildlogsAnalysisApi->list_buildlog_analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] 

### Return type

[**AnalysisListingResponse**](AnalysisListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_buildlog_analyze**
> AnalysisResponse post_buildlog_analyze(body, output_format=output_format, handler=handler, limit=limit, force=force)

Analyze the given build log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsAnalysisApi()
body = thamos.swagger_client.Log() # Log | Build log to be stored.
output_format = 'output_format_example' # str | Type of output format which build analyser returns. (optional)
handler = 'handler_example' # str | Handler to parse log dependencies. (optional)
limit = 56 # int | Limit number of candidates. (optional)
force = true # bool | Do not use cached results, always run analysis.  (optional)

try:
    # Analyze the given build log.
    api_response = api_instance.post_buildlog_analyze(body, output_format=output_format, handler=handler, limit=limit, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildlogsAnalysisApi->post_buildlog_analyze: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Log**](Log.md)| Build log to be stored. | 
 **output_format** | **str**| Type of output format which build analyser returns. | [optional] 
 **handler** | **str**| Handler to parse log dependencies. | [optional] 
 **limit** | **int**| Limit number of candidates. | [optional] 
 **force** | **bool**| Do not use cached results, always run analysis.  | [optional] 

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

