# URF Spine public quickstart

Requires Git and Python 3.

```bash
git clone https://github.com/inaciovasquez2020/urf-spine-public.git
cd urf-spine-public
python3 tools/verify_public_spine_surface.py
```

Expected output is `PUBLIC_SPINE_SURFACE_OK`. This checks the public README and [minimal certificate](examples/minimal_certificate/minimal_spine_certificate.json), including its declared proof boundaries. See [status](STATUS.md) and [scope limitations](SCOPE_LIMITATIONS_STATUS.md).
