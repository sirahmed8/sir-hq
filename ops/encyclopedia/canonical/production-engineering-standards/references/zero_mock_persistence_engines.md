# Zero-Mock Persistence Engines & Data Layers

This reference provides concrete, production-ready persistence layers. Hardcoded dummy arrays and mock data are strictly prohibited.

---

## 1. SQLite with Drizzle ORM (Local / Lightweight Full-Stack)

### Schema Definition (`src/db/schema.ts`)
```typescript
import { sqliteTable, text, integer } from "drizzle-orm/sqlite-core";
import { sql } from "drizzle-orm";

export const tasks = sqliteTable("tasks", {
  id: text("id").primaryKey(),
  title: text("title").notNull(),
  completed: integer("completed", { mode: "boolean" }).notNull().default(false),
  createdAt: text("created_at").default(sql`CURRENT_TIMESTAMP`).notNull(),
});

export type Task = typeof tasks.$inferSelect;
export type NewTask = typeof tasks.$inferInsert;
```

### Database Client (`src/db/index.ts`)
```typescript
import { drizzle } from "drizzle-orm/better-sqlite3";
import Database from "better-sqlite3";
import * as schema from "./schema";

const sqlite = new Database(process.env.DATABASE_URL || "app.db");
export const db = drizzle(sqlite, { schema });
```

---

## 2. Client-Side Browser Storage with Dexie.js (IndexedDB)

For offline-capable web and desktop applications, use IndexedDB with Dexie.js rather than transient in-memory arrays:

```typescript
import Dexie, { type Table } from "dexie";

export interface UserNote {
  id: string;
  title: string;
  body: string;
  updatedAt: number;
}

export class AppDatabase extends Dexie {
  notes!: Table<UserNote, string>;

  constructor() {
    super("AppDatabase");
    this.version(1).stores({
      notes: "id, title, updatedAt",
    });
  }
}

export const localDb = new AppDatabase();
```

---

## 3. Persistent LocalStorage with Zod Validation

```typescript
import { z } from "zod";

const SettingsSchema = z.object({
  theme: z.enum(["light", "dark", "system"]).default("dark"),
  notificationsEnabled: z.boolean().default(true),
  sidebarCollapsed: z.boolean().default(false),
});

export type UserSettings = z.infer<typeof SettingsSchema>;

const STORAGE_KEY = "app_user_settings";

export function loadSettings(): UserSettings {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return SettingsSchema.parse({});
    return SettingsSchema.parse(JSON.parse(raw));
  } catch (error) {
    console.warn("Invalid settings payload in localStorage, resetting to defaults", error);
    return SettingsSchema.parse({});
  }
}

export function saveSettings(settings: Partial<UserSettings>): UserSettings {
  const current = loadSettings();
  const updated = SettingsSchema.parse({ ...current, ...settings });
  localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
  return updated;
}
```
