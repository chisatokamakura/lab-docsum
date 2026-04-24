# AGENTS.md

This repository contains an LLM-based agent that can inspect files, run tools, and modify the repository.

## Tool Usage Rules
- Always use relative paths.
- Never use absolute paths or paths containing `..`.
- Prefer using tools like `ls`, `cat`, `grep`, `write_file`, `write_files`, and `rm`.

## File Modification
- When creating or modifying files, commit changes with a message starting with `[chat]`.

## Testing
- Use the `doctests` tool to validate Python files when appropriate.

## Notes
- The agent should avoid unnecessary verbosity and return concise outputs.