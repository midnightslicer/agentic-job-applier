# Job Sourcing Playbook

Goal: find good openings, especially ones other applicants miss. Always apply on the company's own site when possible.

## Titles to search

<!-- Filled in during setup: target titles in priority order, plus close synonyms and adjacent titles. -->
{{titles}}

Seniority: {{target level}}. Skip roles demanding more than {{N}} years unless everything else fits closely.

## Keywords

<!-- The candidate's strongest skills and tools, for combining with titles in searches. -->
{{keywords}}

## Hidden-market sources (check these first)

1. **Company ATS boards via public APIs** (most postings are here before they reach job boards, with reliable posted dates and pay):
   - Greenhouse: `boards-api.greenhouse.io/v1/boards/<slug>/jobs` and `/jobs/<id>?pay_transparency=true&questions=true` (`first_published` is the posted date; list `updated_at` is not).
   - Lever: `api.lever.co/v0/postings/<slug>?mode=json` (`createdAt`).
   - Ashby: `api.ashbyhq.com/posting-api/job-board/<slug>?includeCompensation=true` (`publishedAt`).
   - Lists of thousands of live company slugs: `github.com/Feashliaa/job-board-aggregator`, files `data/{ashby,lever,greenhouse}_companies.json` (fetch via raw.githubusercontent.com). Sweep with a title filter, a few threads, and a short delay; then fetch details only for candidates. The repo's releases also include Paylocity, iCIMS, Workday and BambooHR listings (no posted date there: age-check on the ATS page).
   - Web search: `site:boards.greenhouse.io`, `site:jobs.lever.co`, `site:jobs.ashbyhq.com`, `site:apply.workable.com`, `site:myworkdayjobs.com`, `site:jobs.smartrecruiters.com`, `site:recruitee.com`, `site:bamboohr.com/careers`, `site:breezy.hr`, `site:jazzhr.com`, combined with titles, keywords, and "remote" or the candidate's city.
2. **Companies whose products or work match the candidate's background** (check their careers pages directly).
   {{industry-specific company types}}
3. **Local employers within the commute range** (only if onsite/hybrid is acceptable):
   {{list from setup: employer, careers URL, distance}}
   - Also: hospitals and health systems, universities and community colleges, school districts, city/county/state government job sites, large regional employers, local service firms.
4. **Community and niche boards:** {{field-specific boards, professional associations, state job board, USAJOBS if eligible}}. Remote boards: We Work Remotely, Remotive, RemoteOK, Himalayas, Wellfound, Y Combinator Work at a Startup, Built In, Hacker News "Who is hiring?" (tech).
5. **Big boards last** (Indeed, LinkedIn, ZipRecruiter, Glassdoor): use them to discover openings, then trace each one back to the company's own site.

## Quality signals

Good: named team or hiring manager, clear duties, posted pay, recent date, required skills overlap the candidate's real skills.
Bad: reposted for months, staffing agency with no client named, "unpaid trial", vague duties, commission-only, aggregator reposts (for example the Lever slug `jobgether`).

## Record what works

After each scout batch, add a one-line note to `LESSONS.md` under "Job boards and ATS quirks" or "Outcome patterns" naming productive and dry sources, so the next scout starts in the right place.
