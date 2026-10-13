title: Retry a judgement the proxy rate limited
expect: VOICE-2 | VOICE-3
grade: warn
why: one fact padded to ten times its length; the fact survives, so it is a warning.
commit: Retry a judgement the proxy rate limited
file: src/bugflow/usecases/calibrate_judge.py +18 -2
---
It is worth noting at this juncture that, in the event that the proxy in question should happen to respond with a status code of 429, which is to say the status code that is conventionally understood to indicate that a rate limit of some description has been encountered, the behaviour that will now be observed is that the request will be attempted for a second time, following a delay, the duration of which is to be taken from the value of the Retry-After header where such a header has in fact been provided by the proxy, and which otherwise falls back to a delay of fifteen seconds in the first instance and sixty seconds thereafter.
