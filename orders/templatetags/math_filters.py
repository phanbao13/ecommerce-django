from django import template
register = template.Library()

@register.filter
def addition(value, arg):
    """Addition the given value by the provided argument."""
    try:
        return value + arg
    except (ValueError, TypeError):
        return ""  # Return an empty string if there's an error