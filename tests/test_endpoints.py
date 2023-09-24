# coding: utf-8
"""Test server module."""

import copy

from fastapi import status


def test_server_run_without_error(test_app):
    """Should success and return 200 for code status."""
    response = test_app.get("/")
    assert response.status_code == status.HTTP_200_OK


def test_server_run_with_non_existant_endpoint(test_app):
    """Should failed and return 404 for code status."""
    response = test_app.get("/tests")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_verify_http_traffic(test_app, user_headers):
    """Should success and return 201 for code status."""

    signals = {
        "host": "127.0.0.1",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    }
    response = test_app.post(
        "/check_incomming_http_traffic",
        headers=user_headers,
        json=signals,
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_verify_http_traffic_with_unknow_origin(test_app, user_headers):
    """Should failed and return 503 for code status."""
    headers = copy.deepcopy(user_headers)
    del headers["X-Origin"]
    signals = {
        "host": "127.0.0.1",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    }
    response = test_app.post(
        "/check_incomming_http_traffic",
        headers=headers,
        json=signals,
    )
    assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE


def test_verify_http_traffic_with_bot_user_agent(test_app, user_headers):
    """Should failed and return 403 for code status."""

    signals = {
        "host": "127.0.0.1",
        "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    }
    response = test_app.post(
        "/check_incomming_http_traffic",
        headers=user_headers,
        json=signals,
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
