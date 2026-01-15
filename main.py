from __future__ import annotations
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


def _load_yaml(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Missing data file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def define_env(env):
    """
    MkDocs Macros entrypoint.
    """

    # --- Load module registry once ---
    data_path = Path(env.project_dir) / "docs" / "assets" / "edia_modules_info.yml"
    registry = _load_yaml(data_path).get("modules", {})

    def _get_module(key: str) -> Dict[str, Any]:
        if key not in registry:
            known = ", ".join(sorted(registry.keys()))
            raise KeyError(f"Unknown EDIA module key '{key}'. Known keys: {known}")
        return registry[key]

    # ----------------------------
    # Macro API
    # ----------------------------

    @env.macro
    def edia(
        key: str,
        *,
        version: Optional[str] = None,
        text: Optional[str] = None,
        target_blank: bool = True,
    ) -> str:
        """
        Render a single EDIA module link with icon + label + [stage] + optional version.

        Usage:
          {{ edia("eye") }}
          {{ edia("eye", version="0.2") }}
          {{ edia("eye", text="Custom Label") }}
        """
        m = _get_module(key)

        name = text or m["name"]
        icon = m["icon"]
        url = m["url"]

        version_final = version or m.get("default_version")

        # Build display label
        suffix_parts = []
        if version_final:
            suffix_parts.append(f"{version_final}")

        suffix = f" [{' • '.join(suffix_parts)}]" if suffix_parts else ""

        # mkdocs-material emoji/icon syntax:
        # [:icon-name: Label](url){:target="_blank"}
        attrs = '{:target="_blank"}' if target_blank else ""
        return f"[:{icon}: {name}{suffix}]({url}){attrs}"

    @env.macro
    def edia_list(
        keys: List[str],
        *,
        version: Optional[str] = None,
        stage: Optional[str] = None,
    ) -> str:
        """
        Render a bullet list of EDIA modules.

        Usage:
          {{ edia_list(["core","eye","eye_vive"]) }}
        """
        lines = [f"- {edia(k, version=version)}" for k in keys]
        return "\n".join(lines)

    @env.macro
    def edia_inline(
        keys: List[str],
        *,
        sep: str = " · ",
        version: Optional[str] = None,
        stage: Optional[str] = None,
    ) -> str:
        """
        Render an inline sequence of module links.

        Usage:
          {{ edia_inline(["core","eye"]) }}
        """
        return sep.join(edia(k, version=version) for k in keys)

    @env.macro
    def edia_modules() -> List[str]:
        """
        Return known module keys (useful for debugging / docs).
        """
        return sorted(registry.keys())
