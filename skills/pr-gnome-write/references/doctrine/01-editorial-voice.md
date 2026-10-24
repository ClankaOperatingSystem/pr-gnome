# Editorial voice

Applies to prose everywhere: the project's own documents, commit messages,
pull request descriptions, comments, docstrings, and any text the system
itself emits.

**VOICE-1. Plain register.** Write as one engineer to another: factual and
short. Do not persuade.

**VOICE-2. Say it once.** Put the point first. Do not lead up to it, and do
not repeat it afterwards. Remove a paragraph that summarises the one before
it.

**VOICE-3. Short and precise.** Use the shortest form that is still precise. Do not cut a
qualifier that carries meaning.

**VOICE-4. Active voice.** Write in the active voice. Do not use a passive
that hides the actor, such as "it was determined that".

**VOICE-5. Tables, lists and sentences.** Choose the form by the content. A comparison across more than two
dimensions is a table. A sequence is a list. Everything else is a sentence.
Do not bullet-point prose to make it look organised.

## What not to write

**VOICE-6. Marketing register.** No "robust", "seamless", "powerful",
"elegant", "comprehensive", "battle-tested", "first-class" as praise,
"blazing fast", "delightful", "leverage" as a verb, "utilise". Describe the
property, or say nothing.

**VOICE-7. Self-congratulation.** Do not describe your own output as
"significantly improved", "dramatically simpler", "much cleaner", "a solid
foundation". Describe what changed, and leave the judgement to the reader.

**VOICE-8. Aphorism and epigram.** A sentence written for its rhythm,
which states no fact, anywhere in the text. No "simplicity is the ultimate
sophistication", no "the best code is no code", no "X is not Y, it is Z"
reversals used as rhetoric, no restatement written as a moral. These are
commonest as a closing line. A maxim in the middle of a paragraph, or in bold
like a heading, is the same fault.

The test is rewriting. Put the sentence as a plain statement of fact. If that
statement is already in the text, the maxim repeats it and is deleted. If
there is no statement to be had, the sentence was empty. "The bars passed
twice and failed on the third run, so one pass is not evidence" is the
statement; "a bar that passes twice is not a bar that holds" is the maxim
made from it. The text keeps the statement.

**VOICE-9. Filler openers.** No "Basically", "Essentially", "Simply put",
"At its core", "In essence", "Let's dive in", "In today's landscape". Delete
the opener and start at the noun.

**VOICE-10. Hedging.** No "it's worth noting that",
"it should be mentioned", "arguably", "somewhat", "fairly", "quite",
"I think", "perhaps". Either the claim holds or it is stated as an open
question with what would settle it.

**VOICE-11. Rhetorical questions.** No headings phrased as questions to the
reader, no "So what does this mean?" as a transition. A question mark
belongs only in a list of open questions.

**VOICE-12. Emphasis inflation.** Do not bold for emphasis in running prose.
No exclamation marks. No ALL CAPS. No scare quotes to signal disdain. Emoji
are forbidden everywhere, including commit messages.

**VOICE-13. Fake precision.** No "~40% faster", "roughly 3x", "most users"
unless you measured it and can say how. An unmeasured estimate is labelled as
an estimate.

**VOICE-14. Anthropomorphism.** The workflow does not "want" anything, the
judge does not "feel" that a PR is sloppy, the test suite is not "unhappy".
Say what the code does.

**VOICE-15. Unresolved references.** An identifier is not a substitute for
the thing it names. Do not write "satisfies FR-15", "per ADR-004", "blocked on
question 9", "lands in 0.5" and leave the reader to look it up. Name the
thing, then cite the id if the id is useful: "the exception registry (FR-15)".
This matters most in text written for someone who is not reading the
specification: pull request descriptions, comments, findings the system
emits, and anything addressed to a person.

**VOICE-16. Padding.** "In order to" is "to". "Due to the fact that" is
"because". "At this point in time" is "now". "Has the ability to" is "can".
Do not restate a heading in the sentence beneath it.

**VOICE-17. Comment slop.** A comment that restates the code is deleted. A
docstring that begins "This function is responsible for" is rewritten to
start with the verb. Comments explain why, and record the constraint that is
not visible from the code. Delete commented-out code. Git keeps the
history.

**VOICE-18. Forward promises.** Documentation describes what is, in the
present tense. Not "will eventually support Windows". Intent belongs where
the project tracks it, under milestones or open questions.

**VOICE-19. Narrating yourself.** Pull request descriptions and commit
messages describe the change, not the process of arriving at it. No "I first
tried X, then realised Y". No apologies. No "as requested".

**VOICE-20. Rhetorical triples.** Three parallel items where the meaning
needs one or two. "It is faster, cleaner, and more maintainable" says
"faster" and adds two words that state nothing. Each item in a list must
state a separate fact.

**VOICE-21. Em dashes.** Use a colon, a comma or a full stop.
A sentence with an em dash is almost always two sentences. Write two.

**VOICE-22. Telling the reader what they think.** No "and that is what you
really want", no "you might be wondering", no "the astute reader will
notice". State the thing.

**VOICE-24. Slop vocabulary.** Words that fill the place of a specific
word:
"leverage" for "use", "utilise" for "use", "honest" for "accurate", "delve", "unpack", "landscape",
"realm", "tapestry", "testament to", "journey", "seamlessly", "robustly",
"holistic", "synergy", "paradigm", "game-changing", "best-in-class",
"cutting-edge", "elevate", "empower", "unlock", "supercharge". Each entry
adds nothing to the sentence it is in.

**VOICE-25. Because we can.** A change justified by its own availability is
not justified. No "because we can", no "why not", no "it seemed like a good
idea". Say what the change is for.

**VOICE-26. Coy teasers.** A list that is announced with a hint or a
ranking before its items are given: "one of them matters", "and here is the
interesting part", "guess which one". Say which item matters and why in the sentence that gives the item, or say nothing about the ranking.

**VOICE-27. Manufactured antithesis.** "X, not Y", "X, rather than Y", "not
only Y but X", where Y is not a live alternative anyone proposed. "Make the
round trip a command, not only a test" is four faults in one line:

- The negative half states nothing new. The sentence's job is to name the change;
  half of it describes the state being left behind, which the reader can see.
- It argues with an imagined objection. "not only a test" implies someone
  thought a test was enough, and presents the writer as the one who
  noticed.
- The contrast is empty. A command is not a test, so saying so adds nothing.
  The sentence has the form of a distinction and makes none.
- It delays the change and leaves the scope unclear. The change is "add a
  command". The sentence names it late, and "not only" does not say whether
  the test remains.

"Add the round trip command" is the same change in fewer words.

The test is deletion. Strike the negated half. If every fact remains, the
half stated nothing and the clause is broken. If a fact goes with it, the
contrast stated a fact and the sentence is fine: what the code did
before, which of two options was rejected and why, a measurement that only
means something beside another one. "Nine of ten cases pass, not the eleven
claimed" loses a number when struck. "A command, not only a test" loses
nothing.

**VOICE-28. Garden paths.** A sentence the reader must parse twice. "Correct
references the doctrine cannot resolve" reads first as "correct references",
then as "references the doctrine", and only then as intended. Give the noun
its article and put its modifiers before it: "Correct the unresolvable
doctrine references". If a clause must follow the noun, keep its "that".

The test is the opening words. If they form a phrase the sentence does not
mean, rewrite it.

**VOICE-29. One instruction to a sentence.** A rule tells the reader what to
do. Each sentence gives one instruction, uses a literal verb, and names what
it applies to. "The description carries what the diff cannot show, and no
more" puts two rules into one description of an ideal. "The description
should state what is not obvious from the diff. Do not simply describe the
diff." gives each rule its own sentence.

The test: can the reader do what the sentence says without reading the next
one?
