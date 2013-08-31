from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from cms.cms_toolbar import CMSToolbar
from cms.plugin_base import CMSPluginBase, CMSPluginBaseMetaclass
from cms.plugin_pool import plugin_pool
from cms.utils.compat.type_checks import string_types
from menus.menu_pool import menu_pool
from menus.base import Menu

from .utils import build_and_register
from .menu import Node

__all__ = [
    'plugin',
    'menu',
    'app',
]


class PopulateProxy(CMSToolbar):
    def populate(self):
        return self.populate_func(self.toolbar, self.request, self.is_current_app, self.app_path)


def plugin(name, **options):
    options.update({'name': name})
    def decorator(func):
        return build_and_register(CMSPluginBase, str(name), plugin_pool.register_plugin,
            metaclass=CMSPluginBaseMetaclass,
            attrs=options,
            methods={
                'render': func,
            }
        )
    return decorator

def app(name, urls, **options):
    if isinstance(urls, string_types):
        urls = [urls]
    options.update({
        'name': name,
        'urls': urls,
    })
    return build_and_register(CMSApp, str(name), apphook_pool.register,
        attrs=options,
    )


def may_return_node(func):
    def inner(request):
        output = func(request)
        if isinstance(output, Node):
            return output._as_list()
        else:
            return output
    return inner

def menu(*args, **options):
    def decorator(func):
        return build_and_register(Menu, func.__name__, menu_pool.register_menu,
            attrs=options,
            methods={
                'get_nodes': may_return_node(func)
            }
        )
    if args and not options:
        return decorator(args[0])
    else:
        return decorator

try:
    from cms.toolbar_pool import toolbar_pool

    __all__.append('toolbar')

    def toolbar(func):
        build_and_register(PopulateProxy, func.__name__, toolbar_pool.register,
            methods={
                'populate_func': func
            }
        )
except ImportError:
    pass

