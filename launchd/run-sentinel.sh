#!/bin/bash
# Wrapper invoked by launchd. Captures full env + output so we never fly blind.
# Calls Python directly via the project venv to avoid depending on `uv` at the
# launchd boundary (uv-under-launchd has been a source of silent exit-78s).

set -u

PROJECT_ROOT="/Users/sn0rks/Code/github.com/allienna/veilleur"
LOG_DIR="$PROJECT_ROOT/data/logs"
DATE="$(date +%Y-%m-%d)"
LOG="$LOG_DIR/launchd-$DATE.log"

mkdir -p "$LOG_DIR"

{
    echo "===================================================================="
    echo "[$(date -Iseconds)] launchd wrapper starting"
    echo "  args: $*"
    echo "  cwd: $(pwd)"
    echo "  user: $(id)"
    echo "  PATH: $PATH"
    echo "  HOME: ${HOME:-unset}"
    echo "--- env (filtered) ---"
    env | grep -vE "^(LS_COLORS|TERMCAP|__CFBundle)" | sort
    echo "--- /opt/homebrew/bin/uv ---"
    ls -la /opt/homebrew/bin/uv 2>&1 || true
    echo "--- venv python ---"
    ls -la "$PROJECT_ROOT/.venv/bin/python3" 2>&1 || true
    echo "===================================================================="
} >> "$LOG" 2>&1

cd "$PROJECT_ROOT" || { echo "[$(date -Iseconds)] cd failed" >> "$LOG"; exit 78; }

"$PROJECT_ROOT/.venv/bin/python3" scripts/sentinel.py "$@" >> "$LOG" 2>&1
EXIT=$?

echo "[$(date -Iseconds)] sentinel exited with code $EXIT" >> "$LOG"
exit $EXIT
