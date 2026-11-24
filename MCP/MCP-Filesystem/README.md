# MCP-Filesystem

My first project using the Filesystem MCP server with Claude.

## What this project does

- Lets Claude create, read, and edit files inside this folder through the Filesystem MCP server.
- Only this folder (`C:\LearningZone\MCP-Filesystem`) is exposed to Claude. Nothing outside it can be touched.

## Files

| File | Description |
|------|-------------|
| `hello.txt` | First test file, created by Claude through MCP |
| `README.md` | Project notes (this file) |

## Filesystem MCP tools used

- `write_file`: create a file or overwrite an existing one
- `read_text_file`: read a file's contents
- `list_allowed_directories`: show which folders Claude can access

## Using this folder with Git

### First-time setup

```bash
cd C:\LearningZone\MCP-Filesystem
git init
git add .
git commit -m "Initial commit: hello.txt and README"
```

### Connect to GitHub

1. Create an empty repository on GitHub (no README, since one already exists here).
2. Run:

```bash
git remote add origin https://github.com/<your-username>/MCP-Filesystem.git
git branch -M main
git push -u origin main
```

### Everyday workflow

```bash
git status                      # see what changed
git add .                       # stage all changes
git commit -m "Describe change" # save a snapshot
git push                        # upload to GitHub
```

## Notes

- `write_file` overwrites without warning, so commit before asking Claude to change important files.
- Use `git diff` to review what Claude changed before committing.
- Don't store passwords, API keys, or personal data in this folder if you push it to a public repo.
