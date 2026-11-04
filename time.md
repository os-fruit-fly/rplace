# Time and costs

How long each part of the study took and what it consumed, where it was recorded. All dates are 2026 and all times UTC; money is in US dollars. From the first recorded community coding run on 18 August to the last aggregator session on 28 October is 71 days. The figures come from the cost and time dataset that the run's handler, the conversation that ran the aggregator's stages, built on 29 October, built from the session transcripts, the Codex receipts and the OpenRouter export, unless a line says otherwise. The records are in the research repository.

| | |
|---|---|
| The aggregator's run | 516.4 hours, 21.5 days, 6 Oct 12:15 to 28 Oct 00:38, in 314 sessions |
| The aggregator working | 247.9 hours, 10.3 days |
| Tokens, all work | 51.82 billion, 96.7% of them cached input |
| Value at list prices | $20,497: Anthropic $6,721, OpenAI Codex $13,708, DeepSeek $68 |
| Paid in cash | $68, to DeepSeek through OpenRouter; Claude and Codex ran on subscriptions |

Table: The study in five numbers

The value at list prices is the tokens times each model's published price. It values the work; the cash paid is in the table's last line.

## By part of the work

| Part | Model | Tokens | Value at list prices |
|---|---|---:|---:|
| Community coding, 705 communities | gpt-5.6-sol | 15.74 billion | $10,256 |
| The return, D2 | gpt-6.1-sol | 3.24 billion | $859 |
| The re-check, D3 | gpt-6.1-sol | 3.53 billion | $1,200 |
| The aggregator, A1 to E2 | Claude Opus 5.5 | 21.45 billion | $6,719 |
| Independent readers, B2 to E1 | DeepSeek V4.1 Flash | 252.5 million | $68, paid |
| The r/place subreddit, read for C4 and its interviews | gpt-6.1-sol | 7.62 billion | $1,392 |
| Readers at C2 and C5 | Claude Opus 5.5 | not recorded in full | $2 |

Table: Tokens and their value, by part of the work

## Community coding

Earlier contracts coded 347 communities in 462 runs between 18 August and 5 September, mostly with Claude Opus 5; that coding was later redone. The final coding ran from 7 September to 4 October with gpt-5.6-sol: 5,097 agents at medium reasoning effort and 65 at extra high.

The selected medium runs of the 705 communities used 15.74 billion tokens: 5.21 billion for the community coders and 10.53 billion for the fleet coders, worth $10,256 at list prices. The coding handler's own count, 15.89 billion, also includes runs that were not selected. The September coding has no start and end times in these sources, so coding hours are not known. The earlier contracts' tokens were not recorded.

[How community coding works](how-coding-works.html) · [The population: community coding](results/population-coding.html)

## The return to the model

| Step | When | Communities | Tokens | Value at list prices |
|---|---|---|---:|---:|
| D1, tasks prepared | 15 Oct, 15:54 to 19:49 | 705 | in the aggregator's line | |
| D2, first return | first answer 15 Oct 21:41, last 16 Oct 08:01 | 705 | 3.24 billion | $859 |
| D3, re-check | first answer 21 Oct 15:19, last 22 Oct 19:10; 472 back by 21 Oct 19:26, when the account ran out of tokens | 705 | 3.53 billion | $1,200 |

Table: The return, step by step

Each community coder answered with gpt-6.1-sol at medium effort; its answers took a median of about six minutes at each pass. Two DeepSeek readers judged every community's fit: 25.6 million tokens at D2 and 27.3 million at D3.

[How community coding works: the return](how-coding-works.html#after-the-coding-the-return) · [The population: the return](results/population-return.html)

## The aggregator

Run claude-v43-1, with Claude Opus 5.5, from 6 October to 28 October. A session runs from its first transcript entry to its close; working hours count only intervals of five minutes or less between entries. Each API call is counted once.

| Stage | Start | End | Sessions | Hours in sessions | Working hours | Tokens, millions | Value at list prices |
|---|---|---|---:|---:|---:|---:|---:|
| [A1](stages/A1.html) | 6 Oct 12:15 | 7 Oct 13:02 | 57 | 18.9 | 17.8 | 3,506 | $954 |
| [B1](stages/B1.html) | 7 Oct 13:11 | 11 Oct 14:49 | 44 | 91.2 | 82.3 | 6,012 | $1,758 |
| [B2](stages/B2.html) | 11 Oct 14:57 | 12 Oct 14:09 | 12 | 7.5 | 3.2 | 339 | $110 |
| [B3](stages/B3.html) | 12 Oct 14:17 | 12 Oct 21:18 | 3 | 2.3 | 1.2 | 64 | $22 |
| [B4](stages/B4.html) | 12 Oct 21:19 | 13 Oct 17:47 | 12 | 18.5 | 17.5 | 1,087 | $461 |
| [C1](stages/C1.html) | 13 Oct 18:17 | 14 Oct 00:56 | 11 | 5.8 | 5.2 | 462 | $162 |
| [C2](stages/C2.html) | 14 Oct 06:04 | 14 Oct 13:49 | 7 | 5.5 | 5.0 | 762 | $245 |
| [C3](stages/C3.html) | 14 Oct 13:59 | 14 Oct 15:16 | 3 | 1.2 | 1.0 | 134 | $41 |
| [C4](stages/C4.html) | 14 Oct 22:43 | 14 Oct 23:03 | 1 | 0.3 | 0.3 | 32 | $12 |
| [C5](stages/C5.html) | 14 Oct 23:30 | 15 Oct 15:00 | 21 | 5.8 | 4.4 | 559 | $169 |
| [D1](stages/D1.html) | 15 Oct 15:54 | 15 Oct 19:49 | 1 | 3.9 | 0.7 | 47 | $14 |
| [D2](stages/D2.html) | 16 Oct 08:59 | 16 Oct 10:21 | 1 | 1.4 | 0.7 | 25 | $9 |
| [D3](stages/D3.html) | 16 Oct 11:00 | 24 Oct 10:54 | 59 | 171.6 | 81.6 | 6,003 | $2,032 |
| [D4](stages/D4.html) | 24 Oct 11:39 | 26 Oct 22:05 | 8 | 7.0 | 4.0 | 390 | $128 |
| [D5](stages/D5.html) | 25 Oct 21:01 | 27 Oct 03:20 | 42 | 23.4 | 16.0 | 1,288 | $370 |
| [D6](stages/D6.html) | 27 Oct 03:28 | 27 Oct 15:41 | 19 | 6.7 | 4.0 | 458 | $141 |
| [E1](stages/E1.html) | 27 Oct 18:22 | 27 Oct 23:52 | 11 | 4.5 | 2.7 | 233 | $77 |
| [E2](stages/E2.html) | 27 Oct 23:55 | 28 Oct 00:38 | 2 | 0.7 | 0.4 | 46 | $13 |
| **Total** | 6 Oct | 28 Oct | **314** | **376.2** | **247.9** | **21,447** | **$6,719** |

Table: The aggregator, stage by stage

D4 and D5 overlap on 26 October. The earlier count of 316 sessions came from the run's session log; this dataset counts 314.

[How the aggregator works](how-it-works.html)

### Where the 516.4 hours went

| | Hours | Days |
|---|---:|---:|
| The aggregator working | 247.9 | 10.3 |
| Usage limits of the Claude subscription | 93.9 | 3.9 |
| Waiting for us: rulings, go-aheads, pushes, interviews | 39.9 | 1.7 |
| Waiting for the Codex coders at D2 and D3 | 30.0 | 1.2 |
| Waiting for the independent readers | 14.0 | 0.6 |
| Waiting for both the readers and the Codex coders | 6.8 | 0.3 |
| Waiting for the r/place reading at C4 and C5 | 9.4 | 0.4 |
| Handovers under 30 minutes and short pauses | 53.4 | 2.2 |
| The handler: late checks and publishing | 7.0 | 0.3 |
| Disk, network and a computer off | 4.5 | 0.2 |
| Not recorded | 9.7 | 0.4 |
| **Wall clock** | **516.4** | **21.5** |

Table: Where the aggregator's hours went

Without delays the run would have taken between 10.3 days, counting working time only, and 15.1 days, counting also handovers, short pauses and the fleet and Codex waits as they ran.

## The r/place subreddit

r/place itself, read by a separate agent for C4, used 7.62 billion tokens in its pilots, its production coding, its lead and the interviews at C4 and C5, worth $1,392 at list prices. Work on r/place after C5 is not counted.

## Prices used

<details class="fold"><summary>Show the prices used and what is not counted</summary>

| Model | Uncached input | Cached input | Cache write | Output |
|---|---:|---:|---:|---:|
| Claude Opus 5.5 | 4,000 | 200 | 8,000 | 20,000 |
| gpt-5.6-sol, community coding | 4,000 | 400 | 5,000 | 20,000 |
| gpt-6.1-sol, D2, D3 and r/place | 2,000 | 100 | 2,500 | 10,000 |
| DeepSeek V4.1 Flash through OpenRouter, as paid | 240 | 41 | | 590 |

Table: Prices used, US dollars per billion tokens

 D2 and D3 carry the long-context surcharge on 6,964 responses with input over 272,000 tokens. The community coding is priced at short-context rates, since its receipts give no context size; at long-context rates it would cost $19,676 more.

Not counted: the handler's own sessions, Claude's side of the interviews at C4 and C5, a Codex arm at B4 (9.6 million tokens), community coding runs other than the selected medium runs, and work on r/place after C5.

</details>

## Accounts

The work ran on a Claude subscription (the aggregator and the earlier coding), a Codex account (the final coding, the returns and r/place) and OpenRouter (DeepSeek).

## Files

[The headline](assets/data/cost-time/00_headline.json) · [By part of the work](assets/data/cost-time/01_overview_by_workstream.csv) · [Every aggregator session](assets/data/cost-time/02_claude_legs.csv) · [By stage](assets/data/cost-time/03_stages.csv) · [Every wait of 30 minutes or more](assets/data/cost-time/04_waits.csv) · [The time budget](assets/data/cost-time/05_time_budget.csv) · [The DeepSeek dispatches](assets/data/cost-time/06_deepseek_dispatches.csv) · [Every community and pass](assets/data/cost-time/07_codex_705_by_community_and_pass.csv) · [D2 and D3 timing](assets/data/cost-time/09_codex_d2_d3_timing.csv) · [What each file holds](assets/data/cost-time/README.md)

## Sources

The handler's cost and time dataset of 29 October 2026: the session transcripts and the handler's per-session file; the Codex token and cost reports for the 705 communities and r/place; the DeepSeek dispatch logs and the OpenRouter export of 13 October. For the earlier coding: the coding handler's `STATUS.tsv`, `CODING-PROGRESS.json` and `PRIOR-RUNS.tsv`.
