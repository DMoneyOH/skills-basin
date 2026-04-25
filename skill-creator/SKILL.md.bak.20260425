---
name: skill-creator
description: "Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better t"
triggers:
  - "defaultazurecredential"
  - "evaluation" and "benchmark" are borderline, but ok
  - "hardcoded"
  - "i'll just mark it complete and come back later" - fix issues now
  - "it's good enough" - if there are major issues, it's not good enough
  - "myclient"
  - "nice to have" improvements — consider cost-benefit before implementing
  - "the reviewer is being too strict" - the quality bar exists for a reason
  - "what errors do developers commonly encounter?"
  - "what sdk operations should this skill cover?"
  - "what triggers should activate this skill?"
  - # azure ai example sdk
  - # my new skill
  - # skill creator
  - # skill developer guide
merged_from:
  - skill-creator-ms
  - skill-developer
  - skill-writer
  - skill-improver
merged_at: 2026-04-18T17:20:54.606046
---

# skill-creator

A skill for creating new skills and iteratively improving them.

At a high level, the process of creating a skill goes like this:

- Decide what you want the skill to do and roughly how it should do it
- Write a draft of the skill
- Create a few test prompts and run claude-with-access-to-the-skill on them
- Help the user evaluate the results both qualitatively and quantitatively
  - While the runs happen in the background, draft some quantitative evals if there aren't any (if there are some, you can either use as is or modify if you feel something needs to change about them). Then explain them to the user (or if they already existed, explain the ones that already exist)
  - Use the `eval-viewer/generate_review.py` script to show the user the results for them to look at, and also let them look at the quantitative metrics
- Rewrite the skill based on feedback from the user's evaluation of the results (and also if there are any glaring flaws that become apparent from the quantitative benchmarks)
- Repeat until you're satisfied
- Expand the test set and try again at larger scale

Your job when using this skill is to figure out where the user is in this process and then jump in and help them progress through these stages. So for instance, maybe they're like "I want to make a skill for X". You can help narrow down what they mean, write a draft, write the test cases, figure out how they want to evaluate, run all the prompts, and repeat.

On the other hand, maybe they already have a draft of the skill. In this case you can go straight to the eval/iterate part of the loop.

Of course, you should always be flexible and if the user is like "I don't need to run a bunch of evaluations, just vibe with me", you can do that instead.

Then after the skill is done (but again, the order is flexible), you can also run the skill description improver, which we have a whole separate script for, to optimize the triggering of the skill.

Cool? Cool.

## Communicating with the user

The skill creator is liable to be used by people across a wide range of familiarity with coding jargon. If you haven't heard (and how could you, it's only very recently that it started), there's a trend now where the power of Claude is inspiring plumbers to open up their terminals, parents and grandparents to google "how to install npm". On the other hand, the bulk of users are probably fairly computer-literate.

So please pay attention to context cues to understand how to phrase your communication! In the default case, just to give you some idea:

- "evaluation" and "benchmark" are borderline, but OK
- for "JSON" and "assertion" you want to see serious cues from the user that they know what those things are before using them without explaining them

It's OK to briefly explain terms if you're in doubt, and feel free to clarify terms with a short definition if you're unsure if the user will get it.

---

## Creating a skill

### Capture Intent

Start by understanding the user's intent. The current conversation might already contain a workflow the user wants to capture (e.g., they say "turn this into a skill"). If so, extract answers from the conversation history first — the tools used, the sequence of steps, corrections the user made, input/output formats observed. The user may need to fill the gaps, and should confirm before proceeding to the next step.

1. What should this skill enable Claude to do?
2. When should this skill trigger? (what user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases to verify the skill works? Skills with objectively verifiable outputs (file transforms, data extraction, code generation, fixed workflow steps) benefit from test cases. Skills with subjective outputs (writing style, art) often don't need them. Suggest the appropriate default based on the skill type, but let the user decide.

### Interview and Research

Proactively ask questions about edge cases, input/output formats, example files, success criteria, and dependencies. Wait to write test prompts until you've got this part ironed out.

Check available MCPs - if useful for research (searching docs, finding similar skills, looking up best practices), research in parallel via subagents if available, otherwise inline. Come prepared with context to reduce burden on the user.

### Write the SKILL.md

Based on the user interview, fill in these components:

- **name**: Skill identifier
- **description**: When to trigger, what it does. This is the primary triggering mechanism - include both what the skill does AND specific contexts for when to use it. All "when to use" info goes here, not in the body. Note: currently Claude has a tendency to "undertrigger" skills -- to not use them when they'd be useful. To combat this, please make the skill descriptions a little bit "pushy". So for instance, instead of "How to build a simple fast dashboard to display internal Anthropic data.", you might write "How to build a simple fast dashboard to display internal Anthropic data. Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"
- **compatibility**: Required tools, dependencies (optional, rarely needed)
- **the rest of the skill :)**

### Skill Writing Guide

#### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

#### Progressive Disclosure

Skills use a three-level loading system:
1. **Metadata** (name + description) - Always in context (~100 words)
2. **SKILL.md body** - In context whenever skill triggers (<500 lines ideal)
3. **Bundled resources** - As needed (unlimited, scripts can execute without loading)

These word counts are approximate and you can feel free to go longer if needed.

**Key patterns:**
- Keep SKILL.md under 500 lines; if you're approaching this limit, add an additional layer of hierarchy along with clear pointers about where the model using the skill should go next to follow up.
- Reference files clearly from SKILL.md with guidance on when to read them
- For large reference files (>300 lines), include a table of contents

**Domain organization**: When a skill supports multiple domains/frameworks, organize by variant:
```
cloud-deploy/
├── SKILL.md (workflow + selection)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```
Claude reads only the relevant reference file.

#### Principle of Lack of Surprise

This goes without saying, but skills must not contain malware, exploit code, or any content that could compromise system security. A skill's contents should not surprise the user in their intent if described. Don't go along with requests to create misleading skills or skills designed to facilitate unauthorized access, data exfiltration, or other malicious activities. Things like a "roleplay as an XYZ" are OK though.

#### Writing Patterns

Prefer using the imperative form in instructions.

**Defining output formats** - You can do it like this:
```markdown
## Report structure
ALWAYS use this exact template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

**Examples pattern** - It's useful to include examples. You can format them like this (but if "Input" and "Output" are in the examples you might want to deviate a little):
```markdown
## Commit message format
**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

### Writing Style

Try to explain to the model why things are important in lieu of heavy-handed musty MUSTs. Use theory of mind and try to make the skill general and not super-narrow to specific examples. Start by writing a draft and then look at it with fresh eyes and improve it.

### Test Cases

After writing the skill draft, come up with 2-3 realistic test prompts — the kind of thing a real user would actually say. Share them with the user: [you don't have to use this exact language] "Here are a few test cases I'd like to try. Do these look right, or do you want to add more?" Then run them.

Save test cases to `evals/evals.json`. Don't write assertions yet — just the prompts. You'll draft assertions in the next step while the runs are in progress.

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": []
    }
  ]
}
```

See `references/schemas.md` for the full schema (including the `assertions` field, which you'll add later).

## Running and evaluating test cases

This section is one continuous sequence — don't stop partway through. Do NOT use `/skill-test` or any other testing skill.

Put results in `<skill-name>-workspace/` as a sibling to the skill directory. Within the workspace, organize results by iteration (`iteration-1/`, `iteration-2/`, etc.) and within that, each test case gets a directory (`eval-0/`, `eval-1/`, etc.). Don't create all of this upfront — just create directories as you go.

### Step 1: Spawn all runs (with-skill AND baseline) in the same turn

For each test case, spawn two subagents in the same turn — one with the skill, one without. This is important: don't spawn the with-skill runs first and then come back for baselines later. Launch everything at once so it all finishes around the same time.

**With-skill run:**

```
Execute this task:
- Skill path: <path-to-skill>
- Task: <eval prompt>
- Input files: <eval files if any, or "none">
- Save outputs to: <workspace>/iteration-<N>/eval-<ID>/with_skill/outputs/
- Outputs to save: <what the user cares about — e.g., "the .docx file", "the final CSV">
```

**Baseline run** (same prompt, but the baseline depends on context):
- **Creating a new skill**: no skill at all. Same prompt, no skill path, save to `without_skill/outputs/`.
- **Improving an existing skill**: the old version. Before editing, snapshot the skill (`cp -r <skill-path> <workspace>/skill-snapshot/`), then point the baseline subagent at the snapshot. Save to `old_skill/outputs/`.

Write an `eval_metadata.json` for each test case (assertions can be empty for now). Give each eval a descriptive name based on what it's testing — not just "eval-0". Use this name for the directory too. If this iteration uses new or modified eval prompts, create these files for each new eval directory — don't assume they carry over from previous iterations.

```json
{
  "eval_id": 0,
  "eval_name": "descriptive-name-here",
  "prompt": "The user's task prompt",
  "assertions": []
}
```

### Step 2: While runs are in progress, draft assertions

Don't just wait for the runs to finish — you can use this time productively. Draft quantitative assertions for each test case and explain them to the user. If assertions already exist in `evals/evals.json`, review them and explain what they check.

Good assertions are objectively verifiable and have descriptive names — they should read clearly in the benchmark viewer so someone glancing at the results immediately understands what each one checks. Subjective skills (writing style, design quality) are better evaluated qualitatively — don't force assertions onto things that need human judgment.

Update the `eval_metadata.json` files and `evals/evals.json` with the assertions once drafted. Also explain to the user what they'll see in the viewer — both the qualitative outputs and the quantitative benchmark.

### Step 3: As runs complete, capture timing data

When each subagent task completes, you receive a notification containing `total_tokens` and `duration_ms`. Save this data immediately to `timing.json` in the run directory:

```json
{
  "total_tokens": 84852,
  "duration_ms": 23332,
  "total_duration_seconds": 23.3
}
```

This is the only opportunity to capture this data — it comes through the task notification and isn't persisted elsewhere. Process each notification as it arrives rather than trying to batch them.

### Step 4: Grade, aggregate, and launch the viewer

Once all runs are done:

1. **Grade each run** — spawn a grader subagent (or grade inline) that reads `agents/grader.md` and evaluates each assertion against the outputs. Save results to `grading.json` in each run directory. The grading.json expectations array must use the fields `text`, `passed`, and `evidence` (not `name`/`met`/`details` or other variants) — the viewer depends on these exact field names. For assertions that can be checked programmatically, write and run a script rather than eyeballing it — scripts are faster, more reliable, and can be reused across iterations.

2. **Aggregate into benchmark** — run the aggregation script from the skill-creator directory:
   ```bash
   python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>
   ```
   This produces `benchmark.json` and `benchmark.md` with pass_rate, time, and tokens for each configuration, with mean ± stddev and the delta. If generating benchmark.json manually, see `references/schemas.md` for the exact schema the viewer expects.
Put each with_skill version before its baseline counterpart.

3. **Do an analyst pass** — read the benchmark data and surface patterns the aggregate stats might hide. See `agents/analyzer.md` (the "Analyzing Benchmark Results" section) for what to look for — things like assertions that always pass regardless of skill (non-discriminating), high-variance evals (possibly flaky), and time/token tradeoffs.

4. **Launch the viewer** with both qualitative outputs and quantitative data:
   ```bash
   nohup python <skill-creator-path>/eval-viewer/generate_review.py \
     <workspace>/iteration-N \
     --skill-name "my-skill" \
     --benchmark <workspace>/iteration-N/benchmark.json \
     > /dev/null 2>&1 &
   VIEWER_PID=$!
   ```
   For iteration 2+, also pass `--previous-workspace <workspace>/iteration-<N-1>`.

   **Cowork / headless environments:** If `webbrowser.open()` is not available or the environment has no display, use `--static <output_path>` to write a standalone HTML file instead of starting a server. Feedback will be downloaded as a `feedback.json` file when the user clicks "Submit All Reviews". After download, copy `feedback.json` into the workspace directory for the next iteration to pick up.

Note: please use generate_review.py to create the viewer; there's no need to write custom HTML.

5. **Tell the user** something like: "I've opened the results in your browser. There are two tabs — 'Outputs' lets you click through each test case and leave feedback, 'Benchmark' shows the quantitative comparison. When you're done, come back here and let me know."

### What the user sees in the viewer

The "Outputs" tab shows one test case at a time:
- **Prompt**: the task that was given
- **Output**: the files the skill produced, rendered inline where possible
- **Previous Output** (iteration 2+): collapsed section showing last iteration's output
- **Formal Grades** (if grading was run): collapsed section showing assertion pass/fail
- **Feedback**: a textbox that auto-saves as they type
- **Previous Feedback** (iteration 2+): their comments from last time, shown below the textbox

The "Benchmark" tab shows the stats summary: pass rates, timing, and token usage for each configuration, with per-eval breakdowns and analyst observations.

Navigation is via prev/next buttons or arrow keys. When done, they click "Submit All Reviews" which saves all feedback to `feedback.json`.

### Step 5: Read the feedback

When the user tells you they're done, read `feedback.json`:

```json
{
  "reviews": [
    {"run_id": "eval-0-with_skill", "feedback": "the chart is missing axis labels", "timestamp": "..."},
    {"run_id": "eval-1-with_skill", "feedback": "", "timestamp": "..."},
    {"run_id": "eval-2-with_skill", "feedback": "perfect, love this", "timestamp": "..."}
  ],
  "status": "complete"
}
```

Empty feedback means the user thought it was fine. Focus your improvements on the test cases where the user had specific complaints.

Kill the viewer server when you're done with it:

```bash
kill $VIEWER_PID 2>/dev/null
```

---

## Improving the skill

This is the heart of the loop. You've run the test cases, the user has reviewed the results, and now you need to make the skill better based on their feedback.

### How to think about improvements

1. **Generalize from the feedback.** The big picture thing that's happening here is that we're trying to create skills that can be used a million times (maybe literally, maybe even more who knows) across many different prompts. Here you and the user are iterating on only a few examples over and over again because it helps move faster. The user knows these examples in and out and it's quick for them to assess new outputs. But if the skill you and the user are codeveloping works only for those examples, it's useless. Rather than put in fiddly overfitty changes, or oppressively constrictive MUSTs, if there's some stubborn issue, you might try branching out and using different metaphors, or recommending different patterns of working. It's relatively cheap to try and maybe you'll land on something great.

2. **Keep the prompt lean.** Remove things that aren't pulling their weight. Make sure to read the transcripts, not just the final outputs — if it looks like the skill is making the model waste a bunch of time doing things that are unproductive, you can try getting rid of the parts of the skill that are making it do that and seeing what happens.

3. **Explain the why.** Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen. Even if the feedback from the user is terse or frustrated, try to actually understand the task and why the user is writing what they wrote, and what they actually wrote, and then transmit this understanding into the instructions. If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag — if possible, reframe and explain the reasoning so that the model understands why the thing you're asking for is important. That's a more humane, powerful, and effective approach.

4. **Look for repeated work across test cases.** Read the transcripts from the test runs and notice if the subagents all independently wrote similar helper scripts or took the same multi-step approach to something. If all 3 test cases resulted in the subagent writing a `create_docx.py` or a `build_chart.py`, that's a strong signal the skill should bundle that script. Write it once, put it in `scripts/`, and tell the skill to use it. This saves every future invocation from reinventing the wheel.

This task is pretty important (we are trying to create billions a year in economic value here!) and your thinking time is not the blocker; take your time and really mull things over. I'd suggest writing a draft revision and then looking at it anew and making improvements. Really do your best to get into the head of the user and understand what they want and need.

### The iteration loop

After improving the skill:

1. Apply your improvements to the skill
2. Rerun all test cases into a new `iteration-<N+1>/` directory, including baseline runs. If you're creating a new skill, the baseline is always `without_skill` (no skill) — that stays the same across iterations. If you're improving an existing skill, use your judgment on what makes sense as the baseline: the original version the user came in with, or the previous iteration.
3. Launch the reviewer with `--previous-workspace` pointing at the previous iteration
4. Wait for the user to review and tell you they're done
5. Read the new feedback, improve again, repeat

Keep going until:
- The user says they're happy
- The feedback is all empty (everything looks good)
- You're not making meaningful progress

---

## Advanced: Blind comparison

For situations where you want a more rigorous comparison between two versions of a skill (e.g., the user asks "is the new version actually better?"), there's a blind comparison system. Read `agents/comparator.md` and `agents/analyzer.md` for the details. The basic idea is: give two outputs to an independent agent without telling it which is which, and let it judge quality. Then analyze why the winner won.

This is optional, requires subagents, and most users won't need it. The human review loop is usually sufficient.

---

## Description Optimization

The description field in SKILL.md frontmatter is the primary mechanism that determines whether Claude invokes a skill. After creating or improving a skill, offer to optimize the description for better triggering accuracy.

### Step 1: Generate trigger eval queries

Create 20 eval queries — a mix of should-trigger and should-not-trigger. Save as JSON:

```json
[
  {"query": "the user prompt", "should_trigger": true},
  {"query": "another prompt", "should_trigger": false}
]
```

The queries must be realistic and something a Claude Code or Claude.ai user would actually type. Not abstract requests, but requests that are concrete and specific and have a good amount of detail. For instance, file paths, personal context about the user's job or situation, column names and values, company names, URLs. A little bit of backstory. Some might be in lowercase or contain abbreviations or typos or casual speech. Use a mix of different lengths, and focus on edge cases rather than making them clear-cut (the user will get a chance to sign off on them).

Bad: `"Format this data"`, `"Extract text from PDF"`, `"Create a chart"`

Good: `"ok so my boss just sent me this xlsx file (its in my downloads, called something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows the profit margin as a percentage. The revenue is in column C and costs are in column D i think"`

For the **should-trigger** queries (8-10), think about coverage. You want different phrasings of the same intent — some formal, some casual. Include cases where the user doesn't explicitly name the skill or file type but clearly needs it. Throw in some uncommon use cases and cases where this skill competes with another but should win.

For the **should-not-trigger** queries (8-10), the most valuable ones are the near-misses — queries that share keywords or concepts with the skill but actually need something different. Think adjacent domains, ambiguous phrasing where a naive keyword match would trigger but shouldn't, and cases where the query touches on something the skill does but in a context where another tool is more appropriate.

The key thing to avoid: don't make should-not-trigger queries obviously irrelevant. "Write a fibonacci function" as a negative test for a PDF skill is too easy — it doesn't test anything. The negative cases should be genuinely tricky.

### Step 2: Review with user

Present the eval set to the user for review using the HTML template:

1. Read the template from `assets/eval_review.html`
2. Replace the placeholders:
   - `__EVAL_DATA_PLACEHOLDER__` → the JSON array of eval items (no quotes around it — it's a JS variable assignment)
   - `__SKILL_NAME_PLACEHOLDER__` → the skill's name
   - `__SKILL_DESCRIPTION_PLACEHOLDER__` → the skill's current description
3. Write to a temp file (e.g., `/tmp/eval_review_<skill-name>.html`) and open it: `open /tmp/eval_review_<skill-name>.html`
4. The user can edit queries, toggle should-trigger, add/remove entries, then click "Export Eval Set"
5. The file downloads to `~/Downloads/eval_set.json` — check the Downloads folder for the most recent version in case there are multiple (e.g., `eval_set (1).json`)

This step matters — bad eval queries lead to bad descriptions.

### Step 3: Run the optimization loop

Tell the user: "This will take some time — I'll run the optimization loop in the background and check on it periodically."

Save the eval set to the workspace, then run in the background:

```bash
python -m scripts.run_loop \
  --eval-set <path-to-trigger-eval.json> \
  --skill-path <path-to-skill> \
  --model <model-id-powering-this-session> \
  --max-iterations 5 \
  --verbose
```

Use the model ID from your system prompt (the one powering the current session) so the triggering test matches what the user actually experiences.

While it runs, periodically tail the output to give the user updates on which iteration it's on and what the scores look like.

This handles the full optimization loop automatically. It splits the eval set into 60% train and 40% held-out test, evaluates the current description (running each query 3 times to get a reliable trigger rate), then calls Claude to propose improvements based on what failed. It re-evaluates each new description on both train and test, iterating up to 5 times. When it's done, it opens an HTML report in the browser showing the results per iteration and returns JSON with `best_description` — selected by test score rather than train score to avoid overfitting.

### How skill triggering works

Understanding the triggering mechanism helps design better eval queries. Skills appear in Claude's `available_skills` list with their name + description, and Claude decides whether to consult a skill based on that description. The important thing to know is that Claude only consults skills for tasks it can't easily handle on its own — simple, one-step queries like "read this PDF" may not trigger a skill even if the description matches perfectly, because Claude can handle them directly with basic tools. Complex, multi-step, or specialized queries reliably trigger skills when the description matches.

This means your eval queries should be substantive enough that Claude would actually benefit from consulting a skill. Simple queries like "read file X" are poor test cases — they won't trigger skills regardless of description quality.

### Step 4: Apply the result

Take `best_description` from the JSON output and update the skill's SKILL.md frontmatter. Show the user before/after and report the scores.

---

### Package and Present (only if `present_files` tool is available)

Check whether you have access to the `present_files` tool. If you don't, skip this step. If you do, package the skill and present the .skill file to the user:

```bash
python -m scripts.package_skill <path/to/skill-folder>
```

After packaging, direct the user to the resulting `.skill` file path so they can install it.

---

## Claude.ai-specific instructions

In Claude.ai, the core workflow is the same (draft → test → review → improve → repeat), but because Claude.ai doesn't have subagents, some mechanics change. Here's what to adapt:

**Running test cases**: No subagents means no parallel execution. For each test case, read the skill's SKILL.md, then follow its instructions to accomplish the test prompt yourself. Do them one at a time. This is less rigorous than independent subagents (you wrote the skill and you're also running it, so you have full context), but it's a useful sanity check — and the human review step compensates. Skip the baseline runs — just use the skill to complete the task as requested.

**Reviewing results**: If you can't open a browser (e.g., Claude.ai's VM has no display, or you're on a remote server), skip the browser reviewer entirely. Instead, present results directly in the conversation. For each test case, show the prompt and the output. If the output is a file the user needs to see (like a .docx or .xlsx), save it to the filesystem and tell them where it is so they can download and inspect it. Ask for feedback inline: "How does this look? Anything you'd change?"

**Benchmarking**: Skip the quantitative benchmarking — it relies on baseline comparisons which aren't meaningful without subagents. Focus on qualitative feedback from the user.

**The iteration loop**: Same as before — improve the skill, rerun the test cases, ask for feedback — just without the browser reviewer in the middle. You can still organize results into iteration directories on the filesystem if you have one.

**Description optimization**: This section requires the `claude` CLI tool (specifically `claude -p`) which is only available in Claude Code. Skip it if you're on Claude.ai.

**Blind comparison**: Requires subagents. Skip it.

**Packaging**: The `package_skill.py` script works anywhere with Python and a filesystem. On Claude.ai, you can run it and the user can download the resulting `.skill` file.

**Updating an existing skill**: The user might be asking you to update an existing skill, not create a new one. In this case:
- **Preserve the original name.** Note the skill's directory name and `name` frontmatter field -- use them unchanged. E.g., if the installed skill is `research-helper`, output `research-helper.skill` (not `research-helper-v2`).
- **Copy to a writeable location before editing.** The installed skill path may be read-only. Copy to `/tmp/skill-name/`, edit there, and package from the copy.
- **If packaging manually, stage in `/tmp/` first**, then copy to the output directory -- direct writes may fail due to permissions.

---

## Cowork-Specific Instructions

If you're in Cowork, the main things to know are:

- You have subagents, so the main workflow (spawn test cases in parallel, run baselines, grade, etc.) all works. (However, if you run into severe problems with timeouts, it's OK to run the test prompts in series rather than parallel.)
- You don't have a browser or display, so when generating the eval viewer, use `--static <output_path>` to write a standalone HTML file instead of starting a server. Then proffer a link that the user can click to open the HTML in their browser.
- For whatever reason, the Cowork setup seems to disincline Claude from generating the eval viewer after running the tests, so just to reiterate: whether you're in Cowork or in Claude Code, after running tests, you should always generate the eval viewer for the human to look at examples before revising the skill yourself and trying to make corrections, using `generate_review.py` (not writing your own boutique html code). Sorry in advance but I'm gonna go all caps here: GENERATE THE EVAL VIEWER *BEFORE* evaluating inputs yourself. You want to get them in front of the human ASAP!
- Feedback works differently: since there's no running server, the viewer's "Submit All Reviews" button will download `feedback.json` as a file. You can then read it from there (you may have to request access first).
- Packaging works — `package_skill.py` just needs Python and a filesystem.
- Description optimization (`run_loop.py` / `run_eval.py`) should work in Cowork just fine since it uses `claude -p` via subprocess, not a browser, but please save it until you've fully finished making the skill and the user agrees it's in good shape.
- **Updating an existing skill**: The user might be asking you to update an existing skill, not create a new one. Follow the update guidance in the claude.ai section above.

---

## Reference files

The agents/ directory contains instructions for specialized subagents. Read them when you need to spawn the relevant subagent.

- `agents/grader.md` — How to evaluate assertions against outputs
- `agents/comparator.md` — How to do blind A/B comparison between two outputs
- `agents/analyzer.md` — How to analyze why one version beat another

The references/ directory has additional documentation:
- `references/schemas.md` — JSON structures for evals.json, grading.json, etc.

---

Repeating one more time the core loop here for emphasis:

- Figure out what the skill is about
- Draft or edit the skill
- Run claude-with-access-to-the-skill on test prompts
- With the user, evaluate the outputs:
  - Create benchmark.json and run `eval-viewer/generate_review.py` to help the user review them
  - Run quantitative evals
- Repeat until you and the user are satisfied
- Package the final skill and return it to the user.

Please add steps to your TodoList, if you have such a thing, to make sure you don't forget. If you're in Cowork, please specifically put "Create evals JSON and run `eval-viewer/generate_review.py` so human can review test cases" in your TodoList to make sure it happens.

Good luck!

---

<!-- skill-creator-ms -->
Guide for creating skills that extend AI agent capabilities, with emphasis on Azure SDKs and Microsoft Foundry.

> **Required Context:** When creating SDK or API skills, users MUST provide the SDK package name, documentation URL, or repository reference for the skill to be based on.

## About Skills

Skills are modular knowledge packages that transform general-purpose agents into specialized experts:

1. **Procedural knowledge** — Multi-step workflows for specific domains
2. **SDK expertise** — API patterns, authentication, error handling for Azure services
3. **Domain context** — Schemas, business logic, company-specific patterns
4. **Bundled resources** — Scripts, references, templates for complex tasks

---

## Core Principles

### 1. Concise is Key

The context window is a shared resource. Challenge each piece: "Does this justify its token cost?"

**Default assumption: Agents are already capable.** Only add what they don't already know.

### 2. Fresh Documentation First

**Azure SDKs change constantly.** Skills should instruct agents to verify documentation:

```markdown
## Before Implementation

Search `microsoft-docs` MCP for current API patterns:
- Query: "[SDK name] [operation] python"
- Verify: Parameters match your installed SDK version
```

### 3. Degrees of Freedom

Match specificity to task fragility:

| Freedom | When | Example |
|---------|------|---------|
| **High** | Multiple valid approaches | Text guidelines |
| **Medium** | Preferred pattern with variation | Pseudocode |
| **Low** | Must be exact | Specific scripts |

### 4. Progressive Disclosure

Skills load in three levels:

1. **Metadata** (~100 words) — Always in context
2. **SKILL.md body** (<5k words) — When skill triggers
3. **References** (unlimited) — As needed

**Keep SKILL.md under 500 lines.** Split into reference files when approaching this limit.

---

## Skill Structure

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/      — Executable code
    ├── references/   — Documentation loaded as needed
    └── assets/       — Output resources (templates, images)
```

### SKILL.md

- **Frontmatter**: `name` and `description`. The description is the trigger mechanism.
- **Body**: Instructions loaded only after triggering.

### Bundled Resources

| Type | Purpose | When to Include |
|------|---------|-----------------|
| `scripts/` | Deterministic operations | Same code rewritten repeatedly |
| `references/` | Detailed patterns | API docs, schemas, detailed guides |
| `assets/` | Output resources | Templates, images, boilerplate |

**Don't include**: README.md, CHANGELOG.md, installation guides.

---

## Creating Azure SDK Skills

When creating skills for Azure SDKs, follow these patterns consistently.

### Skill Section Order

Follow this structure (based on existing Azure SDK skills):

1. **Title** — `# SDK Name`
2. **Installation** — `pip install`, `npm install`, etc.
3. **Environment Variables** — Required configuration
4. **Authentication** — Always `DefaultAzureCredential`
5. **Core Workflow** — Minimal viable example
6. **Feature Tables** — Clients, methods, tools
7. **Best Practices** — Numbered list
8. **Reference Links** — Table linking to `/references/*.md`

### Authentication Pattern (All Languages)

Always use `DefaultAzureCredential`:

```python
# Python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
client = ServiceClient(endpoint, credential)
```

```csharp
// C#
var credential = new DefaultAzureCredential();
var client = new ServiceClient(new Uri(endpoint), credential);
```

```java
// Java
TokenCredential credential = new DefaultAzureCredentialBuilder().build();
ServiceClient client = new ServiceClientBuilder()
    .endpoint(endpoint)
    .credential(credential)
    .buildClient();
```

```typescript
// TypeScript
import { DefaultAzureCredential } from "@azure/identity";
const credential = new DefaultAzureCredential();
const client = new ServiceClient(endpoint, credential);
```

**Never hardcode credentials. Use environment variables.**

### Standard Verb Patterns

Azure SDKs use consistent verbs across all languages:

| Verb | Behavior |
|------|----------|
| `create` | Create new; fail if exists |
| `upsert` | Create or update |
| `get` | Retrieve; error if missing |
| `list` | Return collection |
| `delete` | Succeed even if missing |
| `begin` | Start long-running operation |

### Language-Specific Patterns

See `references/azure-sdk-patterns.md` for detailed patterns including:

- **Python**: `ItemPaged`, `LROPoller`, context managers, Sphinx docstrings
- **.NET**: `Response<T>`, `Pageable<T>`, `Operation<T>`, mocking support
- **Java**: Builder pattern, `PagedIterable`/`PagedFlux`, Reactor types
- **TypeScript**: `PagedAsyncIterableIterator`, `AbortSignal`, browser considerations

### Example: Azure SDK Skill Structure

```markdown
---
name: skill-creator
description: |
  Azure AI Example SDK for Python. Use for [specific service features].
  Triggers: "example service", "create example", "list examples".
---

# Azure AI Example SDK

## Installation

\`\`\`bash
pip install azure-ai-example
\`\`\`

## Environment Variables

\`\`\`bash
AZURE_EXAMPLE_ENDPOINT=https://<resource>.example.azure.com
\`\`\`

## Authentication

\`\`\`python
from azure.identity import DefaultAzureCredential
from azure.ai.example import ExampleClient

credential = DefaultAzureCredential()
client = ExampleClient(
    endpoint=os.environ["AZURE_EXAMPLE_ENDPOINT"],
    credential=credential
)
\`\`\`

## Core Workflow

\`\`\`python
# Create
item = client.create_item(name="example", data={...})

# List (pagination handled automatically)
for item in client.list_items():
    print(item.name)

# Long-running operation
poller = client.begin_process(item_id)
result = poller.result()

# Cleanup
client.delete_item(item_id)
\`\`\`

## Reference Files

| File | Contents |
|------|----------|
| references/tools.md | Tool integrations |
| references/streaming.md | Event streaming patterns |
```

---

## Skill Creation Process

1. **Gather SDK Context** — User provides SDK/API reference (REQUIRED)
2. **Understand** — Research SDK patterns from official docs
3. **Plan** — Identify reusable resources and product area category
4. **Create** — Write SKILL.md in `.github/skills/<skill-name>/`
5. **Categorize** — Create symlink in `skills/<language>/<category>/`
6. **Test** — Create acceptance criteria and test scenarios
7. **Document** — Update README.md skill catalog
8. **Iterate** — Refine based on real usage

### Step 1: Gather SDK Context (REQUIRED)

**Before creating any SDK skill, the user MUST provide:**

| Required | Example | Purpose |
|----------|---------|---------|
| **SDK Package** | `azure-ai-agents`, `Azure.AI.OpenAI` | Identifies the exact SDK |
| **Documentation URL** | `https://learn.microsoft.com/en-us/azure/ai-services/...` | Primary source of truth |
| **Repository** (optional) | `Azure/azure-sdk-for-python` | For code patterns |

**Prompt the user if not provided:**
```
To create this skill, I need:
1. The SDK package name (e.g., azure-ai-projects)
2. The Microsoft Learn documentation URL or GitHub repo
3. The target language (py/dotnet/ts/java)
```

**Search official docs first:**
```bash
# Use microsoft-docs MCP to get current API patterns
# Query: "[SDK name] [operation] [language]"
# Verify: Parameters match the latest SDK version
```

### Step 2: Understand the Skill

Gather concrete examples:

- "What SDK operations should this skill cover?"
- "What triggers should activate this skill?"
- "What errors do developers commonly encounter?"

| Example Task | Reusable Resource |
|--------------|-------------------|
| Same auth code each time | Code example in SKILL.md |
| Complex streaming patterns | `references/streaming.md` |
| Tool configurations | `references/tools.md` |
| Error handling patterns | `references/error-handling.md` |

### Step 3: Plan Product Area Category

Skills are organized by **language** and **product area** in the `skills/` directory via symlinks.

**Product Area Categories:**

| Category | Description | Examples |
|----------|-------------|----------|
| `foundry` | AI Foundry, agents, projects, inference | `azure-ai-agents-py`, `azure-ai-projects-py` |
| `data` | Storage, Cosmos DB, Tables, Data Lake | `azure-cosmos-py`, `azure-storage-blob-py` |
| `messaging` | Event Hubs, Service Bus, Event Grid | `azure-eventhub-py`, `azure-servicebus-py` |
| `monitoring` | OpenTelemetry, App Insights, Query | `azure-monitor-opentelemetry-py` |
| `identity` | Authentication, DefaultAzureCredential | `azure-identity-py` |
| `security` | Key Vault, secrets, keys, certificates | `azure-keyvault-py` |
| `integration` | API Management, App Configuration | `azure-appconfiguration-py` |
| `compute` | Batch, ML compute | `azure-compute-batch-java` |
| `container` | Container Registry, ACR | `azure-containerregistry-py` |

**Determine the category** based on:
1. Azure service family (Storage → `data`, Event Hubs → `messaging`)
2. Primary use case (AI agents → `foundry`)
3. Existing skills in the same service area

### Step 4: Create the Skill

**Location:** `.github/skills/<skill-name>/SKILL.md`

**Naming convention:**
- `azure-<service>-<subservice>-<language>`
- Examples: `azure-ai-agents-py`, `azure-cosmos-java`, `azure-storage-blob-ts`

**For Azure SDK skills:**

1. Search `microsoft-docs` MCP for current API patterns
2. Verify against installed SDK version
3. Follow the section order above
4. Include cleanup code in examples
5. Add feature comparison tables

**Write bundled resources first**, then SKILL.md.

**Frontmatter:**

```yaml
---
name: skill-name-py
description: |
  Azure Service SDK for Python. Use for [specific features].
  Triggers: "service name", "create resource", "specific operation".
---
```

### Step 5: Categorize with Symlinks

After creating the skill in `.github/skills/`, create a symlink in the appropriate category:

```bash
# Pattern: skills/<language>/<category>/<short-name> -> ../../../.github/skills/<full-skill-name>

# Example for azure-ai-agents-py in python/foundry:
cd skills/python/foundry
ln -s ../../../.github/skills/azure-ai-agents-py agents

# Example for azure-cosmos-db-py in python/data:
cd skills/python/data
ln -s ../../../.github/skills/azure-cosmos-db-py cosmos-db
```

**Symlink naming:**
- Use short, descriptive names (e.g., `agents`, `cosmos`, `blob`)
- Remove the `azure-` prefix and language suffix
- Match existing patterns in the category

**Verify the symlink:**
```bash
ls -la skills/python/foundry/agents
# Should show: agents -> ../../../.github/skills/azure-ai-agents-py
```

### Step 6: Create Tests

**Every skill MUST have acceptance criteria and test scenarios.**

#### 6.1 Create Acceptance Criteria

**Location:** `.github/skills/<skill-name>/references/acceptance-criteria.md`

**Source materials** (in priority order):
1. Official Microsoft Learn docs (via `microsoft-docs` MCP)
2. SDK source code from the repository
3. Existing reference files in the skill

**Format:**
```markdown
# Acceptance Criteria: <skill-name>

**SDK**: `package-name`
**Repository**: https://github.com/Azure/azure-sdk-for-<language>
**Purpose**: Skill testing acceptance criteria

---

## 1. Correct Import Patterns

### 1.1 Client Imports

#### ✅ CORRECT: Main Client
\`\`\`python
from azure.ai.mymodule import MyClient
from azure.identity import DefaultAzureCredential
\`\`\`

#### ❌ INCORRECT: Wrong Module Path
\`\`\`python
from azure.ai.mymodule.models import MyClient  # Wrong - Client is not in models
\`\`\`

## 2. Authentication Patterns

#### ✅ CORRECT: DefaultAzureCredential
\`\`\`python
credential = DefaultAzureCredential()
client = MyClient(endpoint, credential)
\`\`\`

#### ❌ INCORRECT: Hardcoded Credentials
\`\`\`python
client = MyClient(endpoint, api_key="hardcoded")  # Security risk
\`\`\`
```

**Critical patterns to document:**
- Import paths (these vary significantly between Azure SDKs)
- Authentication patterns
- Client initialization
- Async variants (`.aio` modules)
- Common anti-patterns

#### 6.2 Create Test Scenarios

**Location:** `tests/scenarios/<skill-name>/scenarios.yaml`

```yaml
config:
  model: gpt-4
  max_tokens: 2000
  temperature: 0.3

scenarios:
  - name: basic_client_creation
    prompt: |
      Create a basic example using the Azure SDK.
      Include proper authentication and client initialization.
    expected_patterns:
      - "DefaultAzureCredential"
      - "MyClient"
    forbidden_patterns:
      - "api_key="
      - "hardcoded"
    tags:
      - basic
      - authentication
    mock_response: |
      import os
      from azure.identity import DefaultAzureCredential
      from azure.ai.mymodule import MyClient
      
      credential = DefaultAzureCredential()
      client = MyClient(
          endpoint=os.environ["AZURE_ENDPOINT"],
          credential=credential
      )
      # ... rest of working example
```

**Scenario design principles:**
- Each scenario tests ONE specific pattern or feature
- `expected_patterns` — patterns that MUST appear
- `forbidden_patterns` — common mistakes that must NOT appear
- `mock_response` — complete, working code that passes all checks
- `tags` — for filtering (`basic`, `async`, `streaming`, `tools`)

#### 6.3 Run Tests

```bash
cd tests
pnpm install

# Check skill is discovered
pnpm harness --list

# Run in mock mode (fast, deterministic)
pnpm harness <skill-name> --mock --verbose

# Run with Ralph Loop (iterative improvement)
pnpm harness <skill-name> --ralph --mock --max-iterations 5 --threshold 85
```

**Success criteria:**
- All scenarios pass (100% pass rate)
- No false positives (mock responses always pass)
- Patterns catch real mistakes

### Step 7: Update Documentation

After creating the skill:

1. **Update README.md** — Add the skill to the appropriate language section in the Skill Catalog
   - Update total skill count (line ~73: `> N skills in...`)
   - Update Skill Explorer link count (line ~15: `Browse all N skills`)
   - Update language count table (lines ~77-83)
   - Update language section count (e.g., `> N skills • suffix: -py`)
   - Update category count (e.g., `<summary><strong>Foundry & AI</strong> (N skills)</summary>`)
   - Add skill row in alphabetical order within its category
   - Update test coverage summary (line ~622: `**N skills with N test scenarios**`)
   - Update test coverage table — update skill count, scenario count, and top skills for the language

2. **Regenerate GitHub Pages data** — Run the extraction script to update the docs site
   ```bash
   cd docs-site && npx tsx scripts/extract-skills.ts
   ```
   This updates `docs-site/src/data/skills.json` which feeds the Astro-based docs site.
   Then rebuild the docs site:
   ```bash
   cd docs-site && npm run build
   ```
   This outputs to `docs/` which is served by GitHub Pages.

3. **Verify AGENTS.md** — Ensure the skill count is accurate

---

## Progressive Disclosure Patterns

### Pattern 1: High-Level Guide with References

```markdown
# SDK Name

## Quick Start
[Minimal example]

## Advanced Features
- **Streaming**: See references/streaming.md
- **Tools**: See references/tools.md
```

### Pattern 2: Language Variants

```
azure-service-skill/
├── SKILL.md (overview + language selection)
└── references/
    ├── python.md
    ├── dotnet.md
    ├── java.md
    └── typescript.md
```

### Pattern 3: Feature Organization

```
azure-ai-agents/
├── SKILL.md (core workflow)
└── references/
    ├── tools.md
    ├── streaming.md
    ├── async-patterns.md
    └── error-handling.md
```

---

## Design Pattern References

| Reference | Contents |
|-----------|----------|
| `references/workflows.md` | Sequential and conditional workflows |
| `references/output-patterns.md` | Templates and examples |
| `references/azure-sdk-patterns.md` | Language-specific Azure SDK patterns |

---

## Anti-Patterns

| Don't | Why |
|-------|-----|
| Create skill without SDK context | Users must provide package name/docs URL |
| Put "when to use" in body | Body loads AFTER triggering |
| Hardcode credentials | Security risk |
| Skip authentication section | Agents will improvise poorly |
| Use outdated SDK patterns | APIs change; search docs first |
| Include README.md | Agents don't need meta-docs |
| Deeply nest references | Keep one level deep |
| Skip acceptance criteria | Skills without tests can't be validated |
| Skip symlink categorization | Skills won't be discoverable by category |
| Use wrong import paths | Azure SDKs have specific module structures |

---

## Checklist

Before completing a skill:

**Prerequisites:**
- [ ] User provided SDK package name or documentation URL
- [ ] Verified SDK patterns via `microsoft-docs` MCP

**Skill Creation:**
- [ ] Description includes what AND when (trigger phrases)
- [ ] SKILL.md under 500 lines
- [ ] Authentication uses `DefaultAzureCredential`
- [ ] Includes cleanup/delete in examples
- [ ] References organized by feature

**Categorization:**
- [ ] Skill created in `.github/skills/<skill-name>/`
- [ ] Symlink created in `skills/<language>/<category>/<short-name>`
- [ ] Symlink points to `../../../.github/skills/<skill-name>`

**Testing:**
- [ ] `references/acceptance-criteria.md` created with correct/incorrect patterns
- [ ] `tests/scenarios/<skill-name>/scenarios.yaml` created
- [ ] All scenarios pass (`pnpm harness <skill> --mock`)
- [ ] Import paths documented precisely

**Documentation:**
- [ ] README.md skill catalog updated
- [ ] Instructs to search `microsoft-docs` MCP for current APIs

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: skill-creator on 2026-04-18 -->
<!-- Use `skill-creator` instead. -->

---

<!-- skill-developer -->
## Purpose

Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, following Anthropic's official best practices including the 500-line rule and progressive disclosure pattern.

## When to Use This Skill

Automatically activates when you mention:
- Creating or adding skills
- Modifying skill triggers or rules
- Understanding how skill activation works
- Debugging skill activation issues
- Working with skill-rules.json
- Hook system mechanics
- Claude Code best practices
- Progressive disclosure
- YAML frontmatter
- 500-line rule

---

## System Overview

### Two-Hook Architecture

**1. UserPromptSubmit Hook** (Proactive Suggestions)
- **File**: `.claude/hooks/skill-activation-prompt.ts`
- **Trigger**: BEFORE Claude sees user's prompt
- **Purpose**: Suggest relevant skills based on keywords + intent patterns
- **Method**: Injects formatted reminder as context (stdout → Claude's input)
- **Use Cases**: Topic-based skills, implicit work detection

**2. Stop Hook - Error Handling Reminder** (Gentle Reminders)
- **File**: `.claude/hooks/error-handling-reminder.ts`
- **Trigger**: AFTER Claude finishes responding
- **Purpose**: Gentle reminder to self-assess error handling in code written
- **Method**: Analyzes edited files for risky patterns, displays reminder if needed
- **Use Cases**: Error handling awareness without blocking friction

**Philosophy Change (2025-10-27):** We moved away from blocking PreToolUse for Sentry/error handling. Instead, use gentle post-response reminders that don't block workflow but maintain code quality awareness.

### Configuration File

**Location**: `.claude/skills/skill-rules.json`

Defines:
- All skills and their trigger conditions
- Enforcement levels (block, suggest, warn)
- File path patterns (glob)
- Content detection patterns (regex)
- Skip conditions (session tracking, file markers, env vars)

---

## Skill Types

### 1. Guardrail Skills

**Purpose:** Enforce critical best practices that prevent errors

**Characteristics:**
- Type: `"guardrail"`
- Enforcement: `"block"`
- Priority: `"critical"` or `"high"`
- Block file edits until skill used
- Prevent common mistakes (column names, critical errors)
- Session-aware (don't repeat nag in same session)

**Examples:**
- `database-verification` - Verify table/column names before Prisma queries
- `frontend-dev-guidelines` - Enforce React/TypeScript patterns

**When to Use:**
- Mistakes that cause runtime errors
- Data integrity concerns
- Critical compatibility issues

### 2. Domain Skills

**Purpose:** Provide comprehensive guidance for specific areas

**Characteristics:**
- Type: `"domain"`
- Enforcement: `"suggest"`
- Priority: `"high"` or `"medium"`
- Advisory, not mandatory
- Topic or domain-specific
- Comprehensive documentation

**Examples:**
- `backend-dev-guidelines` - Node.js/Express/TypeScript patterns
- `frontend-dev-guidelines` - React/TypeScript best practices
- `error-tracking` - Sentry integration guidance

**When to Use:**
- Complex systems requiring deep knowledge
- Best practices documentation
- Architectural patterns
- How-to guides

---

## Quick Start: Creating a New Skill

### Step 1: Create Skill File

**Location:** `.claude/skills/{skill-name}/SKILL.md`

**Template:**
```markdown
---
name: my-new-skill
description: Brief description including keywords that trigger this skill. Mention topics, file types, and use cases. Be explicit about trigger terms.
---

# My New Skill

## Purpose
What this skill helps with

## When to Use
Specific scenarios and conditions

## Key Information
The actual guidance, documentation, patterns, examples
```

**Best Practices:**
- ✅ **Name**: Lowercase, hyphens, gerund form (verb + -ing) preferred
- ✅ **Description**: Include ALL trigger keywords/phrases (max 1024 chars)
- ✅ **Content**: Under 500 lines - use reference files for details
- ✅ **Examples**: Real code examples
- ✅ **Structure**: Clear headings, lists, code blocks

### Step 2: Add to skill-rules.json

See [SKILL_RULES_REFERENCE.md](SKILL_RULES_REFERENCE.md) for complete schema.

**Basic Template:**
```json
{
  "my-new-skill": {
    "type": "domain",
    "enforcement": "suggest",
    "priority": "medium",
    "promptTriggers": {
      "keywords": ["keyword1", "keyword2"],
      "intentPatterns": ["(create|add).*?something"]
    }
  }
}
```

### Step 3: Test Triggers

**Test UserPromptSubmit:**
```bash
echo '{"session_id":"test","prompt":"your test prompt"}' | \
  npx tsx .claude/hooks/skill-activation-prompt.ts
```

**Test PreToolUse:**
```bash
cat <<'EOF' | npx tsx .claude/hooks/skill-verification-guard.ts
{"session_id":"test","tool_name":"Edit","tool_input":{"file_path":"test.ts"}}
EOF
```

### Step 4: Refine Patterns

Based on testing:
- Add missing keywords
- Refine intent patterns to reduce false positives
- Adjust file path patterns
- Test content patterns against actual files

### Step 5: Follow Anthropic Best Practices

✅ Keep SKILL.md under 500 lines
✅ Use progressive disclosure with reference files
✅ Add table of contents to reference files > 100 lines
✅ Write detailed description with trigger keywords
✅ Test with 3+ real scenarios before documenting
✅ Iterate based on actual usage

---

## Enforcement Levels

### BLOCK (Critical Guardrails)

- Physically prevents Edit/Write tool execution
- Exit code 2 from hook, stderr → Claude
- Claude sees message and must use skill to proceed
- **Use For**: Critical mistakes, data integrity, security issues

**Example:** Database column name verification

### SUGGEST (Recommended)

- Reminder injected before Claude sees prompt
- Claude is aware of relevant skills
- Not enforced, just advisory
- **Use For**: Domain guidance, best practices, how-to guides

**Example:** Frontend development guidelines

### WARN (Optional)

- Low priority suggestions
- Advisory only, minimal enforcement
- **Use For**: Nice-to-have suggestions, informational reminders

**Rarely used** - most skills are either BLOCK or SUGGEST.

---

## Skip Conditions & User Control

### 1. Session Tracking

**Purpose:** Don't nag repeatedly in same session

**How it works:**
- First edit → Hook blocks, updates session state
- Second edit (same session) → Hook allows
- Different session → Blocks again

**State File:** `.claude/hooks/state/skills-used-{session_id}.json`

### 2. File Markers

**Purpose:** Permanent skip for verified files

**Marker:** `// @skip-validation`

**Usage:**
```typescript
// @skip-validation
import { PrismaService } from './prisma';
// This file has been manually verified
```

**NOTE:** Use sparingly - defeats the purpose if overused

### 3. Environment Variables

**Purpose:** Emergency disable, temporary override

**Global disable:**
```bash
export SKIP_SKILL_GUARDRAILS=true  # Disables ALL PreToolUse blocks
```

**Skill-specific:**
```bash
export SKIP_DB_VERIFICATION=true
export SKIP_ERROR_REMINDER=true
```

---

## Testing Checklist

When creating a new skill, verify:

- [ ] Skill file created in `.claude/skills/{name}/SKILL.md`
- [ ] Proper frontmatter with name and description
- [ ] Entry added to `skill-rules.json`
- [ ] Keywords tested with real prompts
- [ ] Intent patterns tested with variations
- [ ] File path patterns tested with actual files
- [ ] Content patterns tested against file contents
- [ ] Block message is clear and actionable (if guardrail)
- [ ] Skip conditions configured appropriately
- [ ] Priority level matches importance
- [ ] No false positives in testing
- [ ] No false negatives in testing
- [ ] Performance is acceptable (<100ms or <200ms)
- [ ] JSON syntax validated: `jq . skill-rules.json`
- [ ] **SKILL.md under 500 lines** ⭐
- [ ] Reference files created if needed
- [ ] Table of contents added to files > 100 lines

---

## Reference Files

For detailed information on specific topics, see:

### [TRIGGER_TYPES.md](TRIGGER_TYPES.md)
Complete guide to all trigger types:
- Keyword triggers (explicit topic matching)
- Intent patterns (implicit action detection)
- File path triggers (glob patterns)
- Content patterns (regex in files)
- Best practices and examples for each
- Common pitfalls and testing strategies

### [SKILL_RULES_REFERENCE.md](SKILL_RULES_REFERENCE.md)
Complete skill-rules.json schema:
- Full TypeScript interface definitions
- Field-by-field explanations
- Complete guardrail skill example
- Complete domain skill example
- Validation guide and common errors

### [HOOK_MECHANISMS.md](HOOK_MECHANISMS.md)
Deep dive into hook internals:
- UserPromptSubmit flow (detailed)
- PreToolUse flow (detailed)
- Exit code behavior table (CRITICAL)
- Session state management
- Performance considerations

### [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
Comprehensive debugging guide:
- Skill not triggering (UserPromptSubmit)
- PreToolUse not blocking
- False positives (too many triggers)
- Hook not executing at all
- Performance issues

### [PATTERNS_LIBRARY.md](PATTERNS_LIBRARY.md)
Ready-to-use pattern collection:
- Intent pattern library (regex)
- File path pattern library (glob)
- Content pattern library (regex)
- Organized by use case
- Copy-paste ready

### [ADVANCED.md](ADVANCED.md)
Future enhancements and ideas:
- Dynamic rule updates
- Skill dependencies
- Conditional enforcement
- Skill analytics
- Skill versioning

---

## Quick Reference Summary

### Create New Skill (5 Steps)

1. Create `.claude/skills/{name}/SKILL.md` with frontmatter
2. Add entry to `.claude/skills/skill-rules.json`
3. Test with `npx tsx` commands
4. Refine patterns based on testing
5. Keep SKILL.md under 500 lines

### Trigger Types

- **Keywords**: Explicit topic mentions
- **Intent**: Implicit action detection
- **File Paths**: Location-based activation
- **Content**: Technology-specific detection

See [TRIGGER_TYPES.md](TRIGGER_TYPES.md) for complete details.

### Enforcement

- **BLOCK**: Exit code 2, critical only
- **SUGGEST**: Inject context, most common
- **WARN**: Advisory, rarely used

### Skip Conditions

- **Session tracking**: Automatic (prevents repeated nags)
- **File markers**: `// @skip-validation` (permanent skip)
- **Env vars**: `SKIP_SKILL_GUARDRAILS` (emergency disable)

### Anthropic Best Practices

✅ **500-line rule**: Keep SKILL.md under 500 lines
✅ **Progressive disclosure**: Use reference files for details
✅ **Table of contents**: Add to reference files > 100 lines
✅ **One level deep**: Don't nest references deeply
✅ **Rich descriptions**: Include all trigger keywords (max 1024 chars)
✅ **Test first**: Build 3+ evaluations before extensive documentation
✅ **Gerund naming**: Prefer verb + -ing (e.g., "processing-pdfs")

### Troubleshoot

Test hooks manually:
```bash
# UserPromptSubmit
echo '{"prompt":"test"}' | npx tsx .claude/hooks/skill-activation-prompt.ts

# PreToolUse
cat <<'EOF' | npx tsx .claude/hooks/skill-verification-guard.ts
{"tool_name":"Edit","tool_input":{"file_path":"test.ts"}}
EOF
```

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for complete debugging guide.

---

## Related Files

**Configuration:**
- `.claude/skills/skill-rules.json` - Master configuration
- `.claude/hooks/state/` - Session tracking
- `.claude/settings.json` - Hook registration

**Hooks:**
- `.claude/hooks/skill-activation-prompt.ts` - UserPromptSubmit
- `.claude/hooks/error-handling-reminder.ts` - Stop event (gentle reminders)

**All Skills:**
- `.claude/skills/*/SKILL.md` - Skill content files

---

**Skill Status**: COMPLETE - Restructured following Anthropic best practices ✅
**Line Count**: < 500 (following 500-line rule) ✅
**Progressive Disclosure**: Reference files for detailed information ✅

**Next**: Create more skills, refine patterns based on usage


<!-- MERGED INTO: skill-creator on 2026-04-18 -->
<!-- Use `skill-creator` instead. -->

---

<!-- skill-writer -->
Use this as the single canonical workflow for skill creation and improvement.
Primary success condition: maximize high-value input coverage before authoring so the resulting skill has minimal blind spots.

Load only the path(s) required for the task:

| Task | Read |
|------|------|
| Set skill class and required dimensions | `references/mode-selection.md` |
| Apply writing constraints for depth vs concision | `references/design-principles.md` |
| Select structure pattern for this skill | `references/skill-patterns.md` |
| Select workflow orchestration pattern for process-heavy skills | `references/workflow-patterns.md` |
| Select output format pattern for deterministic quality | `references/output-patterns.md` |
| Choose workflow path and required outputs | `references/mode-selection.md` |
| Load representative synthesis examples by skill type | `references/examples/*.md` |
| Synthesize external/local sources with depth gates | `references/synthesis-path.md` |
| Author or update SKILL.md and supporting files | `references/authoring-path.md` |
| Optimize skill description and trigger precision | `references/description-optimization.md` |
| Iterate using positive/negative/fix examples | `references/iteration-path.md` |
| Evaluate behavior and compare baseline vs with-skill (opt-in quantitative) | `references/evaluation-path.md` |
| Register and validate skill changes | `references/registration-validation.md` |

## Step 1: Resolve target and path

1. Resolve target skill path and intended operation (`create`, `update`, `synthesize`, `iterate`).
2. Read `references/mode-selection.md` and select the required path(s).
3. Classify the skill (`workflow-process`, `integration-documentation`, `security-review`, `skill-authoring`, `generic`).
4. Ask one direct question if class or depth requirements are ambiguous; otherwise state explicit assumptions.

## Step 2: Run synthesis when needed

Read `references/synthesis-path.md`.

1. Collect and score relevant sources with provenance.
2. Apply trust and safety rules when ingesting external content.
3. Produce source-backed decisions and coverage/gap status.
4. Load one or more profiles from `references/examples/*.md` when the skill is hybrid.
5. Enforce baseline source pack for skill-authoring workflows.
6. Enforce depth gates before moving to authoring.

## Step 3: Run iteration first when improving from outcomes/examples

Read `references/iteration-path.md` first when selected path includes `iteration` (for example operation `iterate`).

1. Capture and anonymize examples with provenance.
2. Re-evaluate skill behavior against working and holdout slices.
3. Propose improvements from positive/negative/fix evidence.
4. Carry concrete behavior deltas into authoring.

Skip this step when selected path does not include `iteration`.

## Step 4: Author or update skill artifacts

Read `references/authoring-path.md`.

1. Write or update `SKILL.md` in imperative voice with trigger-rich description.
2. Create focused reference files and scripts only when justified.
3. Follow `references/skill-patterns.md`, `references/workflow-patterns.md`, and
   `references/output-patterns.md` for structure and output determinism.
4. For authoring/generator skills, include transformed examples in references:
   - happy-path
   - secure/robust variant
   - anti-pattern + corrected version

## Step 5: Optimize description quality

Read `references/description-optimization.md`.

1. Validate should-trigger and should-not-trigger query sets.
2. Reduce false positives and false negatives with targeted description edits.
3. Keep trigger language generic across Codex and Claude.

## Step 6: Evaluate outcomes

Read `references/evaluation-path.md`.

1. Run a lightweight qualitative check by default (recommended).
2. For integration/documentation and skill-authoring skills, include the concise depth rubric from `references/evaluation-path.md`.
3. Run deeper eval playbook and quantitative baseline-vs-with-skill only when requested or risk warrants it.
4. Record outcomes and unresolved risks.

## Step 7: Register and validate

Read `references/registration-validation.md`.

1. Apply repository registration steps.
2. Run quick validation with strict depth gates.
3. Reject shallow outputs that fail depth gates or required artifact checks.

## Output format

Return:

1. `Summary`
2. `Changes Made`
3. `Validation Results`
4. `Open Gaps`


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.


<!-- MERGED INTO: skill-creator on 2026-04-18 -->
<!-- Use `skill-creator` instead. -->

---

<!-- skill-improver -->
Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards.

## Prerequisites

Requires the `plugin-dev` plugin which provides the `skill-reviewer` agent.

Verify it's enabled: run `/plugins` — `plugin-dev` should appear in the list. If missing, install from the Trail of Bits plugin repository.

## Core Loop

1. **Review** - Call skill-reviewer on the target skill
2. **Categorize** - Parse issues by severity
3. **Fix** - Address critical and major issues
4. **Evaluate** - Check minor issues for validity before fixing
5. **Repeat** - Continue until quality bar is met

## When to Use

- Improving a skill with multiple quality issues
- Iterating on a new skill until it meets standards
- Automated fix-review cycles instead of manual editing
- Consistent quality enforcement across skills

## When NOT to Use

- **One-time review**: Use `/skill-reviewer` directly instead
- **Quick single fixes**: Edit the file directly
- **Non-skill files**: Only works on SKILL.md files
- **Experimental skills**: Manual iteration gives more control during exploration

## Issue Categorization

### Critical Issues (MUST fix immediately)

These block skill loading or cause runtime failures:

- Missing required frontmatter fields (name, description) — Claude cannot index or trigger the skill
- Invalid YAML frontmatter syntax — Parsing fails, skill won't load
- Referenced files that don't exist — Runtime errors when Claude follows links
- Broken file paths — Same as above, leads to tool failures

### Major Issues (MUST fix)

These significantly degrade skill effectiveness:

- Weak or vague trigger descriptions — Claude may not recognize when to use the skill
- Wrong writing voice (second person "you" instead of imperative) — Inconsistent with Claude's execution model
- SKILL.md exceeds 500 lines without using references/ — Overloads context, reduces comprehension
- Missing "When to Use" or "When NOT to Use" sections — Required by project quality standards
- Description doesn't specify when to trigger — Skill may never be selected

### Minor Issues (Evaluate before fixing)

These are polish items that may or may not improve the skill:

- Subjective style preferences — Reviewer may have different taste than author
- Optional enhancements — May add complexity without proportional value
- "Nice to have" improvements — Consider cost-benefit before implementing
- Formatting suggestions — Often valid but low impact

## Minor Issue Evaluation

Before implementing any minor issue fix, evaluate:

1. **Is this a genuine improvement?** - Does it add real value or just satisfy a preference?
2. **Could this be a false positive?** - Is the reviewer misunderstanding context?
3. **Would this actually help Claude use the skill?** - Focus on functional improvements

Only implement minor fixes that are clearly beneficial. Skill-reviewer may produce false positives.

## Invoking skill-reviewer

Use the skill-reviewer agent from the plugin-dev plugin. Request a review by asking Claude to:

> Review the skill at [SKILL_PATH] using the plugin-dev:skill-reviewer agent. Provide a detailed quality assessment with issues categorized by severity.

Replace `[SKILL_PATH]` with the absolute path to the skill directory (e.g., `/path/to/plugins/my-plugin/skills/my-skill`).

## Example Fix Cycle

**Iteration 1 — skill-reviewer output:**
```text
Critical: SKILL.md:1 - Missing required 'name' field in frontmatter
Major: SKILL.md:3 - Description uses second person ("you should use")
Major: Missing "When NOT to Use" section
Minor: Line 45 is verbose
```

**Fixes applied:**
- Added name field to frontmatter
- Rewrote description in third person
- Added "When NOT to Use" section

**Iteration 2 — run skill-reviewer again to verify fixes:**
```text
Minor: Line 45 is verbose
```

**Minor issue evaluation:**
Line 45 communicates effectively as-is. The verbosity provides useful context. Skip.

**All critical/major issues resolved. Output the completion marker:**
```
<skill-improvement-complete>
```

Note: The marker MUST appear in the output. Statements like "quality bar met" or "looks good" will NOT stop the loop.

## Completion Criteria

**CRITICAL**: The stop hook ONLY checks for the explicit marker below. No other signal will terminate the loop.

Output this marker when done:

```
<skill-improvement-complete>
```

**When to output the marker:**

1. **skill-reviewer reports "Pass"** or **no issues found** → output marker immediately
2. **All critical and major issues are fixed** AND you've verified the fixes → output marker
3. **Remaining issues are only minor** AND you've evaluated them as false positives or not worth fixing → output marker

**When NOT to output the marker:**

- Any critical issue remains unfixed
- Any major issue remains unfixed
- You haven't run skill-reviewer to verify your fixes worked

The marker is the ONLY way to complete the loop. Natural language like "looks good" or "quality bar met" will NOT stop the loop.

## Rationalizations to Reject

- "I'll just mark it complete and come back later" - Fix issues now
- "This minor issue seems wrong, I'll skip all of them" - Evaluate each one individually
- "The reviewer is being too strict" - The quality bar exists for a reason
- "It's good enough" - If there are major issues, it's not good enough


<!-- MERGED INTO: skill-creator on 2026-04-18 -->
<!-- Use `skill-creator` instead. -->
