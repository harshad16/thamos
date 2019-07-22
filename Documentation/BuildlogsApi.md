# thamos.swagger_client.BuildlogsApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buildlog**](BuildlogsApi.md#get_buildlog) | **GET** /buildlog/{document_id} | Retrieve the given build log.
[**get_buildlog_analyze**](BuildlogsApi.md#get_buildlog_analyze) | **GET** /buildlog-analyze/{analysis_id} | Retrieve a build analyzer result.
[**list_buildlog_analyze**](BuildlogsApi.md#list_buildlog_analyze) | **GET** /buildlog-analyze | Retrieve a list of document ids for build analyzer results.
[**list_buildlogs**](BuildlogsApi.md#list_buildlogs) | **GET** /buildlog | Retrieve a list of document ids for stored build logs.
[**parse_log**](BuildlogsApi.md#parse_log) | **POST** /parse-log | Parse Docker build log or installation log and show installed packages. 
[**post_buildlog**](BuildlogsApi.md#post_buildlog) | **POST** /buildlog | Store the given build log.

# **get_buildlog**
> get_buildlog(document_id)

Retrieve the given build log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
document_id = 'document_id_example' # str | Build log to be retrieved.

try:
    # Retrieve the given build log.
    api_instance.get_buildlog(document_id)
except ApiException as e:
    print("Exception when calling BuildlogsApi->get_buildlog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| Build log to be retrieved. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_buildlog_analyze**
> AnalysisResultResponse get_buildlog_analyze(analysis_id)

Retrieve a build analyzer result.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
analysis_id = 'analysis_id_example' # str | Id of analysis that results should be retrieved.

try:
    # Retrieve a build analyzer result.
    api_response = api_instance.get_buildlog_analyze(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildlogsApi->get_buildlog_analyze: %s\n" % e)
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
api_instance = thamos.swagger_client.BuildlogsApi()
page = 56 # int | Page offset in pagination. (optional)

try:
    # Retrieve a list of document ids for build analyzer results.
    api_response = api_instance.list_buildlog_analyze(page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildlogsApi->list_buildlog_analyze: %s\n" % e)
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

# **list_buildlogs**
> list_buildlogs(page=page)

Retrieve a list of document ids for stored build logs.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
page = 56 # int | Page offset in pagination. (optional)

try:
    # Retrieve a list of document ids for stored build logs.
    api_instance.list_buildlogs(page=page)
except ApiException as e:
    print("Exception when calling BuildlogsApi->list_buildlogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page offset in pagination. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_log**
> parse_log(body)

Parse Docker build log or installation log and show installed packages. 

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
body = thamos.swagger_client.Log() # Log | A full log.

try:
    # Parse Docker build log or installation log and show installed packages. 
    api_instance.parse_log(body)
except ApiException as e:
    print("Exception when calling BuildlogsApi->parse_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Log**](Log.md)| A full log. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_buildlog**
> post_buildlog(body)

Store the given build log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildlogsApi()
body = thamos.swagger_client.Log() # Log | Build log to be stored.

try:
    # Store the given build log.
    api_instance.post_buildlog(body)
except ApiException as e:
    print("Exception when calling BuildlogsApi->post_buildlog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Log**](Log.md)| Build log to be stored. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

