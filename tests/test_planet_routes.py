def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client,two_save_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "Smallest planet",
        "random": "ran random"
    }
def test_create_one_planet(client):

    response = client.post("/planets", json={
        "name": "Pluto",
        "description": "It is a dwarf planet",
        "random": "ran9"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Pluto",
        "description": "It is a dwarf planet",
        "random": "ran9"
    }
