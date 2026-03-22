#!/bin/bash

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RESET='\033[0m'

echo -ne "${BLUE}📝 problem? ${RESET}"
read problem

dir="_result/${problem}"

if [ -d "$dir" ]; then
  i=2
  while [ -d "${dir}_${i}" ]; do
    i=$((i + 1))
  done
  echo -e "${YELLOW}⚠️  Already exists: ${problem} → Saving as ${problem}_${i}${RESET}"
  dir="${dir}_${i}"
fi

echo -e "${BLUE}📁 Saving to ${dir}/main.py${RESET}"
mkdir -p "$dir"
cp main.py "$dir/main.py"

echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
git add "$dir/main.py"
git commit -m "${dir##*/}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"

echo -e "${GREEN}🔄 Resetting main.py from template${RESET}"
cp _template/main.py ./main.py

echo ""
echo -e "${GREEN}✅ Done: ${dir##*/}${RESET}"