# Security — Attack Surface & Guardrails

Threat model for paper-curation and the agent harness that operates it. Scope:
the pipeline repo, its git remote, the public Cloudflare deploy, local-only data,
and the Claude agent that edits/runs all of the above. This is an operational
security document, not a legal one — for copyright/deploy legality see
[`legalcheck/legalcheck.html`](legalcheck/legalcheck.html).

## Assets & trust boundaries

| Asset | Boundary | Notes |
|---|---|---|
| API keys (Anthropic/OpenAI/Gemini) | `config.json`, env | gitignored; never committed |
| Source + pipeline | git → GitHub (public) | code is backed up by the remote |
| Public deploy | Cloudflare, arXiv/OpenReview OA only | license-gated by `prepare_deploy.py` |
| Local-only data | this Mac | `docs/papers/**`, `docs/_agent/**`, `docs/_local_keys.json`, Zotero library — **not** in git |
| Agent harness | `~/.claude/` | permissions, hooks, plugins — controls what the agent may do |

## Attack surface → control → where it runs → verification

### S1 — Secret leaked through git
- **Control:** `scripts/pre-push` scans exactly the commits being pushed (ref
  list read from stdin; new branches scoped with `--not --remotes`, so the first
  push is covered). Hard-blocks on `sk-(ant|proj)-…` keys.
- **Backstop that runs regardless of local hook state:** `.github/workflows/secret-scan.yml`
  (every push/PR) + GitHub-native push protection (repo settings).
- **Activation guard:** `pipeline/doctor.py` check 10 fails if the hook is missing
  or drifted from source, so it cannot sit silently uninstalled.
- **Verified:** isolated-repo reproduction — a committed key on a new-branch first
  push reaches the remote with the old scan (`git diff HEAD` = work tree, not the
  push) and is blocked by the current scan.
- **Do NOT:** `git push --no-verify` (bypasses the scan — also blocked by the
  agent guard); commit real keys "temporarily".

### S2 — Destructive agent action
- **Control (static):** `~/.claude/settings.json` → `permissions.deny` blocks
  `git push --no-verify/--force`, `git init`, `mv .git`, `rm -rf / ~ $HOME`,
  `mkfs`/`diskutil erase`/`tmutil delete`, reads of `config.json`/`~/.ssh`, and
  writes into `.git/` or the guard/settings themselves.
- **Control (dynamic):** `~/.claude/hooks/guard.py` (PreToolUse) catches the
  obfuscated variants prefix matching misses, and restores blocking of `.git`
  destruction, catastrophic `rm`, remote-pipe-to-shell, and self-disable.
- **Prompt restored:** `skipDangerousModePermissionPrompt` removed — dangerous
  actions prompt again instead of auto-approving.
- **Verified:** 25-case block/allow matrix (dangerous → exit 2, normal dev → exit 0).
- **Do NOT:** re-add `skipDangerousModePermissionPrompt`; grant blanket
  `Bash(git init:*)` / `Bash(mv .git…)` allows in project settings (global deny
  overrides them, but do not weaken it).

### S3 — Public deploy exposes copyrighted / original content
- **Control:** `prepare_deploy.py` re-renders only the upload copy in PUBLIC mode,
  license-gating figures/reviews/audio (`lib/license_util.py`); original full text
  (`text.md`) is hard-excluded from the deploy. See the legality review.

### S4 — Local data loss
- **Control:** code is on GitHub. **GAP:** git-external artifacts
  (`docs/papers/**`, `docs/_agent/**`, `docs/_local_keys.json`, Zotero library)
  live only on this Mac. `doctor.py` check 10 warns while no Time Machine
  destination is configured.
- **Action needed:** configure a Time Machine destination (owner task — requires a disk).

### S5 — Supply chain (plugins / MCP)
- **Surface:** `enabledPlugins` + `extraKnownMarketplaces` in `~/.claude`, MCP
  servers in `~/.claude.json`. **Residual risk:** third-party plugin/MCP code runs
  with the agent's privileges. Keep marketplaces pinned and review updates.

## Residual risk / known gaps
- **Time Machine unset** — S4 backup gap (doctor warns).
- **Static deny is brittle** — prefix matching is bypassable by construction; the
  PreToolUse hook is the robust layer, and it fails **open** on its own crash by
  design (a fail-closed guard that blocked every tool would just be removed). The
  static deny remains as the non-bypassable floor.
- **Secret scan pattern** is Anthropic/OpenAI-key specific (`sk-(ant|proj)-`);
  other credential formats are not covered — rely on GitHub-native scanning too.

## Re-verify the controls
- `bash scripts/install-hooks.sh` then `python pipeline/doctor.py` → check 10 shows the hook active.
- Isolated hook test: commit a fake `sk-ant-…` key on a new branch and confirm the push is refused.
- Guard matrix: pipe sample tool-call JSON into `~/.claude/hooks/guard.py` and check exit 2 vs 0.
- CI: the `secret-scan` workflow runs on every push/PR.
