def test_get_all_planets_with_no_records(client):
    #Arrange has already happened
    #Act 
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_succeeds(client, two_saved_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury", 
        "description": "The smallest planet",
        "number_moons": 0, 
        "color": "Gray"

    }

def test_planet_not_found(client):
    #Arrange has already happened
    #Act 
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 404
    assert response_body == {
        "message": "Planet id 1 is not found"
    }

def test_get_all_planets_with_records(client, two_saved_planets):
    #Arrange has already happened
    #Act 
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "name": "Mercury", 
        "description": "The smallest planet",
        "number_moons": 0, 
        "color": "Gray"

    }, 
    {
        "id": 2,
        "name": "Venus", 
        "description": "Our closest neighbor",
        "number_moons": 0, 
        "color": "Yellowish"

    }]

def test_create_one_planet(client): 
    response = client.post("/planets", json={
        "id": 1,
        "name": "Neptune", 
        "description": "Has super sonic winds",
        "number_moons": 16, 
        "color": "Blue"
    })
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Neptune", 
        "description": "Has super sonic winds",
        "number_moons": 16, 
        "color": "Blue"
    }

def test_create_one_planet_with_planets_already_in_db(client, two_saved_planets): 
    response = client.post("/planets", json={
        "id": 1,
        "name": "Neptune", 
        "description": "Has super sonic winds",
        "number_moons": 16, 
        "color": "Blue"
    })
    response_body = response.get_json()

    #Assert 
    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "name": "Neptune", 
        "description": "Has super sonic winds",
        "number_moons": 16, 
        "color": "Blue"
    }