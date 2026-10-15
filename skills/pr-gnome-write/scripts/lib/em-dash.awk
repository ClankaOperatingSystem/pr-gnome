# VOICE-21: an em dash, an en dash or a horizontal bar outside code.
# Alternation, not a bracket expression, so that an awk which reads bytes,
# as in the C locale, matches the whole character and not every character
# that shares a byte with it, such as an arrow or a minus sign.
function judge(file, line, text,   t) {
  t = text
  gsub(/`[^`]*`/, "", t)
  if (t ~ /(—|–|―)/) report(file, line, "VOICE-21 em dash", text)
}
