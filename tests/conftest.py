import pytest

@pytest.fixture
def sample_code():
    return """
    A(user)
    G(user;name:Test)
    F(user;fixed)
    L(user;life)
    """
