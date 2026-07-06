# A Map for Mortals — Literature Module, First-Pass Wisdom Extraction

## TL;DR
- Across Shakespeare, the Greek tragedians, the great moral novelists, the Romantic/Victorian/American poets, Goethe, and folk proverb, the strongest graph-worthy wisdom clusters around six recurring forks — passion vs. duty, revenge vs. forgiveness, ambition vs. love, self-deception vs. truth, freedom vs. fate, pride vs. humility — and the narratives much more often DRAMATISE the cost of each choice than ENDORSE a single side.
- The single most important methodological finding: many "wisdom" lines circulating as authorial doctrine are either (a) spoken by characters the narrative complicates or undercuts (Keats's urn, Macbeth's nihilism, Austen's ironic narrator, Edgar's "ripeness is all"), or (b) outright misattributions (fake Goethe via John Anster, fake Twain, fake Shakespeare, and the *Les Misérables* "face of God" line that is Herbert Kretzmer's 1985 lyric, not Hugo's prose) [C.S. Lewis Institute](https://www.cslewisinstitute.org/resources/les-miserables-a-story-of-gods-hospitality-grace-and-redemption/) — so every unit below carries an `endorsement` and `attribution_confidence` tag.
- For ingestion, prefer public-domain editions throughout (Folger/MIT Shakespeare; Maude for Tolstoy; Garnett for Dostoevsky; Standard Ebooks for Eliot/Austen; Wikisource for the poets; Bayard Taylor for *Faust*; Gilbert Murray for the tragedians) and flag every modern translation you rely on (Pevear & Volokhonsky for Dostoevsky/Tolstoy; modern Penguin/Oxford Greek tragedy) as `in_copyright_translation`.

---

## (a) SOURCE INVENTORY TABLE

| Author / Work | Best public-domain edition/translation to cite | Copyright status | Notes / flagged modern alternatives |
|---|---|---|---|
| Shakespeare — plays | Folger Shakespeare Library editions (online, freely readable); MIT Shakespeare; Perseus (Clark & Wright, Globe text) | `public_domain` | Original text PD. Cite act/scene/line. |
| Shakespeare — Sonnets | 1609 Quarto; Standard Ebooks / Project Gutenberg | `public_domain` | — |
| Aeschylus — Oresteia / Agamemnon | Herbert Weir Smyth (Loeb, 1926); E. D. A. Morshead (1881) | `public_domain` | Flag Robert Fagles (1975), Michael Ewans, Anne Carson as `in_copyright_translation`. |
| Sophocles — Oedipus the King | F. Storr (Loeb, 1912); R. C. Jebb (1880s) | `public_domain` | Flag Fitts & Fitzgerald (1939/49), Robert Fagles as `in_copyright_translation`. |
| Euripides — Bacchae | Gilbert Murray (1902/06); E. P. Coleridge (1891) | `public_domain` | Flag Arrowsmith (1959), Woodruff (1998), Carson, Robertson (2014) as `in_copyright_translation`. |
| Tolstoy — Anna Karenina; What Men Live By; A Confession; Death of Ivan Ilyich | Louise & Aylmer Maude (1918 AK; 1906 tales) — translators knew Tolstoy and had his approval | `public_domain` | Flag Pevear & Volokhonsky (2000/2008), Rosamund Bartlett (2014), Rosemary Edmonds as `in_copyright_translation`. |
| Dostoevsky — Brothers Karamazov; Notes from Underground; Crime and Punishment | Constance Garnett (1912–1920s) | `public_domain` | Flag Pevear & Volokhonsky (BK ©1990; C&P, Notes) and David McDuff (Penguin) as `in_copyright_translation`. |
| George Eliot — Middlemarch | First edition (1871–72); Standard Ebooks | `public_domain` | — |
| Jane Austen — Pride and Prejudice, Emma, Persuasion, Sense and Sensibility | First editions (1811–1817); Standard Ebooks / R. W. Chapman text | `public_domain` | — |
| Victor Hugo — Les Misérables | Isabel F. Hapgood (1887); Charles E. Wilbour (1862) | `public_domain` (novel) | CRITICAL: "To love another person is to see the face of God" is NOT in Hugo's novel [Answers](https://www.answers.com/religious-literature/Where_in_Victor_Hugo's_Les_Miserables_is_the_quote_To_love_another_person_is_to_see_the_face_of_God) — it is Herbert Kretzmer's 1985 English lyric for the Boublil–Schönberg musical [Wikipedia](https://en.wikipedia.org/wiki/Les_Mis%C3%A9rables_(musical)) → `in_copyright_work`. Flag Norman Denny (1976) and Julie Rose (2008) translations as `in_copyright_translation`. |
| Wordsworth, Keats, Tennyson | Wikisource / Oxford editions of the original texts | `public_domain` | — |
| Whitman — Leaves of Grass | 1891–92 "deathbed" edition (Whitman Archive; poets.org) | `public_domain` | — |
| Emily Dickinson | Franklin (1998) and Johnson (1955) numbering for reference; texts PD | poems `public_domain`; **Johnson/Franklin editorial apparatus `in_copyright`** | The 1951/1955 Johnson edition arrangement is ©President & Fellows of Harvard College — cite poem text (PD), not the edited apparatus. |
| Goethe — Faust | Bayard Taylor (1870–71); Anna Swanwick (1850) | `public_domain` | Flag Walter Kaufmann (1961), Walter Arndt (1976), David Luke (1987) as `in_copyright_translation`. |
| Goethe — Wilhelm Meister | Carlyle (1824) translation | `public_domain` | Cross-reference separate Nietzsche prompt. |
| Folk & proverbial | Cite earliest documented printed source where traceable | `public_domain` (communal) | Proverbs are communal/unattributable; `attribution_confidence` should be `dubious`/`apocryphal` for "originator," `probable` for "attested in tradition." |

---

## (b) WISDOM UNITS (grouped by author/work)

### SHAKESPEARE

```yaml
- id: insight.shakespeare.ripeness_is_all
  canonical_claim: Human beings must endure death's timing as they did birth's; readiness, not control, is what matters.
  original_quote: "Men must endure / Their going hence even as their coming hither. / Ripeness is all."
  citation: { author: William Shakespeare, work: King Lear, location: "Act 5, Scene 2", edition: "Folger / MIT (Globe text)", date: "c.1605–06" }
  speaker: Edgar (disguised), to his blinded father Gloucester
  dramatic_context: Lear and Cordelia have just been captured; the despairing Gloucester says "a man may rot even here" and refuses to move. Edgar urges him onward.
  register: aphorism
  claim_type: prudential
  polarity: prescriptive
  conditionality: contested
  life_domains: [death, adversity, old age]
  life_stages: [old age, adult]
  attribution_confidence: verified
  endorsement: complicated
  copyright_flag: public_domain
  addresses_dilemma: freedom_vs_fate
  tension_note: Said by a son consoling a suicidal father moments before more catastrophe — the play's bleak ending (Cordelia's needless death) tests whether "ripeness" is genuine consolation or stoic whistling in the dark. NOTE: commonly misattributed to Lear; the speaker is Edgar (confirmed against Folger, MIT, and Perseus texts).

- id: insight.shakespeare.tomorrow_petty_pace
  canonical_claim: Life is a brief, meaningless performance signifying nothing.
  original_quote: "Tomorrow, and tomorrow, and tomorrow, / Creeps in this petty pace from day to day / To the last syllable of recorded time; ... It is a tale / Told by an idiot, full of sound and fury, / Signifying nothing."
  citation: { author: William Shakespeare, work: Macbeth, location: "Act 5, Scene 5", edition: "Folger / MIT", date: "c.1606" }
  speaker: Macbeth
  dramatic_context: On hearing of Lady Macbeth's death, as enemy armies close in and his crimes collapse around him.
  register: poem
  claim_type: metaphysical
  polarity: descriptive
  conditionality: contested
  life_domains: [death, ambition, adversity, grief]
  life_stages: [adult]
  attribution_confidence: verified
  endorsement: undercut
  copyright_flag: public_domain
  addresses_dilemma: ambition_vs_love
  tension_note: This nihilism is the terminal state of a murderer who chose ambition over loyalty and love; the play frames it as the wage of his crimes, not as Shakespeare's metaphysics. The "tomorrow" speech is genuine — unlike the many floating fakes.
```

**Misattribution flags (Shakespeare):** "Expectation is the root of all heartache" — confirmed NOT Shakespeare by the Folger Shakespeare Library (absent from the canon). [Check Your Fact](https://checkyourfact.com/2019/09/25/fact-check-shakespeare-expectation-root-heartache/) "Oh what a tangled web we weave" is Sir Walter Scott (*Marmion*, 1808), not Shakespeare.

### THE GREEK TRAGEDIANS

```yaml
- id: insight.aeschylus.pathei_mathos
  canonical_claim: Wisdom is won through suffering, by a law the gods imposed on mortals.
  original_quote: "Zeus, who sets mortals on the path to understanding, Zeus, who has established as a fixed law that 'wisdom comes by suffering.'"
  citation: { author: Aeschylus, work: Agamemnon (Oresteia), location: "choral ode to Zeus (~lines 176–183)", edition: "Herbert Weir Smyth, Loeb 1926", date: "458 BCE" }
  speaker: The Chorus of Argive elders
  dramatic_context: Reflecting on Agamemnon's sacrifice of Iphigenia and the moral order of Zeus, early in the play.
  register: principle
  claim_type: metaphysical
  polarity: descriptive
  conditionality: conditional
  life_domains: [adversity, grief, self]
  life_stages: [adult]
  attribution_confidence: verified
  endorsement: ambiguous
  copyright_flag: public_domain
  addresses_dilemma: self_deception_vs_truth
  tension_note: Greek "pathei mathos"; some scholars (e.g. Ewans) argue "learn from experience" is closer than "learn by suffering" and warn against importing Christian redemptive overtones. Recurrence across the trilogy shows suffering does NOT reliably produce wisdom — the vengeance cycle continues. Flag Fagles, Carson as in_copyright.

- id: insight.sophocles.count_no_man_happy
  canonical_claim: No life can be judged fortunate until it has ended free of pain.
  original_quote_modern: "Now as we keep our watch and wait the final day, count no man happy till he dies, free of pain at last."
  original_quote_PD: "Let every man in mankind's frailty consider his last day; and let none presume on his good fortune until he find life, at his death, a memory without pain." (Storr, 1912)
  citation: { author: Sophocles, work: Oedipus the King (Oedipus Rex), location: "closing lines (~1684)", edition: "F. Storr, Loeb 1912 (PD)", date: "c.429 BCE" }
  speaker: The Chorus (closing tag)
  dramatic_context: After Oedipus discovers he has killed his father and married his mother, blinds himself, and is led away.
  register: aphorism
  claim_type: observational
  polarity: cautionary
  conditionality: universal-ish
  life_domains: [death, adversity, ambition]
  life_stages: [old age, adult]
  attribution_confidence: verified
  endorsement: endorsed
  copyright_flag: public_domain
  addresses_dilemma: pride_vs_humility
  tension_note: Echoes Solon's maxim; the play frames it as hard-won truth about the limits of human control. The familiar "count no man happy till he dies" wording is from a modern translation; for PD citation use Storr (1912).

- id: insight.euripides.cleverness_not_wisdom
  canonical_claim: Cleverness is not the same as wisdom; true wisdom accepts limits and reveres what is greater than human striving.
  original_quote: "What else is Wisdom? What of man's endeavour / Or God's high grace, so lovely and so great? / To stand from fear set free, to breathe and wait..." [Project Gutenberg](https://www.gutenberg.org/files/35173/35173-h/35173-h.htm)
  citation: { author: Euripides, work: The Bacchae, location: "second stasimon (choral refrain on 'to sophon')", edition: "Gilbert Murray, 1902/06", date: "405 BCE (posthumous)" }
  speaker: The Chorus (Asian Bacchant women)
  dramatic_context: As Pentheus, King of Thebes, resists the god Dionysus and moves toward his destruction.
  register: principle
  claim_type: normative
  polarity: cautionary
  conditionality: contested
  life_domains: [self, adversity, ambition]
  life_stages: [adult, youth]
  attribution_confidence: probable
  endorsement: complicated
  copyright_flag: public_domain
  addresses_dilemma: pride_vs_humility
  tension_note: Greek "to sophon d' ou sophia." Murray's English is interpretive (he admitted interpolating a line); [Wikisource](https://en.wikisource.org/wiki/The_Bacchae_of_Euripides_(Murray_1906)/Notes) the literal "cleverness is not wisdom" comes from modern (in_copyright) translations like Arrowsmith. The Bacchae fiercely complicates the lesson — Dionysus's "wisdom" is also terrifying and cruel; the play stages Pentheus torn apart by his own mother Agave. [GradeSaver](https://www.gradesaver.com/the-bacchae/study-guide/summary-of-lines-1025-1394)

- id: insight.euripides.gods_many_shapes
  canonical_claim: The divine works in shapes beyond human expectation; what we await does not come, and a path opens where none was thought.
  original_quote: "There be many shapes of mystery. / And many things God makes to be, / Past hope or fear. / And the end men looked for cometh not, / And a path is there where no man thought." [Edmundgriffiths](http://www.edmundgriffiths.com/bacchae.html)
  citation: { author: Euripides, work: The Bacchae, location: "closing chorus", edition: "Gilbert Murray, 1902/06", date: "405 BCE" }
  speaker: The Chorus / Chorus-Leader
  dramatic_context: Final lines, after the catastrophe of Pentheus and Agave.
  register: aphorism
  claim_type: metaphysical
  polarity: descriptive
  conditionality: universal-ish
  life_domains: [adversity, fate, death]
  life_stages: [adult]
  attribution_confidence: verified
  endorsement: ambiguous
  copyright_flag: public_domain
  addresses_dilemma: freedom_vs_fate
  tension_note: This closing formula recurs at the end of several Euripidean plays, [Edmundgriffiths](http://www.edmundgriffiths.com/bacchae.html) which may dilute its specific force; here it caps a horrifying outcome rather than a comforting one.
```

### TOLSTOY

```yaml
- id: insight.tolstoy.happy_families
  canonical_claim: Flourishing requires that many conditions all go right; failure can come from any single missing thing.
  original_quote: "All happy families resemble one another, each unhappy family is unhappy in its own way."
  citation: { author: Leo Tolstoy, work: Anna Karenina, location: "Part 1, Ch. 1 (opening)", edition: "Maude (1918)", date: "1877" }
  speaker: Narrator
  dramatic_context: Opening sentence, framing the Oblonsky household's collapse and the novel's study of marriage and fidelity.
  register: aphorism
  claim_type: observational
  polarity: descriptive
  conditionality: contested
  life_domains: [family, love, marriage]
  life_stages: [adult, parenthood]
  attribution_confidence: verified
  endorsement: complicated
  copyright_flag: public_domain
  addresses_dilemma: passion_vs_duty
  tension_note: The novel itself contains no ideally happy family, and Levin's "happy" marriage still quarrels — the maxim is a thesis the book tests and partly subverts (cf. the "Anna Karenina principle" in statistics/ecology). Maude translation is PD; flag Pevear & Volokhonsky (2000) as in_copyright_translation.

- id: insight.tolstoy.what_men_live_by
  canonical_claim: People survive not by self-care or foresight but by love for one another.
  original_quote: "I have now understood that though it seems to men that they live by care for themselves, in truth it is love alone by which they live."
  citation: { author: Leo Tolstoy, work: What Men Live By, location: "final section (angel Michael's revelation)", edition: "Maude (1906, Twenty-three Tales)", date: "1885" }
  speaker: Michael (an angel in human form)
  dramatic_context: A fallen angel, sheltered by a poor shoemaker, reveals the three truths he was sent to learn; the third is spoken as he ascends.
  register: parable
  claim_type: normative
  polarity: prescriptive
  conditionality: universal-ish
  life_domains: [love, money, family, adversity]
  life_stages: [adult]
  attribution_confidence: verified
  endorsement: endorsed
  copyright_flag: public_domain
  addresses_dilemma: self_vs_others
  tension_note: A post-conversion didactic parable rooted in 1 John ("God is love") — the narrative fully endorses the claim, which is exactly why it reads as sermon rather than drama; lower "shown not preached" value than Anna Karenina. Cross-references A Confession (1882).
```

### DOSTOEVSKY

```yaml
- id: insight.dostoevsky.guilty_for_all
  canonical_claim: Each person is responsible before everyone for everything; recognizing shared guilt is the ground of active love.
  original_quote: "each of us is guilty in everything before everyone, and I most of all."
  citation: { author: Fyodor Dostoevsky, work: The Brothers Karamazov, location: "Book VI (Elder Zosima, repeating his dying brother Markel)", edition: "Garnett (1912)", date: "1880" }
  speaker: Elder Zosima (repeating his dying brother Markel)
  dramatic_context: Zosima's deathbed teaching, the novel's spiritual counterweight to Ivan's rebellion and the Grand Inquisitor.
  register: principle
  claim_type: normative
  polarity: prescriptive
  conditionality: contested
  life_domains: [self, family, adversity, friendship]
  life_stages: [adult]
  attribution_confidence: verified
  endorsement: endorsed
  copyright_flag: public_domain
  addresses_dilemma: revenge_vs_forgiveness
  tension_note: Dostoevsky deliberately sets it against Ivan's powerful counter-argument (the suffering of children) and even has the murderer Smerdyakov twist "all are guilty" into evasion of responsibility — the novel endorses Zosima but refuses to make the case easy. P&V (©1990) is in_copyright; cite Garnett.

- id: insight.dostoevsky.active_love
  canonical_claim: Real love is laborious and unglamorous, the opposite of the dramatic self-sacrifice we fantasise about.
  original_quote: "Active love is a harsh and fearful thing compared with love in dreams. Love in dreams thirsts for immediate action ... whereas active love is labour and perseverance."
  citation: { author: Fyodor Dostoevsky, work: The Brothers Karamazov, location: "Book II (Zosima to Madame Khokhlakova)", edition: "Garnett (1912)", date: "1880" }
  speaker: Elder Zosima
  dramatic_context: Counselling a woman who confesses she dreams of loving humanity but couldn't bear ingratitude.
  register: principle
  claim_type: prudential
  polarity: prescriptive
  conditionality: universal-ish
  life_domains: [love, friendship, work, family]
  life_stages: [adult]
  attribution_confidence: verified
  endorsement: endorsed
  copyright_flag: public_domain
  addresses_dilemma: passion_vs_duty
  tension_note: The wording shown follows P&V phrasing; for PD citation use Garnett. The teaching is endorsed but its difficulty is dramatised through characters who fail at it. Related Zosima line (also PD via Garnett): "The man who lies to himself ... cannot distinguish the truth within him, or around him, and so loses all respect for himself and for others."
```

**Flagged for deeper later pass (Dostoevsky):** the Grand Inquisitor chapter in full (freedom vs. security/bread fork) and *Notes from Underground* (free will vs. determinism, "2+2=5") — named here, not coded as verified units this pass.

### GEORGE ELIOT — MIDDLEMARCH

```yaml
- id: insight.eliot.unhistoric_acts
  canonical_claim: The growing good of the world depends largely on unrecorded, ordinary, faithful lives.
  original_quote: "for the growing good of the world is partly dependent on unhistoric acts; and that things are not so ill with you and me as they might have been, is half owing to the number who lived faithfully a hidden life, and rest in unvisited tombs."
  citation: { author: George Eliot, work: Middlemarch, location: "Finale (final sentence)", edition: "First edition 1871–72 / Standard Ebooks", date: "1871–72" }
  speaker: Narrator (on Dorothea Brooke)
  dramatic_context: Closing the novel's account of Dorothea, whose idealism never found an "epic" outlet.
  register: principle
  claim_type: normative
  polarity: prescriptive
  conditionality: universal-ish
  life_domains: [work, self, adversity, family]
  life_stages: [adult]
  attribution_confidence: verified
  endorsement: endorsed
  copyright_flag: public_domain
  addresses_dilemma: ambition_vs_love
  tension_note: The "incalculably diffusive" good is real, but the melancholy final phrase "unvisited tombs" and the Finale's earlier lament that Dorothea's "full nature ... spent itself in channels which had no great name on the earth" keep it genuinely ambiguous: consolation, or quiet protest at a society that wasted her? Eliot preserves both.
```

### JANE AUSTEN

```yaml
- id: insight.austen.truth_universally_acknowledged
  canonical_claim: Society treats a wealthy single man as obliged to marry — a "truth" that actually exposes the economic pressure on women.
  original_quote: "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
  citation: { author: Jane Austen, work: Pride and Prejudice, location: "Ch. 1 (opening)", edition: "First edition 1813 / Standard Ebooks", date: "1813" }
  speaker: Narrator (free indirect, ventriloquising Mrs. Bennet's worldview)
  dramatic_context: Opening sentence; the next paragraph immediately narrows the "universal truth" to the property-hunting of "surrounding families."
  register: aphorism
  claim_type: observational
  polarity: descriptive
  conditionality: contested
  life_domains: [love, money, family, marriage]
  life_stages: [youth, adult]
  attribution_confidence: verified
  endorsement: undercut
  copyright_flag: public_domain
  addresses_dilemma: ambition_vs_love
  tension_note: Possibly the single most celebrated piece of irony in the English novel — it means close to the OPPOSITE of its literal claim (the eighteenth-century "It is a truth universally acknowledged" was a formula for opening a philosophical premise, à la Hume/Berkeley). A flagship endorsement=undercut case: the narrator states it; the book dismantles it. Pairs with Elizabeth's "till this moment I never knew myself" (Ch. 36) for the self-deception fork; Emma and Persuasion flagged for a deeper later pass.
```

### VICTOR HUGO — LES MISÉRABLES

```yaml
- id: insight.hugo.face_of_god_MISATTRIB
  canonical_claim: To love another person is to encounter the divine.
  original_quote: "And remember, the truth that once was spoken: / To love another person is to see the face of God."
  citation: { author: "Herbert Kretzmer (English lyric), after Boublil–Schönberg; replacing Boublil & Natel's French 'Qui aime son prochain est plus près de Dieu sur la terre'", work: "Les Misérables (musical), Finale", location: "Valjean's death / finale", edition: "1985 English-language production", date: "1985" }
  speaker: Fantine and Éponine (spirits), to the dying Valjean
  dramatic_context: The musical's closing couplet.
  register: aphorism
  claim_type: metaphysical
  polarity: prescriptive
  conditionality: contested
  life_domains: [love, death, grief]
  life_stages: [old age, adult]
  attribution_confidence: apocryphal
  endorsement: endorsed
  copyright_flag: in_copyright_work
  addresses_dilemma: revenge_vs_forgiveness
  tension_note: CRITICAL PROVENANCE FLAG — this is the musical's lyric, NOT a line in Hugo's 1862 novel, though it is endlessly quoted as "Victor Hugo." It compresses a genuinely Hugolian theme (grace; the Bishop's mercy that remakes Valjean) but the words are in copyright and not Hugo's. For a genuine Hugo line on the same fork, cite the Bishop-of-Digne mercy episode in a PD translation (Hapgood 1887). Flag Denny (1976) and Rose (2008) as in_copyright_translation.
```

### THE POETS

```yaml
- id: insight.keats.beauty_is_truth
  canonical_claim: Beauty and truth are ultimately one, and that is all mortals need to know.
  original_quote: "'Beauty is truth, truth beauty,'—that is all / Ye know on earth, and all ye need to know."
  citation: { author: John Keats, work: Ode on a Grecian Urn, location: "final lines (stanza 5)", edition: "Annals of the Fine Arts 1820 / Wikisource", date: "1819" }
  speaker: The urn (a personified object), addressing humankind — NOT Keats in propria persona
  dramatic_context: The poem's close, after the speaker has questioned the silent, eternal figures on the urn ("Cold Pastoral!").
  register: aphorism
  claim_type: metaphysical
  polarity: descriptive
  conditionality: contested
  life_domains: [self, grief, death]
  life_stages: [youth, adult]
  attribution_confidence: verified
  endorsement: ambiguous
  copyright_flag: public_domain
  addresses_dilemma: self_deception_vs_truth
  tension_note: Critics since Robert Bridges and T. S. Eliot have debated whether these glib lines are the urn's limited consolation or Keats's own creed. Keats's letters ("What the imagination seizes as Beauty must be truth") [The Poetry Foundation](https://www.poetryfoundation.org/articles/145240/john-keats-ode-on-a-grecian-urn) lean toward endorsement, but the dramatic frame (quotation marks; the urn as speaker; "ye" addressed to mortals) leaves it ambiguous — a textbook character-vs-author case. Note: surviving 1820 printings differ in where the quotation marks fall, [eNotes](https://www.enotes.com/topics/ode-grecian-urn/questions/truth-and-beauty-in-keats-s-ode-on-a-grecian-urn-3138065) which itself drives the interpretive dispute.

- id: insight.tennyson.loved_and_lost
  canonical_claim: It is better to have loved and lost than never to have loved at all.
  original_quote: "I hold it true, whate'er befall; / I feel it, when I sorrow most; / 'Tis better to have loved and lost / Than never to have loved at all."
  citation: { author: Alfred, Lord Tennyson, work: In Memoriam A.H.H., location: "Canto XXVII", edition: "1850 / Wikisource", date: "1850" }
  speaker: The grieving poetic "I" (mourning Arthur Henry Hallam)
  dramatic_context: Early in the long elegy, in the first year of grief.
  register: aphorism
  claim_type: prudential
  polarity: prescriptive
  conditionality: contested
  life_domains: [love, grief, friendship, death]
  life_stages: [adult, youth]
  attribution_confidence: verified
  endorsement: endorsed
  copyright_flag: public_domain
  addresses_dilemma: passion_vs_duty
  tension_note: Situated at a specific stage of mourning, not as detached doctrine; a counter-proverb exists ("what you never had, you never miss"). [Interesting Literature](https://interestingliterature.com/2021/01/better-loved-lost-than-never-loved-origin-meaning/) Preserve the dissent.

- id: insight.dickinson.hope_feathers
  canonical_claim: Hope is an indestructible, undemanding presence within the self that sustains us in hardship.
  original_quote: "\"Hope\" is the thing with feathers - / That perches in the soul - / And sings the tune without the words - / And never stops - at all -"
  citation: { author: Emily Dickinson, work: "\"Hope\" is the thing with feathers", location: "Fr314 / J254", edition: "poem text PD; cite Franklin/Johnson numbering only for reference", date: "c.1861" }
  speaker: The poetic "I"
  dramatic_context: A "definition poem" metaphorising an abstract noun as a bird.
  register: metaphor
  claim_type: observational
  polarity: descriptive
  conditionality: universal-ish
  life_domains: [adversity, self, grief]
  life_stages: [adult, youth]
  attribution_confidence: verified
  endorsement: endorsed
  copyright_flag: public_domain
  addresses_dilemma: self_deception_vs_truth
  tension_note: Poem text is PD; the 1955 Johnson and 1998 Franklin EDITIONS' apparatus are ©President & Fellows of Harvard College — cite the poem, not the edited volume.

- id: insight.whitman.contain_multitudes
  canonical_claim: A self may legitimately hold contradictions because it is large enough to contain many truths.
  original_quote: "Do I contradict myself? / Very well then I contradict myself, / (I am large, I contain multitudes.)" [Princeton Writes](https://pwrites.princeton.edu/news/a-poem-for-you-song-of-myself-51/)
  citation: { author: Walt Whitman, work: "Song of Myself (Leaves of Grass)", location: "Section 51", edition: "1891–92 'deathbed' edition / Whitman Archive / poets.org", date: "1891–92 (first 1855)" }
  speaker: The expansive poetic "I"
  dramatic_context: Penultimate section (51 of 52), as the speaker prepares to depart ("I stay only a minute longer"). [WhitmanWeb](https://whitmanweb.iwp.uiowa.edu/song-myself/languages/english/section-51)
  register: aphorism
  claim_type: observational
  polarity: descriptive
  conditionality: contested
  life_domains: [self, adversity]
  life_stages: [adult]
  attribution_confidence: verified
  endorsement: endorsed
  copyright_flag: public_domain
  addresses_dilemma: self_deception_vs_truth
  tension_note: Punctuation shown is the FINAL 1891–92 form; the 1855 first edition uses ellipsis dashes and no parentheses ("Very well then . . . . I contradict myself; / I am large . . . . I contain multitudes.") [Shmoop](https://www.shmoop.com/study-guides/song-of-myself/section-51-summary.html) — cite the edition you mean.
```

**Flagged for deeper later pass (poets):** Wordsworth's *Prelude* and the "spots of time" (not separately verified to a primary edition this pass); Shakespeare's Sonnets; Whitman beyond Section 51.

### GOETHE — FAUST

```yaml
- id: insight.goethe.faust_wager
  canonical_claim: To wish any single moment to linger forever is to forfeit one's striving self.
  original_quote_de: "Werd' ich zum Augenblicke sagen: / Verweile doch! du bist so schön!" [the Book of Pain](https://bookofpain.wordpress.com/2018/03/23/linger-a-while-thou-art-so-fair/)
  original_quote_en: "When thus I hail the Moment flying: / 'Ah, still delay—thou art so fair!' / Then bind me in thy bonds undying, / My final ruin then declare!" [Owl Eyes](https://www.owleyes.org/text/faust/read/faust-part-one-scene-iv-the-study-the-compact)
  citation: { author: J. W. von Goethe, work: Faust, Part One, location: "'Studierzimmer' (The Study / Compact scene), vv. ~1699–1702", edition: "Bayard Taylor (1870), PD; Anna Swanwick (1850), PD", date: "1808 (Part One)" }
  speaker: Faust, to Mephistopheles
  dramatic_context: Faust sets the terms of his wager/pact: he loses only if a moment so satisfies him that he wants it to stay.
  register: argument
  claim_type: metaphysical
  polarity: cautionary
  conditionality: contested
  life_domains: [ambition, self, death]
  life_stages: [adult, old age]
  attribution_confidence: verified
  endorsement: complicated
  copyright_flag: public_domain
  addresses_dilemma: ambition_vs_love
  tension_note: Faust is ultimately SAVED, not damned, in Part Two — so the play complicates the wager's apparent logic. Use Bayard Taylor (1870) or Swanwick (1850) for PD; flag Kaufmann (1961), Arndt (1976), Luke (1987) as in_copyright_translation. Cross-references separate Nietzsche prompt.
```

### FOLK & PROVERBIAL WISDOM

```yaml
- id: insight.proverb.look_before_leap_vs_hesitates
  canonical_claim: Prudential proverbs travel in contradicting pairs, so proverb-wisdom is conditional, not absolute.
  original_quote: "Look before you leap." / counter: "He who hesitates is lost."
  citation: { author: communal, work: English proverb tradition, location: "n/a", edition: "n/a", date: "attested 16th–18th c." }
  speaker: communal/anonymous
  dramatic_context: n/a
  register: aphorism
  claim_type: prudential
  polarity: cautionary
  conditionality: contested
  life_domains: [adversity, work, self]
  life_stages: [adult, youth]
  attribution_confidence: probable
  endorsement: ambiguous
  copyright_flag: public_domain
  addresses_dilemma: passion_vs_duty
  tension_note: Proverbs are communal and often unattributable; "originator" confidence is dubious/apocryphal, "attested in tradition" is probable. Their self-contradiction is the point: they encode tendencies, not destinies — a model for the project's conditional-wisdom principle.
```

---

## (c) CONSOLIDATED DILEMMAS / FORKS

1. **Passion vs. Duty** — *Anna Karenina* (passion → ruin, but the dutiful Karenin is no moral victor); Austen's heroines (Marianne's sensibility vs. Elinor's sense); Tennyson (loving-and-grieving vs. safe numbness). *Both costs:* repression deadens; unchecked passion destroys.
2. **Revenge vs. Forgiveness** — the *Oresteia*'s vengeance cycle; Zosima's "guilty for all"; Hugo's Valjean/Javert. *Both costs:* vengeance perpetuates harm; forgiveness can look like injustice (Javert cannot survive being spared).
3. **Ambition vs. Love** — *Macbeth*; *Faust*; Eliot's Dorothea and Lydgate; the "unhistoric acts" finale. *Both costs:* ambition can hollow the soul ("signifying nothing"); renouncing it can waste a "full nature."
4. **Self-deception vs. Truth** — *Oedipus*; the Grand Inquisitor; Dostoevsky's "the man who lies to himself"; Austen's Emma and Elizabeth ("till this moment I never knew myself"). *Both costs:* truth devastates (Oedipus); comforting lies corrode the self.
5. **Freedom vs. Fate** — "ripeness is all"; *Oedipus*; the *Bacchae*'s closing chorus; *pathei mathos*. *Both costs:* fatalism breeds passivity; the illusion of total control invites hubris.
6. **Pride vs. Humility** — *Oedipus*; the *Bacchae* (Pentheus); "count no man happy"; *Pride and Prejudice*. *Both costs:* pride blinds; excessive self-abnegation (Dorothea) can squander gifts.

---

## (d) VIRTUES AND DANGERS SHOWN (through consequence, not sermon)

- **Demonstrated virtue — humility before fortune:** Oedipus's fall shows (does not preach) that confidence in one's own cleverness invites catastrophe.
- **Demonstrated virtue — active, unglamorous love:** Tolstoy's shoemaker [SuperSummary](https://www.supersummary.com/what-men-live-by/summary/) and Hugo's Bishop change lives through small concrete mercies, not grand gestures.
- **Demonstrated danger — ambition severed from love:** Macbeth and (provisionally) Faust dramatise ambition curdling into meaninglessness.
- **Demonstrated danger — self-deception:** Dostoevsky's Fyodor Pavlovich and the self-lying narrator of *Notes from Underground* rot from within.
- **Demonstrated danger — the proud certainty of being right:** Austen's Elizabeth and Emma must be humiliated by events before they see clearly; the lesson arrives through plot, not authorial lecture.
- **Caution about "shown vs. preached":** Tolstoy's late parables (*What Men Live By*) and Zosima's discourses lean toward *telling*; *Anna Karenina*, *Middlemarch*, the tragedies, and Austen *show* — weight these higher for "demonstrated" wisdom.

---

## (e) CANDIDATE CONVERGENCES with philosophical traditions (CANDIDATES for robustness — NOT proof)

- **"Ripeness is all" / "count no man happy" / *pathei mathos* ↔ Stoic acceptance (*amor fati*, *premeditatio malorum*).** Candidate convergence: accept what is not in our control. *Caveat:* the tragedies are far bleaker than Stoic consolation; convergence is partial.
- **Zosima's "guilty for all" + active love ↔ Christian *agape* and Buddhist compassion/interdependence.** Candidate convergence on universal responsibility and non-judgment. *Caveat:* Dostoevsky frames it as faith answering Ivan's atheist rebellion, not a neutral ethics.
- **Eliot's "unhistoric acts" ↔ ethics of small duties / care ethics / Confucian everyday virtue.** Candidate convergence: the moral weight of ordinary fidelity.
- **Faust's wager and Whitman's "multitudes" ↔ Nietzschean striving/self-overcoming and eternal recurrence.** Candidate convergence on restless becoming. *Caveat:* cross-reference the separate Nietzsche prompt; do not collapse the two.
- **Euripides' "cleverness is not wisdom" ↔ Socratic "I know that I know nothing" and the wisdom/cleverness distinction.** Candidate convergence on intellectual humility.
- **Proverb pairs (look before you leap / he who hesitates) ↔ Aristotelian *phronesis* (practical wisdom as context-sensitive judgment).** Candidate convergence: rules underdetermine action; judgment fills the gap.

---

## (f) MISATTRIBUTION WATCHLIST

| Quotation | Commonly credited to | Actual status / true source |
|---|---|---|
| "Whatever you can do or dream you can, begin it. Boldness has genius, power and magic in it." | Goethe (*Faust*) | **Loose paraphrase by John Anster** in his 1835 "very free" translation of *Faust* (rendering the German "Prelude at the Theatre," lines ~214–230). Anster's text reads "What you can do, or dream you can, begin it, / Boldness has genius, power, and magic in it." [Linguistlist](https://listserv.linguistlist.org/pipermail/ads-l/2011-October/113899.html) Quote Investigator concludes Anster "should be credited with its authorship." [Quote Investigator](https://quoteinvestigator.com/2016/02/09/boldness/) The longer "Until one is committed…" preamble is by **W. H. Murray**, *The Scottish Himalayan Expedition* (1951). NOT Goethe's words. — `apocryphal` |
| "The two most important days in your life are the day you are born and the day you find out why." | Mark Twain | **Not Twain.** No source in the Twain corpus (Center for Mark Twain Studies; Barry Popik; Quote Investigator). QI's earliest strong match is a **1970 pamphlet from The Riverside Church, New York City**, popularized by Dr. Ernest T. Campbell; later echoed in self-help (Taylor Hartman, 1999). The Center calls it "currently the most viral piece of Twain apocrypha." [Center for Mark Twain Studies](https://marktwainstudies.com/the-apocryphal-twain/the-apocryphal-twain-the-two-most-important-days-of-your-life/) — `apocryphal` |
| "Twenty years from now you will be more disappointed by the things you didn't do… Sail away from the safe harbor." | Mark Twain | **Not Twain.** Per the Center for Mark Twain Studies, it "likely originated with H. Jackson Brown's 1990 book, *P.S. I Love You*, in which Brown attributes the quote to his mother, Sarah Frances Brown"; spread by a 1999 Peace Corps recruitment ad. — `apocryphal` |
| "If you're going through hell, keep going." | Winston Churchill | **Not Churchill** (International Churchill Society; Quote Investigator). [Yahoo!](https://www.yahoo.com/news/fact-check-winston-churchill-never-184800254.html) Not literary, but flags the "Churchillian Drift" pattern. Earliest variants ~1990 (Douglas Bloch, "If You're Going Through Hell, Don't Stop," *The Oregonian*). [The Saturday Evening Post](https://www.saturdayeveningpost.com/did-winston-churchill-really-say-that-answers/) — `apocryphal` |
| "Expectation is the root of all heartache." | Shakespeare | **Not Shakespeare** (Folger Shakespeare Library; absent from the Quartos Archive and collected poetry). [Check Your Fact](https://checkyourfact.com/2019/09/25/fact-check-shakespeare-expectation-root-heartache/) Possibly a paraphrase of a Buddhist idea. As Twain scholar Sharon McCoy notes of this whole pattern, famous authors are simply "a magnet for quotations." — `apocryphal` |
| "Oh what a tangled web we weave, when first we practise to deceive." | Shakespeare | **Sir Walter Scott**, *Marmion* (1808). — `verified (correct source)` |
| "To love another person is to see the face of God." | Victor Hugo (*Les Misérables*) | **Herbert Kretzmer's 1985 musical lyric** (full couplet: "And remember, the truth that once was spoken: / To love another person is to see the face of God"), [Goodreads](https://www.goodreads.com/quotes/49720-to-love-another-person-is-to-see-the-face-of) [LifeHack](https://www.lifehack.org/294882/50-timeless-quotes-from-les-miserables) replacing Boublil & Natel's French "Qui aime son prochain est plus près de Dieu sur la terre." NOT in Hugo's 1862 novel. [Answers](https://www.answers.com/religious-literature/Where_in_Victor_Hugo's_Les_Miserables_is_the_quote_To_love_another_person_is_to_see_the_face_of_God) — `apocryphal` for Hugo; `in_copyright_work` for the musical. |
| "Ripeness is all." | Often misattributed to King Lear himself | **Spoken by Edgar**, not Lear (*King Lear* 5.2). Quote real; speaker commonly misstated. — `verified` |
| "Tomorrow, and tomorrow, and tomorrow…" | Shakespeare (*Macbeth*) | **Genuine** — *Macbeth* 5.5 (Macbeth). — `verified` |
| "'Tis better to have loved and lost…" | Shakespeare / general | **Tennyson**, *In Memoriam* Canto XXVII. — `verified` |

---

## Recommendations

1. **Ingest the verified core now** (the units above), each with its `endorsement` and `attribution_confidence` tags intact. Treat the endorsement = undercut/complicated/ambiguous units (Austen's opening, Keats's urn, Macbeth, "ripeness is all," *Anna Karenina*'s opening) as the project's flagship demonstrations of the character-vs-author principle.
2. **Quarantine the misattribution watchlist** as a distinct node type ("apocryphal/contested attribution") so the book, site, and game never present these as authentic — and so the *Les Misérables* and Anster/Goethe cases become teachable examples of how false wisdom-attributions spread.
3. **Edition discipline:** default to the PD editions in the Source Inventory; wherever a modern translation's phrasing is more familiar (P&V Dostoevsky/Tolstoy; modern Greek tragedy), store BOTH — the PD text for publication and the modern only as a flagged `in_copyright_translation` reference.
4. **Flag for deeper later passes** (richest unmined veins): Shakespeare's Sonnets and the problem plays; the Grand Inquisitor chapter in full (freedom vs. security fork); *Notes from Underground* (free will vs. determinism); Austen's *Persuasion* and *Emma*; Wordsworth's *Prelude* and the "spots of time"; Whitman beyond Section 51; the full *Oresteia* justice-cycle; Goethe's *Wilhelm Meister*.
5. **Benchmarks that would change the coding:** if a primary-edition check contradicts a quote's wording → downgrade `attribution_confidence` to `dubious` and quarantine; if scholarly consensus shifts on an endorsement reading (e.g., new evidence that Keats meant the urn's words straight) → revise the `endorsement` field rather than averaging the dissent away.

## Caveats

- This is a **representative first pass**, not exhaustive; ~1–4 strong units per author were extracted, prioritising the great forks.
- Several famous "wisdom" lines are spoken by characters the narrative complicates; do not let aphoristic polish override dramatic context.
- **Translation wording for the Greek tragedians and the *Faust* wager varies materially by translator**; the canonical *sense* is stable but exact English wording is edition-dependent — always store the translator. Where I show a modern rendering for sense (e.g., "count no man happy"), the PD citation differs in wording (Storr 1912).
- Convergences are labelled **candidates for robustness, explicitly not proof**; recurrence across traditions increases confidence in a tendency, never establishes a truth.
- I could not separately verify Wordsworth-specific and full Grand-Inquisitor / *Crime and Punishment* quotations against primary editions in this pass; they are named for a future pass rather than coded as verified units here. The *Notes from Underground* "lies to himself" line and Zosima cross-references should be re-verified against the Garnett PD text before publication.