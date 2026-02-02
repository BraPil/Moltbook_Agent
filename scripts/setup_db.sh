#!/usr/bin/env bash
set -euo pipefail

# Wait for postgres then create extension and table
PGHOST=${PGHOST:-localhost}
PGPORT=${PGPORT:-5432}
PGUSER=${PGUSER:-moltbook}
PGDATABASE=${PGDATABASE:-moltbook}

cat <<'SQL' > /tmp/setup_pg.sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS documents (
  id SERIAL PRIMARY KEY,
  title TEXT,
  content TEXT,
  metadata JSONB,
  embedding vector(1536)
);

CREATE INDEX IF NOT EXISTS ON documents USING ivfflat (embedding vector_l2_ops) WITH (lists = 100);
SQL

until psql "host=$PGHOST port=$PGPORT user=$PGUSER dbname=$PGDATABASE" -f /tmp/setup_pg.sql; do
  echo "Waiting for postgres..."
  sleep 2
done

echo "Database setup complete."