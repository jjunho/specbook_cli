#!/usr/bin/env python3
"""
SpecBook — Specification‑Driven Development para livros (protótipo CLI)
"""

from __future__ import annotations
import argparse
import re
from pathlib import Path
from textwrap import dedent
import json

try:
    import yaml  # type: ignore
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

# ---------------------------- Configuração --------------------------------- #

DIR_STRUCTURE = {
    "specs": "specs",
    "characters": "specs/characters",
    "settings": "specs/settings",
    "plans": "plans",
    "tasks": "tasks",
    "fragments": "fragments",
    "scenes": "fragments/scenes",
    "dialogues": "fragments/dialogues",
    "drafts": "drafts",
    "reviews": "reviews",
}


# ---------------------------- Utilidades ----------------------------------- #

def get_project_root(project_path_str: str) -> Path | None:
    root = Path(project_path_str)
    if not root.exists():
        print(f"✖ Projeto não encontrado em: {root}. Rode 'init' antes.")
        return None
    return root

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, content: str, overwrite: bool = False):
    if path.exists() and not overwrite:
        return
    path.write_text(content, encoding="utf-8")

def to_yaml(data: dict) -> str:
    if HAVE_YAML:
        return yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
    return json.dumps(data, ensure_ascii=False, indent=2)

def parse_yaml(path: Path) -> dict:
    if not path.exists(): return {}
    try:
        content = path.read_text(encoding="utf-8")
        if HAVE_YAML: return yaml.safe_load(content) or {}
        return json.loads(content)
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        print(f"⚠ Aviso: Falha ao ler o arquivo {path.name}: {e}")
        return {}

def interactive_prompt(question: str, default: str | None = None) -> str:
    prompt_text = f"{question}\n"
    if default: prompt_text += f"(Padrão: {default}) "
    prompt_text += "(Digite e pressione ENTER)\n> "
    print(prompt_text, end="")
    try:
        return input().strip() or default or ""
    except EOFError:
        return default or ""


# ---------------------------- Templates ------------------------------------ #

CONSTITUTION = "..." # Omitido para brevidade
PLAN_MD = "..."
RESEARCH_MD = "..."
TASKS_MD = "..."
SEED_YAML = {"idea": "", "genre": None, "themes": [], "status": "seeded"}
WORLD_YAML = {"world": {"name": "", "type": "realista|fantástico", "epoch": ""}}
ARCS_YAML = {"arcs": [{"name": "Arco do Protagonista", "start_state": "", "end_state": ""}]}
CHAPTER_MD = dedent("# Capítulo {num:02d}\n**Influências de spec**: personagens=[...], locais=[...], arcos=[...]\n")
CONSISTENCY_HEADER = "# Consistency Report"
SCENE_TEMPLATE = dedent(
"""
# Cena: {char_name} em {setting_name}

## Specs de Influência
- **Personagem:** {char_name} (Desejo: {char_desire}, Medo: {char_fear})
- **Cenário:** {setting_name} (Atmosfera: {setting_mood})

## Objetivo da Cena
- *O que o personagem quer alcançar nesta cena?*

## Rascunho da Cena
> (Comece a escrever aqui)
""")

# ---------------------------- Lógica de Geração ---------------------------- #

def _generate_scene(root: Path, char_name: str | None, setting_name: str | None):
    """Gera um arquivo de esqueleto para uma nova cena."""
    char_dir = root / DIR_STRUCTURE["characters"]
    setting_dir = root / DIR_STRUCTURE["settings"]

    # Seleciona personagem
    if not char_name:
        chars = [f.stem for f in char_dir.glob("*.yaml")]
        if not chars: return print("✖ Nenhum personagem encontrado para gerar cena.")
        print("Selecione um personagem:")
        for i, name in enumerate(chars): print(f"  [{i+1}] {name}")
        choice = int(interactive_prompt("Número do personagem:")) - 1
        char_name = chars[choice]
    
    char_path = char_dir / f"{char_name.lower().replace(' ', '_')}.yaml"
    if not char_path.exists(): return print(f"✖ Personagem '{char_name}' não encontrado.")
    char_data = parse_yaml(char_path)

    # Seleciona cenário
    if not setting_name:
        settings = [f.stem for f in setting_dir.glob("*.yaml")]
        if not settings: return print("✖ Nenhum cenário encontrado para gerar cena.")
        print("Selecione um cenário:")
        for i, name in enumerate(settings): print(f"  [{i+1}] {name}")
        choice = int(interactive_prompt("Número do cenário:")) - 1
        setting_name = settings[choice]

    setting_path = setting_dir / f"{setting_name.lower().replace(' ', '_')}.yaml"
    if not setting_path.exists(): return print(f"✖ Cenário '{setting_name}' não encontrado.")
    setting_data = parse_yaml(setting_path).get("world", {})

    # Gera conteúdo e salva arquivo
    scene_content = SCENE_TEMPLATE.format(
        char_name=char_data.get("name", "N/A"),
        char_desire=char_data.get("desire", "N/A"),
        char_fear=char_data.get("fear", "N/A"),
        setting_name=setting_data.get("name", "N/A"),
        setting_mood=setting_data.get("mood", "N/A"),
    )
    filename = f"scene_{char_name.lower()}_em_{setting_name.lower()}.md".replace(" ", "_")
    scene_path = root / DIR_STRUCTURE["scenes"] / filename
    write_file(scene_path, scene_content)
    print(f"✔ Cena gerada em: {scene_path}")

# (Outras funções de comando como _specify_seed, cmd_init, etc. permanecem aqui)

# ---------------------------- Core CLI ------------------------------------- #

def cmd_init(args): "..." # Omitido
def _specify_seed(root: Path, description: str | None): "..." # Omitido
def _specify_character(root: Path): "..." # Omitido
def _specify_setting(root: Path): "..." # Omitido
def cmd_specify(args): "..." # Omitido
def cmd_status(args): "..." # Omitido
def cmd_plan(args): "..." # Omitido
def cmd_tasks(args): "..." # Omitido
def cmd_draft(args): "..." # Omitido
def cmd_review(args): "..." # Omitido

def cmd_generate(args):
    """Dispatcher para os subcomandos de 'generate'."""
    root = get_project_root(args.project)
    if not root: return

    if args.generate_type == "scene":
        _generate_scene(root, args.character, args.setting)
    else:
        print(f"✖ Tipo de geração desconhecido: {args.generate_type}")

# ... (As implementações completas de cmd_init, etc. estão aqui no código real)

# ---------------------------- Main ----------------------------------------- #

def build_parser():
    p = argparse.ArgumentParser(prog="specbook", description="SpecBook — SDD para livros")
    sub = p.add_subparsers(dest="cmd", required=True)

    # ... (Parsers para init, specify, status, plan, tasks, draft, review)

    # Parser para 'generate'
    sp_gen = sub.add_parser("generate", help="Gera fragmentos de escrita a partir de specs")
    sp_gen.add_argument("--project", required=True, help="Pasta do projeto")
    gen_sub = sp_gen.add_subparsers(dest="generate_type", required=True)

    gen_scene = gen_sub.add_parser("scene", help="Gera um esqueleto de cena")
    gen_scene.add_argument("-c", "--character", help="Nome do personagem (não interativo)")
    gen_scene.add_argument("-s", "--setting", help="Nome do cenário (não interativo)")
    gen_scene.set_defaults(func=cmd_generate)

    return p

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()