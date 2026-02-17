#!/usr/bin/env bash
# tools/count_lines.sh
# Non-destructive inventory script: produces CSV with path, extension, line count and bytes.
# Excludes common heavy/artifact directories. Run from repo root: ./tools/count_lines.sh > repo_line_counts.csv
set -euo pipefail
IFS=$'\n\t'

echo "path,ext,lines,bytes"

# Exclude patterns
EXCLUDES=("./.git" "./frontend/node_modules" "./frontend/.next" "./.next" "./venv" "./env" "./.venv" "./__pycache__" "./test-results")

# Build prune expression for find
PRUNE_EXPR=()
for e in "${EXCLUDES[@]}"; do
  PRUNE_EXPR+=( -path "$e" -o )
done
# remove last -o
unset 'PRUNE_EXPR[${#PRUNE_EXPR[@]}-1]'

# Use find to list files while pruning
find_cmd=(find .)
find_cmd+=(\( "${PRUNE_EXPR[@]}" \) -prune -false -o -type f -print0)

# Execute find and process
"${find_cmd[@]}" \
  | xargs -0 -n1 bash -c 'f="$0"; ext="${f##*.}"; lines=$(wc -l < "$f" 2>/dev/null || echo 0); bytes=$(wc -c < "$f" 2>/dev/null || echo 0); # escape double quotes in path
    # Normalize path to remove leading ./
    p="${f#./}"; printf "%s,%s,%s,%s\n" "$p" "$ext" "$lines" "$bytes'