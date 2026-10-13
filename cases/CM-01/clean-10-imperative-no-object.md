title: Fail closed on a missing secret
expect: 
why: an imperative followed by a when-clause, which does not change the mood.
commit: Fail closed when the webhook secret is unset
---
The ingress refuses to start without a secret rather than accepting deliveries it cannot verify.
