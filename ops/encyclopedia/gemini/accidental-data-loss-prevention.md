# accidental-data-loss-prevention

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\accidental-data-loss-prevention\SKILL.md`
- SKILL.md size: 1316 chars
- Identical content to: `encyclopedia/claude/accidental-data-loss-prevention.md`

Auto-generated stub: this SKILL.md is byte-identical to `encyclopedia/claude/accidental-data-loss-prevention.md`. Read that digest for full details.

Description: | **STOP AND VERIFY**: Before running any command or tool that results in irreversible data loss, you MUST obtain explicit user consent. When in doubt, ask. It is better to wait for confirmation than to accidentally delete production data or critical project assets. Use this for: - SQL: DROP TABLE/VIEW/SCHEMA/DATABASE, TRUNCATE, or broad DELETE (missing WHERE or using 1=1). - Cloud Storage: gsutil rm or gcloud storage rm targeting production data or critical buckets. - Infrastructure: gcloud projects delete, deleting Spanner/BigQuery/Dataproc resources, deleting secrets, or KMS key destruction.