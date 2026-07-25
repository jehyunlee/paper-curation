# Security — Attack Surface & Guardrails

Threat model for paper-curation and the agent harness that operates it. Scope:
the pipeline repo, its git remote, the public Cloudflare deploy, local-only data,
and the Claude agent that edits/runs all of the above. This is an operational
security document, not a legal one — for copyright/deploy legality see
[`operations/legalcheck/legalcheck.html`](operations/legalcheck/legalcheck.html).

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
- **Control:** `scripts/pre-push` passes the exact pushed refs to
  `scripts/scan-secrets.py`. The scanner enumerates newly introduced git
  objects and reads raw commit/tag/blob bytes through `git cat-file --batch`;
  it does not depend on diff generation. This covers merge-resolution blobs,
  `.gitattributes -diff`, NUL/binary blobs, and annotated-tag messages.
- **Patterns:** Anthropic/OpenAI, AWS `AKIA`, GitHub `gh*`, and Google `AIza`;
  whitespace-split and standard-base64 forms are normalized and checked.
- **Backstop:** `.github/workflows/secret-scan.yml` scans the complete current
  HEAD snapshot and tag objects on every push/PR; GitHub-native push protection
  remains the pre-receive prevention layer.
- **Activation guard:** `pipeline/doctor.py` check 10 fails if the hook/scanner
  is missing or drifted from source.
- **Verified:** committed integration tests exercise clean/worktree-only cases
  plus new/existing refs, merge resolution, `-diff`, NUL blob, annotated tag,
  whitespace split, base64, AWS, GitHub, and Google patterns.
- **Do NOT:** `git push --no-verify` (bypasses the scan — also blocked by the
  agent guard); commit real keys "temporarily".

### S2 — Destructive agent action
- **Control (static):** `~/.claude/settings.json` → `permissions.deny` blocks
  `git push --no-verify/--force`, `git init`, `mv .git`, `rm -rf / ~ $HOME`,
  `mkfs`/`diskutil erase`/`tmutil delete`, reads of `config.json`/`~/.ssh`, and
  writes into `.git/` or the guard/settings themselves.
- **Control (dynamic):** `scripts/claude_guard.py` is source-controlled and
  installed by `scripts/install-agent-guard.py` to
  `~/.claude/hooks/guard.py` (PreToolUse). It parses each executable shell line
  (excluding heredoc prose), blocks hook disablement (`chmod -x`,
  `core.hooksPath`), credential discovery, `.git` destruction, catastrophic
  `rm`, remote-pipe-to-shell, and self-disable; Write/Edit targets use realpath
  so symlink escapes are blocked.
- **Prompt restored:** `skipDangerousModePermissionPrompt` is absent.
- **Activation guard:** doctor check 10 verifies installed guard == tracked
  source, deny/PreToolUse wiring, prompt state, and broken agent symlinks.
- **Verified:** committed matrix: dangerous 23/23 blocked, normal 13/13 allowed,
  plus realpath symlink escape blocked.
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
- **Static deny is a coarse floor.** The source-controlled PreToolUse parser is
  the precise layer; malformed hook input fails closed. Doctor detects missing,
  changed, or unconfigured installed guards.
- **Encoded-secret detection is bounded:** standard base64 and whitespace split
  are covered; arbitrary encryption/novel encodings are not. GitHub-native
  secret scanning remains complementary.

## Re-verify the controls
- `bash scripts/install-hooks.sh && python3 scripts/install-agent-guard.py`
- `python pipeline/doctor.py` → check 10 verifies Git + agent activation.
- `python -m unittest -v pipeline.tests.test_security_guardrails`
- CI: the same raw-object scanner runs on every push/PR.
