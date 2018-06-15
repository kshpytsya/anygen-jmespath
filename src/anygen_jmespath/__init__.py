import anygen.scanextras
import functools
import jmespath

try:
    __version__ = __import__('pkg_resources').get_distribution(__name__).version
except:  # noqa # pragma: no cover
    pass


@functools.lru_cache()
def _compile(expr):
    return jmespath.compile(expr)


def _search(expr, data):
    return _compile(expr).search(data)


def yaql_jmespath(expr, data):
    return _search(expr, data)


def jinjaglobals_jmespath(expr, data):
    return _search(expr, data)


def jinjafilter_jmespath(data, expr):
    return _search(expr, data)


extras = anygen.scanextras.scanme()
