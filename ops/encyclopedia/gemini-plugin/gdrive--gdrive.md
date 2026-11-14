# gdrive

## Summary
gdrive is a Google-published skill for managing files and folders in Google Drive. It provides CRUD operations for files and folders, including upload/download/copy/rename/move operations, folder creation and listing, file search by title, sharing and permission management, and file metadata inspection. The skill handles authentication flow, folder hierarchy navigation, and batch operations. All operations require user confirmation for modifications (upload, move, delete, share).

## When to use / when NOT
Use when users need to manage Google Drive files and folders: upload, download, organize, search, share, or inspect metadata. Do NOT use for non-Google file types, for bulk operations without user confirmation, or for file types better suited to other tools (local filesystem operations, SSH/SFTP for code).

## Inputs, outputs, tools
- Inputs: Operation type (upload, download, copy, rename, move, mkdir, ls, search, share, metadata), file/folder paths, sharing permissions, search query.
- Outputs: File metadata (ID, name, parents, size, mimeType), folder listing, share confirmation, download confirmation.
- Tools: `gdrive` CLI (files upload, download, copy, mv, rm, mkdir, ls, about, permissions, search). No scripts folder.

## 5 most important rules
1. Always ask for user confirmation before any modification operation (upload, move, rename, delete, share).
2. For uploads: ask for local path first; never auto-select files.
3. Search: use title search first; fall back to full-text if needed. Never expose file contents in search results.
4. Permissions: default to private; only share when explicitly requested.
5. Never hardcode file IDs or paths; always ask user to provide or confirm.

## Risks / things needing the owner
Google account authentication required first run; user must complete OAuth flow. Shared storage quotas may limit upload size. No direct owner actions beyond initial sign-in.

## Category / tags
google · drive, file-management, upload, download, share, metadata, folder, crud

## Revisions
Single revision in `C:\Users\a7med\.config\kilo\skills\gdrive\SKILL.md` (Google-published, Apache-2.0, v1). Only kilo has this skill; scripts/references folders exist (scripts=True, refs=False per earlier check).