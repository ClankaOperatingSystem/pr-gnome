# The findings of GIT-3 for one commit message, read on standard input,
# each printed as NAME: GIT-3 MESSAGE; exit 1 when there are any. Run in
# the C locale: a length counts each byte but a UTF-8 continuation byte.

function chars(s) {
  gsub(/[\200-\277]/, "", s)
  return length(s)
}

function find(message) {
  printf "%s: GIT-3 %s\n", name, message
  found = 1
}

BEGIN {
  split("feat fix chore docs doc refactor test tests style perf build ci revert wip", list, " ")
  for (i in list) kinds[list[i]] = 1
  # Imperative verbs whose ending is that of another form.
  split("bias alias canvas focus " \
        "bleed breed embed exceed feed heed need proceed seed shed shred " \
        "speed succeed weed " \
        "bring cling fling ping ring sing sling spring sting string swing " \
        "wring", list, " ")
  for (i in list) imperative[list[i]] = 1
}

{ line[NR] = $0 }

END {
  # Trailing blank lines are not part of the message.
  n = NR
  while (n > 0 && line[n] ~ /^[ \t]*$/) n--
  summary = line[1]
  if (summary ~ /^[ \t]*$/) {
    find("the summary is empty")
    exit 1
  }
  if (chars(summary) > 72)
    find("the summary is " chars(summary) " characters, over 72")
  if (match(summary, /^[a-z]+(\([^)]*\))?!?: /)) {
    kind = summary
    sub(/[(!:].*/, "", kind)
    if (kind in kinds)
      find("the summary has the prefix " kind ":, which names a kind of change")
  }
  # The verb is the first word, or the first after a subsystem prefix.
  rest = summary
  sub(/^[a-z0-9_.\/-]+: /, "", rest)
  verb = rest
  sub(/[^A-Za-z].*/, "", verb)
  lower = tolower(verb)
  if (lower ~ /(ed|ing|[^s]s)$/ && !(lower in imperative))
    find("the summary may not be imperative: " verb)
  if (n >= 2 && line[2] !~ /^$/)
    find("the second line is not blank")
  for (i = 2; i <= n; i++) {
    body = line[i]
    sub(/^[ \t]+/, "", body)
    if (chars(line[i]) > 72 && body ~ / /)
      find("line " i " is " chars(line[i]) " characters, over 72")
  }
  exit found
}
