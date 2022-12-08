from enum import Enum


class GraphType(Enum):

    parallel_coords = 0
    chosen_coords = 1
    linear_comb = 2


class ExportMethod(Enum):

    bitmap = 0
    data_series = 1


class Parameters:

    graph_type = GraphType
    export_method = ExportMethod
