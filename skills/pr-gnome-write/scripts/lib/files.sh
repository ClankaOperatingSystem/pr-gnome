# Run one check's awk over the Org and Markdown files beneath the working
# directory: everything but archives, attics, methodologies, hidden and
# underscore directories, node_modules, and any directory that is a git
# repository of its own, since a repository mounted in a tree is a
# product and not the tree's canon. D is the skill's scripts/ directory.
# Files given after the awk file are read instead, - as standard input.
# Findings are sorted; exit 0 clean, 1 with findings.
run_check() {
  D=$1; awkfile=$2; shift 2
  if [ $# -gt 0 ]; then
    found=$(awk -f "$D/lib/prose.awk" -f "$D/lib/$awkfile" "$@")
    status=$?
    [ -z "$found" ] || printf '%s\n' "$found" | LC_ALL=C sort
    exit $status
  fi
  found=$(find . \( -name archives -o -name attic -o -name methodologies \
                    -o -name node_modules -o -name '_*' -o -name '.?*' \
                    -o \( -path './*' -type d -exec test -e '{}/.git' \; \) \) -prune -o \
               \( -name '*.org' -o -name '*.md' \) -type f \
               -exec awk -f "$D/lib/prose.awk" -f "$D/lib/$awkfile" {} +)
  status=$?
  [ -z "$found" ] || printf '%s\n' "$found" | LC_ALL=C sort
  exit $status
}
