#!/usr/bin/env bash
#
# serialized-tech-series-architect 一鍵安裝腳本
#
# 用法：
#   curl -fsSL https://raw.githubusercontent.com/flamerecca/serialized-tech-series-architect/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/flamerecca/serialized-tech-series-architect/main/install.sh | bash -s -- --project

set -euo pipefail

REPO_URL="https://github.com/flamerecca/serialized-tech-series-architect.git"
SCOPE="global"

usage() {
  cat <<'USAGE'
用法：install.sh [--project] [-h|--help]

  --project   安裝到目前目錄下的 .claude/，預設安裝到使用者家目錄的 ~/.claude/
  -h, --help  顯示這份說明
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project)
      SCOPE="project"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "未知參數：$1" >&2
      usage
      exit 1
      ;;
  esac
done

if ! command -v git >/dev/null 2>&1; then
  echo "找不到 git，請先安裝 git，或改用 README 裡方式一的手動複製步驟。" >&2
  exit 1
fi

if [[ "$SCOPE" == "project" ]]; then
  TARGET_DIR="$(pwd)/.claude"
else
  TARGET_DIR="$HOME/.claude"
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

echo "下載 serialized-tech-series-architect..."
git clone --depth 1 --quiet "$REPO_URL" "$TMP_DIR/repo"

mkdir -p "$TARGET_DIR/skills" "$TARGET_DIR/agents"
cp -R "$TMP_DIR/repo/skills/." "$TARGET_DIR/skills/"
cp -R "$TMP_DIR/repo/agents/." "$TARGET_DIR/agents/"

echo "安裝完成，已複製到 $TARGET_DIR"
echo "請重新啟動 Claude Code，即可套用 serialized-tech-series-architect Skill，以及 planning-agent、writing-agent、visual-agent、proofreading-agent 四個 Agent。"
