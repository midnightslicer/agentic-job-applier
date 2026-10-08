# Browser: Chrome debugging mode

Application forms are filled in a real Chrome that you (the candidate) start in **debugging mode**. The debugging port lets any harness, through a Chrome MCP server, drive that exact browser: your tabs, your logins, your autofill. This is the path every harness uses; it is not tied to one agent product.

(If you use Claude Code and prefer the Anthropic browser extension, "Claude in Chrome" still works; see README.md, Prerequisites 3, Option B. The rest of this file is for Chrome debugging mode.)

## 1. Start Chrome in debugging mode

Run the command for your OS in a terminal. Keep that Chrome window open for as long as the run lasts. A dedicated profile directory (`.job-apply-chrome`) is required: newer Chrome versions ignore the debugging port on your default profile, and keeping the profiles separate keeps the automation Chrome out of your day-to-day browsing.

**Linux (Chrome):**

```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=$HOME/.job-apply-chrome
```

Chromium or Brave: same flags with `chromium` or `brave-browser`.

**macOS (Chrome):**

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=$HOME/.job-apply-chrome
```

**Windows (PowerShell):**

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="$HOME\.job-apply-chrome"
```

(Microsoft Edge works the same with `msedge.exe`.)

Check it worked: `curl http://127.0.0.1:9222/json/version` should answer with a line of JSON naming the browser. If not, close every Chrome window of that profile and run the launch command again.

## 2. Sign in once (stays signed in)

In the debugging-mode Chrome window, sign in to:

- LinkedIn, Indeed, and any other job boards you want searched.
- The job-hunting Gmail account (the one in `profile/search_settings.md`).

The profile remembers these across launches. You can keep your normal Chrome window open beside it; the agent only uses the debugging-mode one. Agents cannot create job-board accounts for you, but they do create accounts on company career sites (Workday, iCIMS, and the like) when an application requires one; those logins land in `private/accounts.csv`.

## 3. Connect your harness (Chrome debugging MCP)

The agent reaches the debugging port through an MCP server. Any harness with an MCP client can do this; add either of these servers with the flags shown, then start your harness in the kit folder.

**Option A: chrome-devtools-mcp (Google's, recommended when supported):**

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest", "--browser-url=http://127.0.0.1:9222"]
    }
  }
}
```

Claude Code: `claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest --browser-url http://127.0.0.1:9222`

**Option B: Playwright MCP:**

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest", "--cdp-endpoint=http://127.0.0.1:9222"]
    }
  }
}
```

**Other harnesses:** any MCP browser server that can attach to an existing Chrome via the Chrome DevTools Protocol (look for a browser URL, CDP endpoint, or "connect to running browser" option) behaves the same way. The kit only assumes the agent can: open a page in a new tab, read page text and screenshots, click and type, and run JavaScript in the page.

**No MCP support at all?** The harness can still scout (web search/fetch and ATS API scripts run fine without a browser) but not fill forms; applicants will return `failed` with "no browser connection" rather than doing anything risky.

If browser actions stop working during a long run, the server may have lost the connection: restart the harness, and if Chrome was closed, run the launch command again.

## 4. Rules for agents sharing the browser

- Open your own tab first and use only that tab's ID for the whole job. Do not touch other tabs.
- Do not close the browser or someone else's tab mid-run.
- Verify before you submit (screenshot or JavaScript) and re-check elements after page loads: they go stale.
- Do not sign in or out of any account; use what is already signed in.

## 5. Safety notes

- The debugging port is reachable by every program running as your user, and this Chrome profile holds your job-board and Gmail logins. Start it only while running the kit, and quit it (or relaunch Chrome without the flag) when done.
- Never forward, tunnel, or expose the port beyond this machine.
- On Windows + WSL: run the harness in Windows, or make sure WSL can reach the Windows host port (mirrored networking) before blaming the MCP server.