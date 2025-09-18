import opal_security
from opal_security.models.resource import Resource
from opal_security.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.opal.dev/v1
# See configuration.py for a list of all supported configuration parameters.
import opal_security as opal

configuration = opal.Configuration(
    host = "https://api.opal.dev/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = opal.Configuration(
    access_token = 'ACCESS_TOKEN_HERE' # Generate an Admin Opal API Token and add it here
)



# Enter a context with an instance of the API client
with opal_security.ApiClient(configuration) as api_client:
    # Create an instance of the tags API https://docs.opal.dev/reference/get_tag_by_id
    tags_api_instance = opal_security.TagsApi(api_client)

    tag_name = 'uar_include'
    tag_value = 'true'

    try:
        # Tries to create tag
        tags_api_instance.create_tag(tag_name, tag_value)
        tag = tags_api_instance.get_tag(tag_name, tag_value)
    except:
        # If tag already exists, get it an store in a variable
        tag = tags_api_instance.get_tag(tag_name, tag_value)

    #Create an instance of the IDP Group Mappings API https://docs.opal.dev/reference/getidpgroupmappings
    idp_gm_api_instance = opal_security.IdpGroupMappingsApi(api_client)

    app_resource_id = 'OKTA_APP_ID_HERE' # Input the ID for the AWS Auto-approvals, Owners, and Approvers App Here

    try:
        idp_gm_api_response = idp_gm_api_instance.get_idp_group_mappings(app_resource_id)
        mappings = idp_gm_api_response.mappings
        print("The response of IdpGroupMappingsApi->get_idp_group_mappings:\n")
        for mapping in mappings:
            #Iterate through each IDP Group mapping and apply the tag
            tags_api_instance.add_group_tag(tag.tag_id, mapping.group_id)
            pprint(mapping.group_id + " tagged!")

    except Exception as e:
        print("Exception when calling IdpGroupMappingsApi->get_idp_group_mappings: %s\n" % e)
