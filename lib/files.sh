# Run one check's awk over the Org and Markdown files beneath the working
# directory: everything but archives, attics, methodologies, hidden and
# underscore directories and node_modules. M is the methodology's
# directory. Findings are sorted; exit 0 clean, 1 with findings.
run_check() {
  M=$1; awkfile=$2
  found=$(find . \( -name archives -o -name attic -o -name methodologies \
                    -o -name node_modules -o -name '_*' -o -name '.?*' \) -prune -o \
               \( -name '*.org' -o -name '*.md' \) -type f \
               -exec awk -f "$M/lib/prose.awk" -f "$M/lib/$awkfile" {} +)
  status=$?
  [ -z "$found" ] || printf '%s\n' "$found" | LC_ALL=C sort
  exit $status
}
