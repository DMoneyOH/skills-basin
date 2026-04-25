# Hook Patterns
## When to Extract Hooks
| Pattern | Extract When |
|---------|-------------|
| **useLocalStorage** | Same storage logic needed |
| **useDebounce** | Multiple debounced values |
| **useFetch** | Repeated fetch patterns |
| **useForm** | Complex form state |
## Hook Rules
* Hooks at top level only
* Same order every render
* Custom hooks start with "use"
* Clean up effects on unmount