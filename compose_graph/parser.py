"""Docker Compose YAML to Mermaid flowchart parser."""

from __future__ import annotations

from typing import List
import yaml


def compose_to_mermaid(yaml_text: str) -> str:
    data = yaml.safe_load(yaml_text) or {}
    services = data.get("services", {}) or {}
    lines: List[str] = ["flowchart LR"]
    for name, cfg in services.items():
        lines.append(f"  {name}[{name}]")
        deps = (cfg or {}).get("depends_on", [])
        if isinstance(deps, dict):
            deps = list(deps.keys())
        for dep in deps:
            lines.append(f"  {name} --> {dep}")
    return "\n".join(lines)
