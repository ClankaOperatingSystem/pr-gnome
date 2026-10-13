# The Org and Markdown files a canon check reads, one per line, relative
# to the directory it runs in: everything but archives, attics,
# methodologies, hidden and underscore directories and node_modules.
canon_files() {
  find . \( -name archives -o -name attic -o -name methodologies \
            -o -name node_modules -o -name '_*' -o -name '.?*' \) -prune -o \
       \( -name '*.org' -o -name '*.md' \) -type f -print \
    | sed 's|^\./||' | LC_ALL=C sort
}
# Run one check's awk over the files. M is the methodology's directory.
run_check() {
  M=$1; awkfile=$2
  files=$(canon_files)
  [ -n "$files" ] || exit 0
  printf '%s\n' "$files" | xargs awk -f "$M/lib/prose.awk" -f "$M/lib/$awkfile"
}
