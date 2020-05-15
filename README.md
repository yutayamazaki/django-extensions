# django-extensions

## Installation

```shell
pip install git+https://github.com/yutayamazaki/django-extensions
```

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
