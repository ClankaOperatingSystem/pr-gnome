title: Pace the calibration runs
expect: 
why: a measurement and the decision it led to.
commit: Pace the calibration runs
file: src/bugflow/app/calibration.py +18 -3
---
Three back-to-back runs, 63 requests in about four minutes, exceeded the model's per-minute limit. Runs now wait five seconds between cases and retry after fifteen and sixty.
