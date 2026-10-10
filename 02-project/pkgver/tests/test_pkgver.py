import httpx

from pkgver import latest_version


def fake_pypi(request: httpx.Request) -> httpx.Response:
    assert request.url.path == "/pypi/uv/json"
    return httpx.Response(
        200,
        json={
            "info": {"version": "0.13.0"},
            "urls": [{"upload_time": "2026-10-09T19:49:55"}],
        },
    )


def test_latest_version():
    with httpx.Client(transport=httpx.MockTransport(fake_pypi)) as client:
        assert latest_version(client, "uv") == ("0.13.0", "2026-10-09")
