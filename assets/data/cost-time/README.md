# Cost and time dataset, run claude-v43-1--C4-field

Target length: under 1,100 words. Built by the handler on 29 Oct 2026 for the project website. All times are UTC. All money is USD. Token counts are integers. Every CSV has one header row.

## Headline (`00_headline.json`)

- The run went from 6 Oct 12:15 to 28 Oct 00:38: 516.4 h, or 21.5 days, over 314 Claude legs.
- The Claude analyst worked for 247.9 h.
- All work used 51.82 billion billable tokens. 96.7% of them were cached input.
- At standard API list prices that is $20,497: Anthropic $6,721, OpenAI Codex $13,708, DeepSeek $68.
- Only the DeepSeek $68 is a known cash charge. Claude and Codex ran on subscriptions.
- At DeepSeek V4.1 Flash prices the same tokens would cost $530 off-peak, $1,060 at peak, or $2,562 through OpenRouter.

## Files

| File | Grain | Rows |
|---|---|---|
| `01_overview_by_workstream.csv` | one workstream; a TOTAL row last | 19 |
| `02_claude_legs.csv` | one Claude leg: time, waits, tokens, cost | 314 |
| `03_stages.csv` | one stage (A1 to E2), summed from 02 | 18 |
| `04_waits.csv` | one wait of 30 min or more between legs, or 1 h or more inside a leg | 51 |
| `05_time_budget.csv` | wall clock split by cause, plus estimates without delays | 23 |
| `06_deepseek_dispatches.csv` | one DeepSeek dispatch | 6 |
| `07_codex_705_by_community_and_pass.csv` | one community and one pass (coding, D2, D3) | 2,115 |
| `08_codex_field_sessions.csv` | one Field (Codex) session, pilots and production | 457 |
| `09_codex_d2_d3_timing.csv` | one community and pass: first and last response, turn hours | 1,410 |
| `dataset.json` | every table above, keyed by file name | |

## Column meanings

- **billable_tokens**: uncached input + cached input + cache write + output. Reasoning tokens are already inside output and are never added twice.
- **uncached_input**: input billed at the full rate.
- **cached_input**: input read from cache, billed at the low rate.
- **cache_write**: Claude only. Codex and DeepSeek record none.
- **api_cost_usd**: tokens times the list price in the table below. It is a valuation, not an invoice.
- **deepseek_peak_usd, deepseek_offpeak_usd, deepseek_openrouter_usd**: the same tokens repriced at DeepSeek V4.1 Flash rates. Cache writes count as cache misses.
- **actual_cash_usd**: filled only where a charge was recorded (DeepSeek).
- **leg_h**: from the leg's first transcript entry to its close.
- **active_h**: the sum of intervals of 5 min or less between transcript entries, so time the analyst was working.
- **idle_in_leg_h**: leg_h minus active_h.
- **wait_before_h**: from the previous leg's close to this leg's start.
- **from_utc, to_utc** in `04_waits.csv`: for a wait between legs, the previous close and the next start; for a wait inside a leg, the leg's start and close, since the idle time is spread through the leg.
- **cause**: why a wait happened.
- **basis**: how the cause is known.
  - `diary` means the handler's diary records it.
  - `inferred` means it is read from the surrounding events, with no line naming it.
  - `rule` means it was assigned by size.
  - `none` means nothing records the wait.

## Wait causes

| Cause | Meaning |
|---|---|
| J | waiting for J: a ruling, a go-ahead, a git push, an interview, or J away |
| usage limit | Claude subscription limit (weekly or session) |
| fleet | DeepSeek dispatch, run by J in the Mac Terminal, and its fixes |
| Codex coders | the 705 Codex labelers at D2, or their re-check at D3 |
| Codex Field | waiting for the Field (Codex) reading at C4 and C5 |
| handler (late check), handler (publishing) | the handler noticed a close late, or a publish step failed |
| disk, network, computer off | infrastructure stops |
| routine handover | gaps under 30 min between a close and the next start |
| short in-leg pauses | pauses over 5 min inside a leg (long tool runs, small waits), when the leg's idle time is under 1 h |
| not recorded | no line explains it |

The time budget in `05_time_budget.csv` adds up to the wall clock exactly. The three estimates without delays are:
1. **Active time only:** 247.9 h, 10.3 days. This is the lower bound.
2. **Active time plus routine handovers and short pauses:** 301.3 h, 12.6 days.
3. **The second estimate plus the fleet and Codex waits as they ran:** 361.4 h, 15.1 days. This one counts the C3 to C4 wait, which was shared between J and the Field.

## Prices used (USD per million tokens)

| Model | Uncached input | Cached input | Cache write | Output |
|---|---|---|---|---|
| Claude Opus 5.5 | 4 | 0.20 | 8 (1-hour) | 20 |
| GPT-5.6 Sol (705 coding) | 4 | 0.40 | 5 | 20 |
| GPT-6.1 Sol (D2, D3, Field) | 2 | 0.10 | 2.50 | 10 |
| DeepSeek V4.1 Flash, off-peak | 0.15 | 0.003 | | 0.60 |
| DeepSeek V4.1 Flash, peak | 0.30 | 0.006 | | 1.20 |
| DeepSeek via OpenRouter, as paid in this run | 0.24 | 0.041 | | 0.59 |

Pricing details:
- **Long-context surcharge:** D2 and D3 carry it on 6,964 responses with input over 272,000 tokens (twice the input rates, 1.5 times the output rate). The 705-community coding is priced at short-context rates, because its receipts give no per-request context. Pricing all of it at long-context rates would add $9,420 (`all_long_context_sensitivity_usd` in file 07).
- **Field:** valued at GPT-6.1 Sol rates with no surcharge.
- **DeepSeek list prices:** taken from two third-party reports of DeepSeek's page (September 2026), not checked on DeepSeek's own site.
- **OpenRouter rates:** fitted to the 1,391 V4.1 calls in the 13 Oct OpenRouter export. They are an estimate.

## How the Claude tokens are counted

- One API call appears as several transcript rows that repeat the same usage, so each message id is counted once, in the first leg that holds it.
- Legs A1a to D6a-02 come from the handler's per-leg file. The 34 later legs come from their transcripts, counting only new message ids timestamped at or after the leg's start.
- All cache writes are priced at the 1-hour rate, because every write in the later legs was 1-hour.

## Sources

- Claude: leg transcripts in `CONTROL/snapshots/<leg>/transcript.jsonl`; the handler's per-leg file; `handover-events.log` for closes.
- Codex: the bundles `token-cost-report-20261028` (705 communities) and `field-token-cost-through-model-interviews-20261028T185247Z` (Field), built by Codex from its receipts and journals.
- DeepSeek: `out/_fleet_raw/<dispatch>/log.jsonl` and the OpenRouter export `openrouter_activity_2026-10-13.csv`, which is used for B2.
- Wait causes: `handler/memory/diary.md` and `DECISIONS.tsv`.

## Known gaps and corrections

- **Correction to the earlier total.** It was $20,443, and it left out legs D4a-05 to D4a-08 and most of D6b. The Claude line rises by 192 M tokens and $53, giving $20,497.
- **Not counted:**
  - this handler session;
  - Claude's side of the Field interviews;
  - the Codex gpt-6-astra arm at B4 (9.6 M tokens, no cost recorded);
  - 705-community runs other than the selected medium runs;
  - Field work after C5b.
- **Claude readers at C2 and C5:** the CLI route reported almost no input tokens. Their cost ($1.90, as logged) is right, but their tokens are understated.
- **E1 dispatch:** shows 0 valid returns, because every reader added an end-marker line. E1d validated the returns from the raw files.
- **Field sessions (file 08):** each session row holds the ledger's highest count. The lead's row runs past the C4 interview and includes an inherited pilot baseline. Use file 01 for Field totals.
- **Missing timestamps:** the 705-community coding (September) and the Field have no start and end times in these sources, so their durations are not given. D2 and D3 have them in file 09.
- **Wait causes:** 7 of the 51 classified waits are inferred, and 7 carry no record. Their hours are listed so they can be shown apart.
