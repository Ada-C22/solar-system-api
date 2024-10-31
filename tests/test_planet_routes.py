def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act 
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "moons": 0,
        "surface_area": 28880, 
        "distance_from_sun": 35980,
        "namesake": "Roman god of travelers, aka Hermes."
    }

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Mercury",
        "moons": 0,
        "surface_area": 28880, 
        "distance_from_sun": 35980,
        "namesake": "Roman god of travelers, aka Hermes."
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "moons": 0,
        "surface_area": 28880, 
        "distance_from_sun": 35980,
        "namesake": "Roman god of travelers, aka Hermes."
    }

def test_create_one_planet_with_two_planets_in_database(client, two_saved_planets):
    # Act
    response = client.post("/planets", json={
        "name": "Earth",
        "moons": 1,
        "surface_area": 196900, 
        "distance_from_sun": 92960,
        "namesake": "A variation on the word \"ground\" in several languages."
    })
    
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "name": "Earth",
        "moons": 1,
        "surface_area": 196900, 
        "distance_from_sun": 92960,
        "namesake": "A variation on the word \"ground\" in several languages."
    }