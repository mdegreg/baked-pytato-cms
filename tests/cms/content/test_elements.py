import pytest

from bakedpytato.cms.content import _elements


@pytest.mark.parametrize(
    "tag",
    [
        'html',
        'div',
        'a',
        'img',
        'body',
        'p'
    ]
)
def test_get_tags(tag):
    result = _elements._get_tag(tag)
    assert issubclass(result, _elements.tags.html_tag)
