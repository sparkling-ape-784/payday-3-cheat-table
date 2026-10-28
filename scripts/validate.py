# Build: d28ca4eb88f53c7a13c1f57588ee108b

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
