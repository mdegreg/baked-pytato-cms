import pytest

from bakedpytato.cms.content import _elements


@pytest.mark.parametrize(
    "tag, my_other_val",
    [
        ('html', 1),
        ('div', 2),
        ('a', 3),
        ('img', 4),
        ('body', 5),
        ('p', 6)
    ]
)
def test_get_tags(tag, my_other_val):
    # TODO: remove example second value here; for demonstration only
    print(my_other_val)
    result = _elements._get_tag(tag)
    assert issubclass(result, _elements.tags.html_tag)


@pytest.mark.parametrize(
    "tag",
    [
        'womp',
        'derp'
    ]
)
def test_raises_on_invalid_tag(tag):
    with pytest.raises(AttributeError):
        _elements._get_tag(tag)
