title: Record the posting identity and the judge's role
expect:
why: decisions, ticked tasks and what publishing did are facts, and each id follows the name of the thing it cites.
---
Records the owner's decisions of 2026-09-11.

**Posting identity.**
- **Now.** The reviewbot posts as the owner. The decision record "Forge authentication by personal access token" (ADR-009) records it.
- **Token.** Dogfooding uses the owner's `gh` CLI token. Its scopes, `repo` and `workflow` among them, are broader than ADR-009 asks for, until a fine-grained token with only the listed access replaces it.
- **Later.** Several posting identities, each speaking for one aspect of quality assessed independently. A new open question asks how aspects map to policies, whether each identity holds its own token, and how their comments on one pull request relate.
- **Dogfood.** The identity subtask is ticked.

**The judge's role (ADR-013, "The reviewbot judges; tools check").**
- **Decision.** Judged policies are as important as deterministic ones, and are not the same kind of thing. Linter configuration, CI, git hooks and other tools enforce what can be checked mechanically, and always will. The reviewbot does not re-implement them: it makes the qualitative assessments they cannot, so judged policies proceed.
- **The earlier record stands.** The decision record "The LLM judge is co-equal but fully journaled" (ADR-005) is unchanged. Judged policies are as important as deterministic ones; ADR-013 adds that they are a different kind.
- **Spike closed.** The judge calibration decision task is ticked, and the second milestone, judged policies (M2), is entered.
- **New task in that milestone.** Move each deterministic policy to the tool that should enforce it, a git hook, a linter or a CI job, and out of the reviewbot.
- **Snapshot fidelity.** Decided per policy.

`make check` passes.

**Dogfood (second commit).**
- **First publish.** With publishing on in the local `.env` and the poller watching this repository, this pull request received a summary comment posted as the owner. It had one editorial voice finding, for narrating in the description, and the `doctrine:warn` label, which GitHub created when it was first added.
- **Update in place.** A push and an edit removing that sentence reached the ingress as one delivery. The same comment (`5635331267`) was edited in place, listing the finding as resolved, and the label became `doctrine:pass`. The journal recorded `finding.resolved` and both `action.taken` entries against the same comment id.
- **Result.** That meets the exit criterion of the first milestone (M1), and the dogfood task is ticked.

`make check` passes.


