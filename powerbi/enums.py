from enum import Enum


class ColumnDataTypes(Enum):
    """Represents all the data types you can use
    when creating a new column in a `PowerBiTable`.

    ### Usage:
    ----
        >>> from powerbi.enums import ColumnDataTypes
        >>> ColumnDataTypes.Int64.value
    """

    Int64 = 'Int64'
    Double = 'Double'
    Boolean = 'bool'
    Datetime = 'DateTime'
    String = 'string'
    Decimal = 'Decimal'


class ColumnAggregationMethods(Enum):
    """Represents all the aggregation methods you can
    use  when creating aggregating a new column in a
    `PowerBiTable`.

    ### Usage:
    ----
        >>> from powerbi.enums import ColumnAggregationMethods
        >>> ColumnAggregationMethods.Count.value
    """

    Default = 'default'
    Null = 'none'
    Sum = 'sum'
    Min = 'min'
    Max = 'max'
    Count = 'count'
    Average = 'average'
    DistinctCount = 'distinctCount'