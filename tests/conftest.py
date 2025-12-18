import pytest
from lib.database_connection import DatabaseConnection

# This is a Pytest fixture.
# It creates an object that can be used in tests.
# Used to create a database connection.

@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    return conn

# Now, when a test includes a parameter named `db_connection`, Pytest automatically
# calls this fixture before the test runs and passes in its return value instead 
# of the function itself.
