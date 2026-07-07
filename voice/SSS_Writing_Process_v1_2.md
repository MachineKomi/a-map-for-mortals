# Sweat Soda & Slimes — Writing Process
### v1.2 · Process spec for all shipped prose · **GOLD**

*The lightweight pipeline for producing every word that ships in **Sweat Soda & Slimes** — VN and dating scenes, cutscenes, in-dungeon barks, NPC lines, player choices, quest text, item and card descriptions, combat-log lines, system popups, and the Hound Statue's readouts. It defines the registers, the surfaces, the pass structure, the quality bar, the failure modes, and the harness prompts, at the quality bar set by the **Writing Sample** (gold — its paired doc and the worked demonstration of everything specified here). The voice itself is specified in the **Voice & Style Spec** — the moment map and the voice cards this pipeline enforces. Written for the dev agent that will run it, primarily in **Claude Code** inside the production repo.*

> **v1.2 — locked (2026-07-06; supersedes v1.0 of 2026-06-12).** The voice authority moves to the **Voice & Style Spec** (gold): the moment map, the de-sanitized domination braid, the titles rule, the orthography rules, the lexicon, and the **§9 voice cards** — wired into this pipeline as required drafting and audit inputs (§2/§5/§8). Also adds: the attribution-verb rule (§3.8); the register-sanitization and moment-lean-drift failure modes (§7.11/§7.12); the capitalisation linter (§9.4). Pipeline, harness, surfaces, and bank model unchanged from v1.0.

---

## Section index

- **§1** — First principle — the world first, the spice second
- **§2** — The voice
- **§3** — The registers and the wall
- **§4** — The surfaces — what gets written, and how it attaches to the systems
- **§5** — The pipeline — four passes, scaling with the artifact
- **§6** — The quality bar
- **§7** — Failure modes to actively defend against
- **§8** — Harness prompts
- **§9** — Scriptable checks

---

## 1. First principle — the world first, the spice second

This game is, first, a beautifully written romantic comedy — a VN / dating-sim / JRPG with a realised world, complex and believable characters with multi-dimensional personalities, real story, humour, and emotional depth. The fan service — traditional and sensory alike — is a **unique selling point and a reward**, woven through that world as one flavour among many. It is never the bulk of the writing. Most scenes carry worldbuilding, lore, plot, and character; the scent/sweat/taste layer intensifies with intimacy and arrives as payoff, not wallpaper. A page that is *only* fan service has failed this spec exactly as badly as a page with none of the game's warmth.

Two corollaries every pass below enforces:

- **Character-expressing, never objectifying.** A descriptor that would work the same on any interchangeable body is wrong. (Scent & Taste Reference §9.)
- **Scent loses its charge if it's on every page.** Deploy sparingly; let absence do work too.

---

## 2. The voice

**The authority is the Voice & Style Spec.** It carries the instrument (§1), the moment map (§2), the domination braid (§3), the titles rule (§4), the orthography rules (§5), the lexicon deltas (§6), the calibration exemplars (§8), and — critically — **the voice cards (§9): the imitable specification of each bench source.** No drafter or reviewer should be relying on prior knowledge of Mitchell, Morita, Milne, Harris, Holland, *Slayers*, or *Roman Holiday*; the cards are the working definition, and drafting without them open is a process violation. This section keeps only what the pipeline needs at its fingertips.

### The bench (unchanged — each row's full card is Voice & Style Spec §9)

| Source | Card | What we take |
|---|---|---|
| **David Mitchell** (the comedian — *Peep Show*, the columns, *Back Story*; **not** the novelist) | §9.1 | The protagonist's interior: precision-as-comedy, the scrupulous concession, load-bearing parentheses; the aggrieved-but-reasonable rant rhythm. |
| **"Slimes 300"** (*I've Been Killing Slimes for 300 Years and Maxed Out My Level*, Kisetsu Morita — Inspiration Atlas §A) | §9.2 | Burnout gratitude; the flat verdict line; sentence-titles; the one-beat plain confession; arrival/onboarding directness; game logic as plain world-fact. |
| **A.A. Milne** | §9.3 | The build-and-turn sentence; dignity granted downward; repetition-with-variation in ensemble volleys. **Shapes only — never the Capitalised-Significant-Word orthography.** |
| **Robert Harris / Tom Holland** | §9.4 | Awe via administration: institutions with agency, the appositive dossier, deep time — for **power and old stone only**, never the cosy village. |
| **Slayers** | §9.5 | The banter engine: escalation volleys, insult-as-affection, bicker → bicker → one quiet honest line → bicker. |
| ***Roman Holiday*** | §9.6 | The arc shape: borrowed joy, truth admitted late, the withheld line; changed and enriched, bittersweet permitted, never tragic. |

### The voice equations (defaults; deviate only per the moment map)

- **Izumi's interior** ≈ Mitchell 0.5 + Slimes 300 0.4 + Milne 0.1 — dry, self-aware, parenthetically British, never whiny.
- **World atmosphere** ≈ Harris 0.5 + Holland 0.5 — sparse, solid, sensory establishing detail.
- **Supporting-cast description** ≈ Milne 0.7 + Mitchell 0.3.
- **Banter exchanges** ≈ Slayers rhythm in the project's own diction.

**The moment map (Voice & Style Spec §2) governs when the equations lean:** LN directness for onboarding/arrival/lightest copy and for Izumi's one-beat confessions; chronicler ballast for institutional/power/deep-time establishing; Milne cadence in ensemble hub comedy; plain sensory verbs in the combat log. **The lean is a seasoning, not a key change** — the core voice gets the closer. **When two drafts tie, take the shorter, plainer one.**

**Titles:** chapter/scene titles are whole sentences in the LN tradition; the Milne "In Which…" form is the sanctioned alternate for cosy hub pieces (Voice & Style Spec §4).

### House prose rules (from the Creative DNA, enforced by the Voice Auditor)

- Comedy first; sincerity sneaks up. Punchy and short, like manga captions.
- **Sensory-forward** — never "the room was warm" but *which* warm, *whose* warm. Smell, heat, texture, humidity, weight.
- Romance through micro-rituals, not declarations. Emotion staged, never announced.
- Anachronistic philosophy as comedy (Stoicism applied to fish purchases) is on-brand; meta-wink that celebrates the genre without breaking the world.
- No grimdark, no nihilism, no cruelty without wit, no irreversible despair. T-rated throughout.
- **No decorative capitalisation** — capitals never mark Significance (Voice & Style Spec §5; sanctioned exceptions listed there, including **"Mistress"** and diegetic signage).

---

## 3. The registers and the wall

1. **Narration is pure-sensory.** Prose never names a compound or a microbe, and never deploys a cartoon stink-cloud. Smell is rendered located, conditional, and honest. **These are the only two prose bans.** (Scent & Taste Reference §9.)
2. **No sensory word is banned.** Blunt ("stinky," "reeks," "ripe") and literary ("redolent," "the bloom of") trigger words alike are *pleasing* and encouraged — **sparingly, in character, earned** (Scent & Taste Reference §8.5). The Voice Auditor must not flag blunt dialogue as a lapse; bluntness in a character's mouth is characterisation.
3. **Dialogue may go blunt; narration stays grounded.** The immature/vulgar reaction register ("ew, that's *rank*") belongs to characters, never to the narrator.
4. **Named chemistry lives only in the Hound Statue.** Its readout is a deliberately different voice — dry, technical, faintly absurd edutainment (Writing Sample piece VII is the register target).
5. **One overpoweringly cheesy locus exists: Victoria's feet** — an in-world fact, rendered in prose that stays excellent. Cheese anywhere else, or that beat written cheaply, is a defect.
6. **Write in register.** The register selector (Core Systems & Simulation spec §9.5; Scent & Taste Reference §4.5/§8) chooses *how* a smell is talked about from character + relationship + mood: **genuine recoil · performed-teasing · mean-dommy/warm-domination · bratty · knowing-wink · tender**. Every scent line in a bank is written *for* a register.
7. **The domination register is a braid, written de-sanitized** (Voice & Style Spec §3; Creative DNA §1/§6): chronicler gravity for her presence, LN confession for his reaction, core-voice precision for the scent — **tuned per woman** (Victoria as ceremony; Masha as sport; Lyra inverted, as slips through a wholesome cover — exemplars in Voice & Style Spec §8.2). **The surface runs the full bully spectrum — callous cruelty, humiliation, teasing, gleeful torment; she enjoys his shame and the prose says so.** The floor is unchanged and absolute: emotional, romantic, consensual, equal underneath; never physical harm; never contempt-without-care; **never childlike** — her delight is a cruel smirk, not a child's glee. Softening the surface is a documented failure mode (§7.11), not a courtesy.
8. **Attribution verbs carry register** — *she teases*, not *she says*, when the line is a tease; used sparingly, as seasoning.

---

## 4. The surfaces — what gets written, and how it attaches to the systems

The shipped game **selects authored content; it never generates prose live.** The simulation resolves a character's current state to **sensory tags** (Core Systems & Simulation spec §9.5); the writing is produced as **tag-keyed banks** this pipeline fills.

| Surface | Register notes |
|---|---|
| VN / dating scenes, cutscenes | Full prose voice (§2) with the moment map applied; scent as tag-driven spice, intensifying with intimacy. |
| In-dungeon barks, NPC reactions | One to three lines, tag-keyed, in register; the receiver's nose matters (an appreciative monster and a prim shrine attendant read the same state oppositely). |
| Player dialogue choices | Scent- and state-gated where warranted; the choice text itself stays in Izumi's voice. |
| Laundry beats | The acceptance-dial register ladder: teasing → knowing-wink → tender. |
| Quest-board text | The town's voice — officialese, neighbours, and the cult's oily politeness; comedy with worldbuilding inside it. Diegetic signage may use notice-board caps. |
| Item / soda / card descriptions | Short, warm, one joke that earns its keep; **direct and literal beats decorated**; flavour does worldbuilding. |
| Combat-log lines | Mechanical surface with flavour; statuses and scent effects named sensorially, never chemically; the plain scent-verb family (*thickens, ripens, intensifies, grows more potent*). |
| Hound Statue copy | **The one chemistry register** (§3.4). |
| Tutorials / system popups | Izumi-adjacent dryness; never breaks the world. The LN lean's typographic charms are sanctioned in short-form surfaces only. |

**Bank entry shape:** `character · surface · tagset · register → line(s)`. Tags are sensory only (`feet:toasted-moreish`, `footwear:musky`, `freshness:day-7`) — never compounds. Conditional tells (Lyra's metallic note) key off the **resolved** scent vector, never raw inputs, or the tell misfires.

**Ownership:** this doc owns the *method*; the **Voice & Style Spec** owns the voice; the per-character line banks, running-joke beats, and per-character voice live with **Cast & Romance**; the consolidated bank format and naming conventions land in the **Writing Tag/Register Bank** when built. The Writing Sample (gold) is the register target for every surface above.

---

## 5. The pipeline — four passes, scaling with the artifact

### Harness

- **Claude Code is the primary harness.** The shipped writing is data in the production repo — VN timelines and dialogue files (rendered per the Dialogic & VN Tech Reference: *Dialogic renders; our code remembers the state*), tag-keyed bank files, item/quest text — sitting next to the code, the tests, and the linters. The passes below run as ordinary agent passes (subagent calls or sequential prompts) over those files; the scriptable checks (§9) run as repo scripts/CI.
- Cowork remains acceptable for long-form spec-side prose (documents like the Writing Sample), where the artifact is a doc rather than game data.

### The four passes

1. **BRIEF.** One paragraph, written before drafting: what artifact, what purpose, what length, which voice equation **and which moment-map leans apply (naming the §9 cards involved)**, which registers, what must appear, what must NOT appear.
2. **DRAFT.** Written straight through against the brief, the voice equations, the moment map, and the **voice cards** (Voice & Style Spec §9 — the seeded set; §8.1 below refreshes or extends them when needed). Planned openers and closers honoured; at least one line per piece that surprises the drafter; no mid-piece revision.
3. **REVIEW — three hats, in order.** Each returns flags with line references; on long-form set pieces each hat runs in its own context, on micro-copy they run as one combined pass:
   - **Voice Audit** — find every line that slipped into generic LLM voice (§7 lists the tells); check each lean against its moment **and against its card** (a Milne-lean line that breaks a §9.3 "never does" is a flag); flag decorative capitalisation; check the last paragraph as hard as the first.
   - **Continuity & Scent Lint** — names, world facts, T-rating, monogamy-of-commitment; and the scent-grounding check: every smell **located** on a body or object, **causal** (diet / material + condition / mood / hygiene / exertion — answerable from the Core Systems & Simulation spec), **sensory** rather than cartoon, **chemistry-free** outside Hound-Statue blocks.
   - **Devil's Advocate** — a hostile pass; finds what's embarrassing, clichéd, unearned, off-taste, or skim-past-able — **including sanitization**: any dominant beat gone gentle, any humiliation cushioned into niceness. "Looks good to me" is a failure response.
4. **POLISH & COMMIT.** Apply or defend every flag; cut what earns no place (§6); read for rhythm (stumbles, flatlines, tags that fight the line); commit with a one-line log of what changed.

**Scaling rule:** set pieces (VN scenes, cutscenes) get the full four passes with separate review contexts. Micro-copy (barks, item text, log lines) gets BRIEF → DRAFT → one combined review → commit. **The scent linter (§9) always runs, on everything.**

---

## 6. The quality bar

A piece passes if it has **all of:**

1. **At least one line doing double work** — comic on the surface, emotional underneath.
2. **At least one line of unearned-sounding specificity** — a detail so particular it has to be real.
3. **A closer that lands without overspeaking** — emotion implied, not declared, and delivered in the core voice.
4. **Voice consistency** — opening voice and closing voice are the same instrument; every lean matched to its moment (Voice & Style Spec §2), bounded, and true to its card (§9).
5. **Scent in register** — sensory, grounded, chemistry-free in prose; any cheese is Victoria's feet and written well; trigger words earned and sparing.
6. **Register integrity** — dominant beats carry their real teeth (§3.7); confessions are plain for one beat, then re-armoured.
7. **No flag from the Devil's Advocate the team can't defend.**

A piece fails if it has **any of:**

- A line that could have been written by any LLM.
- Sentimental abstraction (love, longing, connection) without a concrete object to ride it.
- Foreshadowing so heavy the reader sees the reveal coming.
- A dialogue exchange that exists only to deliver information.
- Three adjectives where one verb would do.
- A molecule named in prose, or cheese anywhere but the one sanctioned place.
- Decorative capitalisation outside the sanctioned exceptions.
- Fan service carrying a scene that has nothing else in it (§1).

---

## 7. Failure modes to actively defend against

1. **LLM-default voice.** *"A tapestry of," "the air was thick with," "a symphony of," "in a world where."* The single most common failure; the Voice Auditor exists to kill it.
2. **Sentimentality without an object.** Emotion stated rather than embodied in the small specific thing it causes.
3. **Adverb fog.** *"She said softly"* instead of *"she said, and the fire popped."*
4. **Foreshadow-as-billboard.** Hints so loud they pre-spoil the reveal. (Lyra's route lives or dies on this.)
5. **Voice drift across length.** Page 1 sounds like Mitchell, page 3 sounds like generic narrator. Audit the end hardest.
6. **Genre-tribute autopilot.** The LN trope or the Milne repetition without the wit underneath — the card's tics without the card's "one thing only they do."
7. **Earnestness without armour.** Real feeling must be armoured by humour, specificity, or rhythmic restraint; naked sincerity reads as greeting card. (The sanctioned exception: the one-beat LN confession — one beat, then the armour returns.)
8. **Over-cleverness.** Every line winking. The big beats work because the prose stops being clever for one paragraph and just sits there.
9. **Register bleed in scent.** (a) Chemistry vocabulary in narration instead of a Hound-Statue block; (b) cheese outside Victoria's feet, or that beat written cheaply rather than written *well about* something cheesy.
10. **Scent fatigue.** The spice on every page (§1). If a reviewer can predict that a scene will contain a scent beat, there are too many scent beats.
11. **Register sanitization.** The documented failure mode (Creative DNA §0): the dominant surface drifting gentle across passes — "cruel smirk" becoming "playful smile," humiliation becoming banter, the bully spectrum flattened to warmth. The floor is locked; the surface is not to be softened. When tempted, flag instead.
12. **Moment-lean drift.** A lean escaping its moment — chronicler gravity over the cosy village, LN breeze on floor eighteen, Milne cadence in a Victoria audience. The map (Voice & Style Spec §2) bounds every lean.

---

## 8. Harness prompts (run each in isolation with the listed inputs)

### 8.1 Voice Analyst (refresh/extend the seeded cards; build new ones only for new sources)

*The six bench sources already have seeded cards in the **Voice & Style Spec §9** — those stand as the working reference. Run the Analyst to **refresh a card against real source passages** when a register needs deeper calibration, or to **build a card for a new source** the bench gains later. An Analyst rebuild that contradicts a seeded card is flagged to the author, not silently swapped in.*

> You are a Voice Analyst studying [WRITER / WORK]. You have been given [N] representative passages, and the existing seeded card (Voice & Style Spec §9.[X]) if one exists. Produce a Voice Card with: (1) 2–4 syntactic tics; (2) 2–4 rhythmic / structural tics; (3) one thing this writer does that nobody else does; (4) one thing this writer NEVER does; (5) a two-sentence pastiche demonstrating you can hear them; (6) one paragraph of "what to take for Sweat Soda & Slimes, what to leave behind." Where your findings differ from the seeded card, list the differences explicitly for author review.
> Be specific. Vague answers are failures. If you cannot identify a tic, say so explicitly — do not invent.

### 8.2 Synthesis Architect (when a new artifact type needs its own equation)

> You are the Synthesis Architect. You have the Voice Cards (Voice & Style Spec §9), the moment map (§2), and one project brief. Produce: (1) the dominant register and why; (2) the supporting registers and their triggers; (3) the protagonist's interior voice formula as approximate weights; (4) the world's exterior voice formula; (5) the tonal arc across the artifact, piece by piece, naming each moment-map lean it invokes. Justify each weight in one sentence. Default to the locked equations in the Writing Process spec §2 unless the brief demands otherwise.

### 8.3 Drafter

> You are the Drafter. You have the brief, the voice equations, the moment map and voice cards (Voice & Style Spec §2/§9), the structural plan, and the exemplar bank (§8). Write the artifact straight through, one piece at a time. Honour the planned openers and closers; give the closer to the core voice. Each piece must contain at least one line that surprises you. Do not revise mid-piece. Do not hedge. Do not explain emotion — stage it. Keep scent sensory, located, and causal; never name a molecule in prose; keep cheese to Victoria's feet and write it well; blunt sensory words are allowed in dialogue, sparingly and in character. Write dominant beats with their real teeth — the floor is warmth, the surface is not. Never capitalise a word to make it Significant. When two phrasings tie, take the shorter, plainer one.

### 8.4 Voice Auditor

> You are the Voice Auditor. You have the draft, the voice equations, and the moment map and voice cards (Voice & Style Spec §2/§9). Find every line that sounds like generic LLM output rather than the designed synthesis. For every flag, quote the line, name the failure mode (Writing Process spec §7), and propose a rewrite or mark it for cutting. Audit the final paragraph as hard as the first. Check every lean against its moment and its card: flag chronicler weight on cosy material, LN breeze on deep material, Milne cadence outside ensemble comedy, any breach of a card's "never does," and any lean that holds the closer. Flag any molecule named in prose, any cheese outside Victoria's feet, and any decorative capitalisation outside the sanctioned exceptions. Do NOT flag blunt sensory dialogue ("reeks," "stinky") as a lapse — that register is sanctioned when in character (Scent & Taste Reference §8.5). Do NOT flag cruelty, teasing, or humiliation in a dominant character's surface as a lapse — sanitizing that register is itself the failure (§7.11); flag only a breach of the floor (physical harm, contempt-without-care, non-consent).
> You are failing if you return fewer than [N] flags on a [M]-word draft. Be ruthless.

### 8.5 Continuity & Scent-Grounding Editor

> You are the Continuity Editor. You have the draft, the Core Systems & Simulation spec, the Cast & Romance spec, and the Scent & Taste Reference. Verify names, geography, world rules, T-rating, and monogamy-of-commitment. Then run the scent-grounding pass: for every smell, sweat, or musk description, confirm it is located on a body or object, caused by something the systems model can produce (diet / material + condition / mood / hygiene / exertion), sensory rather than cartoon, and free of named chemistry outside Hound-Statue blocks. Confirm conditional tells key off the resolved state, not raw inputs. Flag every violation with a line reference and a fix.

### 8.6 Devil's Advocate

> You are the Devil's Advocate. You hate this draft. Find what is embarrassing, clichéd, unearned, off-taste, or skim-past-able. You are NOT here to validate or be balanced. Hunt the fan-service line that crosses the taste line (objectifying, cruel-without-care, or carrying a scene alone), any scent prose gone cheesy or chemical, any dominant beat gone soft — a "cruel" line with no cruelty in it, a humiliation that flatters — and the bit a hostile reviewer would screenshot. Return at least [N] specific objections with line references. "Looks good to me" is a failure response and will be rejected.

---

## 9. Scriptable checks (cheap, run always)

Implement as repo scripts; run on every commit of writing data:

1. **Chemistry linter.** A wordlist of compounds/microbes (seeded from the Scent & Taste Reference's named-chemistry layer and the Core Systems appendix). Any hit outside a tagged Hound-Statue block fails the commit.
2. **LLM-phrase linter.** The §7.1 banned-phrase list, greppable, extended as new tells are found.
3. **Cliché-scent linter.** Flag unconditioned scent similes (a scent with no nearby causal anchor: body/garment + state, diet, mood, or exertion within the passage).
4. **Capitalisation linter.** Flag mid-sentence capitalised common nouns in narration and dialogue, against the sanctioned-exception list (proper nouns, named statuses, "Mistress", tagged diegetic signage blocks).
5. **Tag-coverage check.** For each bank: every register variant the systems can request has at least one line; every line's tagset uses only tags the resolver can emit.
6. **Foreshadowing ledger.** A persistent file of debts planted (e.g. Lyra's metallic tell → its route payoff) and debts paid; reviewed whenever a route beat is written.

---

*Paired docs: the **Voice & Style Spec** (the voice authority — instrument, moment map, braid, titles, orthography, lexicon, exemplar bank, and the §9 voice cards); the **Writing Sample** (gold) — the register target and worked example for every surface here; the **Scent & Taste Reference** (gold) — the science and descriptor palette; the **Core Systems & Simulation spec** §9.5 — the resolver and register selector this pipeline writes for; **Cast & Romance** — per-character voice and banks; the **Dialogic & VN Tech Reference** (gold) — where the rendered words live in the build.*
