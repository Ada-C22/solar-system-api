import pytest


# @pytest.fixture
def empty_list():
    return []
# @pytest.fixture
def test_len_of_empty_list(empty_list):
    assert isinstance(empty_list, list)
    assert len(empty_list) == 0

# @pytest.fixture
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []



def test_get_one_planet_404(client):
    # Arrange
    # No setup needed - we want an empty database
    # Act
    response = client.get(f" / planets / {planet_id}")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 404
    assert response_body == {f"message": "Planet not found"}
