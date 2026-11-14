# Complete 5-State UI Implementation Guide

Every interface component and screen must handle all 5 fundamental states to ensure high quality and zero user confusion.

---

## 1. Shimmer Skeleton Loading State

```tsx
export function ProjectListSkeleton() {
  return (
    <div className="space-y-4 w-full animate-pulse">
      {[1, 2, 3].map((i) => (
        <div key={i} className="p-4 rounded-2xl border border-border/40 bg-card/60 flex items-center justify-between">
          <div className="space-y-2">
            <div className="h-5 w-48 bg-muted rounded-md" />
            <div className="h-4 w-32 bg-muted/60 rounded-md" />
          </div>
          <div className="h-9 w-20 bg-muted rounded-lg" />
        </div>
      ))}
    </div>
  );
}
```

---

## 2. Empty State with Clear Actionable CTA

```tsx
import { FolderPlus } from "lucide-react";

interface EmptyStateProps {
  onAction: () => void;
}

export function EmptyProjectsState({ onAction }: EmptyStateProps) {
  return (
    <div className="p-12 text-center rounded-2xl border border-dashed border-border/80 bg-card/30 flex flex-col items-center justify-center">
      <div className="p-3 bg-primary/10 rounded-full text-primary mb-4">
        <FolderPlus className="w-8 h-8" />
      </div>
      <h3 className="text-lg font-semibold text-foreground mb-1">No Projects Found</h3>
      <p className="text-sm text-muted-foreground max-w-sm mb-6">
        You haven't created any projects yet. Get started by creating your first workspace project.
      </p>
      <button
        onClick={onAction}
        className="px-4 py-2 bg-primary text-primary-foreground font-medium rounded-lg text-sm transition-all duration-150 hover:brightness-110 active:scale-[0.98]"
      >
        Create Project
      </button>
    </div>
  );
}
```

---

## 3. Error State with Retry Mechanism

```tsx
import { AlertCircle, RefreshCw } from "lucide-react";

interface ErrorStateProps {
  message: string;
  onRetry: () => void;
}

export function ErrorStateCard({ message, onRetry }: ErrorStateProps) {
  return (
    <div className="p-6 rounded-2xl border border-destructive/30 bg-destructive/10 text-destructive flex items-center justify-between">
      <div className="flex items-center gap-3">
        <AlertCircle className="w-5 h-5 flex-shrink-0" />
        <div>
          <h4 className="font-semibold text-sm">Failed to Load Content</h4>
          <p className="text-xs opacity-90">{message}</p>
        </div>
      </div>
      <button
        onClick={onRetry}
        className="px-3 py-1.5 bg-destructive text-destructive-foreground rounded-lg text-xs font-medium flex items-center gap-1.5 hover:brightness-110"
      >
        <RefreshCw className="w-3.5 h-3.5" />
        Retry
      </button>
    </div>
  );
}
```
