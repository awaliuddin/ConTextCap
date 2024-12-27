# Git Workflow Guide for ConTextCap 🌿

## Daily Code Push Process

### The Safe Way (AxW's Method)
```bash
# 1. Stage your changes
git add README.md .gitignore  # Stage specific files
# OR
git add .                     # Stage all changes

# 2. Commit your changes
git commit -m "docs: update project description"
# Use prefixes like: feat, fix, docs, style, refactor, test, chore

# 3. Pull safely (won't overwrite uncommitted changes)
git pull origin main
# This is safe because your changes are already committed

# 4. Push your changes
git push origin main
```

### Important Notes
- Git WILL NOT overwrite your uncommitted local changes when pulling
- Always commit before pulling to keep your changes safe
- When in doubt, commit first!

### If Something Goes Wrong
```bash
# Undo last commit (keep changes staged)
git reset --soft HEAD^

# Undo staged changes
git reset HEAD <file>

# Discard all local changes (careful!)
git reset --hard HEAD
```

### Branch Management
```bash
# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Delete branch
git branch -d feature-name
```

## Commit Message Guidelines

### Format
```
type: subject

[optional body]
[optional footer]
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semi colons, etc
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples
```bash
git commit -m "docs: update project description and fix gitignore syntax"
git commit -m "feat: add PDF export functionality"
git commit -m "fix: resolve file path issues on Windows"
```

## Quick Reference
1. Always commit before pulling
2. Use descriptive commit messages
3. Pull before pushing
4. Create branches for major features

---

Created by AxW for ConTextCap team 🚀
