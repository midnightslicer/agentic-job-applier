# Claude Job Apply

A folder that turns an AI coding agent into your own job search assistant. It was built on Claude Code and still works best there, but any capable agent harness can run it (Codex CLI, Gemini CLI, pi, OpenCode, Cursor, and similar). The agent finds openings that fit you, writes a tailored resume for each one, fills out the application in your Chrome browser, and keeps a log of everything. When it hits something only you can do (an assessment, an interview request, a CAPTCHA it can't pass), it writes it down in `applications/needs_me.md` and moves on to the next job.

It only uses facts about you that you give it. It will not invent skills, jobs, or numbers.

You do three things:

1. Set up the prerequisites below (one time, about 20 minutes).
2. Put your resume and a skills file in the `input/` folder.
3. Start your agent in this folder and type "Let's get started."

---

## Prerequisites

### 1. An agentic coding harness

**Claude Code (recommended).** You need a paid Claude plan (Pro, Max, Team, or Enterprise) and Claude Code installed. Works on macOS, Linux, and Windows; on Windows, run Claude Code directly in Windows, not inside WSL (Claude in Chrome doesn't work from WSL).

- Install: https://code.claude.com/docs/en/setup
- Sign in with your claude.ai account (`/login`) the first time you run `claude`. Claude in Chrome does not work if you sign in with an API key.

A full run uses a lot of usage, and on Pro you will hit limits sooner. When you hit a limit, the run pauses and picks up where it left off next time.

**Other harnesses.** The kit is plain markdown and scripts, so what it needs from a harness is:

- It reads `AGENTS.md` on start (most do; if not, tell it to read `AGENTS.md` first).
- It can run shell commands and read and write files.
- It can connect MCP servers, including a Chrome browser MCP (Prerequisite 3).
- It can spawn subagents, or it can work serially using the phases in `agents/`.

Harnesses without subagents run more slowly and with less parallelism, but the coordinator loop supports that mode. The Gmail connector described below is a Claude/claude.ai feature; on other harnesses, read the inbox through Chrome instead for now.

### 2. A Gmail account (a new one just for job hunting is best)

Applications need an email address for verification codes, confirmation links, and recruiter replies. Claude reads this inbox for you, so a dedicated address keeps your personal mail out of it.

1. Create a Gmail account at https://accounts.google.com/signup. Something like `firstname.lastname.jobs@gmail.com` looks professional.
2. In Chrome, sign in to that Gmail account and leave it signed in.
3. Connect Gmail to Claude: open https://claude.ai, go to **Settings > Connectors**, find **Gmail**, click **Connect**, and sign in with the job-hunting Gmail account. Claude Code uses the same connectors when you're signed in with the same claude.ai account.
4. Optional: in Gmail settings, forward a copy of everything to your personal email so you don't miss interview requests.

Claude never replies to recruiters for you. It reads the inbox, logs replies, and puts interview requests at the top of `applications/needs_me.md`.

### 3. Chrome, connected for your agent

Applications are filled out in a real Chrome browser that your agent can drive. Two ways to set that up; either works on its own.

**Option A: Chrome debugging mode (works with every harness).** You start Chrome with a debugging port; your agent connects to that port through a Chrome MCP server and fills forms in your real browser.

1. Start Chrome from a terminal with the debugging port and a dedicated profile directory:
   - **Linux:** `google-chrome --remote-debugging-port=9222 --user-data-dir=$HOME/.job-apply-chrome`
   - **macOS:** `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=$HOME/.job-apply-chrome`
   - **Windows (PowerShell):** `& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$HOME\.job-apply-chrome"`
   The dedicated profile directory is required (Chrome ignores the debugging port on your default profile) and keeps the automated browser separate from your day-to-day one.
2. Check it worked: `curl http://127.0.0.1:9222/json/version` answers with a line of JSON.
3. In that Chrome window, sign in to LinkedIn, Indeed, and your job-hunting Gmail. The profile remembers them for next time.
4. Add a Chrome MCP server to your harness, pointed at the debugging port. Two good options:
   - **chrome-devtools-mcp** (Claude Code: `claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest --browser-url http://127.0.0.1:9222`)
   - **Playwright MCP** (`npx @playwright/mcp@latest --cdp-endpoint http://127.0.0.1:9222`)

   Full connection instructions for many harnesses, plus safety notes, are in `docs/browser.md`.
5. Leave that Chrome window open while a run is going. The agent opens its own tabs; you can keep using other tabs, but don't close the ones it's working in. If browser actions stop working mid-run, restart the harness (and Chrome, if it was closed).

**Option B: Claude in Chrome (Claude Code only).** This lets Claude fill out application forms in your real browser through the Anthropic extension.

1. Use Google Chrome or Microsoft Edge. Other Chromium browsers (Brave, Arc, Vivaldi, Opera) also work.
2. Install the **Claude** extension by Anthropic from the Chrome Web Store: https://chromewebstore.google.com (search "Claude"). Make sure the publisher is Anthropic.
3. Click the extension icon and sign in with the same claude.ai account you use for Claude Code.
4. Start Claude Code with `claude --chrome` and press Enter on the one-time intro. Then run `/chrome` and choose **Enabled by default** so you don't need the flag every time. The `/chrome` panel should show "Status: Enabled" and "Extension: Installed".
5. Sign in to LinkedIn, Indeed, and any other job sites you want Claude to search, in Chrome. Claude can't create accounts on job boards for you; it uses yours to find jobs. (It does create accounts on company career sites, like Workday, when an application requires one. See `private/accounts.csv`.)

Leave Chrome open while a run is going. Claude opens its own tabs; you can keep using other tabs, but don't close the ones it's working in.

If browser actions stop working during a long run, the extension has probably gone idle. Run `/chrome` and choose **Reconnect extension**.

Docs: https://code.claude.com/docs/en/chrome

### 4. The unslop skill

Unslop strips the "written by AI" tells out of resumes, cover letters, and form answers so they read like you wrote them.

Works in any harness with a skills folder. Install with Node.js (https://nodejs.org) installed:

- Claude Code (and other agents the skills CLI knows):

```bash
npx skills add theclaymethod/unslop -g -a claude-code
```

- Any harness, by hand:

```bash
git clone https://github.com/theclaymethod/unslop.git ~/unslop
mkdir -p ~/.claude/skills
ln -s ~/unslop ~/.claude/skills/unslop
```

(For a different harness, symlink it into that harness's skills folder instead of `~/.claude/skills`.) Restart your agent afterward and check that the skill shows up. If a harness has no skills support, the kit falls back to applying `profile/writing_rules.md` by hand, which works but is weaker.

### 5. Resume build tools (the agent will help with this during setup)

- Python 3.9 or newer.
- LibreOffice, for turning resumes into PDFs: https://www.libreoffice.org/download (on Linux, install `libreoffice` from your package manager; on Mac, `brew install --cask libreoffice`).

Setup creates a Python virtual environment in `.venv/` and installs `python-docx` for you.

---

## What to put in `input/`

Put exactly these two things in the `input/` folder:

### Your most recent resume

Any format: `.pdf`, `.docx`, `.txt`, or `.md`. Name it whatever you like.

### A skills file (`skills.txt`)

This is the most important file in the kit. Your resume is a summary; this file is where the agent gets everything else it can truthfully say about you. More detail here means better tailored resumes and better answers to "tell us about a time when..." questions. The agent won't make up information about you, and it skips jobs whose hard requirements (a degree, license, or years of experience) you don't meet, so anything you leave out here can cost you jobs you'd qualify for.

Write everything you can do, have done, and have built: tools, software, equipment, certifications, projects, side work, volunteer work, problems you solved, things you're proud of, numbers you know are true. Messy is fine. The agent organizes it.

Three ways to make it:

1. **Talk it out (recommended).** Start a voice recorder on your phone and ramble for 20 to 30 minutes about your work. Go job by job: what you did each day, what broke and how you fixed it, what you built, what you got praised for, what tools you used, what you learned on your own. Then turn the recording into text (most phones' recorder apps can transcribe; otherwise use a transcription tool like Otter, Google Recorder, Apple Voice Memos transcripts, or Whisper) and save the text as `input/skills.txt`. Don't clean it up. People remember far more out loud than when staring at a blank page, and the stories you tell are exactly what interview and screening questions ask for.
2. **Ask an AI that knows you.** If you've used ChatGPT, Claude, or another assistant with memory for a while, ask it: "Write down everything you know about my skills, work history, projects, tools I use, and accomplishments. Be detailed and only include things I've actually told you." Read it over, delete anything that isn't true, and save it as `input/skills.txt`.
3. **Write it by hand.** A bulleted list is fine. Aim for a page or more.

You can combine these: paste all of it into the one file.

---

## First run

Start your agent in this folder, with Chrome running (either Option A above or Option B):

```bash
cd claude_job_apply
claude --chrome   # Claude Code with Claude in Chrome (Option B); plain `claude` if you set up the Chrome debugging MCP (Option A).
                  # Other harnesses: start them here the usual way.
```

Then type: **Let's get started.**

On the first run the agent will:

1. **Disconnect this folder from git.** It deletes the `.git` folder so your personal information can never be pushed back to the repo you downloaded this from.
2. Check the prerequisites (Chrome connection, Gmail connector, unslop, Python and LibreOffice) and help you fix anything missing.
3. Read your resume and skills file.
4. **Interview you.** Answer in plain language. It takes about 20 to 40 minutes. It asks everything job applications ask, so that later it can fill in forms without stopping to ask you:
   - **Contact and location:** the email and phone to put on applications, your mailing address (forms only, never the resume), your state, remote preference, and how far you'll drive.
   - **The job you want:** target job titles, experience level, pay range (your minimum and what to ask for), full-time/part-time/contract, travel, schedule (evenings, weekends, on-call), and companies or industries to avoid.
   - **Work authorization and immigration:** whether you're authorized to work in the US, whether you need visa sponsorship now or in the future, your status (US citizen, green card, H-1B, H-1B transfer, OPT/STEM OPT, TN, etc.), and security clearance.
   - **Voluntary demographic questions:** race, Hispanic/Latino, gender, veteran status, disability, and a few less common ones (pronouns, age 40+, tribal membership). These are optional on every application. "I'd rather not say" is always a fine answer, and it's the default.
   - **Background and logistics:** background check, drug screen, driver's license, non-competes, relatives at a company, SMS and AI-transcription consent, start date.
   - **Your experience:** one honest "years of experience" number, years with your main tools, numbers you're sure of, and 2 to 4 short stories (a problem you solved, a project you're proud of) for the "tell us about a time..." questions.

   Criminal history questions are never asked during setup. Any application that asks one gets set aside for you to answer yourself.
5. Build your profile, a master resume, your standard form answers, and a job-search plan, then show you the master resume to approve.

It will not apply to anything until you approve the master resume and say go.

## Running it

After setup, start a run any time. Launch Chrome in debugging mode (Option A) or keep Claude in Chrome connected (Option B), then:

```bash
claude        # Claude Code. Other harnesses: start them here the usual way.
```

and type:

```
Read AGENTS.md and start the coordinator loop. Run autonomously, park anything that needs me in applications/needs_me.md, and keep going until I stop you.
```

The same prompt resumes a stopped run.

### Running unattended

By default the harness asks permission before many actions, which means you'd have to sit there clicking "yes". Set its approval mode so a run can continue on its own. In Claude Code, pick one:

- **Auto mode (recommended).** Switch Claude Code to Auto mode (press Shift+Tab until the mode line says auto). Claude Code then approves routine actions itself, and browser actions it approves skip the Chrome extension's per-site prompts. This works most of the time; check back occasionally for a prompt it stopped on.
- **Approve as you go.** Approve tools as they come up and choose "don't ask again" for each. Safest, but it takes a while the first time.
- **Skip all permissions.** Start with `claude --chrome --dangerously-skip-permissions` (drop `--chrome` if you use the Chrome debugging MCP instead). This lets Claude run any command without asking. Only do this on a computer or user account with nothing on it you'd hate to lose.

Other harnesses have their own approval settings; allow file and shell actions up front so the run doesn't stall.

## Checking in

| File | What's in it |
|---|---|
| `applications/needs_me.md` | Things waiting on you. Interviews and assessments are at the top. |
| `applications/applications_log.csv` | Every application and its status. Opens in Excel or Google Sheets. |
| `tailored/` | One folder per job: the posting, the resume sent, and any written answers. Read these before an interview. |
| `private/accounts.csv` | Logins the agent created on company career sites. |
| `LESSONS.md` | What it learned, and questions it wants you to answer. |

## Privacy

- Everything stays on your computer, except what's sent to the agent while it works and what goes into the applications themselves.
- `private/accounts.csv` holds passwords in plain text. Keep this folder on an encrypted disk or delete the file when you're done. Never upload it or share it.
- Don't put this folder back into a git repo with a remote. Setup removes the git connection for this reason.

## What it won't do

- Lie or stretch the truth. If you didn't tell it, it won't claim it.
- Take assessments, coding tests, writing exercises, or video interviews as you. Those get parked for you.
- Enter your Social Security number, date of birth, or bank details.
- Pay for anything, or accept "placement fee" or "income share" deals.
- Reply to recruiters. That's yours.

## Customizing

After setup, everything is plain text you can edit:

- `profile/search_settings.md`: location, distance, pay floor, remote preference, filters.
- `profile/candidate_profile.md`: facts about you. Add to it any time.
- `profile/application_answers.md`: standard answers for form questions.
- `profile/job_sourcing.md`: job titles and where to look.

Or tell your agent in plain language ("I'd also take contract roles", "raise my pay floor to $70k") and it will update the files.