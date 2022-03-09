from collections.abc import Generator
from typing import Any

COORD_RE: Any
COL_RANGE: str
ROW_RANGE: str
RANGE_EXPR: str
ABSOLUTE_RE: Any
SHEET_TITLE: str
SHEETRANGE_RE: Any

def get_column_interval(start, end): ...
def coordinate_from_string(coord_string): ...
def absolute_coordinate(coord_string): ...

col: Any

def get_column_letter(idx): ...
def column_index_from_string(str_col): ...
def range_boundaries(range_string): ...
def rows_from_range(range_string) -> Generator[Any, None, None]: ...
def cols_from_range(range_string) -> Generator[Any, None, None]: ...
def coordinate_to_tuple(coordinate): ...
def range_to_tuple(range_string): ...
def quote_sheetname(sheetname): ...