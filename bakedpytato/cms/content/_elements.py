import json
import typing

from dominate import tags

from . import schemas


def _get_tag(tag: str):
    """
    Internal utility function to convert a string tag
    into a reference to the appropriate dominate class.
    :param tag: The tag to retrieve
    :return: A dominate DOM class
    """
    return getattr(tags, tag)


def render(
        config:
        typing.Union[str, typing.Dict]) -> tags.html_tag:
    if isinstance(config, str):
        pass

