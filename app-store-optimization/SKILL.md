---
name: "app-store-optimization"
description: App Store Optimization (ASO) toolkit for researching keywords, analyzing competitor rankings, generating metadata suggestions, and improving app visibility on Apple App Store and Google Play Store. Use when the user asks about ASO, app store rankings, app metadata, app titles and descriptions, app store listings, app visibility, or mobile app marketing on iOS or Android. Supports keyword research and scoring, competitor keyword analysis, metadata optimization, A/B test planning, launch checklists, and tracking ranking changes.
triggers:
  - ASO
  - app store optimization
  - app store ranking
  - app keywords
  - app metadata
  - play store optimization
  - app store listing
  - improve app rankings
  - app visibility
  - app store SEO
  - mobile app marketing
  - app conversion rate
---

# App Store Optimization (ASO)

---

## Keyword Research Workflow

Discover and evaluate keywords that drive app store visibility.

### Workflow: Conduct Keyword Research

1. Define target audience and core app functions:
   - Primary use case (what problem does the app solve)
   - Target user demographics
   - Competitive category
2. Generate seed keywords from:
   - App features and benefits
   - User language (not developer terminology)
   - App store autocomplete suggestions
3. Expand keyword list using:
   - Modifiers (free, best, simple)
   - Actions (create, track, organize)
   - Audiences (for students, for teams, for business)
4. Evaluate each keyword:
   - Search volume (estimated monthly searches)
   - Competition (number and quality of ranking apps)
   - Relevance (alignment with app function)
5. Score and prioritize keywords:
   - Primary: Title and keyword field (iOS)
   - Secondary: Subtitle and short description
   - Tertiary: Full description only
6. Map keywords to metadata locations
7. Document keyword strategy for tracking
8. **Validation:** Keywords scored; placement mapped; no competitor brand names included; no plurals in iOS keyword field

### Keyword Evaluation Criteria

| Factor | Weight | High Score Indicators |
|--------|--------|----------------------|
| Relevance | 35% | Describes core app function |
| Volume | 25% | 10,000+ monthly searches |
| Competition | 25% | Top 10 apps have <4.5 avg rating |
| Conversion | 15% | Transactional intent ("best X app") |

### Keyword Placement Priority

| Location | Search Weight |
|----------|---------------|
| App Title | Highest |
| Subtitle (iOS) | High |
| Keyword Field (iOS) | High |
| Short Description (Android) | High |
| Full Description | Medium |

See: [references/keyword-research-guide.md](references/keyword-research-guide.md)

---

## Metadata Optimization Workflow

Optimize app store listing elements for search ranking and conversion.

### Workflow: Optimize App Metadata

1. Audit current metadata against platform limits:
   - Title character count and keyword presence
   - Subtitle/short description usage
   - Keyword field efficiency (iOS)
   - Description keyword density
2. Optimize title following formula:
   ```
   [Brand Name] - [Primary Keyword] [Secondary Keyword]
   ```
3. Write subtitle (iOS) or short description (Android):
   - Focus on primary benefit
   - Include secondary keyword
   - Use action verbs
4. Optimize keyword field (iOS only):
   - Remove duplicates from title
   - Remove plurals (Apple indexes both forms)
   - No spaces after commas
   - Prioritize by score
5. Rewrite full description:
   - Hook paragraph with value proposition
   - Feature bullets with keywords
   - Social proof section
   - Call to action
6. Validate character counts for each field
7. Calculate keyword density (target 2-3% primary)
8. **Validation:** All fields within character limits; primary keyword in title; no keyword stuffing (>5%); natural language preserved

### Platform Character Limits

| Field | Apple App Store | Google Play Store |
|-------|-----------------|-------------------|
| Title | 30 characters | 50 characters |
| Subtitle | 30 characters | N/A |
| Short Description | N/A | 80 characters |
| Keywords | 100 characters | N/A |
| Promotional Text | 170 characters | N/A |
| Full Description | 4,000 characters | 4,000 characters |
| What's New | 4,000 characters | 500 characters |

### Description Structure

```
PARAGRAPH 1: Hook (50-100 words)
├── Address user pain point
├── State main value proposition
└── Include primary keyword

PARAGRAPH 2-3: Features (100-150 words)
├── Top 5 features with benefits
├── Bullet points for scanability
└── Secondary keywords naturally integrated

PARAGRAPH 4: Social Proof (50-75 words)
├── Download count or rating
├── Press mentions or awards
└── Summary of user testimonials

PARAGRAPH 5: Call to Action (25-50 words)
├── Clear next step
└── Reassurance (free trial, no signup)
```

See: [references/platform-requirements.md](references/platform-requirements.md)

---

## Competitor Analysis Workflow

Analyze top competitors to identify keyword gaps and positioning opportunities.

### Workflow: Analyze Competitor ASO Strategy

1. Identify top 10 competitors:
   - Direct competitors (same core function)
   - Indirect competitors (overlapping audience)
   - Category leaders (top downloads)
2. Extract competitor keywords from:
   - App titles and subtitles
   - First 100 words of descriptions
   - Visible metadata patterns
3. Build competitor keyword matrix:
   - Map which keywords each competitor targets
   - Calculate coverage percentage per keyword
4. Identify keyword gaps:
   - Keywords with <40% competitor coverage
   - High volume terms competitors miss
   - Long-tail opportunities
5. Analyze competitor visual assets:
   - Icon design patterns
   - Screenshot messaging and style
   - Video presence and quality
6. Compare ratings and review patterns:
   - Average rating by competitor
   - Common praise themes
   - Common complaint themes
7. Document positioning opportunities
8. **Validation:** 10+ competitors analyzed; keyword matrix complete; gaps identified with volume estimates; visual audit documented

### Competitor Analysis Matrix

| Analysis Area | Data Points |
|---------------|-------------|
| Keywords | Title keywords, description frequency |
| Metadata | Character utilization, keyword density |
| Visuals | Icon style, screenshot count/style |
| Ratings | Average rating, total count, velocity |
| Reviews | Top praise, top complaints |

### Gap Analysis Template

| Opportunity Type | Example | Action |
|------------------|---------|--------|
| Keyword gap | "habit tracker" (40% coverage) | Add to keyword field |
| Feature gap | Competitor lacks widget | Highlight in screenshots |
| Visual gap | No videos in top 5 | Create app preview |
| Messaging gap | None mention "free" | Test free positioning |

---

## App Launch Workflow

Execute a structured launch for maximum initial visibility.

### Workflow: Launch App to Stores

1. Complete pre-launch preparation (4 weeks before):
   - Finalize keywords and metadata
   - Prepare all visual assets
   - Set up analytics (Firebase, Mixpanel)
   - Build press kit and media list
2. Submit for review (2 weeks before):
   - Complete all store requirements
   - Verify compliance with guidelines
   - Prepare launch communications
3. Configure post-launch systems:
   - Set up review monitoring
   - Prepare response templates
   - Configure rating prompt timing
4. Execute launch day:
   - Verify app is live in both stores
   - Announce across all channels
   - Begin review response cycle
5. Monitor initial performance (days 1-7):
   - Track download velocity hourly
   - Monitor reviews and respond within 24 hours
   - Document any issues for quick fixes
6. Conduct 7-day retrospective:
   - Compare performance to projections
   - Identify quick optimization wins
   - Plan first metadata update
7. Schedule first update (2 weeks post-launch)
8. **Validation:** App live in stores; analytics tracking; review responses within 24h; download velocity documented; first update scheduled

### Pre-Launch Checklist

| Category | Items |
|----------|-------|
| Metadata | Title, subtitle, description, keywords |
| Visual Assets | Icon, screenshots (all sizes), video |
| Compliance | Age rating, privacy policy, content rights |
| Technical | App binary, signing certificates |
| Analytics | SDK integration, event tracking |
| Marketing | Press kit, social content, email ready |

### Launch Timing Considerations

| Factor | Recommendation |
|--------|----------------|
| Day of week | Tuesday-Wednesday (avoid weekends) |
| Time of day | Morning in target market timezone |
| Seasonal | Align with relevant category seasons |
| Competition | Avoid major competitor launch dates |

See: [references/aso-best-practices.md](references/aso-best-practices.md)

---

## A/B Testing Workflow

Test metadata and visual elements to improve conversion rates.

### Workflow: Run A/B Test

1. Select test element (prioritize by impact):
   - Icon (highest impact)
   - Screenshot 1 (high impact)
   - Title (high impact)
   - Short description (medium impact)
2. Form hypothesis:
   ```
   If we [change], then [metric] will [improve/increase] by [amount]
   because [rationale].
   ```
3. Create variants:
   - Control: Current version
   - Treatment: Single variable change
4. Calculate required sample size:
   - Baseline conversion rate
   - Minimum detectable effect (usually 5%)
   - Statistical significance (95%)
5. Launch test:
   - Apple: Use Product Page Optimization
   - Android: Use Store Listing Experiments
6. Run test for minimum duration:
   - At least 7 days
   - Until statistical significance reached
7. Analyze results:
   - Compare conversion rates
   - Check statistical significance
   - Document learnings
8. **Validation:** Single variable tested; sample size sufficient; significance reached (95%); results documented; winner implemented

### A/B Test Prioritization

| Element | Conversion Impact | Test Complexity |
|---------|-------------------|-----------------|
| App Icon | 10-25% lift possible | Medium (design needed) |
| Screenshot 1 | 15-35% lift possible | Medium |
| Title | 5-15% lift possible | Low |
| Short Description | 5-10% lift possible | Low |
| Video | 10-20% lift possible | High |

### Sample Size Quick Reference

| Baseline CVR | Impressions Needed (per variant) |
|--------------|----------------------------------|
| 1% | 31,000 |
| 2% | 15,500 |
| 5% | 6,200 |
| 10% | 3,100 |

### Test Documentation Template

```
TEST ID: ASO-2025-001
ELEMENT: App Icon
HYPOTHESIS: A bolder color icon will increase conversion by 10%
START DATE: [Date]
END DATE: [Date]

RESULTS:
├── Control CVR: 4.2%
├── Treatment CVR: 4.8%
├── Lift: +14.3%
├── Significance: 97%
└── Decision: Implement treatment

LEARNINGS:
- Bold colors outperform muted tones in this category
- Apply to screenshot backgrounds for next test
```

---

## Before/After Examples

### Title Optimization

**Productivity App:**

| Version | Title | Analysis |
|---------|-------|----------|
| Before | "MyTasks" | No keywords, brand only (8 chars) |
| After | "MyTasks - Todo List & Planner" | Primary + secondary keywords (29 chars) |

**Fitness App:**

| Version | Title | Analysis |
|---------|-------|----------|
| Before | "FitTrack Pro" | Generic modifier (12 chars) |
| After | "FitTrack: Workout Log & Gym" | Category keywords (27 chars) |

### Subtitle Optimization (iOS)

| Version | Subtitle | Analysis |
|---------|----------|----------|
| Before | "Get Things Done" | Vague, no keywords |
| After | "Daily Task Manager & Planner" | Two keywords, benefit clear |

### Keyword Field Optimization (iOS)

**Before (Inefficient - 89 chars, 8 keywords):**
```
task manager, todo list, productivity app, daily planner, reminder app
```

**After (Optimized - 97 chars, 14 keywords):**
```
task,todo,checklist,reminder,organize,daily,planner,schedule,deadline,goals,habit,widget,sync,team
```

**Improvements:**
- Removed spaces after commas (+8 chars)
- Removed duplicates (task manager → task)
- Removed plurals (reminders → reminder)
- Removed words in title
- Added more relevant keywords

### Description Opening

**Before:**
```
MyTasks is a comprehensive task management solution designed
to help busy professionals organize their daily activities
and boost productivity.
```

**After:**
```
Forget missed deadlines. MyTasks keeps every task, reminder,
and project in one place—so you focus on doing, not remembering.
Trusted by 500,000+ professionals.
```

**Improvements:**
- Leads with user pain point
- Specific benefit (not generic "boost productivity")
- Social proof included
- Keywords natural, not stuffed

### Screenshot Caption Evolution

| Version | Caption | Issue |
|---------|---------|-------|
| Before | "Task List Feature" | Feature-focused, passive |
| Better | "Create Task Lists" | Action verb, but still feature |
| Best | "Never Miss a Deadline" | Benefit-focused, emotional |

---

## Tools and References

### Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| [keyword_analyzer.py](scripts/keyword_analyzer.py) | Analyze keywords for volume and competition | `python keyword_analyzer.py --keywords "todo,task,planner"` |
| [metadata_optimizer.py](scripts/metadata_optimizer.py) | Validate metadata character limits and density | `python metadata_optimizer.py --platform ios --title "App Title"` |
| [competitor_analyzer.py](scripts/competitor_analyzer.py) | Extract and compare competitor keywords | `python competitor_analyzer.py --competitors "App1,App2,App3"` |
| [aso_scorer.py](scripts/aso_scorer.py) | Calculate overall ASO health score | `python aso_scorer.py --app-id com.example.app` |
| [ab_test_planner.py](scripts/ab_test_planner.py) | Plan tests and calculate sample sizes | `python ab_test_planner.py --cvr 0.05 --lift 0.10` |
| [review_analyzer.py](scripts/review_analyzer.py) | Analyze review sentiment and themes | `python review_analyzer.py --app-id com.example.app` |
| [launch_checklist.py](scripts/launch_checklist.py) | Generate platform-specific launch checklists | `python launch_checklist.py --platform ios` |
| [localization_helper.py](scripts/localization_helper.py) | Manage multi-language metadata | `python localization_helper.py --locales "en,es,de,ja"` |

### References

| Document | Content |
|----------|---------|
| [platform-requirements.md](references/platform-requirements.md) | iOS and Android metadata specs, visual asset requirements |
| [aso-best-practices.md](references/aso-best-practices.md) | Optimization strategies, rating management, launch tactics |
| [keyword-research-guide.md](references/keyword-research-guide.md) | Research methodology, evaluation framework, tracking |

### Assets

| Template | Purpose |
|----------|---------|
| [aso-audit-template.md](assets/aso-audit-template.md) | Structured audit checklist for app store listings |

---

## Platform Notes

| Platform / Constraint | Behavior / Impact |
|-----------------------|-------------------|
| iOS keyword changes | Require app submission |
| iOS promotional text | Editable without an app update |
| Android metadata changes | Index in 1-2 hours |
| Android keyword field | None — use description instead |
| Keyword volume data | Estimates only; no official source |
| Competitor data | Public listings only |

**When not to use this skill:** web apps (use web SEO), enterprise/internal apps, TestFlight-only betas, or paid advertising strategy.

---

## Related Skills

| Skill | Integration Point |
|-------|-------------------|
| [content-creator](../content-creator/) | App description copywriting |
| [marketing-demand-acquisition](../marketing-demand-acquisition/) | Launch promotion campaigns |
| [marketing-strategy-pmm](../marketing-strategy-pmm/) | Go-to-market planning |

## Proactive Triggers

- **No keyword optimization in title** → App title is the #1 ranking factor. Include top keyword.
- **Screenshots don't show value** → Screenshots should tell a story, not show UI.
- **No ratings strategy** → Below 4.0 stars kills conversion. Implement in-app rating prompts.
- **Description keyword-stuffed** → Natural language with keywords beats keyword stuffing.

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| "ASO audit" | Full app store listing audit with prioritized fixes |
| "Keyword research" | Keyword list with search volume and difficulty scores |
| "Optimize my listing" | Rewritten title, subtitle, description, keyword field |

## Communication

All output passes quality verification:
- Self-verify: source attribution, assumption audit, confidence scoring
- Output format: Bottom Line → What (with confidence) → Why → How to Act
- Results only. Every finding tagged: 🟢 verified, 🟡 medium, 🔴 assumed.


---

## Additional Coverage (Merged from local version)

<!-- Merged 2026-04-12: combined incoming + existing -->

---
name: app-store-optimization
description: "Complete App Store Optimization (ASO) toolkit for researching, optimizing, and tracking mobile app performance on Apple App Store and Google Play Store"
risk: unknown
source: community
date_added: "2026-02-27"
---

# App Store Optimization (ASO) Skill

This comprehensive skill provides complete ASO capabilities for successfully launching and optimizing mobile applications on the Apple App Store and Google Play Store.

## Capabilities

### Research & Analysis
- **Keyword Research**: Analyze keyword volume, competition, and relevance for app discovery
- **Competitor Analysis**: Deep-dive into top-performing apps in your category
- **Market Trend Analysis**: Identify emerging trends and opportunities in your app category
- **Review Sentiment Analysis**: Extract insights from user reviews to identify strengths and issues
- **Category Analysis**: Evaluate optimal category and subcategory placement strategies

### Metadata Optimization
- **Title Optimization**: Create compelling titles with optimal keyword placement (platform-specific character limits)
- **Description Optimization**: Craft both short and full descriptions that convert and rank
- **Subtitle/Promotional Text**: Optimize Apple-specific subtitle (30 chars) and promotional text (170 chars)
- **Keyword Field**: Maximize Apple's 100-character keyword field with strategic selection
- **Category Selection**: Data-driven recommendations for primary and secondary categories
- **Icon Best Practices**: Guidelines for designing high-converting app icons
- **Screenshot Optimization**: Strategies for creating screenshots that drive installs
- **Preview Video**: Best practices for app preview videos
- **Localization**: Multi-language optimization strategies for global reach

### Conversion Optimization
- **A/B Testing Framework**: Plan and track metadata experiments for continuous improvement
- **Visual Asset Testing**: Test icons, screenshots, and videos for maximum conversion
- **Store Listing Optimization**: Comprehensive page optimization for impression-to-install conversion
- **Call-to-Action**: Optimize CTAs in descriptions and promotional materials

### Rating & Review Management
- **Review Monitoring**: Track and analyze user reviews for actionable insights
- **Response Strategies**: Templates and best practices for responding to reviews
- **Rating Improvement**: Tactical approaches to improve app ratings organically
- **Issue Identification**: Surface common problems and feature requests from reviews

### Launch & Update Strategies
- **Pre-Launch Checklist**: Complete validation before submitting to stores
- **Launch Timing**: Optimize release timing for maximum visibility and downloads
- **Update Cadence**: Plan optimal update frequency and feature rollouts
- **Feature Announcements**: Craft "What's New" sections that re-engage users
- **Seasonal Optimization**: Leverage seasonal trends and events

### Analytics & Tracking
- **ASO Score**: Calculate overall ASO health score across multiple factors
- **Keyword Rankings**: Track keyword position changes over time
- **Conversion Metrics**: Monitor impression-to-install conversion rates
- **Download Velocity**: Track download trends and momentum
- **Performance Benchmarking**: Compare against category averages and competitors

### Platform-Specific Requirements
- **Apple App Store**:
  - Title: 30 characters
  - Subtitle: 30 characters
  - Promotional Text: 170 characters (editable without app update)
  - Description: 4,000 characters
  - Keywords: 100 characters (comma-separated, no spaces)
  - What's New: 4,000 characters
- **Google Play Store**:
  - Title: 50 characters (formerly 30, increased in 2021)
  - Short Description: 80 characters
  - Full Description: 4,000 characters
  - No separate keyword field (keywords extracted from title and description)

## Input Requirements

### Keyword Research
```json
{
  "app_name": "MyApp",
  "category": "Productivity",
  "target_keywords": ["task manager", "productivity", "todo list"],
  "competitors": ["Todoist", "Any.do", "Microsoft To Do"],
  "language": "en-US"
}
```

### Metadata Optimization
```json
{
  "platform": "apple" | "google",
  "app_info": {
    "name": "MyApp",
    "category": "Productivity",
    "target_audience": "Professionals aged 25-45",
    "key_features": ["Task management", "Team collaboration", "AI assistance"],
    "unique_value": "AI-powered task prioritization"
  },
  "current_metadata": {
    "title": "Current Title",
    "subtitle": "Current Subtitle",
    "description": "Current description..."
  },
  "target_keywords": ["productivity", "task manager", "todo"]
}
```

### Review Analysis
```json
{
  "app_id": "com.myapp.app",
  "platform": "apple" | "google",
  "date_range": "last_30_days" | "last_90_days" | "all_time",
  "rating_filter": [1, 2, 3, 4, 5],
  "language": "en"
}
```

### ASO Score Calculation
```json
{
  "metadata": {
    "title_quality": 0.8,
    "description_quality": 0.7,
    "keyword_density": 0.6
  },
  "ratings": {
    "average_rating": 4.5,
    "total_ratings": 15000
  },
  "conversion": {
    "impression_to_install": 0.05
  },
  "keyword_rankings": {
    "top_10": 5,
    "top_50": 12,
    "top_100": 18
  }
}
```

## Output Formats

### Keyword Research Report
- List of recommended keywords with search volume estimates
- Competition level analysis (low/medium/high)
- Relevance scores for each keyword
- Strategic recommendations for primary vs. secondary keywords
- Long-tail keyword opportunities

### Optimized Metadata Package
- Platform-specific title (with character count validation)
- Subtitle/promotional text (Apple)
- Short description (Google)
- Full description (both platforms)
- Keyword field (Apple - 100 chars)
- Character count validation for all fields
- Keyword density analysis
- Before/after comparison

### Competitor Analysis Report
- Top 10 competitors in category
- Their metadata strategies
- Keyword overlap analysis
- Visual asset assessment
- Rating and review volume comparison
- Identified gaps and opportunities

### ASO Health Score
- Overall score (0-100)
- Category breakdown:
  - Metadata Quality (0-25)
  - Ratings & Reviews (0-25)
  - Keyword Performance (0-25)
  - Conversion Metrics (0-25)
- Specific improvement recommendations
- Priority action items

### A/B Test Plan
- Hypothesis and test variables
- Test duration recommendations
- Success metrics definition
- Sample size calculations
- Statistical significance thresholds

### Launch Checklist
- Pre-submission validation (all required assets, metadata)
- Store compliance verification
- Testing checklist (devices, OS versions)
- Marketing preparation items
- Post-launch monitoring plan

## How to Use

### Keyword Research
```
Hey Claude—I just added the "app-store-optimization" skill. Can you research the best keywords for a productivity app targeting professionals? Focus on keywords with good search volume but lower competition.
```

### Optimize App Store Listing
```
Hey Claude—I just added the "app-store-optimization" skill. Can you optimize my app's metadata for the Apple App Store? Here's my current listing: [provide current metadata]. I want to rank for "task management" and "productivity tools".
```

### Analyze Competitor Strategy
```
Hey Claude—I just added the "app-store-optimization" skill. Can you analyze the ASO strategies of Todoist, Any.do, and Microsoft To Do? I want to understand what they're doing well and where there are opportunities.
```

### Review Sentiment Analysis
```
Hey Claude—I just added the "app-store-optimization" skill. Can you analyze recent reviews for my app (com.myapp.ios) and identify the most common user complaints and feature requests?
```

### Calculate ASO Score
```
Hey Claude—I just added the "app-store-optimization" skill. Can you calculate my app's overall ASO health score and provide specific recommendations for improvement?
```

### Plan A/B Test
```
Hey Claude—I just added the "app-store-optimization" skill. I want to A/B test my app icon and first screenshot. Can you help me design the test and determine how long to run it?
```

### Pre-Launch Checklist
```
Hey Claude—I just added the "app-store-optimization" skill. Can you generate a comprehensive pre-launch checklist for submitting my app to both Apple App Store and Google Play Store?
```

## Scripts

### keyword_analyzer.py
Analyzes keywords for search volume, competition, and relevance. Provides strategic recommendations for primary and secondary keywords.

**Key Functions:**
- `analyze_keyword()`: Analyze single keyword metrics
- `compare_keywords()`: Compare multiple keywords
- `find_long_tail()`: Discover long-tail keyword opportunities
- `calculate_keyword_difficulty()`: Assess competition level

### metadata_optimizer.py
Optimizes titles, descriptions, and keyword fields with platform-specific character limit validation.

**Key Functions:**
- `optimize_title()`: Create compelling, keyword-rich titles
- `optimize_description()`: Generate conversion-focused descriptions
- `optimize_keyword_field()`: Maximize Apple's 100-char keyword field
- `validate_character_limits()`: Ensure compliance with platform limits
- `calculate_keyword_density()`: Analyze keyword usage in metadata

### competitor_analyzer.py
Analyzes top competitors' ASO strategies and identifies opportunities.

**Key Functions:**
- `get_top_competitors()`: Identify category leaders
- `analyze_competitor_metadata()`: Extract and analyze competitor keywords
- `compare_visual_assets()`: Evaluate icons and screenshots
- `identify_gaps()`: Find competitive opportunities

### aso_scorer.py
Calculates comprehensive ASO health score across multiple dimensions.

**Key Functions:**
- `calculate_overall_score()`: Compute 0-100 ASO score
- `score_metadata_quality()`: Evaluate title, description, keywords
- `score_ratings_reviews()`: Assess rating quality and volume
- `score_keyword_performance()`: Analyze ranking positions
- `score_conversion_metrics()`: Evaluate impression-to-install rates
- `generate_recommendations()`: Provide prioritized action items

### ab_test_planner.py
Plans and tracks A/B tests for metadata and visual assets.

**Key Functions:**
- `design_test()`: Create test hypothesis and variables
- `calculate_sample_size()`: Determine required test duration
- `calculate_significance()`: Assess statistical significance
- `track_results()`: Monitor test performance
- `generate_report()`: Summarize test outcomes

### localization_helper.py
Manages multi-language ASO optimization strategies.

**Key Functions:**
- `identify_target_markets()`: Recommend localization priorities
- `translate_metadata()`: Generate localized metadata
- `adapt_keywords()`: Research locale-specific keywords
- `validate_translations()`: Check character limits per language
- `calculate_localization_roi()`: Estimate impact of localization

### review_analyzer.py
Analyzes user reviews for sentiment, issues, and feature requests.

**Key Functions:**
- `analyze_sentiment()`: Calculate positive/negative/neutral ratios
- `extract_common_themes()`: Identify frequently mentioned topics
- `identify_issues()`: Surface bugs and user complaints
- `find_feature_requests()`: Extract desired features
- `track_sentiment_trends()`: Monitor sentiment over time
- `generate_response_templates()`: Create review response drafts

### launch_checklist.py
Generates comprehensive pre-launch and update checklists.

**Key Functions:**
- `generate_prelaunch_checklist()`: Complete submission validation
- `validate_app_store_compliance()`: Check Apple guidelines
- `validate_play_store_compliance()`: Check Google policies
- `create_update_plan()`: Plan update cadence and features
- `optimize_launch_timing()`: Recommend release dates
- `plan_seasonal_campaigns()`: Identify seasonal opportunities

## Best Practices

### Keyword Research
1. **Volume vs. Competition**: Balance high-volume keywords with achievable rankings
2. **Relevance First**: Only target keywords genuinely relevant to your app
3. **Long-Tail Strategy**: Include 3-4 word phrases with lower competition
4. **Continuous Research**: Keyword trends change—research quarterly
5. **Competitor Keywords**: Don't copy blindly; ensure relevance to your features

### Metadata Optimization
1. **Front-Load Keywords**: Place most important keywords early in title/description
2. **Natural Language**: Write for humans first, SEO second
3. **Feature Benefits**: Focus on user benefits, not just features
4. **A/B Test Everything**: Test titles, descriptions, screenshots systematically
5. **Update Regularly**: Refresh metadata every major update
6. **Character Limits**: Use every character—don't waste valuable space
7. **Apple Keyword Field**: No plurals, duplicates, or spaces between commas

### Visual Assets
1. **Icon**: Must be recognizable at small sizes (60x60px)
2. **Screenshots**: First 2-3 are critical—most users don't scroll
3. **Captions**: Use screenshot captions to tell your value story
4. **Consistency**: Match visual style to app design
5. **A/B Test Icons**: Icon is the single most important visual element

### Reviews & Ratings
1. **Respond Quickly**: Reply to reviews within 24-48 hours
2. **Professional Tone**: Always courteous, even with negative reviews
3. **Address Issues**: Show you're actively fixing reported problems
4. **Thank Supporters**: Acknowledge positive reviews
5. **Prompt Strategically**: Ask for ratings after positive experiences

### Launch Strategy
1. **Soft Launch**: Consider launching in smaller markets first
2. **PR Timing**: Coordinate press coverage with launch
3. **Update Frequently**: Initial updates signal active development
4. **Monitor Closely**: Track metrics daily for first 2 weeks
5. **Iterate Quickly**: Fix critical issues immediately

### Localization
1. **Prioritize Markets**: Start with English, Spanish, Chinese, French, German
2. **Native Speakers**: Use professional translators, not machine translation
3. **Cultural Adaptation**: Some features resonate differently by culture
4. **Test Locally**: Have native speakers review before publishing
5. **Measure ROI**: Track downloads by locale to assess impact

## Limitations

### Data Dependencies
- Keyword search volume estimates are approximate (no official data from Apple/Google)
- Competitor data may be incomplete for private apps
- Review analysis limited to public reviews (can't access private feedback)
- Historical data may not be available for new apps

### Platform Constraints
- Apple App Store keyword changes require app submission (except Promotional Text)
- Google Play Store metadata changes take 1-2 hours to index
- A/B testing requires significant traffic for statistical significance
- Store algorithms are proprietary and change without notice

### Industry Variability
- ASO benchmarks vary significantly by category (games vs. utilities)
- Seasonality affects different categories differently
- Geographic markets have different competitive landscapes
- Cultural preferences impact what works in different countries

### Scope Boundaries
- Does not include paid user acquisition strategies (Apple Search Ads, Google Ads)
- Does not cover app development or UI/UX optimization
- Does not include app analytics implementation (use Firebase, Mixpanel, etc.)
- Does not handle app submission technical issues (provisioning profiles, certificates)

### When NOT to Use This Skill
- For web apps (different SEO strategies apply)
- For enterprise apps not in public stores
- For apps in beta/TestFlight only
- If you need paid advertising strategies (use marketing skills instead)

## Integration with Other Skills

This skill works well with:
- **Content Strategy Skills**: For creating app descriptions and marketing copy
- **Analytics Skills**: For analyzing download and engagement data
- **Localization Skills**: For managing multi-language content
- **Design Skills**: For creating optimized visual assets
- **Marketing Skills**: For coordinating broader launch campaigns

## Version & Updates

This skill is based on current Apple App Store and Google Play Store requirements as of November 2025. Store policies and best practices evolve—verify current requirements before major launches.

**Key Updates to Monitor:**
- Apple App Store Connect updates (apple.com/app-store/review/guidelines)
- Google Play Console updates (play.google.com/console/about/guides/releasewithconfidence)
- iOS/Android version adoption rates (affects device testing)
- Store algorithm changes (follow ASO blogs and communities)

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.
