# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject


class LegendConfig(BaseObject):
    """Wrapper for Vega-Lite LegendConfig definition.
    
    Attributes
    ----------
    orient: Unicode
        The orientation of the legend.
    properties: Any
        Optional mark property definitions for custom legend styling.
    shortTimeLabels: Bool
        Whether month names and weekday names should be abbreviated.
    """
    orient = T.Unicode(allow_none=True, default_value=None, help="""The orientation of the legend.""")
    properties = T.Any(allow_none=True, default_value=None, help="""Optional mark property definitions for custom legend styling.""")
    shortTimeLabels = T.Bool(allow_none=True, default_value=None, help="""Whether month names and weekday names should be abbreviated.""")
    
    def __init__(self, orient=None, properties=None, shortTimeLabels=None, **kwargs):
        kwds = dict(orient=orient, properties=properties, shortTimeLabels=shortTimeLabels)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(LegendConfig, self).__init__(**kwargs)