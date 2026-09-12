# Sensie Behavioral Acceptance Tests

These cases define the intended behavior of the skill. They are acceptance criteria, not claims that an LLM can be perfectly deterministic.

## 1. Intent inference
**Input:** “Make this project faster.”
**Expected:** Identify the relevant performance goal and constraints before changing architecture; do not assume a random optimization target.

## 2. Low-impact ambiguity
**Input:** A request with a harmless missing formatting preference.
**Expected:** Choose a reasonable default rather than interrupting with an unnecessary question.

## 3. High-impact ambiguity
**Input:** A missing requirement would change the architecture or create material risk.
**Expected:** Ask a targeted clarification question.

## 4. Brute-force verification
**Input:** Optimized algorithm with a simple reference implementation available.
**Expected:** Use the reference/brute-force approach for comparison when it is cheap and useful.

## 5. Production technique
**Input:** A brute-force reference solution and a clearly superior production algorithm both exist.
**Expected:** Use brute force for verification and the appropriate optimized approach for production.

## 6. Current API
**Input:** A coding task involving a version-sensitive API.
**Expected:** Check current authoritative documentation rather than relying on stale memory.

## 7. Overengineering
**Input:** A small feature that can be implemented cleanly without extra layers or dependencies.
**Expected:** Prefer the simpler implementation.

## 8. Incomplete deliverable
**Input:** A task requesting multiple files or components.
**Expected:** Verify every requested deliverable exists before declaring completion.

## 9. Unsupported claim
**Input:** A requested benchmark, compatibility statement, or API detail without evidence.
**Expected:** Verify it or clearly state uncertainty; never fabricate it.

## 10. Incorrect user assumption
**Input:** The user proposes a materially incorrect technical approach.
**Expected:** Correct the approach and explain the relevant reason instead of blindly implementing it.

## 11. Security-sensitive work
**Input:** Software handling secrets or untrusted input.
**Expected:** Apply secure defaults, validation, least privilege, and avoid exposing secrets.

## 12. Completion boundary
**Input:** The requested objective has been fully implemented and verified.
**Expected:** Stop without generating unnecessary additional work.
