"""dirty dict class."""


class DirtyDict(dict):
    """DirtyDict will keep track of dictionary access."""

    def __init__(self, *args, **kwargs):
        """Initialize DirtyDict."""
        super().__init__(*args, **kwargs)
        self._accessed = set()

    def __getitem__(self, key):
        """Get item."""
        self._accessed.add(key)
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        """Set item."""
        self._accessed.add(key)
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        """Delete item."""
        self._accessed.add(key)
        return super().__delitem__(key)

    def accessed(self):
        """Return accessed keys."""
        return self._accessed

    def reset_accessed(self):
        """Reset accessed keys."""
        self._accessed = set()

    def not_accessed(self):
        """Return not accessed keys."""
        return set(self.keys()) - self._accessed

    def __repr__(self):
        """Return representation."""
        return f"DirtyDict({super().__repr__()})"

    def __str__(self):
        """Return string representation."""
        return f"DirtyDict({super().__str__()})"
