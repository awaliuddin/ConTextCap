# ConTextCap Examples

This directory contains example configurations, scripts, and use cases for ConTextCap.

## Contents

### Configuration Examples

- **`basic-config.yml`**: Simple configuration for getting started
- **`advanced-config.yml`**: Advanced configuration with all options
- **`python-project.yml`**: Optimized for Python projects
- **`web-project.yml`**: Optimized for web development projects
- **`documentation-only.yml`**: Extract only documentation files

### Script Examples

- **`batch-process.sh`**: Batch process multiple projects
- **`git-history.sh`**: Generate PDFs for different git commits
- **`ci-integration.sh`**: Example CI/CD integration script
- **`scheduled-backup.sh`**: Automated backup script

### Use Case Examples

1. **Code Review Package**
2. **LLM Context Generation**
3. **Project Documentation Snapshot**
4. **Legacy Code Archive**
5. **Onboarding Documentation**

## Quick Start

### Example 1: Generate PDF for Current Project

```bash
python ConTextCap.py --input . --output ./project-docs.pdf
```

### Example 2: Use Custom Configuration

```bash
python ConTextCap.py --config ./examples/python-project.yml --input ./my-project
```

### Example 3: Batch Process Multiple Projects

```bash
./examples/batch-process.sh projects.txt
```

## Use Cases

### 1. Code Review Package

Generate a comprehensive PDF for code reviews:

```bash
# Generate PDF from feature branch
git checkout feature/new-feature
python ConTextCap.py --input ./src --output ./reviews/feature-review.pdf

# Share the PDF with reviewers
```

**Benefits:**
- Complete context in one document
- Easy to annotate and comment
- Works offline
- Preserves at a point in time

### 2. LLM Context Generation

Create context for AI assistants:

```bash
# Generate PDF for LLM
python ConTextCap.py \
  --input ./src \
  --exclude "tests,*.log" \
  --output ./context-for-llm.pdf

# Upload to ChatGPT, Claude, etc.
```

**Benefits:**
- Single file upload
- Complete codebase context
- Perfect for AI analysis
- Works with all major LLMs

### 3. Project Documentation Snapshot

Create historical snapshots:

```bash
# Snapshot before major refactoring
python ConTextCap.py \
  --input . \
  --output ./snapshots/v1.0-before-refactor.pdf

# After refactoring
python ConTextCap.py \
  --input . \
  --output ./snapshots/v1.0-after-refactor.pdf
```

**Benefits:**
- Historical record
- Easy comparison
- Version documentation
- Archive compliance

### 4. Legacy Code Archive

Archive old projects:

```bash
# Generate comprehensive archive
python ConTextCap.py \
  --input ./legacy-project \
  --include-hidden \
  --output ./archives/legacy-project-$(date +%Y%m%d).pdf
```

**Benefits:**
- Complete preservation
- No dependencies needed later
- Easy to search (PDF)
- Long-term storage

### 5. Onboarding Documentation

Help new developers:

```bash
# Create onboarding package
python ConTextCap.py \
  --input ./src \
  --config ./examples/documentation-only.yml \
  --output ./onboarding/codebase-overview.pdf
```

**Benefits:**
- Quick overview
- Self-contained
- Easy to share
- Reduces onboarding time

## Advanced Examples

### Automated Git History Documentation

```bash
#!/bin/bash
# Generate PDFs for each major version

tags=$(git tag -l "v*")
for tag in $tags; do
  git checkout $tag
  python ConTextCap.py \
    --input ./src \
    --output ./history/${tag}.pdf
done
```

### CI/CD Integration

```yaml
# .github/workflows/documentation.yml
name: Generate Documentation

on:
  release:
    types: [created]

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate PDF
        run: |
          pip install contextcap
          contextcap --input ./src --output ./release-docs.pdf
      - name: Upload to Release
        uses: actions/upload-release-asset@v1
        with:
          asset_path: ./release-docs.pdf
          asset_name: project-documentation.pdf
```

### Scheduled Backups

```bash
#!/bin/bash
# Cron job: 0 0 * * 0 (weekly on Sunday)

PROJECTS=(
  "/home/user/project1"
  "/home/user/project2"
  "/home/user/project3"
)

BACKUP_DIR="/backup/code-snapshots"
DATE=$(date +%Y%m%d)

for project in "${PROJECTS[@]}"; do
  project_name=$(basename "$project")
  python ConTextCap.py \
    --input "$project" \
    --output "$BACKUP_DIR/${project_name}_${DATE}.pdf"
done
```

## Best Practices

1. **Use Configuration Files**: Create project-specific configs
2. **Version Control Configs**: Commit config files to git
3. **Automate Regular Snapshots**: Use cron or CI/CD
4. **Organize Output**: Use dated directories
5. **Document Your Workflow**: Create project-specific guides
6. **Test Configurations**: Verify before production use
7. **Archive Strategically**: Don't over-archive

## Tips & Tricks

### Faster Processing

```yaml
# Exclude unnecessary directories
filtering:
  exclude_dirs:
    - tests
    - docs
    - examples
```

### Better LLM Context

```yaml
# Include only source code
processing:
  text_extensions:
    - .py
    - .js
    - .ts
```

### Comprehensive Archives

```yaml
# Include everything
filtering:
  include_hidden: true
  exclude_dirs: [".git"]  # Only exclude VCS
```

## Troubleshooting

See the [main documentation](../docs/USER_GUIDE.md) for troubleshooting tips.

## Contributing Examples

Have a great use case or configuration? Please contribute!

1. Create your example in this directory
2. Document it clearly
3. Submit a pull request

---

For more information, visit the [ConTextCap Documentation](../README.md).
