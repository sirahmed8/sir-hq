# AHome: Fix profile picture save and save button state

## Problem (from owner screenshots)
- Profile picture not saving when clicking "احفظ" (Save)
- Save button doesn't change state when clicked (no loading/disabled state)
- Helper text "لسه ماتحفظش، اكتب اسمك واحفظ" shows even after entering name

## Required fixes
1. Fix avatar image save to device storage (العرض تتقص مربع تلقائيا وتتخزن على الجهاز بس)
2. Add proper button states: idle -> loading -> success/error
3. Fix validation: hide "لم تحفظ بعد" helper when name is entered and save succeeds
4. Ensure keyboard doesn't overlap the save button (bottom action area)
5. RTL layout: name input should align properly for Arabic text

## Files to check
- apps/mobile/app/(tabs)/profile-setup.tsx or similar
- components/ProfileAvatar.tsx
- hooks/useProfileSave.ts

## Acceptance
- Photo saves to device gallery/local storage
- Button shows loading spinner while saving
- Success toast appears, helper text disappears
- No keyboard overlap on save button
- Arabic text aligns correctly in input