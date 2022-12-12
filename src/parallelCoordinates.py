from enum import Enum
from dataclasses import dataclass


class GraphType(Enum):

    parallel_coords = 0
    chosen_coords = 1
    linear_comb = 2


class ExportMethod(Enum):

    bitmap = 0
    data_series = 1


@dataclass
class Parameters:
    graph_type: GraphType
    export_method: ExportMethod
    chosenDimensions: list
