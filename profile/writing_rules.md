# Writing Rules

Apply to resumes, cover letters, and every free-text answer written for the candidate.

## Candidate-specific rules (filled in during setup)

<!-- Name spellings and capitalization, employers/clients never to name, preferred titles for past roles, things the candidate never wants claimed. -->
- {{...}}

## Hard rules

1. Never use the em dash character. Use commas, colons, periods, parentheses, or a plain hyphen.
2. Never use "it's not just X, it's Y" / "not only X but Y" constructions. Vary sentence structure instead.
3. Only facts from `candidate_profile.md` and the original resume. No invented metrics, team sizes, percentages, or outcomes. Only numbers the candidate stated.
4. Years of experience: use only the number in `application_answers.md`.
5. A posting's keywords are not facts about the candidate. If they lack a required skill, leave it out; never imply it.

## Voice

- Direct, plain, confident. Peer-to-peer, not salesy.
- Concrete nouns over adjectives: name the tool, the system, the problem.
- No filler: "passionate", "rockstar", "synergy", "results-driven", "leverage", "spearheaded", "dynamic", "fast-paced", "proven track record".
- Short sentences. First person in cover letters and form answers; no pronouns in resume bullets.

## Resume format (build format for tools/build_resume.py)

```
# Jane Doe
Optional Headline - Field or Target Role
City, ST (Remote) | 555.123.4567 | jane.doe.jobs@gmail.com | linkedin.com/in/janedoe

## Summary
Plain paragraph.

## Skills
- **Category:** item, item, item

## Experience
### Job Title | Employer | City, ST | Jan 2022 - Present
- Bullet starting with a strong verb.

## Projects
### Project Name | tools used
- What it does and what it achieved.

## Education
### Degree, Field | School | City, ST | Aug 2016 - May 2020
- Honors or relevant coursework.
```

- `#` = name (once). Lines after it, before the first `##`: an optional headline (no `|`), then the contact line (with `|`).
- `##` = section heading. `###` = entry line, fields separated by ` | ` (last field is right-aligned dates). Entries without dates (projects) render full width.
- `- ` = bullet. `**bold**` supported inline. Plain lines = paragraphs.
- Dates use hyphens: "Jan 2025 - Present".
- Bullets: 1 to 2 lines each, 3 to 5 per recent role, 1 to 2 per older role.
- Default section order: Summary, Skills, Experience, Projects, Education, Certifications. Move Education up for entry-level or internship postings.
- Keep to the page length the candidate chose (default one page for under 10 years of experience).
