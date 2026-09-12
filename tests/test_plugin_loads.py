"""Standalone load test — the plugin must load against FakePluginContext
with zero host dependencies (the Protocol v1 contract)."""
from conftest import load_plugin_module
from fake_plugin_context import FakePluginContext


def test_plugin_loads_and_registers_router():
    ctx = FakePluginContext()
    mod = load_plugin_module()
    mod.Plugin().on_load(ctx)
    assert ctx.registry.routers, "plugin registered no router"
