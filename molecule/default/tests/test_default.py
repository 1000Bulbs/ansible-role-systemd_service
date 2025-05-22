# molecule/default/tests/test_default.py
systemd_service_name = "example"


def test_service_is_enabled(host):
    svc = host.service(systemd_service_name)
    assert svc.is_enabled
