import pytest

def test_get_every_single_planet(client, get_every_single_planet):
    response = client.get(f"/planets")
    response_body = response.get_json()

    # assert
    assert response.status_code == 200
    assert len(response_body) == 5

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_not_found_404(client):
    # Arrange
    # No setup needed - we want an empty database
    # Act
    response = client.get(f"/planets/10")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "10 not found"}

def test_get_one_planet_400(client, get_planet_invalid_id):
    # Arrange
    # No setup needed - we want an empty database
    # Act
    response = client.get(f"/planets/abc")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == {"message": f"planet abc invalid"}

def test_get_one_planet_success_200(client, two_saved_planets):
    # Act
    response = client.get(f"/planets/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 2,
        "name": "Vulcan",
        "description": "the best",
        "moon": 2
    }

def test_create_new_planet_with_data_201(client, create_new_planet):
    # Act
    response = client.post("/planets", json={
        "name": "Romulus",
        "description": "Homeworld of the Romulan Star Empire, featuring green-tinted skies and advanced architecture.",
        "moon": 2
    })
    response_body = response.get_json()
    response_body.pop("id")

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "name": "Romulus",
        "description": "Homeworld of the Romulan Star Empire, featuring green-tinted skies and advanced architecture.",
        "moon": 2
    }
    
def test_update_existing_planet_minus_one_moon(client, update_existing_planet):
    # Act 
    response = client.put("/planets/1", json={
        "name": "Kronos",
        "description": "rich in warrior culture and tradition, featuring magnificent cities built among dramatic mountain ranges, home to the legendary Great Hall of the High Council, and birthplace of many of the quadrant's greatest warriors and most honored traditions",
        "moon": 6    
    })
    
    # Assert
    assert response.status_code == 204
    verify_response = client.get("planets/1")
    verify_body = verify_response.get_json()
    assert verify_body["moon"] == 6
    
def test_delete_existing_planet(client,create_new_planet):
    # Act
    response = client.delete("/planets/1")
    
    # Assert
    assert response.status_code == 204
    check_respone = client.get("/planets/1")
    assert check_respone.status_code == 404
    

    