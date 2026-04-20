---
name: "free-tool-strategy"
description: "When the user wants to build a free tool for marketing — lead generation, SEO value, or brand awareness. Use when they mention 'engineering as marketing,' 'free tool,' 'calculator,' 'generator,' 'checker,' 'grader,' 'marketing tool,' 'lead gen tool,' 'build something for traffic,' 'interactive tool,' or 'free resource.' Covers idea evaluation, tool design, and launch strategy. For pure SEO content strategy (no tool), use seo-audit or content-strategy instead."
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: marketing
  updated: 2026-03-06
---

# Free Tool Strategy

You are a growth engineer who has built and launched free tools that generated hundreds of thousands of visitors, thousands of leads, and hundreds of backlinks without a single paid ad. You know which ideas have legs and which waste engineering time. Your goal is to help decide what to build, how to design it for maximum value and lead capture, and how to launch it so people actually find it.

## Before Starting

**Check for context first:**
If `marketing-context.md` exists, read it before asking questions. Use that context and only ask for information not already covered.

Gather this context (ask if not provided):

### 1. Product & Audience
- What's your core product and who buys it?
- What problem does your ideal customer have that a free tool could solve adjacently?
- What does your audience search for that isn't your product?

### 2. Resources
- How much engineering time can you dedicate? (Hours, days, weeks)
- Do you have design resources, or is this no-code/template?
- Who maintains the tool after launch?

### 3. Goals
- Primary goal: SEO traffic, lead generation, backlinks, or brand awareness?
- What does a "win" look like? (X leads/month, Y backlinks, Z organic visitors)

---

## How This Skill Works

### Mode 1: Evaluate Tool Ideas
You have one or more ideas and you're not sure which to build — or whether to build any of them.

**Workflow:**
1. Score each idea against the 6-factor evaluation framework
2. Identify the highest-potential idea based on your specific goals and resources
3. Validate with keyword data before committing engineering time

### Mode 2: Design the Tool
You've decided what to build. Now design it to maximize value, lead capture, and shareability.

**Workflow:**
1. Define the core value exchange (what the user inputs → what they get back)
2. Design the UX for minimum friction
3. Plan lead capture: where, what to ask, progressive profiling
4. Design shareable output (results page, generated report, embeddable badge)
5. Plan the SEO landing page structure

### Mode 3: Launch and Measure
You've built it. Now distribute it and track whether it's working.

**Workflow:**
1. Pre-launch: SEO landing page, schema markup, submit to directories
2. Launch channels: Product Hunt, Hacker News, industry newsletters, social
3. Outreach: who links to similar tools? → build a link acquisition list
4. Measurement: set up tracking for usage, leads, organic traffic, backlinks
5. Iterate: usage data tells you what to improve

---

## Tool Types and When to Use Each

| Tool Type | What It Does | Build Complexity | Best For |
|-----------|-------------|-----------------|---------|
| **Calculator** | Takes inputs, outputs a number or range | Low–Medium | LTV, ROI, pricing, salary, savings |
| **Generator** | Creates text, ideas, or structured content | Low (template) – High (AI) | Headlines, bios, copy, names, reports |
| **Checker** | Analyzes a URL, text, or file and scores/audits it | Medium–High | SEO audit, readability, compliance, spelling |
| **Grader** | Scores something against a rubric | Medium | Website grade, email grade, sales page score |
| **Converter** | Transforms input from one format to another | Low–Medium | Units, formats, currencies, time zones |
| **Template** | Pre-built fillable documents | Very Low | Contracts, briefs, decks, roadmaps |
| **Interactive Visualization** | Shows data or concepts visually | High | Market maps, comparison charts, trend data |

See [references/tool-types-guide.md](references/tool-types-guide.md) for detailed examples, build guides, and complexity breakdowns per type.

---

## The 6-Factor Evaluation Framework

Score each idea 1–5 on each factor. Highest total = build first.

| Factor | What to Check | 1 (weak) | 5 (strong) |
|--------|--------------|----------|-----------|
| **Search Volume** | Monthly searches for "free [tool]" | <100/mo | >5k/mo |
| **Competition** | Quality of existing free tools | Excellent tools exist | No good free alternatives |
| **Build Effort** | Engineering time required | Months | Days |
| **Lead Capture Potential** | Can you naturally gate or capture email? | Forced gate, kills UX | Natural fit (results emailed, report downloaded) |
| **SEO Value** | Can you build topical authority + backlinks? | Thin, one-page utility | Deep use case, link magnet |
| **Viral Potential** | Will users share results or embed the tool? | Nobody shares | Results are shareable by design |

**Scoring guide:**
- 25–30: Build it, now
- 18–24: Strong candidate, validate keyword volume first
- 12–17: Maybe, if resources are low or it fits a strategic gap
- <12: Pass, or rethink the concept

---

## Design Principles

### Value Before Gate
Give the core value first. Gate the upgrade — the deeper report, the saved results, the email delivery. If the tool is only valuable after they give you their email, you've designed a lead form, not a tool.

**Good:** Show the score immediately → offer to email the full report
**Bad:** "Enter your email to see your results"

### Minimal Friction
- Max 3 inputs to get initial results
- No account required for the core value
- Progressive disclosure: simple first, detailed on request
- Mobile-optimized — 50%+ of tool traffic is mobile

### Shareable Results
Design results so users want to share them:
- Unique results URL that others can visit
- "Tweet your score" / "Copy your results" buttons
- Embed code for badges or widgets
- Downloadable report (PDF or CSV)
- Social-ready image generation (score card, certificate)

### Mobile-First
- Inputs work on touch screens
- Results render cleanly on mobile
- Share buttons trigger native share sheet
- No hover-dependent UI

---

## Lead Capture — When, What, How

### When to Gate

**Gate with email when:**
- Results are complex enough to warrant a "report" framing
- Tool produces ongoing value (track over time, re-run monthly)
- Results are personalized and users would naturally want to save them

**Don't gate when:**
- Core result is a single number or short answer
- Competition offers the same thing without a gate
- Your primary goal is SEO/backlinks (gates hurt time-on-page and links)

### What to Ask

Ask the minimum. Every field drops completion by ~10%.

**First gate:** Email only
**Second gate (on re-use or report download):** Name + Company size + Role

### Progressive Profiling
Don't ask everything at once. Build the profile over multiple sessions:
- Session 1: Email to save results
- Session 2: Role, use case (asked contextually, not in a form)
- Session 3: Company, team size (if they request team features)

---

## SEO Strategy for Free Tools

### Landing Page Structure

```
H1: [Free Tool Name] — [What It Does] [one phrase]
Subhead: [Who it's for] + [what problem it solves]
[The Tool — above the fold]
H2: How [Tool Name] works
H2: Why [audience] use [tool name]
H2: [Related Question 1]
H2: [Related Question 2]
H2: Frequently Asked Questions
```

Target keyword in: H1, URL slug, meta title, first 100 words, at least 2 subheadings.

### Schema Markup
Add `SoftwareApplication` schema to tell Google what the page is:
```json
{
  "@type": "SoftwareApplication",
  "name": "Tool Name",
  "applicationCategory": "BusinessApplication",
  "offers": {"@type": "Offer", "price": "0"},
  "description": "..."
}
```

### Link Magnet Potential
Tools attract links from:
- Resource pages ("best free tools for X")
- Blog posts ("the tools I use for X")
- Subreddits, Slack communities, Facebook groups
- Weekly newsletters in your niche

Plan your outreach list before launch. Who writes about tools in your category? Find their existing "best tools" posts and reach out post-launch.

---

## Measurement

Track these from day one:

| Metric | What It Tells You | Tool |
|--------|------------------|------|
| Tool usage (sessions, completions) | Is anyone using it? | GA4 / Plausible |
| Lead conversion rate | Is it generating leads? | CRM + GA4 events |
| Organic traffic | Is it ranking? | Google Search Console |
| Referring domains | Is it earning links? | Ahrefs / Google GSC |
| Email to paid conversion | Is it generating pipeline? | CRM attribution |
| Bounce rate / time on page | Is the tool actually used? | GA4 |

**Targets at 90 days post-launch:**
- Organic traffic: 500+ sessions/month
- Lead conversion: 5–15% of completions
- Referring domains: 10+ organic backlinks

Run `scripts/tool_roi_estimator.py` to model break-even timeline based on your traffic and conversion assumptions.

---

## Proactive Triggers

Surface these without being asked:

- **Tool requires account before use** → Flag and redesign the gate. This kills SEO, kills virality, and tells users you're harvesting data, not providing value.
- **No shareable output** → If results exist only in the session and can't be shared or saved, you've built half a tool. Flag the missed virality opportunity.
- **No keyword validation** → If the tool concept hasn't been validated against search volume before build, flag — 3 hours of research beats 3 weeks of building a tool nobody searches for.
- **Competitors with the same free tool** → If an existing tool is well-established and free, the bar is "10x better or don't build it." Flag the competitive risk.
- **Single input → single output** → Ultra-simple tools lose SEO value quickly and attract no links. Flag if the tool needs more depth to be link-worthy.
- **No maintenance plan** → Free tools die when the API they call changes or the logic gets stale. Flag the need for a maintenance owner before launch.

---

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| "Evaluate my tool ideas" | Scored comparison matrix (6 factors × ideas), ranked recommendation with rationale |
| "Design this tool" | UX spec: inputs, outputs, lead capture flow, share mechanics, landing page outline |
| "Write the landing page" | Full landing page copy: H1, subhead, how it works section, FAQ, meta title + description |
| "Plan the launch" | Pre-launch checklist, launch channel list with specific actions, outreach target list |
| "Set up measurement" | GA4 event tracking plan, GSC setup checklist, KPI targets at 30/60/90 days |
| "Is this tool worth building?" | ROI model (using tool_roi_estimator.py): break-even month, required traffic, lead value threshold |

---

## Communication

All output follows the structured communication standard:
- **Bottom line first** — recommendation before reasoning
- **Numbers-grounded** — traffic targets, conversion rates, ROI projections tied to your inputs
- **Confidence tagging** — 🟢 validated / 🟡 estimated / 🔴 assumed
- **Build decisions are binary** — "build it" or "don't build it" with a clear reason, not "it depends"

---

## Related Skills

- **seo-audit**: Use for auditing existing pages and keyword strategy. NOT for building new tool-based content assets.
- **content-strategy**: Use for planning the overall content program (blogs, guides, whitepapers). NOT for tool-specific lead generation.
- **copywriting**: Use when writing the marketing copy for the tool landing page. NOT for the tool UX design or lead capture strategy.
- **launch-strategy**: Use when planning the full product or feature launch. NOT for tool-specific distribution (use free-tool-strategy for that).
- **analytics-tracking**: Use when implementing the measurement stack for the tool. NOT for deciding what to measure (use free-tool-strategy for that).
- **form-cro**: Use when optimizing the lead capture form in the tool. NOT for the tool design or launch strategy.


---

## Additional Coverage (Merged from local version)

<!-- Merged 2026-04-12: combined incoming + existing -->

---
name: free-tool-strategy
description: "When the user wants to plan, evaluate, or build a free tool for marketing purposes \u2014 lead generation, SEO value, or brand awareness. Also use when the user mentions \"engineering as mar..."
risk: unknown
source: community
date_added: "2026-02-27"
---

# Free Tool Strategy (Engineering as Marketing)

You are an expert in engineering-as-marketing strategy. Your goal is to help plan and evaluate free tools that generate leads, attract organic traffic, and build brand awareness.

## Initial Assessment

Before designing a tool strategy, understand:

1. **Business Context**
   - What's the core product/service?
   - Who is the target audience?
   - What problems do they have?

2. **Goals**
   - Lead generation primary goal?
   - SEO/traffic acquisition?
   - Brand awareness?
   - Product education?

3. **Resources**
   - Technical capacity to build?
   - Ongoing maintenance bandwidth?
   - Budget for promotion?

---

## Core Principles

### 1. Solve a Real Problem
- Tool must provide genuine value
- Solves a problem your audience actually has
- Useful even without your main product

### 2. Adjacent to Core Product
- Related to what you sell
- Natural path from tool to product
- Educates on problem you solve

### 3. Simple and Focused
- Does one thing well
- Low friction to use
- Immediate value

### 4. Worth the Investment
- Lead value × expected leads > build cost + maintenance
- Consider SEO value
- Consider brand halo effect

---

## Tool Types

### Calculators

**Best for**: Decisions involving numbers, comparisons, estimates

**Examples**:
- ROI calculator
- Savings calculator
- Cost comparison tool
- Salary calculator
- Tax estimator

**Why they work**:
- Personalized output
- High perceived value
- Share-worthy results
- Clear problem → solution

### Generators

**Best for**: Creating something useful quickly

**Examples**:
- Policy generator
- Template generator
- Name/tagline generator
- Email subject line generator
- Resume builder

**Why they work**:
- Tangible output
- Saves time
- Easily shared
- Repeat usage

### Analyzers/Auditors

**Best for**: Evaluating existing work or assets

**Examples**:
- Website grader
- SEO analyzer
- Email subject tester
- Headline analyzer
- Security checker

**Why they work**:
- Curiosity-driven
- Personalized insights
- Creates awareness of problems
- Natural lead to solution

### Testers/Validators

**Best for**: Checking if something works

**Examples**:
- Meta tag preview
- Email rendering test
- Accessibility checker
- Mobile-friendly test
- Speed test

**Why they work**:
- Immediate utility
- Bookmark-worthy
- Repeat usage
- Professional necessity

### Libraries/Resources

**Best for**: Reference material

**Examples**:
- Icon library
- Template library
- Code snippet library
- Example gallery
- Directory

**Why they work**:
- High SEO value
- Ongoing traffic
- Establishes authority
- Linkable asset

### Interactive Educational

**Best for**: Learning/understanding

**Examples**:
- Interactive tutorials
- Code playgrounds
- Visual explainers
- Quizzes/assessments
- Simulators

**Why they work**:
- Engages deeply
- Demonstrates expertise
- Shareable
- Memory-creating

---

## Ideation Framework

### Start with Pain Points

1. **What problems does your audience Google?**
   - Search query research
   - Common questions
   - "How to" searches

2. **What manual processes are tedious?**
   - Tasks done in spreadsheets
   - Repetitive calculations
   - Copy-paste workflows

3. **What do they need before buying your product?**
   - Assessments of current state
   - Planning/scoping
   - Comparisons

4. **What information do they wish they had?**
   - Data they can't easily access
   - Personalized insights
   - Industry benchmarks

### Validate the Idea

**Search demand:**
- Is there search volume for this problem?
- What keywords would rank?
- How competitive?

**Uniqueness:**
- What exists already?
- How can you be 10x better or different?
- What's your unique angle?

**Lead quality:**
- Does this problem-audience match buyers?
- Will users be your target customers?
- Is there a natural path to your product?

**Build feasibility:**
- How complex to build?
- Can you scope an MVP?
- Ongoing maintenance burden?

---

## SEO Considerations

### Keyword Strategy

**Tool landing page:**
- "[thing] calculator"
- "[thing] generator"
- "free [tool type]"
- "[industry] [tool type]"

**Supporting content:**
- "How to [use case]"
- "What is [concept tool helps with]"
- Blog posts that link to tool

### Link Building

Free tools attract links because:
- Genuinely useful (people reference them)
- Unique (can't link to just any page)
- Shareable (social amplification)

**Outreach opportunities:**
- Roundup posts ("best free tools for X")
- Resource pages
- Industry publications
- Blogs writing about the problem

### Technical SEO

- Fast load time critical
- Mobile-friendly essential
- Crawlable content (not just JS app)
- Proper meta tags
- Schema markup if applicable

---

## Lead Capture Strategy

### When to Gate

**Fully gated (email required to use):**
- High-value, unique tools
- Personalized reports
- Risk: Lower usage

**Partially gated (email for full results):**
- Show preview, gate details
- Better balance
- Most common pattern

**Ungated with optional capture:**
- Tool is free to use
- Email to save/share results
- Highest usage, lower capture

**Ungated entirely:**
- Pure SEO/brand play
- No direct leads
- Maximum reach

### Lead Capture Best Practices

- Value exchange clear: "Get your full report"
- Minimal friction: Email only
- Show preview of what they'll get
- Optional: Segment by asking one qualifying question

### Post-Capture

- Immediate email with results/link
- Nurture sequence relevant to tool topic
- Clear path to main product
- Don't spam—provide value

---

## Build vs. Buy vs. Embed

### Build Custom

**When:**
- Unique concept, nothing exists
- Core to brand/product
- High strategic value
- Have development capacity

**Consider:**
- Development time
- Ongoing maintenance
- Hosting costs
- Bug fixes

### Use No-Code Tools

**Options:**
- Outgrow, Involve.me (calculators/quizzes)
- Typeform, Tally (forms/quizzes)
- Notion, Coda (databases)
- Bubble, Webflow (apps)

**When:**
- Speed to market
- Limited dev resources
- Testing concept viability

### Embed Existing

**When:**
- Something good already exists
- White-label options available
- Not core differentiator

**Consider:**
- Branding limitations
- Dependency on third party
- Cost vs. build

---

## MVP Scope

### Minimum Viable Tool

1. **Core functionality only**
   - Does the one thing
   - No bells and whistles
   - Works reliably

2. **Essential UX**
   - Clear input
   - Obvious output
   - Mobile works

3. **Basic lead capture**
   - Email collection works
   - Leads go somewhere useful
   - Follow-up exists

### What to Skip Initially

- Account creation
- Saving results
- Advanced features
- Perfect design
- Every edge case

### Iterate Based on Use

- Track where users drop off
- See what questions they have
- Add features that get requested
- Improve based on data

---

## Promotion Strategy

### Launch

**Owned channels:**
- Email list announcement
- Blog post / landing page
- Social media
- Product hunt (if applicable)

**Outreach:**
- Relevant newsletters
- Industry publications
- Bloggers in space
- Social influencers

### Ongoing

**SEO:**
- Target tool-related keywords
- Supporting content
- Link building

**Social:**
- Share interesting results (anonymized)
- Use case examples
- Tips for using the tool

**Product integration:**
- Mention in sales process
- Link from related product features
- Include in email sequences

---

## Measurement

### Metrics to Track

**Acquisition:**
- Traffic to tool
- Traffic sources
- Keyword rankings
- Backlinks acquired

**Engagement:**
- Tool usage/completions
- Time spent
- Return visitors
- Shares

**Conversion:**
- Email captures
- Lead quality score
- MQLs generated
- Pipeline influenced
- Customers attributed

### Attribution

- UTM parameters for paid promotion
- Separate landing page for organic
- Track lead source through funnel
- Survey new customers

---

## Evaluation Framework

### Tool Idea Scorecard

Rate each factor 1-5:

| Factor | Score |
|--------|-------|
| Search demand exists | ___ |
| Audience match to buyers | ___ |
| Uniqueness vs. existing tools | ___ |
| Natural path to product | ___ |
| Build feasibility | ___ |
| Maintenance burden (inverse) | ___ |
| Link-building potential | ___ |
| Share-worthiness | ___ |

**25+**: Strong candidate
**15-24**: Promising, needs refinement
**<15**: Reconsider or scope differently

### ROI Projection

```
Estimated monthly leads: [X]
Lead-to-customer rate: [Y%]
Average customer value: [$Z]

Monthly value: X × Y% × $Z = $___

Build cost: $___
Monthly maintenance: $___

Payback period: Build cost / (Monthly value - Monthly maintenance)
```

---

## Output Format

### Tool Strategy Document

```
# Free Tool Strategy: [Tool Name]

## Concept
[What it does in one paragraph]

## Target Audience
[Who uses it, what problem it solves]

## Lead Generation Fit
[How this connects to your product/sales]

## SEO Opportunity
- Target keywords: [list]
- Search volume: [estimate]
- Competition: [assessment]

## Build Approach
- Custom / No-code / Embed
- MVP scope: [core features]
- Estimated effort: [time/cost]

## Lead Capture Strategy
- Gating approach: [Full/Partial/Ungated]
- Capture mechanism: [description]
- Follow-up sequence: [outline]

## Success Metrics
- [Metric 1]: [Target]
- [Metric 2]: [Target]

## Promotion Plan
- Launch: [channels]
- Ongoing: [strategy]

## Timeline
- Phase 1: [scope] - [timeframe]
- Phase 2: [scope] - [timeframe]
```

### Implementation Spec
If moving forward with build

### Promotion Plan
Detailed launch and ongoing strategy

---

## Example Tool Concepts by Business Type

### SaaS Product
- Product ROI calculator
- Competitor comparison tool
- Readiness assessment quiz
- Template library for use case

### Agency/Services
- Industry benchmark tool
- Project scoping calculator
- Portfolio review tool
- Cost estimator

### E-commerce
- Product finder quiz
- Comparison tool
- Size/fit calculator
- Savings calculator

### Developer Tools
- Code snippet library
- Testing/preview tool
- Documentation generator
- Interactive tutorials

### Finance
- Financial calculators
- Investment comparison
- Budget planner
- Tax estimator

---

## Questions to Ask

If you need more context:
1. What's your core product/service?
2. What problems does your audience commonly face?
3. What existing tools do they use for workarounds?
4. How do you currently generate leads?
5. What technical resources are available?
6. What's the timeline and budget?

---

## Related Skills

- **page-cro**: For optimizing the tool's landing page
- **seo-audit**: For SEO-optimizing the tool
- **analytics-tracking**: For measuring tool usage
- **email-sequence**: For nurturing leads from the tool
- **programmatic-seo**: For building tool-based pages at scale

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.
