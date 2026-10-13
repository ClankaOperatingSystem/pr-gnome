title: Sign the poller's deliveries
expect: VOICE-2 | VOICE-3
grade: warn
why: a "Summary" heading that repeats the title, and a conclusion that repeats the detail.
commit: Sign the poller's deliveries
file: src/bugflow/adapters/webhook_sink.py +14 -2
---
## Summary

Sign the poller's deliveries.

## Detail

The poller signs each delivery with the webhook secret, so the ingress can verify it.

## Conclusion

In summary, the poller's deliveries are now signed, as described above.
