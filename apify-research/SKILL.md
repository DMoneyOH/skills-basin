---
name: apify-research
description: >
  "Track reviews, ratings, sentiment, and brand mentions across Google Maps, Booking.com, TripAdvisor, Facebook, Instagram, YouTube, and TikTok. Use when user asks to monitor brand reputation, analyze..."
  Covers: apify research, apify audience analysis, apify content analytics, apify brand reputation monitoring.
  Use for any task involving apify research, apify audience analysis, apify content analytics, apify brand reputation monitoring.
merged_from:
  - apify-audience-analysis
  - apify-content-analytics
  - apify-brand-reputation-monitoring
merged_at: 2026-04-25
---

-------|----------|----------|
  - -actor "actor_id" \
merged_from:
  - apify-audience-analysis
  - apify-content-analytics
  - apify-brand-reputation-monitoring
  - apify-competitor-intelligence
  - apify-market-research
  - apify-trend-analysis
merged_at: 2026-04-18T17:21:06.036018
---

# apify-research

<!-- apify-audience-analysis -->
Analyze and understand your audience using Apify Actors to extract follower demographics, engagement patterns, and behavior data from multiple platforms.

## Prerequisites
(No need to check it upfront)

- `.env` file with `APIFY_TOKEN`
- Node.js 20.6+ (for native `--env-file` support)
- `mcpc` CLI tool: `npm install -g @apify/mcpc`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify audience analysis type (select Actor)
- [ ] Step 2: Fetch Actor schema via mcpc
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analysis script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Audience Analysis Type

Select the appropriate Actor based on analysis needs:

| User Need | Actor ID | Best For |
|-----------|----------|----------|
| Facebook follower demographics | `apify/facebook-followers-following-scraper` | FB followers/following lists |
| Facebook engagement behavior | `apify/facebook-likes-scraper` | FB post likes analysis |
| Facebook video audience | `apify/facebook-reels-scraper` | FB Reels viewers |
| Facebook comment analysis | `apify/facebook-comments-scraper` | FB post/video comments |
| Facebook content engagement | `apify/facebook-posts-scraper` | FB post engagement metrics |
| Instagram audience sizing | `apify/instagram-profile-scraper` | IG profile demographics |
| Instagram location-based | `apify/instagram-search-scraper` | IG geo-tagged audience |
| Instagram tagged network | `apify/instagram-tagged-scraper` | IG tag network analysis |
| Instagram comprehensive | `apify/instagram-scraper` | Full IG audience data |
| Instagram API-based | `apify/instagram-api-scraper` | IG API access |
| Instagram follower counts | `apify/instagram-followers-count-scraper` | IG follower tracking |
| Instagram comment export | `apify/export-instagram-comments-posts` | IG comment bulk export |
| Instagram comment analysis | `apify/instagram-comment-scraper` | IG comment sentiment |
| YouTube viewer feedback | `streamers/youtube-comments-scraper` | YT comment analysis |
| YouTube channel audience | `streamers/youtube-channel-scraper` | YT channel subscribers |
| TikTok follower demographics | `clockworks/tiktok-followers-scraper` | TT follower lists |
| TikTok profile analysis | `clockworks/tiktok-profile-scraper` | TT profile demographics |
| TikTok comment analysis | `clockworks/tiktok-comments-scraper` | TT comment engagement |

### Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details dynamically using mcpc:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"
```

Replace `ACTOR_ID` with the selected Actor (e.g., `apify/facebook-followers-following-scraper`).

This returns:
- Actor description and README
- Required and optional input parameters
- Output fields (if available)

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top few results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Number of results**: Based on character of use case

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv
```

**JSON:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json
```

### Step 5: Summarize Findings

After completion, report:
- Number of audience members/profiles analyzed
- File location and name
- Key demographic insights
- Suggested next steps (deeper analysis, segmentation)


## Error Handling

`APIFY_TOKEN not found` - Ask user to create `.env` with `APIFY_TOKEN=your_token`
`mcpc not found` - Ask user to install `npm install -g @apify/mcpc`
`Actor not found` - Check Actor ID spelling
`Run FAILED` - Ask user to check Apify console link in error output
`Timeout` - Reduce input size or increase `--timeout`


<!-- MERGED INTO: apify-research on 2026-04-18 -->
<!-- Use `apify-research` instead. -->

---

<!-- apify-content-analytics -->
Track and analyze content performance using Apify Actors to extract engagement metrics from multiple platforms.

## Prerequisites
(No need to check it upfront)

- `.env` file with `APIFY_TOKEN`
- Node.js 20.6+ (for native `--env-file` support)
- `mcpc` CLI tool: `npm install -g @apify/mcpc`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify content analytics type (select Actor)
- [ ] Step 2: Fetch Actor schema via mcpc
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analytics script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Content Analytics Type

Select the appropriate Actor based on analytics needs:

| User Need | Actor ID | Best For |
|-----------|----------|----------|
| Post engagement metrics | `apify/instagram-post-scraper` | Post performance |
| Reel performance | `apify/instagram-reel-scraper` | Reel analytics |
| Follower growth tracking | `apify/instagram-followers-count-scraper` | Growth metrics |
| Comment engagement | `apify/instagram-comment-scraper` | Comment analysis |
| Hashtag performance | `apify/instagram-hashtag-scraper` | Branded hashtags |
| Mention tracking | `apify/instagram-tagged-scraper` | Tag tracking |
| Comprehensive metrics | `apify/instagram-scraper` | Full data |
| API-based analytics | `apify/instagram-api-scraper` | API access |
| Facebook post performance | `apify/facebook-posts-scraper` | Post metrics |
| Reaction analysis | `apify/facebook-likes-scraper` | Engagement types |
| Facebook Reels metrics | `apify/facebook-reels-scraper` | Reels performance |
| Ad performance tracking | `apify/facebook-ads-scraper` | Ad analytics |
| Facebook comment analysis | `apify/facebook-comments-scraper` | Comment engagement |
| Page performance audit | `apify/facebook-pages-scraper` | Page metrics |
| YouTube video metrics | `streamers/youtube-scraper` | Video performance |
| YouTube Shorts analytics | `streamers/youtube-shorts-scraper` | Shorts performance |
| TikTok content metrics | `clockworks/tiktok-scraper` | TikTok analytics |

### Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details dynamically using mcpc:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"
```

Replace `ACTOR_ID` with the selected Actor (e.g., `apify/instagram-post-scraper`).

This returns:
- Actor description and README
- Required and optional input parameters
- Output fields (if available)

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top few results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Number of results**: Based on character of use case

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv
```

**JSON:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json
```

### Step 5: Summarize Findings

After completion, report:
- Number of content pieces analyzed
- File location and name
- Key performance insights
- Suggested next steps (deeper analysis, content optimization)


## Error Handling

`APIFY_TOKEN not found` - Ask user to create `.env` with `APIFY_TOKEN=your_token`
`mcpc not found` - Ask user to install `npm install -g @apify/mcpc`
`Actor not found` - Check Actor ID spelling
`Run FAILED` - Ask user to check Apify console link in error output
`Timeout` - Reduce input size or increase `--timeout`


<!-- MERGED INTO: apify-research on 2026-04-18 -->
<!-- Use `apify-research` instead. -->

---

<!-- apify-brand-reputation-monitoring -->
Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors.

## Prerequisites
(No need to check it upfront)

- `.env` file with `APIFY_TOKEN`
- Node.js 20.6+ (for native `--env-file` support)
- `mcpc` CLI tool: `npm install -g @apify/mcpc`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Determine data source (select Actor)
- [ ] Step 2: Fetch Actor schema via mcpc
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the monitoring script
- [ ] Step 5: Summarize results
```

### Step 1: Determine Data Source

Select the appropriate Actor based on user needs:

| User Need | Actor ID | Best For |
|-----------|----------|----------|
| Google Maps reviews | `compass/crawler-google-places` | Business reviews, ratings |
| Google Maps review export | `compass/Google-Maps-Reviews-Scraper` | Dedicated review scraping |
| Booking.com hotels | `voyager/booking-scraper` | Hotel data, scores |
| Booking.com reviews | `voyager/booking-reviews-scraper` | Detailed hotel reviews |
| TripAdvisor reviews | `maxcopell/tripadvisor-reviews` | Attraction/restaurant reviews |
| Facebook reviews | `apify/facebook-reviews-scraper` | Page reviews |
| Facebook comments | `apify/facebook-comments-scraper` | Post comment monitoring |
| Facebook page metrics | `apify/facebook-pages-scraper` | Page ratings overview |
| Facebook reactions | `apify/facebook-likes-scraper` | Reaction type analysis |
| Instagram comments | `apify/instagram-comment-scraper` | Comment sentiment |
| Instagram hashtags | `apify/instagram-hashtag-scraper` | Brand hashtag monitoring |
| Instagram search | `apify/instagram-search-scraper` | Brand mention discovery |
| Instagram tagged posts | `apify/instagram-tagged-scraper` | Brand tag tracking |
| Instagram export | `apify/export-instagram-comments-posts` | Bulk comment export |
| Instagram comprehensive | `apify/instagram-scraper` | Full Instagram monitoring |
| Instagram API | `apify/instagram-api-scraper` | API-based monitoring |
| YouTube comments | `streamers/youtube-comments-scraper` | Video comment sentiment |
| TikTok comments | `clockworks/tiktok-comments-scraper` | TikTok sentiment |

### Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details dynamically using mcpc:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"
```

Replace `ACTOR_ID` with the selected Actor (e.g., `compass/crawler-google-places`).

This returns:
- Actor description and README
- Required and optional input parameters
- Output fields (if available)

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top few results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Number of results**: Based on character of use case

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv
```

**JSON:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json
```

### Step 5: Summarize Results

After completion, report:
- Number of reviews/mentions found
- File location and name
- Key fields available
- Suggested next steps (sentiment analysis, filtering)


## Error Handling

`APIFY_TOKEN not found` - Ask user to create `.env` with `APIFY_TOKEN=your_token`
`mcpc not found` - Ask user to install `npm install -g @apify/mcpc`
`Actor not found` - Check Actor ID spelling
`Run FAILED` - Ask user to check Apify console link in error output
`Timeout` - Reduce input size or increase `--timeout`


<!-- MERGED INTO: apify-research on 2026-04-18 -->
<!-- Use `apify-research` instead. -->

---

<!-- apify-competitor-intelligence -->
Analyze competitors using Apify Actors to extract data from multiple platforms.

## Prerequisites
(No need to check it upfront)

- `.env` file with `APIFY_TOKEN`
- Node.js 20.6+ (for native `--env-file` support)
- `mcpc` CLI tool: `npm install -g @apify/mcpc`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify competitor analysis type (select Actor)
- [ ] Step 2: Fetch Actor schema via mcpc
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analysis script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Competitor Analysis Type

Select the appropriate Actor based on analysis needs:

| User Need | Actor ID | Best For |
|-----------|----------|----------|
| Competitor business data | `compass/crawler-google-places` | Location analysis |
| Competitor contact discovery | `poidata/google-maps-email-extractor` | Email extraction |
| Feature benchmarking | `compass/google-maps-extractor` | Detailed business data |
| Competitor review analysis | `compass/Google-Maps-Reviews-Scraper` | Review comparison |
| Hotel competitor data | `voyager/booking-scraper` | Hotel benchmarking |
| Hotel review comparison | `voyager/booking-reviews-scraper` | Review analysis |
| Competitor ad strategies | `apify/facebook-ads-scraper` | Ad creative analysis |
| Competitor page metrics | `apify/facebook-pages-scraper` | Page performance |
| Competitor content analysis | `apify/facebook-posts-scraper` | Post strategies |
| Competitor reels performance | `apify/facebook-reels-scraper` | Reels analysis |
| Competitor audience analysis | `apify/facebook-comments-scraper` | Comment sentiment |
| Competitor event monitoring | `apify/facebook-events-scraper` | Event tracking |
| Competitor audience overlap | `apify/facebook-followers-following-scraper` | Follower analysis |
| Competitor review benchmarking | `apify/facebook-reviews-scraper` | Review comparison |
| Competitor ad monitoring | `apify/facebook-search-scraper` | Ad discovery |
| Competitor profile metrics | `apify/instagram-profile-scraper` | Profile analysis |
| Competitor content monitoring | `apify/instagram-post-scraper` | Post tracking |
| Competitor engagement analysis | `apify/instagram-comment-scraper` | Comment analysis |
| Competitor reel performance | `apify/instagram-reel-scraper` | Reel metrics |
| Competitor growth tracking | `apify/instagram-followers-count-scraper` | Follower tracking |
| Comprehensive competitor data | `apify/instagram-scraper` | Full analysis |
| API-based competitor analysis | `apify/instagram-api-scraper` | API access |
| Competitor video analysis | `streamers/youtube-scraper` | Video metrics |
| Competitor sentiment analysis | `streamers/youtube-comments-scraper` | Comment sentiment |
| Competitor channel metrics | `streamers/youtube-channel-scraper` | Channel analysis |
| TikTok competitor analysis | `clockworks/tiktok-scraper` | TikTok data |
| Competitor video strategies | `clockworks/tiktok-video-scraper` | Video analysis |
| Competitor TikTok profiles | `clockworks/tiktok-profile-scraper` | Profile data |

### Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details dynamically using mcpc:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"
```

Replace `ACTOR_ID` with the selected Actor (e.g., `compass/crawler-google-places`).

This returns:
- Actor description and README
- Required and optional input parameters
- Output fields (if available)

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top few results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Number of results**: Based on character of use case

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv
```

**JSON:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json
```

### Step 5: Summarize Findings

After completion, report:
- Number of competitors analyzed
- File location and name
- Key competitive insights
- Suggested next steps (deeper analysis, benchmarking)


## Error Handling

`APIFY_TOKEN not found` - Ask user to create `.env` with `APIFY_TOKEN=your_token`
`mcpc not found` - Ask user to install `npm install -g @apify/mcpc`
`Actor not found` - Check Actor ID spelling
`Run FAILED` - Ask user to check Apify console link in error output
`Timeout` - Reduce input size or increase `--timeout`


<!-- MERGED INTO: apify-research on 2026-04-18 -->
<!-- Use `apify-research` instead. -->

---

<!-- apify-market-research -->
Conduct market research using Apify Actors to extract data from multiple platforms.

## Prerequisites
(No need to check it upfront)

- `.env` file with `APIFY_TOKEN`
- Node.js 20.6+ (for native `--env-file` support)
- `mcpc` CLI tool: `npm install -g @apify/mcpc`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify market research type (select Actor)
- [ ] Step 2: Fetch Actor schema via mcpc
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analysis script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Market Research Type

Select the appropriate Actor based on research needs:

| User Need | Actor ID | Best For |
|-----------|----------|----------|
| Market density | `compass/crawler-google-places` | Location analysis |
| Geospatial analysis | `compass/google-maps-extractor` | Business mapping |
| Regional interest | `apify/google-trends-scraper` | Trend data |
| Pricing and demand | `apify/facebook-marketplace-scraper` | Market pricing |
| Event market | `apify/facebook-events-scraper` | Event analysis |
| Consumer needs | `apify/facebook-groups-scraper` | Group research |
| Market landscape | `apify/facebook-pages-scraper` | Business pages |
| Business density | `apify/facebook-page-contact-information` | Contact data |
| Cultural insights | `apify/facebook-photos-scraper` | Visual research |
| Niche targeting | `apify/instagram-hashtag-scraper` | Hashtag research |
| Hashtag stats | `apify/instagram-hashtag-stats` | Market sizing |
| Market activity | `apify/instagram-reel-scraper` | Activity analysis |
| Market intelligence | `apify/instagram-scraper` | Full data |
| Product launch research | `apify/instagram-api-scraper` | API access |
| Hospitality market | `voyager/booking-scraper` | Hotel data |
| Tourism insights | `maxcopell/tripadvisor-reviews` | Review analysis |

### Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details dynamically using mcpc:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"
```

Replace `ACTOR_ID` with the selected Actor (e.g., `compass/crawler-google-places`).

This returns:
- Actor description and README
- Required and optional input parameters
- Output fields (if available)

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top few results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Number of results**: Based on character of use case

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv
```

**JSON:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json
```

### Step 5: Summarize Findings

After completion, report:
- Number of results found
- File location and name
- Key market insights
- Suggested next steps (deeper analysis, validation)


## Error Handling

`APIFY_TOKEN not found` - Ask user to create `.env` with `APIFY_TOKEN=your_token`
`mcpc not found` - Ask user to install `npm install -g @apify/mcpc`
`Actor not found` - Check Actor ID spelling
`Run FAILED` - Ask user to check Apify console link in error output
`Timeout` - Reduce input size or increase `--timeout`


<!-- MERGED INTO: apify-research on 2026-04-18 -->
<!-- Use `apify-research` instead. -->

---

<!-- apify-trend-analysis -->
Discover and track emerging trends using Apify Actors to extract data from multiple platforms.

## Prerequisites
(No need to check it upfront)

- `.env` file with `APIFY_TOKEN`
- Node.js 20.6+ (for native `--env-file` support)
- `mcpc` CLI tool: `npm install -g @apify/mcpc`

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: Identify trend type (select Actor)
- [ ] Step 2: Fetch Actor schema via mcpc
- [ ] Step 3: Ask user preferences (format, filename)
- [ ] Step 4: Run the analysis script
- [ ] Step 5: Summarize findings
```

### Step 1: Identify Trend Type

Select the appropriate Actor based on research needs:

| User Need | Actor ID | Best For |
|-----------|----------|----------|
| Search trends | `apify/google-trends-scraper` | Google Trends data |
| Hashtag tracking | `apify/instagram-hashtag-scraper` | Hashtag content |
| Hashtag metrics | `apify/instagram-hashtag-stats` | Performance stats |
| Visual trends | `apify/instagram-post-scraper` | Post analysis |
| Trending discovery | `apify/instagram-search-scraper` | Search trends |
| Comprehensive tracking | `apify/instagram-scraper` | Full data |
| API-based trends | `apify/instagram-api-scraper` | API access |
| Engagement trends | `apify/export-instagram-comments-posts` | Comment tracking |
| Product trends | `apify/facebook-marketplace-scraper` | Marketplace data |
| Visual analysis | `apify/facebook-photos-scraper` | Photo trends |
| Community trends | `apify/facebook-groups-scraper` | Group monitoring |
| YouTube Shorts | `streamers/youtube-shorts-scraper` | Short-form trends |
| YouTube hashtags | `streamers/youtube-video-scraper-by-hashtag` | Hashtag videos |
| TikTok hashtags | `clockworks/tiktok-hashtag-scraper` | Hashtag content |
| Trending sounds | `clockworks/tiktok-sound-scraper` | Audio trends |
| TikTok ads | `clockworks/tiktok-ads-scraper` | Ad trends |
| Discover page | `clockworks/tiktok-discover-scraper` | Discover trends |
| Explore trends | `clockworks/tiktok-explore-scraper` | Explore content |
| Trending content | `clockworks/tiktok-trends-scraper` | Viral content |

### Step 2: Fetch Actor Schema

Fetch the Actor's input schema and details dynamically using mcpc:

```bash
export $(grep APIFY_TOKEN .env | xargs) && mcpc --json mcp.apify.com --header "Authorization: Bearer $APIFY_TOKEN" tools-call fetch-actor-details actor:="ACTOR_ID" | jq -r ".content"
```

Replace `ACTOR_ID` with the selected Actor (e.g., `apify/google-trends-scraper`).

This returns:
- Actor description and README
- Required and optional input parameters
- Output fields (if available)

### Step 3: Ask User Preferences

Before running, ask:
1. **Output format**:
   - **Quick answer** - Display top few results in chat (no file saved)
   - **CSV** - Full export with all fields
   - **JSON** - Full export in JSON format
2. **Number of results**: Based on character of use case

### Step 4: Run the Script

**Quick answer (display in chat, no file):**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT'
```

**CSV:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.csv \
  --format csv
```

**JSON:**
```bash
node --env-file=.env ${CLAUDE_PLUGIN_ROOT}/reference/scripts/run_actor.js \
  --actor "ACTOR_ID" \
  --input 'JSON_INPUT' \
  --output YYYY-MM-DD_OUTPUT_FILE.json \
  --format json
```

### Step 5: Summarize Findings

After completion, report:
- Number of results found
- File location and name
- Key trend insights
- Suggested next steps (deeper analysis, content opportunities)


## Error Handling

`APIFY_TOKEN not found` - Ask user to create `.env` with `APIFY_TOKEN=your_token`
`mcpc not found` - Ask user to install `npm install -g @apify/mcpc`
`Actor not found` - Check Actor ID spelling
`Run FAILED` - Ask user to check Apify console link in error output
`Timeout` - Reduce input size or increase `--timeout`


## When to Use

Use this skill when tackling tasks related to its primary domain or functionality as described above.


<!-- MERGED INTO: apify-research on 2026-04-18 -->
<!-- Use `apify-research` instead. -->
