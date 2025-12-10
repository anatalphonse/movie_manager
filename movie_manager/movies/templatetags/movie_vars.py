from django import template

register = template.Library()

@register.filter
def get_stars(value):
    """
    Returns a list of 5 booleans/integers representing stars.
    Value is assumed to be out of 10.
    Example: 8.5 -> 4.25 stars -> [1, 1, 1, 1, 0.5] or similar.
    For simplicity:
    - full: 1
    - half: 0.5 (optional, or just logic in template)
    - empty: 0
    """
    try:
        score = float(value)
    except (ValueError, TypeError):
        score = 0
    
    # Scale 10 -> 5
    rating = score / 2.0
    
    stars = []
    for i in range(1, 6):
        if rating >= i:
            stars.append(1) # Full
        elif rating >= i - 0.5:
            stars.append(2) # Half
        else:
            stars.append(0) # Empty
            
    return stars

@register.filter
def to_float(value):
    try:
        return float(value)
    except:
        return 0.0
