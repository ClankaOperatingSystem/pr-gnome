title: Wait as long as the proxy asks
expect: VOICE-3
grade: warn
why: a fact stated once, then padded without restating it.
commit: Wait as long as the proxy asks
file: src/bugflow/adapters/litellm_judge.py +16 -4
---
The retry delay is taken from the Retry-After header when the proxy sends
one. In the situation where the proxy has not seen fit to furnish a header
of that particular description, the delay that will subsequently be applied
is a delay of fifteen seconds on the first occasion and a delay of sixty
seconds on each and every occasion subsequent to that one.
