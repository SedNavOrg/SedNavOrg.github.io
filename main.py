import re
import os

def define_env(env):
    @env.macro
    def render_glossary(filepath="includes/glossaire.md"):
        if not os.path.exists(filepath):
            return f"**Error**: Glossary file not found at {filepath}"

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find: *[Term]: Definition
        # Group 1: Term, Group 2: Definition
        pattern = r"\*\[(.*?)\]:\s*(.*)"
        matches = re.findall(pattern, content)

        if not matches:
            return "_No definitions found in glossary._"

        # Format the output as a Markdown table
        output = "| Terme | Définition |\n| :--- | :--- |\n"
        for term, definition in matches:
            output += f"| **{term}** | {definition} |\n"

        return output