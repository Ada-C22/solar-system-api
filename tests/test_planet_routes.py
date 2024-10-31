# Wave 6
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_with_no_data_returns_404(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "planet 1 not found"}

def test_get_one_planet(client,two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id" : 1,
        "name" : "Mercury",
        "description" : "Smallest, closest to the Sun, extreme temperatures.", 
        "distance_from_sun" : 57.9
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets",
        json={
        "name" : "Earth",
        "description" : "Supports life, water in all forms, protective atmosphere.",
        "distance_from_sun" : 149.6
        })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id" : 1,
        "name" : "Earth",
        "description" : "Supports life, water in all forms, protective atmosphere.",
        "distance_from_sun" : 149.6
        }
    
def test_create_one_planet_with_planets_already_in_db(client, two_saved_planets):
    # Act
    response = client.post("/planets",
        json={
        "name" : "Earth",
        "description" : "Supports life, water in all forms, protective atmosphere.",
        "distance_from_sun" : 149.6
        })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id" : 3,
        "name" : "Earth",
        "description" : "Supports life, water in all forms, protective atmosphere.",
        "distance_from_sun" : 149.6
        }
    