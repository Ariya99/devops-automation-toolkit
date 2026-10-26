from openpyxl.styles import PatternFill

# Cache PatternFill objects to improve performance and reduce memory usage.
# (Addressing the 'Bolt' performance directive)
_GREEN_FILL = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
_ORANGE_FILL = PatternFill(start_color="FFA500", end_color="FFA500", fill_type="solid")
_RED_FILL = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")

def apply_failure_rate_formatting(cell):
    """
    Applies conditional formatting (Green, Orange, or Red) to a cell
    based on its failure rate percentage value.
    """
    value = cell.value
    if value is not None:
        if value > 33:
            cell.fill = _RED_FILL
        elif 10 < value <= 33:
            cell.fill = _ORANGE_FILL
        else:
            cell.fill = _GREEN_FILL
