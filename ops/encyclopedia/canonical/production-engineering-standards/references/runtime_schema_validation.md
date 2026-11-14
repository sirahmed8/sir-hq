# Runtime Schema Validation & Data Contracts

Enforce strict runtime data validation at every system boundary (API inputs, database results, IPC payloads, and localStorage).

---

## 1. TypeScript Validation with Zod

```typescript
import { z } from "zod";

export const CreateUserSchema = z.object({
  email: z.string().email("Invalid email format"),
  name: z.string().min(2, "Name must be at least 2 characters").max(50),
  role: z.enum(["admin", "member", "viewer"]).default("member"),
  age: z.number().int().positive().optional(),
});

export type CreateUserInput = z.infer<typeof CreateUserSchema>;

export function validateUserInput(data: unknown): { success: true; data: CreateUserInput } | { success: false; errors: string[] } {
  const result = CreateUserSchema.safeParse(data);
  if (!result.success) {
    return {
      success: false,
      errors: result.error.errors.map((e) => `${e.path.join(".")}: ${e.message}`),
    };
  }
  return { success: true, data: result.data };
}
```

---

## 2. Python Validation with Pydantic v2

```python
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional

class UserCreateDTO(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=50)
    role: str = Field(default="member")
    age: Optional[int] = Field(default=None, gt=0)

    @field_validator("name")
    def name_must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Name cannot be whitespace only")
        return v.strip()
```
