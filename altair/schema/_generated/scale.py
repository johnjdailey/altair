# This file auto-generated by `_schema_parser.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .nicetime import NiceTime
from .scaletype import ScaleType


class Scale(BaseObject):
    """Wrapper for Vega-Lite Scale definition.
    
    Attributes
    ----------
    bandSize: CFloat
        
    clamp: Bool
        If true, values that exceed the data domain are clamped to either the minimum or maximum range value.
    domain: Union(Unicode, List(CFloat), List(Unicode))
        The domain of the scale, representing the set of data values.
    exponent: CFloat
        Sets the exponent of the scale transformation.
    includeRawDomain: Bool
        Uses the source data range as scale domain instead of aggregated data for aggregate axis.
    nice: Union(Bool, NiceTime)
        If specified, modifies the scale domain to use a more human-friendly value range.
    padding: CFloat
        Applies spacing among ordinal elements in the scale range.
    range: Union(Unicode, List(CFloat), List(Unicode))
        The range of the scale, representing the set of visual values.
    round: Bool
        If true, rounds numeric output values to integers.
    type: ScaleType
        
    zero: Bool
        If true, ensures that a zero baseline value is included in the scale domain.
    """
    bandSize = T.CFloat(allow_none=True, default_value=None, min=0)
    clamp = T.Bool(allow_none=True, default_value=None, help="""If true, values that exceed the data domain are clamped to either the minimum or maximum range value.""")
    domain = T.Union([T.Unicode(allow_none=True, default_value=None), T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None), T.List(T.Unicode(allow_none=True, default_value=None), allow_none=True, default_value=None)])
    exponent = T.CFloat(allow_none=True, default_value=None, help="""Sets the exponent of the scale transformation.""")
    includeRawDomain = T.Bool(allow_none=True, default_value=None, help="""Uses the source data range as scale domain instead of aggregated data for aggregate axis.""")
    nice = T.Union([T.Bool(allow_none=True, default_value=None), NiceTime(allow_none=True, default_value=None)])
    padding = T.CFloat(allow_none=True, default_value=None, help="""Applies spacing among ordinal elements in the scale range.""")
    range = T.Union([T.Unicode(allow_none=True, default_value=None), T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None), T.List(T.Unicode(allow_none=True, default_value=None), allow_none=True, default_value=None)])
    round = T.Bool(allow_none=True, default_value=None, help="""If true, rounds numeric output values to integers.""")
    type = ScaleType(allow_none=True, default_value=None)
    zero = T.Bool(allow_none=True, default_value=None, help="""If true, ensures that a zero baseline value is included in the scale domain.""")
    
    def __init__(self, bandSize=None, clamp=None, domain=None, exponent=None, includeRawDomain=None, nice=None, padding=None, range=None, round=None, type=None, zero=None, **kwargs):
        kwds = dict(bandSize=bandSize, clamp=clamp, domain=domain, exponent=exponent, includeRawDomain=includeRawDomain, nice=nice, padding=padding, range=range, round=round, type=type, zero=zero)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(Scale, self).__init__(**kwargs)