# Telegram bot architecture: one bot per product, multi-tenant (HQ decision, 2026-11-11)

The owner asked which is better: a bot per user, or one bot everyone links their own account to. Decision: **one bot per product (already created by BotFather), shared by every user of that product, each user links their own account to it once.** This is the standard, correct pattern (it is how every real product with a Telegram integration works: Linear, Notion, banking bots, etc.) and is the only one that scales past a handful of users; a bot-per-user approach would require creating and maintaining a new Telegram bot for every signup, which BotFather and Telegram's own rate limits do not support gracefully and which nobody else does.

How it works, and what every product must build:
1. One bot token per product (SIR AI already has `@SirAiAssistantBot`; other products get their own when they need Telegram).
2. A user links their own account from inside the product: the product shows a short-lived link code (already built for SIR AI); the user sends `/start <code>` to the bot (or opens a deep link `https://t.me/<bot>?start=<code>`), and the server maps that Telegram chat id to that user's account.
3. Every message the bot sends or receives after that is scoped to the linked user: incoming messages are looked up by Telegram chat id to find the user, outgoing messages are sent to that user's own stored chat id. Two different users linked to the same bot never see each other's messages.
4. The link flow shows a tappable "link" button/deep link, not only a code to copy (a code with no link is not native-app friendly); offer both: a one-tap `https://t.me/<bot>?start=<code>` link/button to open the bot directly, and the code as a fallback.
5. Unlinking, relinking, and multiple devices: a user can unlink and relink; the server always keeps the latest linked chat id per user.

Apply this pattern to every product that integrates Telegram.
