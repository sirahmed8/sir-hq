# Report: r68-sir-ai-bot-answers - Privacy Classifier Fix for Telegram Bot

## Summary
Fixed the SIR AI Telegram bot's privacy classifier which was incorrectly blocking normal messages like "Hi" with "This looks like a private question and was not sent to any outside model."

## Root Cause
The original `classifyMessage()` in `packages/core/src/privacy.ts` had several issues:
1. All messages defaulted to P1 tier, but no providers had `noTraining: true` without explicit env flags (`*_NO_TRAINING=1`)
2. Arabic word boundaries (`\b`) don't work with Arabic characters in JavaScript regex
3. Pattern priority was wrong - greedy P1 patterns matched before P2/P3 patterns
4. Missing Arabic patterns for sensitive terms

## Solution Implemented

### 1. Rewrote `classifyMessage()` with Collect-All-Matches Strategy
- Scans all P3, P2, P1 patterns and collects every match
- Sorts by tier priority (P3=3, P2=2, P1=1, P0=0)
- Returns highest priority match
- This prevents greedy P1 patterns from blocking legitimate P2/P3 detections

### 2. Fixed Arabic Unicode Word Boundaries
- Replaced `\b` with Unicode-aware lookbehind/lookahead: `(?<![\p{L}\p{N}_])` / `(?![\p{L}\p{N}_])`
- Works with Arabic letters, possessive suffixes, and definite article "ال" prefix

### 3. Comprehensive Pattern Coverage

**P3 (Highly Sensitive - Local Only):**
- English: password, passwd, secret, api_key, token, private key, secret_key
- Arabic: كلمة المرور، كلمة السر، المرور، السر
- Telegram bot tokens, emails
- Credit cards with separators (4111 1111 1111 1111, 3782 822463 10005)
- Bare 15-16 digit numbers (credit card lengths)
- AHome/Habiba references (أهوم، حبيبة)

**P2 (Sensitive - noTraining + Explicit Consent):**
- Health: diabetes, cancer, doctor, hospital, medication... + Arabic (سكري، سرطان، طبيب، مستشفى، السكري with "ال" prefix)
- Financial: salary, bank, loan, income... + Arabic (راتب، بنك، قرض، الراتب with "ال" prefix and possessives)
- IDs: national ID, رقم قومي، بطاقة رقم، هوية with "ال" prefix
- Explicit private/confidential: "this is private", "هذه معلومات شخصية سرية" (feminine suffixes)

**P1 (Personal Non-Sensitive - noTraining Only):**
- English: my, our, I am/have/need/want/like/prefer/enjoy/hate/love/usually/wake up/sleep/eat/drink/work/study/exercise/run/walk
- Arabic: خطي، لي، أنا، عندي، أريد، أحب، أفضل، أكره، أستمتع، أستيقظ، أنام، آكل، أشرب، أعمل، أدرس، أتمرين، أجري، أمشي + possessives

**P0 (Public - Any Provider):**
- Greetings, general questions, factual queries, general chat

### 4. Credit Card vs National ID Disambiguation
- Credit cards: require separators (spaces/dashes) in standard groupings OR bare 15-16 digits
- National IDs: 14 digits caught by "national ID" / "رقم قومي" pattern → P2
- Test case "My national ID is 12345678901234" (14 digits) → P2 ✓
- Test case "1234567890123456" (16 digits bare) → P3 ✓

### 5. Files Modified
- `packages/core/src/privacy.ts`: Complete rewrite (~180 lines)
- `packages/core/test/privacy-classifier.test.ts`: 21 new tests (4 P0, 6 P1, 4 P2, 4 P3, 3 edge cases)
- `apps/bot/src/handlers.ts`: Removed unused `clearMemory` function
- `.sir/BOT_PLAN.md`: Planning document created per brief

## Verification Results
- **Privacy Classifier Tests**: 21/21 pass
- **Full Test Suite**: 324 tests pass across 32 test files
- **TypeCheck**: Clean across all 10 workspaces
- **ESLint**: Clean (4 pre-existing unused vars fixed)
- **Commit**: `8db88ac` pushed to main

## Remaining Work (Per Brief)
The privacy classifier is now fixed. Remaining bot improvements needed:
1. Voice message handling (Whisper via Groq, `.ogg` files)
2. Photo analysis (Gemini vision)
3. Conversation memory per user (last N turns)
4. Typing indicator and message editing (placeholder → final answer)
5. Commands: `/plan`, `/agents`, `/privacy`
6. Language detection (Egyptian Arabic default, English when user writes English)
7. E2E test against real bot with `[test]` labelled messages
8. Screenshots of chat at 320/390/768/1280

## Honest Gaps
- Real Whisper/Gemini vision integration not yet implemented
- Provider chain `noTraining` flags (`*_NO_TRAINING=1`) not yet set in Vercel env
- Live bot testing with owner's account not performed
- E2E screenshots not yet captured