# gcloud-auth-verification

## Summary
Tiny but critical triage skill for Google Cloud auth failures. Catalogs the exact error signatures: gcloud/bq CLI errors ("You do not currently have an active account selected", "No credentialed accounts", "Configuration error: No account is currently active") and library/notebook errors (`google.auth.exceptions.DefaultCredentialsError: Could not automatically determine credentials`, and 403 Access Denied that may actually be IAM). Required first step is independent verification via `gcloud auth list` — never ask the user to log in before checking. Key distinction: if an account IS listed but calls return 403, the problem is IAM permissions on that account, not missing auth — investigate roles, don't re-login. If truly no credentials, STOP and hand the user the exact commands (`gcloud auth login` for CLI, `gcloud auth application-default login` for ADC used by bq CLI and Python libraries/notebooks). Credentials must be established by the user — never attempt code workarounds.

## When to use / when NOT
Use whenever gcloud, bq, dataform, or Google client libraries throw auth-looking errors. Not for diagnosing 403s when auth is verified (that's an IAM problem — other skills/skills' IAM guidance apply).

## Inputs, outputs, tools
- Inputs: error message text, `gcloud auth list` output.
- Outputs: diagnosis (missing creds vs IAM vs auth OK), exact user commands.
- Tools: `gcloud auth list`, `gcloud auth login`, `gcloud auth application-default login`.

## 5 most important rules
1. ALWAYS run `gcloud auth list` yourself before asking the user to authenticate — verification first, never assume.
2. An active account + 403 = IAM permission gap, not an auth problem; investigate roles instead of re-login loops.
3. Two separate credentials exist: gcloud CLI auth AND Application Default Credentials — ADC is required for bq CLI and most Python libs; user may need both commands.
4. Never fix credentials via code or alternative tooling — auth is a user action (browser login/consent).
5. After user confirms login, re-run `gcloud auth list` to verify before resuming the original task.

## Risks / owner needs
Login is inherently an owner action (browser OAuth, possibly 2FA) — this skill's whole point is producing the exact minimal command set for OWNER_ACTIONS.md rather than stalling.

## Category and tags
Category: cloud. Tags: gcloud, authentication, adc, iam, troubleshooting, google-cloud.

## Revisions
Single gemini skill copy; no competing revisions.
