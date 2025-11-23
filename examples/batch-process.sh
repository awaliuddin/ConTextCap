#!/bin/bash
# ConTextCap Batch Processing Script
#
# Usage: ./batch-process.sh projects.txt
#
# projects.txt format (one project per line):
#   /path/to/project1
#   /path/to/project2
#   /path/to/project3

set -e

# Configuration
OUTPUT_DIR="${OUTPUT_DIR:-./batch-output}"
CONFIG_FILE="${CONFIG_FILE:-}"
DATE=$(date +%Y%m%d_%H%M%S)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check arguments
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <projects-file>"
    echo ""
    echo "Example:"
    echo "  $0 projects.txt"
    exit 1
fi

PROJECTS_FILE="$1"

# Verify projects file exists
if [ ! -f "$PROJECTS_FILE" ]; then
    echo -e "${RED}Error: Projects file '$PROJECTS_FILE' not found${NC}"
    exit 1
fi

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Log file
LOG_FILE="$OUTPUT_DIR/batch-process-${DATE}.log"
echo "Starting batch process at $(date)" > "$LOG_FILE"

# Counters
TOTAL=0
SUCCESS=0
FAILED=0

# Process each project
while IFS= read -r project_path || [ -n "$project_path" ]; do
    # Skip empty lines and comments
    [[ -z "$project_path" || "$project_path" =~ ^# ]] && continue

    TOTAL=$((TOTAL + 1))
    project_name=$(basename "$project_path")
    output_file="$OUTPUT_DIR/${project_name}_${DATE}.pdf"

    echo -e "${YELLOW}Processing [$TOTAL]: $project_name${NC}"
    echo "Processing: $project_path" >> "$LOG_FILE"

    # Build command
    cmd="python ConTextCap.py --input \"$project_path\" --output \"$output_file\""

    if [ -n "$CONFIG_FILE" ]; then
        cmd="$cmd --config \"$CONFIG_FILE\""
    fi

    # Execute ConTextCap
    if eval $cmd >> "$LOG_FILE" 2>&1; then
        echo -e "${GREEN}✓ Success: $project_name${NC}"
        echo "Success: $output_file" >> "$LOG_FILE"
        SUCCESS=$((SUCCESS + 1))
    else
        echo -e "${RED}✗ Failed: $project_name${NC}"
        echo "Failed: $project_path" >> "$LOG_FILE"
        FAILED=$((FAILED + 1))
    fi

    echo "" >> "$LOG_FILE"
done < "$PROJECTS_FILE"

# Summary
echo ""
echo "================================================"
echo "Batch Process Summary"
echo "================================================"
echo "Total Projects: $TOTAL"
echo -e "Successful: ${GREEN}$SUCCESS${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo "Output Directory: $OUTPUT_DIR"
echo "Log File: $LOG_FILE"
echo "================================================"

# Write summary to log
{
    echo ""
    echo "Summary:"
    echo "  Total: $TOTAL"
    echo "  Success: $SUCCESS"
    echo "  Failed: $FAILED"
    echo ""
    echo "Completed at $(date)"
} >> "$LOG_FILE"

# Exit with error if any failed
[ $FAILED -eq 0 ] && exit 0 || exit 1
