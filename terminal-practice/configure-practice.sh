#!/bin/sh
set -eu
cd /Users/seanmacbook/Projects/agent-workflow-research/terminal-practice
cmux rename-tab --workspace workspace:2 --tab surface:2 'Agent'
cmux rename-tab --workspace workspace:2 --tab surface:3 'Checks'
cmux reload-config
cmux shortcuts > /tmp/cmux-terminal-practice-shortcuts.txt
cmux tree > /tmp/cmux-terminal-practice-tree.txt
