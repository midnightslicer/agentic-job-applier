# First-Run Setup (instructions for Claude)

You are setting up this job application kit for a new person ("the candidate"). Work through these steps in order. Be friendly and plain-spoken; the candidate may not be technical. Keep each message short. Tell them roughly how long the setup takes (15 to 30 minutes) and that they can stop and resume any time: you track progress in `setup_progress.md`.

**Resuming:** if `setup_progress.md` exists, read it and continue from the first unchecked step. Update it after each step.

Create `setup_progress.md` at the start with this checklist:

```
- [ ] 1. Git connection removed
- [ ] 2. Prerequisites checked
- [ ] 3. Input files read
- [ ] 4. Interview: basics
- [ ] 5. Interview: job search preferences
- [ ] 6. Interview: form answers
- [ ] 7. Interview: filling gaps and stories
- [ ] 8. Profile files written
- [ ] 9. Master resume approved
- [ ] 10. Job sourcing plan written
- [ ] 11. Final approval and finish
```

---

## Step 1. Remove the git connection (do this first, before reading any personal files)

This folder was downloaded from a shared repo. Once the candidate's personal information is in it, it must never be pushed back. Remove the connection:

1. Run `git rev-parse --show-toplevel 2>/dev/null` and `pwd`.
2. If the top level equals this folder (there is a `.git` directory here): run `git remote -v` and note the remote, then delete this folder's `.git` directory (`rm -rf .git`). Run `git rev-parse --show-toplevel` again to confirm it now fails.
3. If the top level is a PARENT folder (this kit sits inside some other repo): do NOT delete the parent's `.git`. Tell the candidate their personal data could be committed to that parent repo, and recommend they move this folder somewhere outside it and reopen Claude there. Continue only if they say it's fine.
4. If there is no git repo at all: nothing to do.
5. Tell the candidate in one sentence what you did and why ("I disconnected this folder from git so your personal info can't accidentally be uploaded").

## Step 2. Check prerequisites

Check each, report a short checklist (✔ / ✘), and help fix anything missing. Point to the README's Prerequisites section for full instructions.

1. **Claude in Chrome.** Load the Chrome tools with ToolSearch and call `tabs_context_mcp`. If it works, Chrome is connected. If not, tell them to install the Claude extension, sign in, and run `/chrome` (or restart with `claude --chrome`).
2. **Gmail.** Search the deferred tool list for a Gmail connector (ToolSearch "gmail"). If found, note it. If not, they can connect Gmail at claude.ai > Settings > Connectors. As a fallback, Chrome logged in to their Gmail works too. Ask which Gmail address is the job-hunting inbox (you'll confirm it again in the interview).
3. **unslop skill.** Check whether `unslop` is in your available skills list. If not, give them the install command from the README (`npx skills add theclaymethod/unslop -g -a claude-code`) and note they must restart Claude Code afterward. Setup can continue without it, but tell them applications will read less naturally until it's installed.
4. **Python and resume builder.** Run `python3 --version` (on Windows, `py --version`). Create the venv and install the dependency: `python3 -m venv .venv && .venv/bin/pip install -q python-docx`. On Windows the venv's Python is `.venv\Scripts\python.exe`: use it wherever the kit says `.venv/bin/python`, and add a line to the Tooling section of `LESSONS.md` saying so.
5. **LibreOffice** (for PDFs). Check `which soffice libreoffice`. If missing, give the install command for their OS (Linux package manager `libreoffice`; macOS `brew install --cask libreoffice`; Windows installer from libreoffice.org). Without it, resumes build as `.docx` only.

Do not block on Chrome, Gmail, or unslop being fixed right now; note what's missing in `setup_progress.md` and re-check at Step 11.

## Step 3. Read the input files

Look in `input/` (ignore `input/README.md`).

- **Resume:** any of `.pdf`, `.docx`, `.doc`, `.txt`, `.md`, `.rtf`. Extract the text (Read tool for PDF; `.venv/bin/python -c` with python-docx for `.docx`; `soffice --headless --convert-to txt` for others). Save the text to `resume/ORIGINAL_resume.txt`, keeping the candidate's wording exactly.
- **Skills file:** usually `skills.txt` or any other text/markdown file. It may be a raw voice transcript: rambling, repetitive, with transcription errors. Read all of it carefully. It is a primary source of facts.

If either file is missing, tell the candidate what to add (see README "What to put in `input/`", including the voice-recorder tip), and wait. If the skills file is very thin (under ~300 words), suggest the voice-recorder approach before moving on, but let them continue if they prefer; the interview can fill gaps.

Summarize back what you learned in 5 to 8 bullets (roles, years, main skills, education) so they can correct anything early.

## Steps 4 to 7. Interview

Ask in small rounds (3 to 5 questions at a time). Use the AskUserQuestion tool for multiple-choice questions; ask open questions in plain text. Skip anything the files already answer clearly, but confirm key facts. Record answers as you go (write a scratch `profile/_interview_notes.md` after each round so nothing is lost if the session ends; delete it at Step 11).

### Step 4. Basics

- Full name as it should appear on applications; preferred first name if different.
- **Email** to use on every application (should be the job-hunting Gmail Claude can read).
- **Phone number.**
- **Mailing address** (street, city, state, ZIP). Explain: the street address only goes into form address fields, never on the resume. The resume shows "City, ST".
- LinkedIn URL, portfolio/GitHub/website (optional).
- Which state they live in (many remote postings only hire in certain states and ask "Which state do you reside in?").

### Step 5. Job search preferences

- **Location** for distance checks: their home city/town and ZIP.
- **Remote preference:** remote only / remote preferred but open to onsite or hybrid nearby / no preference / prefers in-person.
- **Driving range:** the farthest one-way commute they'd accept for onsite or hybrid work, in miles. Optionally a different range for hybrid (fewer days) than full onsite.
- **Relocation:** willing or not.
- **Pay range:** the hard floor (skip anything posted below this) and the target range to give when a form asks for desired salary, plus a single number for single-number fields. Ask whether hourly roles are OK and convert the floor to hourly (divide by 2,080).
- **Job types:** full-time, part-time, contract, temp-to-hire, internships.
- **Target roles:** job titles they want, in priority order. Offer suggestions based on their resume and skills, including adjacent titles they might not have thought of. Ask which they'd be happy doing and which are stretch or fallback.
- **Experience level:** what level to target (entry, junior, mid, senior). Agree on a cutoff (for example "skip postings requiring more than 5 years").
- **Industries or companies to avoid**, including their current employer if their search is confidential.
- **Travel** tolerance (none / up to 25% / more) and **schedule** limits (time zones, shifts, weekends, nights).
- **On-call, overtime, evenings, weekends, holidays:** acceptable? (Forms ask each one as a separate Yes/No.)
- **Onsite days:** for hybrid roles, how many days a week in the office is acceptable?
- **Physical requirements:** can they meet common ones (lifting 25 or 50 lbs, standing for long periods)? Only matters for hands-on roles.
- **Driving:** valid driver's license? Reliable transportation? Own vehicle they'd use for work travel (some roles also check driving records)?
- **Remote setup:** quiet home workspace and reliable high-speed internet? (Remote forms often ask.)
- **Languages** spoken and how well (some forms ask; bilingual roles can pay more).
- Anything that's a dealbreaker or a must-have (benefits, schedule, company size, mission, startups vs. large companies, stretch roles OK or not).
- **Parallel applicants:** how many applications at once (1 to 4; default 2). More is faster but uses Claude usage faster.

### Step 6. Form answers

Application forms ask the same questions over and over. Every answer collected here is one less job parked later. Before starting, tell the candidate: "Next I'll ask the standard questions job applications ask, including race, gender, veteran status, disability, and visa/H-1B status. The demographic ones are voluntary on every form and 'I'd rather not say' is always a fine answer. I only record what you tell me, and it only goes into application forms that ask." Ask in small groups, using AskUserQuestion where the choices are fixed.

**Work authorization and immigration** (required on nearly every form; answer wrong and the application is auto-rejected):
- Legally authorized to work in the US (or their country)?
- Need employer sponsorship for a work visa now **or in the future**? (Forms ask both; someone on OPT or H-1B usually answers Yes to "in the future".)
- Current status: US citizen / permanent resident (green card) / H-1B / H-1B needing transfer / F-1 OPT or STEM OPT (with end date) / TN / L-1 / H-4 or other EAD / other. Record the visa type and expiration if not a citizen or resident.
- Citizenship (US citizen yes/no). Needed for roles that require US citizenship, "US person" status under export control (ITAR/EAR), or clearance eligibility.
- Security clearance: none / level held, active or inactive / willing and eligible to obtain one?

**Voluntary self-identification (EEO).** For each, ask whether to answer or decline. Default to "decline" if they don't care. Record exact answers:
- Gender (Male / Female / Non-binary / decline). Some forms also ask whether they identify as transgender.
- Hispanic or Latino (Yes / No / decline). US forms ask this separately from race.
- Race (American Indian or Alaska Native / Asian / Black or African American / Native Hawaiian or Other Pacific Islander / White / Two or more races / decline).
- Veteran status: not a veteran / protected veteran (and which: disabled veteran, recently separated, active duty wartime or campaign badge veteran, Armed Forces Service Medal veteran) / veteran but not protected / decline. Also: military spouse or dependent? Any DD-214 they'd use for veterans' preference?
- Disability (Yes / No / decline). Explain that the federal disability form (CC-305) asks for a typed name and date as a signature; applicants may fill those in only if the candidate chooses Yes or No here.
- Sexual orientation, pronouns, first-generation college graduate, age range ("40 or over?"): some forms ask; answer or decline.
- Tribal or Native preference: are they an enrolled member of a federally recognized tribe, with a CDIB or tribal ID? (Tribal employers and some government jobs give hiring preference and ask for the card.)

**Background and eligibility:**
- At least 18? (Confirm, since it is asked often and a wrong click has caused trouble.)
- Willing to do a background check? Drug screen? Credit check (finance roles)? Driving record check?
- Criminal history and convictions questions ("Have you been convicted...", "unspent convictions or cautions"): tell them these always get parked for them to answer personally. Do not ask about their history.
- Any non-compete, non-solicit, or other agreement that limits where they can work?
- Previously worked for, interviewed with, or applied to any companies they might apply to? Any relatives working at a company they'd target?
- Former government employee (some contractors ask, for conflict-of-interest rules)?
- Need any accommodation during the hiring process? (Usually "No"; record their answer.)

**Experience and education:**
- Years of experience to claim: agree on ONE honest number and what it counts (total work, field-specific, professional only). Check it against the resume dates. Forms ask in many shapes ("years of X experience", dropdown ranges like "3 - 5 years"); applicants answer from this number and the dates on the resume.
- Years with each main tool or skill (forms often ask "How many years of experience do you have with X?"). Record honest numbers for their top 5 to 10 skills.
- Highest education, field, graduation date, GPA (only if they want it given).
- Certifications and licenses held, with numbers and expiration dates if forms might ask.

**Compensation and timing:**
- Desired salary already covered in Step 5. Current or past salary: many US states ban the question; default to leaving it blank or "Prefer not to say". Ask whether they ever want it given.
- Earliest start date / notice period.
- Currently employed? (Some forms ask; also affects the "why are you looking" answer.)

**Consents and contact preferences** (forms make these required checkboxes or Yes/No):
- SMS / text message consent from recruiters: Yes or No? (Past default: No, email only.)
- Consent to AI note-taking or transcription in interviews: Yes or No?
- Keep their application on file for future roles / talent community: Yes or No?
- Applicants accept standard privacy policy and "information is accurate" attestations. Arbitration agreements always get parked.

**Other common questions:**
- "How did you hear about us?": applicants use the actual source. Do they have any referral contacts at companies they want? (Record names only if they say the person agreed.)
- Why are they looking for a new job? (Their words; you'll smooth it into a short answer.)
- How do they use AI tools in their work, if at all? (Asked often on tech and office applications. Record the honest answer.)

- **Approval for autonomous actions.** Explain plainly and get an explicit yes for each:
  - Submit applications without them reviewing each one first.
  - Create accounts on company career sites with their email and generated passwords, stored in `private/accounts.csv` (plaintext on their disk).
  - Read their job-hunting Gmail for verification codes and replies.
  If they decline any, record that in `search_settings.md` under "Autonomy" and adjust: if no auto-submit, applicants park every job at the final Submit step for them.

### Step 7. Filling gaps and stories

This is where application quality comes from. Go through the resume and skills file and ask about:

- **Numbers.** For each role, anything countable they're confident is true: team size, users, tickets per day, systems managed, money saved, time saved. Never estimate for them; only record numbers they state. If they're unsure, leave the claim unquantified.
- **Unclear claims** in the transcript ("I did some stuff with databases": which ones, what did you do?).
- **Tools and skills levels:** which they use daily vs. have touched once. Record the honest level.
- **Gaps** in the work history, so applicants can answer if asked.
- **Stories** (2 to 4 short ones, in their words) for common free-text questions: a problem they solved or something that broke and how they fixed it; a project they're proud of; working with a difficult person or teaching someone; a mistake and what they learned. Record what happened, what they did, and the result.
- **Names to never use:** former employers, clients, or products they don't want named, or names with special spelling or capitalization. These go into `writing_rules.md` and `banned_terms.txt`.
- **Resume preferences:** one page or two, anything they always want included, and any title they prefer for a role.

## Step 8. Write the profile files

Fill in the templates in `profile/` (replace every `{{placeholder}}`; delete template instructions in `<!-- -->` comments once used). Keep the structure; write in plain sentences.

1. `profile/search_settings.md`: every value from Steps 4 to 6.
2. `profile/candidate_profile.md`: all facts, organized. Mark anything unknown as **[ASK]**. Include the stories. Include "Angles": 2 to 4 ways to pitch the candidate for their different target roles, each listing which facts to lead with.
3. `profile/application_answers.md`: identity table, eligibility table, EEO choice, reusable answers.
4. `profile/writing_rules.md`: fill the candidate-specific rules at the top.
5. `profile/banned_terms.txt`: one per line, names that must never appear on a resume. Leave only the comment lines if there are none.

Run the `unslop` skill on any prose you wrote for reuse (summary text, reusable answers). Never write an em dash.

## Step 9. Master resume

1. Write `resume/master_resume.md` in the build format described in `profile/writing_rules.md`. Start from the candidate's own wording in `resume/ORIGINAL_resume.txt`, and strengthen it with facts from the profile. Every claim must trace to the original resume, the skills file, or an interview answer.
2. Header: name, optional headline, then contact line: `City, ST (Remote) | phone | email | linkedin` (drop "(Remote)" if they don't want remote work). Never the street address.
3. Run `unslop` on it, then build: `.venv/bin/python tools/build_resume.py resume/master_resume.md`.
4. Check the PDF (Read it) for layout problems and length. Fix and rebuild.
5. Show the candidate the result (give the path to the PDF and paste the text). Ask them to read every line and correct anything wrong or overstated. Iterate until they approve.

## Step 10. Job sourcing plan

Fill in `profile/job_sourcing.md`:

1. Titles to search, from Step 5, plus close synonyms.
2. Keywords from their strongest skills, for ATS searches.
3. **Local employers** (only if they'd take onsite/hybrid work): use WebSearch to list 15 to 30 real employers within their driving range likely to hire for their target roles (hospitals, school districts, universities and colleges, city/county/state government, large local companies, tribal nations or other major regional employers, local agencies and service companies). Include the careers page URL for each. Verify a few distances with a map search.
4. Niche boards for their field (for example: professional association job boards, industry-specific boards, state job boards, USAJOBS if they qualify).

## Step 11. Finish

1. Re-check any prerequisites that were missing in Step 2. List anything still missing and how to fix it.
2. Create `private/accounts.csv` with the header `date,site,url,username,password,notes`.
3. Write the first entry in `applications/coordinator_state.md`: setup date, settings summary, "no runs yet".
4. Delete `profile/_interview_notes.md` after confirming everything in it made it into the profile files.
5. Give the candidate a short summary: target roles, location rules, pay floor, how many at once, what gets parked for them.
6. Ask for final approval to begin. When they say yes, create `.setup_complete` containing today's date, delete `setup_progress.md`, and tell them:
   - To start (now or later): run `claude --chrome` in this folder and paste the prompt from the README "Running it" section. If they want to start right now, begin the coordinator loop in `CLAUDE.md` immediately.
   - Check `applications/needs_me.md` daily.
   - They can change any setting by telling Claude in plain language.
