#!/bin/bash

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RESET='\033[0m'

echo -ne "${BLUE}📝 problem number? ${RESET}"
read num

problem=$(printf "%04d" "$num")
dir="_result/${problem}"
dest="${dir}/main.py"

if [ -f "$dest" ]; then
  i=2
  while [ -f "${dir}/main_${i}.py" ]; do
    i=$((i + 1))
  done
  echo -e "${YELLOW}⚠️  Already exists: ${problem}/main.py → Saving as main_${i}.py${RESET}"
  dest="${dir}/main_${i}.py"
fi

echo -e "${BLUE}📁 Saving to ${dest}${RESET}"
mkdir -p "$dir"
cp main.py "$dest"

echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
git add "$dest"
git commit -m "${problem} (${dest##*/})"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"

echo -e "${GREEN}🔄 Resetting main.py from template${RESET}"
cp _template/main.py ./main.py

echo ""
echo -e "${GREEN}✅ Done: ${dir##*/}/${dest##*/}${RESET}"