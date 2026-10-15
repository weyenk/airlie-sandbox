import unicodedata
import re

def slugify(title: str) -> str:
    """Convert a title into a URL-friendly slug."""
    # Normalize unicode characters to ASCII
    normalized = unicodedata.normalize('NFKD', title)
    # Convert to ASCII, removing non-ASCII characters
    ascii_title = normalized.encode('ascii', 'ignore').decode('ascii')
    # Replace non-alphanumeric characters with dashes
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', ascii_title)
    # Remove leading/trailing dashes
    slug = slug.strip('-')
    # Convert to lowercase
    slug = slug.lower()
    return slug