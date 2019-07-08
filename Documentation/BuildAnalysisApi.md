# thamos.swagger_client.BuildAnalysisApi

All URIs are relative to *https://raw.githubusercontent.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_build**](BuildAnalysisApi.md#post_build) | **POST** /build-analysis | Analyze the given build imagestream and log.

# **post_build**
> AnalysisResponse post_build(body, base_image=base_image, image=image, registry_user=registry_user, registry_password=registry_password, environment_type=environment_type, origin=origin, debug=debug, verify_tls=verify_tls, force=force)

Analyze the given build imagestream and log.

### Example
```python
from __future__ import print_function
import time
import thamos.swagger_client
from thamos.swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = thamos.swagger_client.BuildAnalysisApi()
body = thamos.swagger_client.Log() # Log | Build log to be stored.
base_image = 'base_image_example' # str | Name of base image - can also specify remote registry to pull image from.  (optional)
image = 'image_example' # str | Name of image - can also specify remote registry to pull image from.  (optional)
registry_user = 'registry_user_example' # str | Registry user to be used for pulling images from registry.  (optional)
registry_password = 'registry_password_example' # str | Registry password or token to be used for pulling images from registry.  (optional)
environment_type = 'environment_type_example' # str | Type of environment (runtime or buildtime) which is being analyzed.  (optional)
origin = 'origin_example' # str | A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available.  (optional)
debug = true # bool | Run the given analyzer in a verbose mode so developers can debug analyzer.  (optional)
verify_tls = true # bool | Verify TLS certificates of registry from where images are pulled from.  (optional)
force = true # bool | Do not use cached results, always run analysis.  (optional)

try:
    # Analyze the given build imagestream and log.
    api_response = api_instance.post_build(body, base_image=base_image, image=image, registry_user=registry_user, registry_password=registry_password, environment_type=environment_type, origin=origin, debug=debug, verify_tls=verify_tls, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildAnalysisApi->post_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Log**](Log.md)| Build log to be stored. | 
 **base_image** | **str**| Name of base image - can also specify remote registry to pull image from.  | [optional] 
 **image** | **str**| Name of image - can also specify remote registry to pull image from.  | [optional] 
 **registry_user** | **str**| Registry user to be used for pulling images from registry.  | [optional] 
 **registry_password** | **str**| Registry password or token to be used for pulling images from registry.  | [optional] 
 **environment_type** | **str**| Type of environment (runtime or buildtime) which is being analyzed.  | [optional] 
 **origin** | **str**| A remote where the image is being used. This is used for tracking as well as for automated reporting when results are available.  | [optional] 
 **debug** | **bool**| Run the given analyzer in a verbose mode so developers can debug analyzer.  | [optional] 
 **verify_tls** | **bool**| Verify TLS certificates of registry from where images are pulled from.  | [optional] 
 **force** | **bool**| Do not use cached results, always run analysis.  | [optional] 

### Return type

[**AnalysisResponse**](AnalysisResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

