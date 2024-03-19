import enum


class Permissions(enum.StrEnum):
    """
    Generic permission flags for modifying specific content
    within the permission attached object. Inheritable.
    """
    NONE = enum.auto()
    READ = enum.auto()
    READ_CHILDREN = enum.auto()
    WRITE = enum.auto()
    WRITE_CHILDREN = enum.auto()
    CREATE = enum.auto()
    CREATE_CHILDREN = enum.auto()
    DELETE = enum.auto()
    DELETE_CHILDREN = enum.auto()
