

def test_get_planets(client):
    response = client.get("/planets")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert response_body == []



def test_get_single_planet(client, three_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "some_planet",
        "description": "rocky, no signs of life", 
        "size": 100
    }
    
def test_get_single_planet_no_records(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404

def test_get_all_planets(client, three_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "some_planet",
        "description": "rocky, no signs of life", 
        "size": 100
    },
    {
        "id": 2,
        "name": "Earth",
        "description": "with lifeforms, water and land", 
        "size": 5000
    },
    {
        "id": 3,
        "name": "Pluto",
        "description": "still a planet", 
        "size": 200
    },
    ]

def test_create_new_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Venus",
        "description": "closest to the Earth",
        "size": 1244
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Venus",
        "description": "closest to the Earth",
        "size": 1244
    }