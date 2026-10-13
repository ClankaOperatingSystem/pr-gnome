title: Fix the ingress port in the example environment
expect: 
why: one sentence that states the problem.
---
`.env.example` set `INGRESS_PORT=8080`; the compose file and the ingress image
listen on 8000.
