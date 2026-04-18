---
name: engineering-craft
description: "Use when writing new code, reviewing PRs, refactoring, or auditing an existing codebase for accumulated debt. Covers two complementary modes: CRAFT (preventive standards for clean, readable, maintainable code) and TRIAGE (identifying, categorizing, and prioritizing technical debt for remediation). Triggers: 'review this code', 'refactor', 'code smell', 'tech debt', 'clean up', 'this is messy', 'how do I name this', 'is this well-structured', 'what should we fix first'."
metadata:
  version: 1.0.0
  source: maeve-merge
  merged_from: [clean-code, tech-debt]
  date_merged: "2026-04-18"
  preferred_model: sonnet
---

# Engineering Craft

Two modes, one skill. **CRAFT** for writing clean code. **TRIAGE** for dealing with the mess that already exists.

---

## Activation

| Request type | Mode |
|---|---|
| Writing new code, naming, structuring functions | CRAFT |
| Reviewing a PR, catching smells | CRAFT |
| Auditing an existing codebase | TRIAGE |
| "What should we fix first?" | TRIAGE |
| Refactoring legacy code | Both -- TRIAGE to identify, CRAFT to execute |

---

## MODE: CRAFT

### Core Principle
> "Code is clean if it can be read and enhanced by a developer other than its original author." -- Grady Booch

Clean code is not about aesthetics. It is about the next person (often future-you) being able to understand, change, and extend the code without fear.

### Naming
- Names reveal intent: `elapsedTimeInDays` not `d`.
- Avoid disinformation: don't call it `accountList` if it's a `Map`.
- Classes are nouns (`Customer`, `WikiPage`). Avoid `Manager`, `Processor`, `Data`.
- Methods are verbs (`postPayment`, `deletePage`, `isEligibleForFullBenefits`).
- Searchable names only. Single-letter variables exist only as loop counters.

### Functions
- Small. Smaller than you think. Under 20 lines is a ceiling, not a target.
- Do one thing. If you need "and" to describe it, split it.
- One level of abstraction per function. Don't mix business logic with string parsing.
- Arguments: 0 is ideal, 1-2 acceptable, 3+ requires justification, 4+ is a design smell.
- No side effects. A function named `checkPassword` should not initialize a session.

### Comments
- Bad comments are a failure to express intent in code. Rewrite the code first.
- Good comments: legal notices, intent behind a non-obvious algorithm, TODO with owner.
- Bad comments: restating what the code does, commented-out code, position markers.
- The best comment is a well-named function that makes the comment unnecessary.

### Structure and Formatting
- Newspaper metaphor: high-level concept at the top, implementation detail at the bottom.
- Related lines travel together. Unrelated lines have whitespace between them.
- Declare variables close to their use.
- Dependent functions: caller above callee.

### Error Handling
- Exceptions over return codes. Return codes pollute the call chain.
- Write try-catch-finally first -- it defines the transaction boundary.
- Never return null. Never pass null. Both force the caller to deal with your failure.
- Error messages must have enough context to diagnose the problem.

### Classes
- Single Responsibility Principle: one reason to change.
- Small. If you need to scroll to see the whole class, it's doing too much.
- Stepdown rule: public interface at the top, private implementation below.
- Law of Demeter: don't chain `a.getB().getC().doSomething()`. You shouldn't know that much.

### Code Smell Checklist
- [ ] Function under 20 lines and does exactly one thing?
- [ ] Every name intention-revealing and searchable?
- [ ] Comments explain *why*, not *what*?
- [ ] No null returns or null arguments?
- [ ] Classes have a single, stateable responsibility?
- [ ] No duplicated logic anywhere in the call chain?

---

## MODE: TRIAGE

### Debt Taxonomy

**Deliberate debt** -- a conscious tradeoff. Acceptable with a documented payoff date.
**Accidental debt** -- lack of knowledge at time of writing. Most common. Fix with refactor.
**Bit rot** -- code that was fine when written but the world changed around it. Requires audit.
**Test debt** -- missing or inadequate tests. The most dangerous because it hides everything else.

### Identification Patterns

When auditing a codebase, scan for:
- Functions over 30 lines
- Files over 300 lines
- Cyclomatic complexity over 10 (more than 10 decision branches in one function)
- Test coverage under 60% on business-critical paths
- TODO/FIXME/HACK comments older than 90 days
- Duplicate logic across more than 2 locations
- Direct database access outside data layer
- Hardcoded configuration values
- Missing error handling on I/O operations
- Dependency on deprecated libraries or EOL runtimes

### Prioritization Framework (WSJF)

**Weighted Shortest Job First** -- score each debt item on three axes, divide by effort:

```
WSJF = (Business Value + Time Criticality + Risk Reduction) / Job Size
```

Score each axis 1-8 (Fibonacci). Highest WSJF score = fix first.

| Axis | High score means... |
|---|---|
| Business Value | Fixing this unblocks features or revenue |
| Time Criticality | Gets worse or more expensive the longer we wait |
| Risk Reduction | Active security, data integrity, or stability risk |
| Job Size (divisor) | Small = high WSJF; large = lower priority unless other scores are extreme |

### Debt Remediation Sequence

1. **Stabilize** -- add tests around the debt area before touching anything. No tests = no refactor.
2. **Isolate** -- extract the debt behind an interface so changes are contained.
3. **Replace** -- rewrite the isolated unit cleanly using CRAFT mode standards.
4. **Verify** -- tests pass, behavior unchanged, complexity score improved.
5. **Document** -- update any ADRs or comments that referenced the old approach.

### Output Format for Debt Reports

When asked to produce a debt report:

```
CRITICAL  (fix before next deploy):   <items with active risk>
HIGH      (fix this sprint):          <items blocking velocity>
MEDIUM    (schedule in next quarter): <items with accumulating cost>
LOW       (backlog):                  <items that are minor or stable>
DEFERRED  (documented tradeoff):      <deliberate debt with payoff date>
```

---

## MODE: REVIEW (PR / Code Audit)

When reviewing existing code rather than writing new code.

### Process
1. Read context and requirements first -- understand intent before judging execution.
2. Run TRIAGE scan mentally -- identify debt category before labeling severity.
3. Provide actionable feedback with rationale, not just verdicts.
4. Ask clarifying questions when intent is genuinely unclear.

### Output Format
```
SUMMARY: <1-2 sentence overall assessment>

BLOCKING:   <must fix before merge -- correctness, security, data integrity>
IMPORTANT:  <should fix -- maintainability, performance, test gaps>
MINOR:      <nice to fix -- style, naming, minor structure>
QUESTIONS:  <unclear intent requiring author clarification>
CLEAN:      <explicitly confirm what is correct -- don't leave it implicit>
```

### Review Anti-patterns
- Gatekeeping tone. Reviews are knowledge transfer, not approval theater.
- Vague feedback. "This is messy" is not actionable. Cite the smell, explain the fix.
- Ignoring test coverage. Missing tests on changed paths is always at least IMPORTANT.
- Reviewing style over substance. Run CRAFT checks mentally, not as the primary output.
