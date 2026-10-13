title: File four things the trace work turned up
expect: VOICE-19
grade: warn
why: "found while verifying the trace work" names the occasion the author was busy with.
---
All found while verifying the trace work on the host; none of them is a
regression from it.

**The sweep starves the session probe.** The daily sweep queues one run
per repository partition, 326 of them, and at three concurrent runs that
saturates the queue for half an hour every morning.

**The cron comment is stale.** It describes a weekly Sunday schedule and
explains at length why Sunday rather than Monday. The schedule is daily.
