# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T


class AxisOrient(T.Enum):
    """One of ['top', 'right', 'left', 'bottom']"""
    def __init__(self, default_value=T.Undefined, **metadata):
        super(AxisOrient, self).__init__(['top', 'right', 'left', 'bottom'],
                                    default_value=default_value,
                                    **metadata)