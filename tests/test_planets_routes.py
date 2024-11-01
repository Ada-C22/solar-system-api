def test_get_all_planets_with_no_records(client):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_cat_succeeds(client, two_saved_planets):
    response = client.get("planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name" : "Mercury", 
        "description": "terrestrial planet", 
        "size" : 1516
    }


def test_create_one_planet_in_empty_db(client):
    response = client.post("/planets", json={
        "name" : "Venus", 
        "description" : "Earth's twin", 
        "size" : 3760
    })
    response_body = response.get_json()
    
    assert response.status_code == 201
    assert response_body == {
        "name" : "Venus", 
        "description" : "Earth's twin",
        "size" : 3760,
        "id": 1     
    }

def test_create_one_planet(client):
    response = client.post("/planets", json={
        "name" : "some_planet",
        "description" :"random",
        "size" : 78378
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id" : 1,
        "name" : "some_planet",
        "description" :"random",
        "size" : 78378

    }

def test_create_one_planet_with_planets_already_in_db(client, two_saved_planets):
    response = client.post("/planets", json={
        "name" : "Garfield",
        "description" : "orangish",
        "size" : 3959
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id" : 3,
        "name" : "Garfield",
        "description" : "orangish",
        "size" : 3959
    }


