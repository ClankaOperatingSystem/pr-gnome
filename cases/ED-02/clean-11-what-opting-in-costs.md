title: Let the local stack take stock
expect:
why: states what opting in costs, which the diff cannot show.
commit: Let the local stack take stock
|
| The worker schedules a stocktake of each repository in
| WATCHED_REPOSITORIES and the measurement site shows them with their
| ENFORCEMENT, but the local compose passed neither to measure and
| WATCHED_REPOSITORIES to nothing, so a laptop could not take stock at
| all. REVIEW_AGENTS and FORGE_CLONE_URL could not be set locally either.
| All four now pass through, empty by default, so nothing changes until
| one is set; FORGE_CLONE_URL keeps the code's github.com default, which
| an empty value would otherwise override.
|
| The configuration table names the worker and measure as readers of
| WATCHED_REPOSITORIES and measure as a reader of ENFORCEMENT.
|
| Closes C1.11 and C1.12 in cleanup.org.
file: .env.example +13 -0
file: cleanup.org +5 -2
file: docker-compose.yml +9 -0
file: index.org +24 -2
---
Setting `WATCHED_REPOSITORIES` with a review runner configured makes the laptop dispatch a real review every Sunday night it is running, at what a review costs; that is the opt-in the owner chose over keeping the variables deployment-only.
