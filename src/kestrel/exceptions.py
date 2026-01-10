"""Exit codes and exceptions for Kestrel CLI."""

# Exit codes as constants
EXIT_SUCCESS = 0
EXIT_QUERY_ERROR = 1
EXIT_CONFIG_ERROR = 2


class KestrelError(Exception):
    """Base exception for Kestrel."""

    exit_code: int = EXIT_QUERY_ERROR


class ConfigurationError(KestrelError):
    """Raised when configuration/authentication fails."""

    exit_code = EXIT_CONFIG_ERROR


class QueryError(KestrelError):
    """Raised when query execution fails."""

    exit_code = EXIT_QUERY_ERROR
