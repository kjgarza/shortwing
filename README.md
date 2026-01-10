# Kestrel

Lightweight CLI wrapper for Dimensions DSL queries via dimcli.

## Installation

```bash
uv pip install .
```

## Usage

```bash
# Query as argument
kestrel "search grants for \"malaria\" return researchers"

# Query from stdin
echo 'search grants for "malaria"' | kestrel

# With subcommand
kestrel query "search grants return grants"

# Compact JSON output
kestrel --compact "search grants"

# Use a specific instance from dsl.ini
kestrel --instance test "search grants"
```

## Configuration

Credentials are loaded in the following order of priority:

1. **CLI flags** (`--key`, `--endpoint`)
2. **Environment variables** (`DIMENSIONS_KEY`, `DIMENSIONS_ENDPOINT`)
3. **dsl.ini file** (default)

### Using dsl.ini (Recommended)

Kestrel uses the same `dsl.ini` configuration file as dimcli. Create the file at `~/.dimensions/dsl.ini`:

```ini
[instance.live]
url=https://app.dimensions.ai
login=
password=
key=your-api-key
```

You can define multiple instances and select them with `--instance`:

```ini
[instance.live]
url=https://app.dimensions.ai
key=your-live-key

[instance.test]
url=https://test.dimensions.ai
key=your-test-key
```

```bash
kestrel --instance test "search grants"
```

### Using Environment Variables

```bash
export DIMENSIONS_KEY=your-api-key
export DIMENSIONS_ENDPOINT=https://app.dimensions.ai  # optional
```

### Using CLI Flags

```bash
kestrel --key your-api-key "search grants"
kestrel --key your-api-key --endpoint https://custom.endpoint.com "search grants"
```

## Exit Codes

- 0: Success
- 1: Query/API error
- 2: Configuration/authentication error
