# Component Design Principles
## Component Types
| Type | Use | State |
|------|-----|-------|
| **Server** | Data fetching, static | None |
| **Client** | Interactivity | useState, effects |
| **Presentational** | UI display | Props only |
| **Container** | Logic/state | Heavy state |
## Design Rules
* One responsibility per component
* Props down, events up
* Composition over inheritance
* Prefer small, focused components