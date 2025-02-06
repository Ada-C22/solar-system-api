def test_get_all_planets_with_no_records(client):
  # Act
  response = client.get("/planets")
  response_body = response.get_json()

  # Assert
  assert response.status_code == 200
  assert response_body == []

def test_get_all_planets_with_two_records(client, two_saved_planets):
  # Act
  response = client.get("/planets")
  response_body = response.get_json()

  # Assert
  response.status_code == 200
  assert len(response_body) == 2

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "name": "Earth",
        "description": "Earth is the fifth largest planet in our solar system and is the largest of the terrestrial planets",
        "diameter": 7926,
    }

def test_get_nonexisting_planet(client):
    # Act
    response = client.get("/planets/100")

    # Assert
    assert response.status_code == 404

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Saturn",
        "description": "Saturn is the sixth planet from the Sun and the second largest in the Solar System",
        "diameter": 74897,
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Saturn",
        "description": "Saturn is the sixth planet from the Sun and the second largest in the Solar System",
        "diameter": 74897,
    }
