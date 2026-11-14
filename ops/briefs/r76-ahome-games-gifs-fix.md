# AHome: Fix GIF picker, search, and games (XO, invitations, notifications)

## Problem (from owner screenshots and text)
1. GIF picker: hardcoded GIFs, categories shown - should show trending GIFs only, no categories
2. Search box in GIF picker broken/poor
3. Game invitation not working - "sending request to play a game not working"
4. XO game: plays with self - "Any 1v1 game should not start until the other start"
5. Notification when someone starts game or leaves during game
6. Fix cropped buttons and texts in games cards
7. GIF thumbnails showing "THIS CONTENT IS NOT AVAILABLE" (broken CDN/API)

## Required fixes
### GIF Picker
- Remove hardcoded GIF categories (فرح، ضحك، حب، الكل)
- Fetch trending GIFs from Giphy/Tenor API
- Fix search: debounced, proper RTL placeholder, results render correctly
- Fix broken thumbnail loading (check API keys, CDN, fallback)

### Games (XO + others)
- Multiplayer invitation flow: send invite -> wait for accept -> start game
- Game should NOT start until both players joined
- Add real-time notifications: "X started a game", "X left the game"
- Fix layout: buttons/text not cropped in game cards
- Turn indicator clear: "الدور على: أحمد"
- Win detection: lock board immediately on win, show victory overlay

## Files to check
- apps/mobile/app/(tabs)/games.tsx
- components/GIFPicker.tsx
- components/GameCard.tsx
- components/XOGameBoard.tsx
- services/games/MultiplayerManager.ts
- services/gifs/GiphyService.ts
- hooks/useGameInvitation.ts
- hooks/useGIFSearch.ts

## Acceptance
- GIF picker: trending GIFs load, search works, no categories
- Game invite: sends push/notification, recipient sees accept/decline
- XO: waits for both players, locks on win, shows winner
- Notifications appear for game start/leave
- No cropped UI in game cards