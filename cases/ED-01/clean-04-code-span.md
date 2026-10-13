title: Remove the unused retry option
expect: 
why: "seamless" sits inside a code span, which is not judged.
---
The worker read no `seamless_retry` setting, but the compose file still passed
it. It is removed from the compose file and from `.env.example`.

A search for `seamless_retry` across `src/` and `tests/` finds nothing.
