# from app.routes.planet_routes import planet_id
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet_succeeds(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "first planet",
        "num_moons": 0
    }

def test_get_one_planet_fails_return_404(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": f"Planet 1 not found."}

def test_create_one_planet_in_empty_db(client):
    response = client.post("/planets", json={
        "name": "Earth",
        "description": "Blue planet",
        "num_moons": 1
    })

    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id" : 1,
        "name": "Earth",
        "description": "Blue planet",
        "num_moons": 1
    }
