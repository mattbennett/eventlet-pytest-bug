# eventlet-pytest-bug

Testing incompatibilities between versions of python, pytest and eventlet.

## Discovered incompatibilities

1. python 3, pytest >= 2.8.0 and eventlet < 0.18.0:

```
TypeError: read() missing 1 required positional argument: 'buflen'
```

2. python 3, pytest >= 2.8.0 and eventlet >= 0.18.0:

```
RuntimeError: Second simultaneous read on fileno 20 detected.
```
