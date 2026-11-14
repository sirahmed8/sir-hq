# alloydb-omni-container

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-container\SKILL.md`.

## Summary
This Google skill guides an agent through running AlloyDB Omni in a Docker or Podman container for local or offline development. It covers starting a named container with a persistent data directory and `POSTGRES_PASSWORD`, checking status and logs, stopping or optionally removing the container, and giving the user the interactive `psql` command to connect.

## When to use / when NOT
Use for local development, evaluation, or offline PostgreSQL-compatible workloads where the lightweight container model is acceptable. Do not use it for production workloads that need high availability, automated backups, or managed operations; the source explicitly says the container model lacks those high-end features.

## Inputs, outputs, tools
Inputs are the AlloyDB Omni image tag, container name, host data directory, `postgres` password, and whether the user prefers Docker or Podman. Outputs are a running detached container, status and log inspection, optional stop/remove actions, and connection instructions for `psql`. Tools are `docker` or `podman`, the `google/alloydbomni` image, a host volume at `/var/lib/postgresql/data`, port `5432`, and `psql` inside the container.

## 5 most important rules
1. Ask for version, container name, data directory, password, and Docker versus Podman before running anything.
2. Create the data directory with `mkdir -p` if needed and mount it to `/var/lib/postgresql/data` so data survives container replacement.
3. Run detached with `--name`, `-e POSTGRES_PASSWORD`, `-v`, `-p 5432:5432`, and `--restart=always`.
4. Check state with `ps -a -f name=<CONTAINER_NAME>` and inspect problems with `logs`; ask before removing a container.
5. For connection, provide the interactive `docker exec -it <CONTAINER_NAME> psql -U postgres` or Podman equivalent for the user rather than trying to run an interactive shell yourself.

## Risks / owner notes
The password appears in the run command and process environment, and port `5432` can conflict with an existing database. Container restart policy does not provide production HA or backups, and removing a container should be confirmed because the mounted data directory is what preserves data. The owner should choose credentials and storage location deliberately.

## Category / tags
data · alloydb, postgres, docker, podman, container, local-development, psql, google-cloud

## Revisions
Single gemini skill revision. No codex, claude, kilo, cursor, opencode, or windsurf copy was present.
