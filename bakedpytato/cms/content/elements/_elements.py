from dominate import tags


def get_tag(tag: str):
    return getattr(tags, tag)
