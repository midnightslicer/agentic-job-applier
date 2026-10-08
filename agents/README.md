# Subagents

This folder holds the two worker agent definitions shared by every harness. The coordinator instructions in `AGENTS.md` spawn them.

- `job-scout.md`: finds up to 20 qualifying jobs, appends them to `applications/job_queue.csv` and `applications/seen_postings.csv`, then retires. Never submits anything.
- `job-applicant.md`: applies to exactly one job with a tailored resume, then retires. Spawned with the job's full queue row pasted into the prompt.

The files are plain markdown with a small frontmatter block (`name`, `description`, `model`). The frontmatter is harness metadata; everything under it is the prompt.

## Spawn contract (rely on this; other files do)

- A FRESH agent is spawned for every batch (scout) or every job (applicant). Never reuse a subagent.
- The applicant gets the job's full `job_queue.csv` row in its prompt.
- The applicant returns exactly one result: `applied`, `parked`, `skipped`, or `failed`, plus the report details listed in its file. The coordinator, not the applicant, updates `job_queue.csv` and `applications_log.csv`.
- Keep the two names and the report format stable: `AGENTS.md`, `SETUP.md`, and the queue tooling depend on them.

## Wiring per harness

- **Claude Code** (already wired): `.claude/agents/` holds pointer stubs with the same names, so the Task tool spawns `job-scout` and `job-applicant` as before. The stubs load the real files from here. Do not edit the stubs; edit the real files in this folder.
- **Harnesses with a local agent directory** (for example `.pi/agents/`, `.codex/`, `.cursor/agents/`): symlink these files into it, or paste each file's body into that harness's subagent-prompt field.
- **Harnesses without subagents**: run serially. Do a scout phase and work through its queue with applicant phases one at a time, treating each agent file's body as your prompt for that phase. Follow `AGENTS.md` for the loop, filters, and hard rules throughout.
- **The shared definitions carry no `model` field.** Model choice is harness-coupled metadata and lives where the harness understands it. Claude Code's pointer stubs pin `model: sonnet`, which never blocks a launch there (an unavailable alias is substituted or falls back to the main model). Other harnesses run subagents on their default model, or on the `subagent_model` recorded in `profile/search_settings.md` during setup. If a harness requires a model per agent, map it with that harness's own spec, for example a provider-qualified `provider/model-id`. If a harness rejects the frontmatter or cannot spawn at all, map or drop the field, or run the phase serially; never stall the loop over an unspawnable subagent.