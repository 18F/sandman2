"""Tests for non-core functionality in sandman2."""

from pytest_flask.fixtures import client

def test_pagination(client):
    """Do we return paginated results when a 'page' parameter is provided?"""
    response = client.get('/artist?page=2')
    assert response.status_code == 200
    assert len(response.json['resources']) == 20
    assert response.json['resources'][0]['ArtistId'] == 21

def test_filtering(client):
    """Do we return filtered results when a URL parameter is provided?"""
    response = client.get('/artist?Name=AC/DC')
    assert response.status_code == 200
    assert len(response.json['resources']) == 1
    assert response.json['resources'][0]['ArtistId'] == 1

def test_gt_filtering(client):
    """Do we return results filtered by greater-than when requested?"""
    response = client.get('/artist?Name__gt=R&sort=Name')
    assert response.status_code == 200
    assert response.json['resources'][0]['Name'] == 'R.E.M.'

def test_wildcard_filtering(client):
    """Do we return filtered results when a wildcarded URL parameter is provided?"""
    response = client.get('/artist?Name__like=%25DC%25')
    assert response.status_code == 200
    assert len(response.json['resources']) == 1
    assert response.json['resources'][0]['ArtistId'] == 1

def test_sorting(client):
    """Do we return sorted results when a 'sort' URL parameter is provided?"""
    response = client.get('/artist?sort=Name&per_page=1000')
    assert response.status_code == 200
    assert len(response.json['resources']) == 275
    assert response.json['resources'][0]['ArtistId'] == 43
