class RCONError(Exception):
    """Base class for RCON-related errors."""
    pass

class AuthenticationError(RCONError):
    """Raised when authentication fails."""
    pass

class ConnectionError(RCONError):
    """Raised when there is a connection issue."""
    pass