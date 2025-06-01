class UserExistsException(Exception):
    """Email Exists!"""

class CredentialsException(Exception):
    """Invalid Credentials!"""

class UserNotFoundException(Exception):
    """User not found!"""