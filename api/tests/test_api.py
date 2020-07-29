import pytest
from django.conf import settings
from rest_framework.test import APIClient

from api.tests import expected


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.parametrize(
    'from_, to, expected_response',
    [(5, 10, expected.EXPECTED_FIB_5_TO_10), (7, 15, expected.EXPECTED_FIB_7_TO_15)]
)
def test_get_correct_slice(client, from_, to, expected_response):

    resp = client.get(f'/fibonachi/?from_={from_}&to={to}')

    assert resp.status_code == 200
    assert resp.json() == expected_response


def test_reverse_slice(client):
    from_ = 10
    to = 5
    resp = client.get(f'/fibonachi/?from_={from_}&to={to}')

    assert resp.status_code == 400
    assert resp.json() == expected.EXPECTED_REVERSE_SLICE


def test_max_right_border(client):
    from_ = 1
    to = settings.MAX_FIBONACHI_INDEX + 1

    resp = client.get(f'/fibonachi/?from_={from_}&to={to}')

    assert resp.status_code == 400
    assert resp.json() == expected.EXPECTED_MAX_RIGHT_BORDER


def test_min_left_border(client):
    from_ = 0
    to = 3

    resp = client.get(f'/fibonachi/?from_={from_}&to={to}')

    assert resp.status_code == 400
    assert resp.json() == expected.EXPECTED_MIN_LEFT_BORDER
