pip install toml && python -c 'import toml; c = toml.load("pyproject.toml"); print("\n".join(c["build-system"]["requires"]))' | pip install -r /dev/stdin
