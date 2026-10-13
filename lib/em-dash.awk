# VOICE-21: an em dash, an en dash or a horizontal bar outside code.
function judge(file, line, text,   t) {
  t = text
  gsub(/`[^`]*`/, "", t)
  if (t ~ /[—–―]/) report(file, line, "VOICE-21 em dash", text)
}
