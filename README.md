# anotherme-plugin-template

Skeleton for building [AnotherMe](https://github.com/MatousVavra/AnotherMe)
plugins.

## Layout

    plugin/               # the installable plugin dir (this is what ships)
      plugin.yaml        # manifest: name, version, capabilities, deps, ui, settings
      plugin/__init__.py # entrypoint module exposing `class Plugin`
      ui/                # optional UI fragment (needs the `ui` capability)
    tests/               # standalone unit tests (no host checkout needed)
    tests/integration/   # route tests that run inside the released app image
    .github/workflows/   # CI: unit job + integration job

## The contract (Protocol v1)

- Your plugin may import stdlib, `fastapi`, `pydantic`, `httpx`, `yaml`, and
  `openai` — never `src.*` or `kernel.*`.
- Everything else comes through `PluginContext` (`ctx.get_env`,
  `ctx.vault_manager`, `ctx.db_module`, `ctx.llm_client`, ...).
- `tests/fake_plugin_context.py` is the contract surface for unit tests;
  `tests/test_no_host_imports.py` fails CI if you break the import rule.

## Developing

1. Click "Use this template" on GitHub, or copy this dir.
2. Edit `plugin/plugin.yaml` (name, description, capabilities) and
   `plugin/plugin/__init__.py`.
3. Run unit tests:

       pip install fastapi pydantic httpx pyyaml pytest pytest-asyncio openai
       pytest tests/ --ignore=tests/integration

4. To develop against a live app: point `COMMUNITY_PLUGINS_DIR` at this
   checkout's parent directory and start AnotherMe — the plugin hot-reloads.

## Releasing

Tag a release (`v0.1.0`), then add an entry to the
[community index](https://github.com/MatousVavra/anotherme-plugins):

    {"name": "hello", "repo": "<owner>/<repo>", "tag": "v0.1.0",
     "description": "...", "author": "..."}
