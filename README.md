# Opal Python SDK Script For Mass Tagging Items for a UAR

## About
This script uses the [Opal Python SDK](https://github.com/opalsecurity/opal-python) to get all groups associated with an Okta Bookmark app (IDP Group Mappings) and apply a tag to them so they can be more easily included in a UAR audit. This is a one off script consideration to help with a customer issue.

## How to use

- Make sure you have `python3` version `3.13.7` or above installed
- Clone this repository
- In the terminal, change to the `add_uar_tags_opal_python` directory:

Unix Like Systems:
```shell
cd add_uar_tags_opal_python
```


Windows:

```shell
dir add_uar_tags_opal_python
```
- Make a python virtual environment and activate it:
```shell
python3 -m venv .
source bin/activate
```
- Install dependencies
```shell
python3 -m pip install -r requirements.txt
```
- (OPTIONAL) Replace the host string with your self hosted URL
```python
configuration = opal.Configuration(
    host = "https://api.opal.dev/v1" # Replace with self-hosted domain (e.g. https://opal.example.com/v1)
)
```
- Replace `'ACCESS_TOKEN_HERE'` on line 21 with your access token

```python
configuration = opal.Configuration(
    access_token = "ACCESS_TOKEN_HERE" # Opal Access Token here NOTE: can not be a read-only token
)
```

- (OPTIONAL) Change the tag name and value on lines 31 and 32

```python
    tag_name = 'uar_include'
    tag_value = 'true'
```

- Replace `'OKTA_APP_ID_HERE'` on line 45 with your Okta App ID

```python
    app_resource_id = 'OKTA_APP_ID_HERE' # Input the ID for the Here
```

- Run the script
```shell
python3 opal.py
```