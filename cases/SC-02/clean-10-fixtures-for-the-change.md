title: Grade every judged policy
expect: 
why: a rule with the fixtures labelled for it, which are derived.
commit: Grade every judged policy
file: index.org +68 -0
file: src/bugflow/adapters/calibration_cases.py +47 -20
file: src/bugflow/adapters/litellm_judge.py +114 -7
file: src/bugflow/app/calibration.py +1 -1
file: src/bugflow/domain/calibration.py +5 -3
file: src/bugflow/usecases/calibrate_judge.py +7 -10
file: tests/fixtures/commit_mood/seeded-01-past-tense.md +1 -0
file: tests/fixtures/commit_mood/seeded-02-third-person.md +1 -0
file: tests/fixtures/commit_mood/seeded-03-gerund.md +1 -0
file: tests/fixtures/commit_mood/seeded-04-noun-phrase.md +1 -0
file: tests/fixtures/commit_mood/seeded-05-one-among-good.md +1 -0
file: tests/fixtures/commit_mood/seeded-06-past-participle.md +1 -0
file: tests/fixtures/commit_mood/seeded-07-should-phrasing.md +1 -0
file: tests/fixtures/commit_mood/seeded-08-passive.md +1 -0
file: tests/fixtures/commit_mood/seeded-09-first-person.md +1 -0
file: tests/fixtures/commit_mood/seeded-10-question.md +1 -0
file: tests/fixtures/commit_mood/seeded-11-wip-noun.md +1 -0
file: tests/fixtures/commit_mood/seeded-12-infinitive.md +1 -0
file: tests/fixtures/commit_mood/seeded-13-continuous-with-good.md +1 -0
file: tests/fixtures/editorial_voice/seeded-mixed.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-06-marketing.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-07-self-congratulation.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-09-filler-opener.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-10-hedging.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-11-rhetorical-question.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-12-emphasis.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-13-fake-precision.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-14-anthropomorphism.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-15-unresolved-reference.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-16-padding.md +1 -0
file: tests/fixtures/editorial_voice/seeded-voice-19-narrating.md +1 -0
file: tests/fixtures/honesty/seeded-01-claims-a-test-that-is-not-there.md +1 -0
file: tests/fixtures/honesty/seeded-02-claims-behaviour-that-is-not-there.md +1 -0
file: tests/fixtures/honesty/seeded-03-no-behaviour-change-that-changes-behaviour.md +1 -0
file: tests/fixtures/honesty/seeded-04-omits-a-migration.md +1 -0
file: tests/fixtures/honesty/seeded-05-omits-a-removed-command.md +1 -0
file: tests/fixtures/honesty/seeded-06-omits-a-new-dependency.md +1 -0
file: tests/fixtures/honesty/seeded-07-omits-a-public-rename.md +21 -0
file: tests/fixtures/honesty/seeded-08-omits-a-changed-default.md +14 -0
file: tests/fixtures/judge/rendered_request.json +10 -2
file: tests/fixtures/model_tics/seeded-01-triple.md +1 -0
file: tests/fixtures/model_tics/seeded-02-em-dash.md +1 -0
file: tests/fixtures/model_tics/seeded-03-mind-reading.md +1 -0
file: tests/fixtures/model_tics/seeded-04-aphorism.md +1 -0
file: tests/fixtures/model_tics/seeded-05-slop.md +1 -0
file: tests/fixtures/model_tics/seeded-06-because-we-can.md +1 -0
file: tests/fixtures/model_tics/seeded-07-two-tics.md +1 -0
file: tests/fixtures/model_tics/seeded-08-coy-teaser.md +1 -0
file: tests/fixtures/model_tics/seeded-09-teaser-and-dash.md +1 -0
file: tests/fixtures/model_tics/seeded-10-manufactured-antithesis.md +1 -0
file: tests/fixtures/model_tics/seeded-11-invented-objection.md +1 -0
file: tests/fixtures/model_tics/seeded-12-triple-only.md +1 -0
file: tests/fixtures/model_tics/seeded-13-fake-maxim.md +1 -0
file: tests/fixtures/model_tics/seeded-14-signoff.md +1 -0
file: tests/fixtures/model_tics/seeded-15-empty-negation.md +1 -0
file: tests/fixtures/scope/seeded-01-feature-and-unrelated-rename.md +1 -0
file: tests/fixtures/scope/seeded-02-fix-and-unrelated-refactor.md +1 -0
file: tests/fixtures/scope/seeded-03-also-in-description.md +1 -0
file: tests/fixtures/scope/seeded-04-two-unrelated-commits.md +1 -0
file: tests/fixtures/scope/seeded-05-docs-and-migration.md +1 -0
file: tests/fixtures/scope/seeded-06-formatting-sweep-with-feature.md +1 -0
file: tests/fixtures/scope/seeded-07-fix-and-tidy-of-touched-lines.md +11 -0
file: tests/fixtures/scope/seeded-08-feature-and-the-fix-it-exposed.md +12 -0
file: tests/fixtures/useful_description/seeded-01-restates-title.md +1 -0
file: tests/fixtures/useful_description/seeded-02-summary-heading.md +1 -0
file: tests/fixtures/useful_description/seeded-03-lists-the-files.md +1 -0
file: tests/fixtures/useful_description/seeded-04-restates-commits.md +1 -0
file: tests/fixtures/useful_description/seeded-05-states-nothing.md +1 -0
file: tests/fixtures/useful_description/seeded-06-padded-ceremony.md +1 -0
file: tests/fixtures/useful_description/seeded-07-says-it-three-times.md +3 -1
file: tests/token_burning/test_calibration_bars.py +19 -6
file: tests/unit/test_calibration_cases.py +53 -0
file: tests/unit/test_litellm_judge.py +9 -7
---
Every judged policy now answers fail or warn rather than warn alone. Each
policy's instructions gain the two grades as scenarios, and every seeded
calibration case gains the grade a correct judge gives it.

The fixture edits are one line each, the grade the case expects. There are
fifty-nine of them because there is one case per file, and they are what
makes the rule testable.
