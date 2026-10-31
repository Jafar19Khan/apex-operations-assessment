# Security

- `.env` is ignored by Git; `.env.example` is a placeholder only.
- PostgreSQL has no published host port; API binds to host loopback only.
- API container runs as a non-root user.
- SQL uses parameterized values; request fields are validated and length-limited.
- Client errors are generic; diagnostic details remain in container logs.
- Jenkins Docker socket access is effectively privileged. Keep Jenkins local and never expose it publicly.
- A real hosted deployment should use a secrets manager, least-privilege identity, private networking, TLS, patched images and restricted CI agents.
- Run and retain an actual image/dependency scan; no scan result is asserted here.
