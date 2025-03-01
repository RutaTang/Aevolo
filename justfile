#!/usr/bin/env just --justfile

build:
    #!/usr/bin/env bash
    source .venv/bin/activate
    python -m build

upload:
    #!/usr/bin/env bash
    source .venv/bin/activate
    python -m twine upload --skip-existing dist/*