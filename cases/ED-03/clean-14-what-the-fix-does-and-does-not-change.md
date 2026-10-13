title: Escape what a contributor wrote in the judge's evidence
expect:
why: "does not change how evidence is laid out" loses a fact when struck.
---
A pull request whose description contained `</description>` ended its own evidence block, so the text after it reached the judge outside the block that marks it as untrusted. A malicious description could use that to tell the judge to report nothing. The same held for the title, commit messages, patches and file paths.

The escaping breaks only closing tags inside contributor text, and does not change how evidence is laid out. So the prompt for any pull request without such text is byte-identical to before: the golden prompt tests pass unchanged, and none of the seven policies' calibration cases contains a closing tag, so their bars stand without a re-run.
