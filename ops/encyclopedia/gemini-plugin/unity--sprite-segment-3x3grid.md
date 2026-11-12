# sprite-segment-3x3grid

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\sprite-segment-3x3grid\SKILL.md`
- SKILL.md size: 4863 chars

## What it does

Segments a Sprite texture into a 3x3 grid and outputs a pattern of cells matching the center cell's color. Use when the user asks to analyze or document a sprite's structure or color distribution.

## Structure (headings inside SKILL.md)

- Sprite Color Grid Analysis
- Purpose
- Parameters
- Match Threshold
- Algorithm
- Output Legend
- Output Format
- Grid Position Mapping
- Examples
- Implementation Guidance
- Calculating Center's Majority Color
- Matching Non-Center Cells
- Color Tolerance
- Sprite Bounds
- References
- Use Cases
- Notes
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - The Y-axis is flipped from Unity's texture coordinates to produce top-to-bottom output

## Key rules (verbatim lines from SKILL.md)

1. 1. **Segment the Sprite**: Divide the Sprite's texture region into a 3x3 grid (9 cells total)
2. 2. **Identify Center Color**: Calculate the majority (most frequent) color in the center cell (position [1,1])
3. 3. **Compare Each Cell**: For each of the 8 surrounding cells, calculate what percentage of pixels match the center's majority color. If the percentage meets or exceeds the **match threshold**, the cell is a match (`.`); otherwise it is not (`X`)

## Files inside the skill

- `scripts/SpriteGridAnalysis.cs`
