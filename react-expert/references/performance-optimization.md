# Performance Principles
## When to Optimize
| Signal | Action |
|--------|--------|
| Slow renders | Profile first |
| Large lists | Virtualize |
| Expensive calc | useMemo |
| Stable callbacks | useCallback |
## Optimization Order
1. Check if actually slow
2. Profile with DevTools
3. Identify bottleneck
4. Apply targeted fix