# GIT-5: a description of more than limit words outside code blocks.
FNR == 1 { if (seen) judge(); file = FILENAME; words = 0; skip = 0; seen = 1 }
/^[ \t]*```/ { skip = !skip; next }
!skip { words += NF }
function judge() {
  if (words > limit) {
    print file ": GIT-5 description runs to " words " words, over " limit
    any = 1
  }
}
END { if (seen) judge(); exit any ? 1 : 0 }
