import requests

base_url = "https://ru.yougile.com"
auth = "Bearer Token"   # Введите свой токен авторизации
title = "Автоматизация"

created_id = None


def test_create_project():
    global created_id
    resp = requests.post(base_url + "/api-v2/projects", json={
        "title": title}, headers={"Authorization": auth})
    created_id = resp.json()["id"]
    assert resp.status_code == 201
    assert "application/json" in resp.headers["Content-Type"]
    assert len(created_id) > 0


def test_create_untitled():
    resp = requests.post(base_url + "/api-v2/projects",
                         headers={"Authorization": auth})
    body = resp.json()["message"]
    assert resp.status_code == 400
    assert "title should not be empty" in body


def test_get_project():
    resp = requests.get(base_url + "/api-v2/projects/" + created_id,
                        headers={"Authorization": auth})
    body = resp.json()
    assert resp.status_code == 200
    assert body["title"] == title


def test_get_project_error():
    resp = requests.get(base_url + "/api-v2/projects/" + created_id + "123",
                        headers={"Authorization": auth})
    body = resp.json()["message"]
    assert resp.status_code == 404
    assert body == "Проект не найден"


def test_change_project():
    resp = requests.put(base_url + "/api-v2/projects/" + created_id, json={
        "title": "Прикольная автоматизация"}, headers={"Authorization": auth})
    nev_id = resp.json()["id"]
    assert resp.status_code == 200
    assert nev_id == created_id
    resp = requests.get(base_url + "/api-v2/projects/" + nev_id,
                        headers={"Authorization": auth})
    body = resp.json()
    assert body["title"] == "Прикольная автоматизация"


def test_change_project_unauthorized():
    resp = requests.put(base_url + "/api-v2/projects/" + created_id,
                        json={"title": "Nev автоматизация"})
    response_body = resp.json()["message"]
    assert resp.status_code == 401
    assert response_body == "Unauthorized"


def test_delete_project():
    resp = requests.put(base_url + "/api-v2/projects/" + created_id,
                        json={"deleted": True,
                              "title": "Прикольная автоматизация"},
                        headers={"Authorization": auth})
    assert resp.status_code == 200
    resp = requests.get(base_url + "/api-v2/projects/",
                        headers={"Authorization": auth})
    body = resp.json()
    print(body)
