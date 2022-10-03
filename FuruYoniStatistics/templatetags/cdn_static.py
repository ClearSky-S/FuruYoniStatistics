
from sys import prefix
from urllib.parse import quote, urljoin

from django import template
from django.utils.encoding import iri_to_uri
from django.utils.html import conditional_escape

register = template.Library()

class CDNStaticNode(template.Node):
    def __init__(self, varname, path):
        if path is None:
            raise template.TemplateSyntaxError(
                "Static template nodes must be given a path to return."
            )

        self.path = path
        self.varname = varname

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(varname={self.varname!r}, path={self.path!r})"
        )

    def url_prefix(self):
        try:
            from django.conf import settings
        except ImportError:
            return ""

        prefix = getattr(settings, "CDN_STATIC_URL", "")
        if prefix == "":
            prefix = getattr(settings, "STATIC_URL", "")

        return iri_to_uri(prefix)

    def url(self, context):
        prefix = self.url_prefix()
        path = self.path.resolve(context)
        return urljoin(prefix, quote(path))

    def render(self, context):
        url = self.url(context)
        if context.autoescape:
            url = conditional_escape(url)
        if self.varname is None:
            return url
        context[self.varname] = url
        return ""

    @classmethod
    def handle_token(cls, parser, token):
        """
        Class method to parse prefix node and return a Node.
        """
        bits = token.split_contents()

        if len(bits) < 2:
            raise template.TemplateSyntaxError(
                "'%s' takes at least one argument (path to file)" % bits[0]
            )

        path = parser.compile_filter(bits[1])

        if len(bits) >= 2 and bits[-2] == "as":
            varname = bits[3]
        else:
            varname = None

        return cls(varname, path)

@register.tag("cdn_static")
def do_cdn_static(parser, token):
    """
    This tag is used to replace the static template tag when using a CDN.
    Join the given path with the CDN_STATIC_URL setting.

    Usage::

        {% cdn_static path [as varname] %}

    Examples::

        {% cdn_static "myapp/css/base.css" %}
        {% cdn_static variable_with_path %}
        {% cdn_static "myapp/css/base.css" as admin_base_css %}
        {% cdn_static variable_with_path as varname %}
    """
    return CDNStaticNode.handle_token(parser, token)