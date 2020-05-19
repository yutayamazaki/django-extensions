# django-extensions

## Installation

```shell
pip install git+https://github.com/yutayamazaki/django-extensions
```

If you use `requirements.txt`.

```txt
-e git://github.com/yutayamazaki/django-extensions.git
```

When you need to use specific version, follow this page.

https://stackoverflow.com/questions/16584552/how-to-state-in-requirements-txt-a-direct-github-source

## Usage

### Middllewares

#### AdminIPRestrictionMiddleware

It is possible to restrict the IP address on the admin screen, http://domain.name/admin/, of the production environment. You can set the IP address to be accessible by entering it into the ALLOWED_ADMIN_IP_LIST in settings.py.

```python
# settings.py
ALLOWED_ADMIN_IP_LIST = ['xxx.xxx.xxx.xxx', 'xxx.xx.xx.xx']

MIDDLEWARE = [
    ...
    'django_extensions.middlewares.AdminIPRestrictionMiddleware'
    ...
]
```
