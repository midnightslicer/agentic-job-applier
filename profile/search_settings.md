# Search Settings

<!-- Filled in during setup (SETUP.md). The screening filters in AGENTS.md read these values. Change only with the candidate's approval. -->

## Contact used on applications

- Application email: {{email}}  (the inbox Claude reads for codes and replies)
- Phone: {{phone}}
- Resume location line: {{City, ST}} {{(Remote) if open to remote}}

## Location

- Home location for distance checks: {{city, state ZIP}}
- work_arrangement: {{remote only | remote preferred, onsite/hybrid OK within range | any | prefers onsite}}
- max_commute_miles (onsite): {{number}}
- max_commute_miles (hybrid): {{number, or same as onsite}}
- Relocation: {{no | yes, to: ...}}
- Priority order for the queue: {{e.g. remote first, then local hybrid, then local onsite; ties broken by fit score}}

## Pay

- pay_floor: {{$N/yr}} (= {{$N/hr}} at 2,080 hrs). Skip postings whose top of range is below this. No posted pay is fine.
- Desired salary range (for forms): {{$N to $N}}
- Single-number desired salary: {{$N}}
- Hourly roles OK: {{yes/no}}

## Job types and level

- Employment types: {{full-time | part-time | contract | temp-to-hire | internship}}
- Target level: {{entry | junior | mid | senior}}
- Experience cutoff: skip postings that require more than {{N}} years.
- Travel: {{none | up to N%}}
- Schedule limits: {{time zones, shifts, weekends, nights}}

## Extra filters

<!-- Candidate-specific skips: industries, companies (e.g. current employer), required tools they lack, anything else. One per line. -->
- {{...}}

## Run settings

- max_parallel_applicants: {{1-4, default 2}}
- active_window_days: 7 (applied rows older than this with no reply become no_response)
- One application per company: {{yes (default) | no}}
- Posting age window: 14 days by default; scouts may widen to 30 (and older for strong fits) when volume is low.

## Autonomy (approved by the candidate on {{date}})

- Submit without review: {{yes/no}}  (if no: applicants fill everything, then park at the Submit step)
- Create career-site accounts and store passwords in private/accounts.csv: {{yes/no}}
- Read the application inbox for codes and replies: {{yes/no}}
