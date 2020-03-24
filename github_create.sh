#!/bin/bash
set -e

REPO_NAME=$(basename ${PWD})
PRIVATE=true
JSON_STRING=$( jq -n \
                  --arg rn "$REPO_NAME" \
                  --arg p "$PRIVATE" \
                  --arg tl "$TARGET_LOCATION" \
                  '{name: $rn, private: $p,}' )
curl -H "Authorization: token 7c40f62703d3c0772438fcf5b3c2b055f5a7987d" \
--data "${JSON_STRING}" \
https://api.github.com/user/repos

git init
git commit -m "first commit"
git remote add origin git@github.com:enrilohm/${REPO_NAME}.git
git push -u origin master
