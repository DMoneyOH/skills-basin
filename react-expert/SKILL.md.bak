---
name: react-expert
description: "React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance pat..."
triggers:
  - # functional programming in react
  - # react modernization
  - # react patterns
  - # react state management
  - # react ui patterns
  - # vercel react best practices
  - ## 1. component design principles
  - ## 10. anti-patterns
  - ## 2. form validation with either
  - ## 2. hook patterns
  - ## 3. data fetching with taskeither
  - ## 3. state management selection
  - ## 4. react 19 patterns
  - ## 5. composition patterns
  - ## 6. dependency injection with context
merged_from:
  - react-patterns
  - react-ui-patterns
  - react-state-management
  - react-best-practices
  - fp-react
  - fp-ts-react
  - react-modernization
merged_at: 2026-04-18T17:20:54.594716
---

# react-expert

<!-- react-patterns -->
> Principles for building production-ready React applications.

---

## 1. Component Design Principles

### Component Types

| Type | Use | State |
|------|-----|-------|
| **Server** | Data fetching, static | None |
| **Client** | Interactivity | useState, effects |
| **Presentational** | UI display | Props only |
| **Container** | Logic/state | Heavy state |

### Design Rules

- One responsibility per component
- Props down, events up
- Composition over inheritance
- Prefer small, focused components

---

## 2. Hook Patterns

### When to Extract Hooks

| Pattern | Extract When |
|---------|-------------|
| **useLocalStorage** | Same storage logic needed |
| **useDebounce** | Multiple debounced values |
| **useFetch** | Repeated fetch patterns |
| **useForm** | Complex form state |

### Hook Rules

- Hooks at top level only
- Same order every render
- Custom hooks start with "use"
- Clean up effects on unmount

---

## 3. State Management Selection

| Complexity | Solution |
|------------|----------|
| Simple | useState, useReducer |
| Shared local | Context |
| Server state | React Query, SWR |
| Complex global | Zustand, Redux Toolkit |

### State Placement

| Scope | Where |
|-------|-------|
| Single component | useState |
| Parent-child | Lift state up |
| Subtree | Context |
| App-wide | Global store |

---

## 4. React 19 Patterns

### New Hooks

| Hook | Purpose |
|------|---------|
| **useActionState** | Form submission state |
| **useOptimistic** | Optimistic UI updates |
| **use** | Read resources in render |

### Compiler Benefits

- Automatic memoization
- Less manual useMemo/useCallback
- Focus on pure components

---

## 5. Composition Patterns

### Compound Components

- Parent provides context
- Children consume context
- Flexible slot-based composition
- Example: Tabs, Accordion, Dropdown

### Render Props vs Hooks

| Use Case | Prefer |
|----------|--------|
| Reusable logic | Custom hook |
| Render flexibility | Render props |
| Cross-cutting | Higher-order component |

---

## 6. Performance Principles

### When to Optimize

| Signal | Action |
|--------|--------|
| Slow renders | Profile first |
| Large lists | Virtualize |
| Expensive calc | useMemo |
| Stable callbacks | useCallback |

### Optimization Order

1. Check if actually slow
2. Profile with DevTools
3. Identify bottleneck
4. Apply targeted fix

---

## 7. Error Handling

### Error Boundary Usage

| Scope | Placement |
|-------|-----------|
| App-wide | Root level |
| Feature | Route/feature level |
| Component | Around risky component |

### Error Recovery

- Show fallback UI
- Log error
- Offer retry option
- Preserve user data

---

## 8. TypeScript Patterns

### Props Typing

| Pattern | Use |
|---------|-----|
| Interface | Component props |
| Type | Unions, complex |
| Generic | Reusable components |

### Common Types

| Need | Type |
|------|------|
| Children | ReactNode |
| Event handler | MouseEventHandler |
| Ref | RefObject<Element> |

---

## 9. Testing Principles

| Level | Focus |
|-------|-------|
| Unit | Pure functions, hooks |
| Integration | Component behavior |
| E2E | User flows |

### Test Priorities

- User-visible behavior
- Edge cases
- Error states
- Accessibility

---

## 10. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| Prop drilling deep | Use context |
| Giant components | Split smaller |
| useEffect for everything | Server components |
| Premature optimization | Profile first |
| Index as key | Stable unique ID |

---

> **Remember:** React is about composition. Build small, combine thoughtfully.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: react-expert on 2026-04-18 -->
<!-- Use `react-expert` instead. -->

---

<!-- react-ui-patterns -->
## Core Principles

1. **Never show stale UI** - Loading spinners only when actually loading
2. **Always surface errors** - Users must know when something fails
3. **Optimistic updates** - Make the UI feel instant
4. **Progressive disclosure** - Show content as it becomes available
5. **Graceful degradation** - Partial data is better than no data

## Loading State Patterns

### The Golden Rule

**Show loading indicator ONLY when there's no data to display.**

```typescript
// CORRECT - Only show loading when no data exists
const { data, loading, error } = useGetItemsQuery();

if (error) return <ErrorState error={error} onRetry={refetch} />;
if (loading && !data) return <LoadingState />;
if (!data?.items.length) return <EmptyState />;

return <ItemList items={data.items} />;
```

```typescript
// WRONG - Shows spinner even when we have cached data
if (loading) return <LoadingState />; // Flashes on refetch!
```

### Loading State Decision Tree

```
Is there an error?
  → Yes: Show error state with retry option
  → No: Continue

Is it loading AND we have no data?
  → Yes: Show loading indicator (spinner/skeleton)
  → No: Continue

Do we have data?
  → Yes, with items: Show the data
  → Yes, but empty: Show empty state
  → No: Show loading (fallback)
```

### Skeleton vs Spinner

| Use Skeleton When | Use Spinner When |
|-------------------|------------------|
| Known content shape | Unknown content shape |
| List/card layouts | Modal actions |
| Initial page load | Button submissions |
| Content placeholders | Inline operations |

## Error Handling Patterns

### The Error Handling Hierarchy

```
1. Inline error (field-level) → Form validation errors
2. Toast notification → Recoverable errors, user can retry
3. Error banner → Page-level errors, data still partially usable
4. Full error screen → Unrecoverable, needs user action
```

### Always Show Errors

**CRITICAL: Never swallow errors silently.**

```typescript
// CORRECT - Error always surfaced to user
const [createItem, { loading }] = useCreateItemMutation({
  onCompleted: () => {
    toast.success({ title: 'Item created' });
  },
  onError: (error) => {
    console.error('createItem failed:', error);
    toast.error({ title: 'Failed to create item' });
  },
});

// WRONG - Error silently caught, user has no idea
const [createItem] = useCreateItemMutation({
  onError: (error) => {
    console.error(error); // User sees nothing!
  },
});
```

### Error State Component Pattern

```typescript
interface ErrorStateProps {
  error: Error;
  onRetry?: () => void;
  title?: string;
}

const ErrorState = ({ error, onRetry, title }: ErrorStateProps) => (
  <div className="error-state">
    <Icon name="exclamation-circle" />
    <h3>{title ?? 'Something went wrong'}</h3>
    <p>{error.message}</p>
    {onRetry && (
      <Button onClick={onRetry}>Try Again</Button>
    )}
  </div>
);
```

## Button State Patterns

### Button Loading State

```tsx
<Button
  onClick={handleSubmit}
  isLoading={isSubmitting}
  disabled={!isValid || isSubmitting}
>
  Submit
</Button>
```

### Disable During Operations

**CRITICAL: Always disable triggers during async operations.**

```tsx
// CORRECT - Button disabled while loading
<Button
  disabled={isSubmitting}
  isLoading={isSubmitting}
  onClick={handleSubmit}
>
  Submit
</Button>

// WRONG - User can tap multiple times
<Button onClick={handleSubmit}>
  {isSubmitting ? 'Submitting...' : 'Submit'}
</Button>
```

## Empty States

### Empty State Requirements

Every list/collection MUST have an empty state:

```tsx
// WRONG - No empty state
return <FlatList data={items} />;

// CORRECT - Explicit empty state
return (
  <FlatList
    data={items}
    ListEmptyComponent={<EmptyState />}
  />
);
```

### Contextual Empty States

```tsx
// Search with no results
<EmptyState
  icon="search"
  title="No results found"
  description="Try different search terms"
/>

// List with no items yet
<EmptyState
  icon="plus-circle"
  title="No items yet"
  description="Create your first item"
  action={{ label: 'Create Item', onClick: handleCreate }}
/>
```

## Form Submission Pattern

```tsx
const MyForm = () => {
  const [submit, { loading }] = useSubmitMutation({
    onCompleted: handleSuccess,
    onError: handleError,
  });

  const handleSubmit = async () => {
    if (!isValid) {
      toast.error({ title: 'Please fix errors' });
      return;
    }
    await submit({ variables: { input: values } });
  };

  return (
    <form>
      <Input
        value={values.name}
        onChange={handleChange('name')}
        error={touched.name ? errors.name : undefined}
      />
      <Button
        type="submit"
        onClick={handleSubmit}
        disabled={!isValid || loading}
        isLoading={loading}
      >
        Submit
      </Button>
    </form>
  );
};
```

## Anti-Patterns

### Loading States

```typescript
// WRONG - Spinner when data exists (causes flash)
if (loading) return <Spinner />;

// CORRECT - Only show loading without data
if (loading && !data) return <Spinner />;
```

### Error Handling

```typescript
// WRONG - Error swallowed
try {
  await mutation();
} catch (e) {
  console.log(e); // User has no idea!
}

// CORRECT - Error surfaced
onError: (error) => {
  console.error('operation failed:', error);
  toast.error({ title: 'Operation failed' });
}
```

### Button States

```typescript
// WRONG - Button not disabled during submission
<Button onClick={submit}>Submit</Button>

// CORRECT - Disabled and shows loading
<Button onClick={submit} disabled={loading} isLoading={loading}>
  Submit
</Button>
```

## Checklist

Before completing any UI component:

**UI States:**
- [ ] Error state handled and shown to user
- [ ] Loading state shown only when no data exists
- [ ] Empty state provided for collections
- [ ] Buttons disabled during async operations
- [ ] Buttons show loading indicator when appropriate

**Data & Mutations:**
- [ ] Mutations have onError handler
- [ ] All user actions have feedback (toast/visual)

## Integration with Other Skills

- **graphql-schema**: Use mutation patterns with proper error handling
- **testing-patterns**: Test all UI states (loading, error, empty, success)
- **formik-patterns**: Apply form submission patterns

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: react-expert on 2026-04-18 -->
<!-- Use `react-expert` instead. -->

---

<!-- react-state-management -->
Comprehensive guide to modern React state management patterns, from local component state to global stores and server state synchronization.

## Do not use this skill when

- The task is unrelated to react state management
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Use this skill when

- Setting up global state management in a React app
- Choosing between Redux Toolkit, Zustand, or Jotai
- Managing server state with React Query or SWR
- Implementing optimistic updates
- Debugging state-related issues
- Migrating from legacy Redux to modern patterns

## Core Concepts

### 1. State Categories

| Type | Description | Solutions |
|------|-------------|-----------|
| **Local State** | Component-specific, UI state | useState, useReducer |
| **Global State** | Shared across components | Redux Toolkit, Zustand, Jotai |
| **Server State** | Remote data, caching | React Query, SWR, RTK Query |
| **URL State** | Route parameters, search | React Router, nuqs |
| **Form State** | Input values, validation | React Hook Form, Formik |

### 2. Selection Criteria

```
Small app, simple state → Zustand or Jotai
Large app, complex state → Redux Toolkit
Heavy server interaction → React Query + light client state
Atomic/granular updates → Jotai
```

## Quick Start

### Zustand (Simplest)

```typescript
// store/useStore.ts
import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'

interface AppState {
  user: User | null
  theme: 'light' | 'dark'
  setUser: (user: User | null) => void
  toggleTheme: () => void
}

export const useStore = create<AppState>()(
  devtools(
    persist(
      (set) => ({
        user: null,
        theme: 'light',
        setUser: (user) => set({ user }),
        toggleTheme: () => set((state) => ({
          theme: state.theme === 'light' ? 'dark' : 'light'
        })),
      }),
      { name: 'app-storage' }
    )
  )
)

// Usage in component
function Header() {
  const { user, theme, toggleTheme } = useStore()
  return (
    <header className={theme}>
      {user?.name}
      <button onClick={toggleTheme}>Toggle Theme</button>
    </header>
  )
}
```

## Patterns

### Pattern 1: Redux Toolkit with TypeScript

```typescript
// store/index.ts
import { configureStore } from '@reduxjs/toolkit'
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux'
import userReducer from './slices/userSlice'
import cartReducer from './slices/cartSlice'

export const store = configureStore({
  reducer: {
    user: userReducer,
    cart: cartReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST'],
      },
    }),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch

// Typed hooks
export const useAppDispatch: () => AppDispatch = useDispatch
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector
```

```typescript
// store/slices/userSlice.ts
import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit'

interface User {
  id: string
  email: string
  name: string
}

interface UserState {
  current: User | null
  status: 'idle' | 'loading' | 'succeeded' | 'failed'
  error: string | null
}

const initialState: UserState = {
  current: null,
  status: 'idle',
  error: null,
}

export const fetchUser = createAsyncThunk(
  'user/fetchUser',
  async (userId: string, { rejectWithValue }) => {
    try {
      const response = await fetch(`/api/users/${userId}`)
      if (!response.ok) throw new Error('Failed to fetch user')
      return await response.json()
    } catch (error) {
      return rejectWithValue((error as Error).message)
    }
  }
)

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    setUser: (state, action: PayloadAction<User>) => {
      state.current = action.payload
      state.status = 'succeeded'
    },
    clearUser: (state) => {
      state.current = null
      state.status = 'idle'
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.status = 'loading'
        state.error = null
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.status = 'succeeded'
        state.current = action.payload
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.status = 'failed'
        state.error = action.payload as string
      })
  },
})

export const { setUser, clearUser } = userSlice.actions
export default userSlice.reducer
```

### Pattern 2: Zustand with Slices (Scalable)

```typescript
// store/slices/createUserSlice.ts
import { StateCreator } from 'zustand'

export interface UserSlice {
  user: User | null
  isAuthenticated: boolean
  login: (credentials: Credentials) => Promise<void>
  logout: () => void
}

export const createUserSlice: StateCreator<
  UserSlice & CartSlice, // Combined store type
  [],
  [],
  UserSlice
> = (set, get) => ({
  user: null,
  isAuthenticated: false,
  login: async (credentials) => {
    const user = await authApi.login(credentials)
    set({ user, isAuthenticated: true })
  },
  logout: () => {
    set({ user: null, isAuthenticated: false })
    // Can access other slices
    // get().clearCart()
  },
})

// store/index.ts
import { create } from 'zustand'
import { createUserSlice, UserSlice } from './slices/createUserSlice'
import { createCartSlice, CartSlice } from './slices/createCartSlice'

type StoreState = UserSlice & CartSlice

export const useStore = create<StoreState>()((...args) => ({
  ...createUserSlice(...args),
  ...createCartSlice(...args),
}))

// Selective subscriptions (prevents unnecessary re-renders)
export const useUser = () => useStore((state) => state.user)
export const useCart = () => useStore((state) => state.cart)
```

### Pattern 3: Jotai for Atomic State

```typescript
// atoms/userAtoms.ts
import { atom } from 'jotai'
import { atomWithStorage } from 'jotai/utils'

// Basic atom
export const userAtom = atom<User | null>(null)

// Derived atom (computed)
export const isAuthenticatedAtom = atom((get) => get(userAtom) !== null)

// Atom with localStorage persistence
export const themeAtom = atomWithStorage<'light' | 'dark'>('theme', 'light')

// Async atom
export const userProfileAtom = atom(async (get) => {
  const user = get(userAtom)
  if (!user) return null
  const response = await fetch(`/api/users/${user.id}/profile`)
  return response.json()
})

// Write-only atom (action)
export const logoutAtom = atom(null, (get, set) => {
  set(userAtom, null)
  set(cartAtom, [])
  localStorage.removeItem('token')
})

// Usage
function Profile() {
  const [user] = useAtom(userAtom)
  const [, logout] = useAtom(logoutAtom)
  const [profile] = useAtom(userProfileAtom) // Suspense-enabled

  return (
    <Suspense fallback={<Skeleton />}>
      <ProfileContent profile={profile} onLogout={logout} />
    </Suspense>
  )
}
```

### Pattern 4: React Query for Server State

```typescript
// hooks/useUsers.ts
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'

// Query keys factory
export const userKeys = {
  all: ['users'] as const,
  lists: () => [...userKeys.all, 'list'] as const,
  list: (filters: UserFilters) => [...userKeys.lists(), filters] as const,
  details: () => [...userKeys.all, 'detail'] as const,
  detail: (id: string) => [...userKeys.details(), id] as const,
}

// Fetch hook
export function useUsers(filters: UserFilters) {
  return useQuery({
    queryKey: userKeys.list(filters),
    queryFn: () => fetchUsers(filters),
    staleTime: 5 * 60 * 1000, // 5 minutes
    gcTime: 30 * 60 * 1000, // 30 minutes (formerly cacheTime)
  })
}

// Single user hook
export function useUser(id: string) {
  return useQuery({
    queryKey: userKeys.detail(id),
    queryFn: () => fetchUser(id),
    enabled: !!id, // Don't fetch if no id
  })
}

// Mutation with optimistic update
export function useUpdateUser() {
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: updateUser,
    onMutate: async (newUser) => {
      // Cancel outgoing refetches
      await queryClient.cancelQueries({ queryKey: userKeys.detail(newUser.id) })

      // Snapshot previous value
      const previousUser = queryClient.getQueryData(userKeys.detail(newUser.id))

      // Optimistically update
      queryClient.setQueryData(userKeys.detail(newUser.id), newUser)

      return { previousUser }
    },
    onError: (err, newUser, context) => {
      // Rollback on error
      queryClient.setQueryData(
        userKeys.detail(newUser.id),
        context?.previousUser
      )
    },
    onSettled: (data, error, variables) => {
      // Refetch after mutation
      queryClient.invalidateQueries({ queryKey: userKeys.detail(variables.id) })
    },
  })
}
```

### Pattern 5: Combining Client + Server State

```typescript
// Zustand for client state
const useUIStore = create<UIState>((set) => ({
  sidebarOpen: true,
  modal: null,
  toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),
  openModal: (modal) => set({ modal }),
  closeModal: () => set({ modal: null }),
}))

// React Query for server state
function Dashboard() {
  const { sidebarOpen, toggleSidebar } = useUIStore()
  const { data: users, isLoading } = useUsers({ active: true })
  const { data: stats } = useStats()

  if (isLoading) return <DashboardSkeleton />

  return (
    <div className={sidebarOpen ? 'with-sidebar' : ''}>
      <Sidebar open={sidebarOpen} onToggle={toggleSidebar} />
      <main>
        <StatsCards stats={stats} />
        <UserTable users={users} />
      </main>
    </div>
  )
}
```

## Best Practices

### Do's
- **Colocate state** - Keep state as close to where it's used as possible
- **Use selectors** - Prevent unnecessary re-renders with selective subscriptions
- **Normalize data** - Flatten nested structures for easier updates
- **Type everything** - Full TypeScript coverage prevents runtime errors
- **Separate concerns** - Server state (React Query) vs client state (Zustand)

### Don'ts
- **Don't over-globalize** - Not everything needs to be in global state
- **Don't duplicate server state** - Let React Query manage it
- **Don't mutate directly** - Always use immutable updates
- **Don't store derived data** - Compute it instead
- **Don't mix paradigms** - Pick one primary solution per category

## Migration Guides

### From Legacy Redux to RTK

```typescript
// Before (legacy Redux)
const ADD_TODO = 'ADD_TODO'
const addTodo = (text) => ({ type: ADD_TODO, payload: text })
function todosReducer(state = [], action) {
  switch (action.type) {
    case ADD_TODO:
      return [...state, { text: action.payload, completed: false }]
    default:
      return state
  }
}

// After (Redux Toolkit)
const todosSlice = createSlice({
  name: 'todos',
  initialState: [],
  reducers: {
    addTodo: (state, action: PayloadAction<string>) => {
      // Immer allows "mutations"
      state.push({ text: action.payload, completed: false })
    },
  },
})
```

## Resources

- [Redux Toolkit Documentation](https://redux-toolkit.js.org/)
- [Zustand GitHub](https://github.com/pmndrs/zustand)
- [Jotai Documentation](https://jotai.org/)
- [TanStack Query](https://tanstack.com/query)


<!-- MERGED INTO: react-expert on 2026-04-18 -->
<!-- Use `react-expert` instead. -->

---

<!-- react-best-practices -->
Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Contains 45 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

## When to Apply

Reference these guidelines when:
- Writing new React components or Next.js pages
- Implementing data fetching (client or server-side)
- Reviewing code for performance issues
- Refactoring existing React/Next.js code
- Optimizing bundle size or load times

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Eliminating Waterfalls | CRITICAL | `async-` |
| 2 | Bundle Size Optimization | CRITICAL | `bundle-` |
| 3 | Server-Side Performance | HIGH | `server-` |
| 4 | Client-Side Data Fetching | MEDIUM-HIGH | `client-` |
| 5 | Re-render Optimization | MEDIUM | `rerender-` |
| 6 | Rendering Performance | MEDIUM | `rendering-` |
| 7 | JavaScript Performance | LOW-MEDIUM | `js-` |
| 8 | Advanced Patterns | LOW | `advanced-` |

## Quick Reference

### 1. Eliminating Waterfalls (CRITICAL)

- `async-defer-await` - Move await into branches where actually used
- `async-parallel` - Use Promise.all() for independent operations
- `async-dependencies` - Use better-all for partial dependencies
- `async-api-routes` - Start promises early, await late in API routes
- `async-suspense-boundaries` - Use Suspense to stream content

### 2. Bundle Size Optimization (CRITICAL)

- `bundle-barrel-imports` - Import directly, avoid barrel files
- `bundle-dynamic-imports` - Use next/dynamic for heavy components
- `bundle-defer-third-party` - Load analytics/logging after hydration
- `bundle-conditional` - Load modules only when feature is activated
- `bundle-preload` - Preload on hover/focus for perceived speed

### 3. Server-Side Performance (HIGH)

- `server-cache-react` - Use React.cache() for per-request deduplication
- `server-cache-lru` - Use LRU cache for cross-request caching
- `server-serialization` - Minimize data passed to client components
- `server-parallel-fetching` - Restructure components to parallelize fetches
- `server-after-nonblocking` - Use after() for non-blocking operations

### 4. Client-Side Data Fetching (MEDIUM-HIGH)

- `client-swr-dedup` - Use SWR for automatic request deduplication
- `client-event-listeners` - Deduplicate global event listeners

### 5. Re-render Optimization (MEDIUM)

- `rerender-defer-reads` - Don't subscribe to state only used in callbacks
- `rerender-memo` - Extract expensive work into memoized components
- `rerender-dependencies` - Use primitive dependencies in effects
- `rerender-derived-state` - Subscribe to derived booleans, not raw values
- `rerender-functional-setstate` - Use functional setState for stable callbacks
- `rerender-lazy-state-init` - Pass function to useState for expensive values
- `rerender-transitions` - Use startTransition for non-urgent updates

### 6. Rendering Performance (MEDIUM)

- `rendering-animate-svg-wrapper` - Animate div wrapper, not SVG element
- `rendering-content-visibility` - Use content-visibility for long lists
- `rendering-hoist-jsx` - Extract static JSX outside components
- `rendering-svg-precision` - Reduce SVG coordinate precision
- `rendering-hydration-no-flicker` - Use inline script for client-only data
- `rendering-activity` - Use Activity component for show/hide
- `rendering-conditional-render` - Use ternary, not && for conditionals

### 7. JavaScript Performance (LOW-MEDIUM)

- `js-batch-dom-css` - Group CSS changes via classes or cssText
- `js-index-maps` - Build Map for repeated lookups
- `js-cache-property-access` - Cache object properties in loops
- `js-cache-function-results` - Cache function results in module-level Map
- `js-cache-storage` - Cache localStorage/sessionStorage reads
- `js-combine-iterations` - Combine multiple filter/map into one loop
- `js-length-check-first` - Check array length before expensive comparison
- `js-early-exit` - Return early from functions
- `js-hoist-regexp` - Hoist RegExp creation outside loops
- `js-min-max-loop` - Use loop for min/max instead of sort
- `js-set-map-lookups` - Use Set/Map for O(1) lookups
- `js-tosorted-immutable` - Use toSorted() for immutability

### 8. Advanced Patterns (LOW)

- `advanced-event-handler-refs` - Store event handlers in refs
- `advanced-use-latest` - useLatest for stable callback refs

## How to Use

Read individual rule files for detailed explanations and code examples:

```
rules/async-parallel.md
rules/bundle-barrel-imports.md
rules/_sections.md
```

Each rule file contains:
- Brief explanation of why it matters
- Incorrect code example with explanation
- Correct code example with explanation
- Additional context and references

## Full Compiled Document

For the complete guide with all rules expanded: `AGENTS.md`

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: react-expert on 2026-04-18 -->
<!-- Use `react-expert` instead. -->

---

<!-- fp-react -->
Practical patterns for React apps. No jargon, just code that works.

---

## Quick Reference

| Pattern | Use When |
|---------|----------|
| `Option` | Value might be missing (user not loaded yet) |
| `Either` | Operation might fail (form validation) |
| `TaskEither` | Async operation might fail (API calls) |
| `RemoteData` | Need to show loading/error/success states |
| `pipe` | Chaining multiple transformations |

---

## 1. State with Option (Maybe It's There, Maybe Not)

Use `Option` instead of `null | undefined` for clearer intent.

### Basic Pattern

```typescript
import { useState } from 'react'
import * as O from 'fp-ts/Option'
import { pipe } from 'fp-ts/function'

interface User {
  id: string
  name: string
  email: string
}

function UserProfile() {
  // Option says "this might not exist yet"
  const [user, setUser] = useState<O.Option<User>>(O.none)

  const handleLogin = (userData: User) => {
    setUser(O.some(userData))
  }

  const handleLogout = () => {
    setUser(O.none)
  }

  return pipe(
    user,
    O.match(
      // When there's no user
      () => <button onClick={() => handleLogin({ id: '1', name: 'Alice', email: 'alice@example.com' })}>
        Log In
      </button>,
      // When there's a user
      (u) => (
        <div>
          <p>Welcome, {u.name}!</p>
          <button onClick={handleLogout}>Log Out</button>
        </div>
      )
    )
  )
}
```

### Chaining Optional Values

```typescript
import * as O from 'fp-ts/Option'
import { pipe } from 'fp-ts/function'

interface Profile {
  user: O.Option<{
    name: string
    settings: O.Option<{
      theme: string
    }>
  }>
}

function getTheme(profile: Profile): string {
  return pipe(
    profile.user,
    O.flatMap(u => u.settings),
    O.map(s => s.theme),
    O.getOrElse(() => 'light') // default
  )
}
```

---

## 2. Form Validation with Either

Either is perfect for validation: `Left` = errors, `Right` = valid data.

### Simple Form Validation

```typescript
import * as E from 'fp-ts/Either'
import * as A from 'fp-ts/Array'
import { pipe } from 'fp-ts/function'

// Validation functions return Either<ErrorMessage, ValidValue>
const validateEmail = (email: string): E.Either<string, string> =>
  email.includes('@')
    ? E.right(email)
    : E.left('Invalid email address')

const validatePassword = (password: string): E.Either<string, string> =>
  password.length >= 8
    ? E.right(password)
    : E.left('Password must be at least 8 characters')

const validateName = (name: string): E.Either<string, string> =>
  name.trim().length > 0
    ? E.right(name.trim())
    : E.left('Name is required')
```

### Collecting All Errors (Not Just First One)

```typescript
import * as E from 'fp-ts/Either'
import { sequenceS } from 'fp-ts/Apply'
import { getSemigroup } from 'fp-ts/NonEmptyArray'
import { pipe } from 'fp-ts/function'

// This collects ALL errors, not just the first one
const validateAll = sequenceS(E.getApplicativeValidation(getSemigroup<string>()))

interface SignupForm {
  name: string
  email: string
  password: string
}

interface ValidatedForm {
  name: string
  email: string
  password: string
}

function validateForm(form: SignupForm): E.Either<string[], ValidatedForm> {
  return pipe(
    validateAll({
      name: pipe(validateName(form.name), E.mapLeft(e => [e])),
      email: pipe(validateEmail(form.email), E.mapLeft(e => [e])),
      password: pipe(validatePassword(form.password), E.mapLeft(e => [e])),
    })
  )
}

// Usage in component
function SignupForm() {
  const [form, setForm] = useState({ name: '', email: '', password: '' })
  const [errors, setErrors] = useState<string[]>([])

  const handleSubmit = () => {
    pipe(
      validateForm(form),
      E.match(
        (errs) => setErrors(errs),     // Show all errors
        (valid) => {
          setErrors([])
          submitToServer(valid)         // Submit valid data
        }
      )
    )
  }

  return (
    <form onSubmit={e => { e.preventDefault(); handleSubmit() }}>
      <input
        value={form.name}
        onChange={e => setForm(f => ({ ...f, name: e.target.value }))}
        placeholder="Name"
      />
      <input
        value={form.email}
        onChange={e => setForm(f => ({ ...f, email: e.target.value }))}
        placeholder="Email"
      />
      <input
        type="password"
        value={form.password}
        onChange={e => setForm(f => ({ ...f, password: e.target.value }))}
        placeholder="Password"
      />

      {errors.length > 0 && (
        <ul style={{ color: 'red' }}>
          {errors.map((err, i) => <li key={i}>{err}</li>)}
        </ul>
      )}

      <button type="submit">Sign Up</button>
    </form>
  )
}
```

### Field-Level Errors (Better UX)

```typescript
type FieldErrors = Partial<Record<keyof SignupForm, string>>

function validateFormWithFieldErrors(form: SignupForm): E.Either<FieldErrors, ValidatedForm> {
  const errors: FieldErrors = {}

  pipe(validateName(form.name), E.mapLeft(e => { errors.name = e }))
  pipe(validateEmail(form.email), E.mapLeft(e => { errors.email = e }))
  pipe(validatePassword(form.password), E.mapLeft(e => { errors.password = e }))

  return Object.keys(errors).length > 0
    ? E.left(errors)
    : E.right({ name: form.name.trim(), email: form.email, password: form.password })
}

// In component
{errors.email && <span className="error">{errors.email}</span>}
```

---

## 3. Data Fetching with TaskEither

TaskEither = async operation that might fail. Perfect for API calls.

### Basic Fetch Hook

```typescript
import { useState, useEffect } from 'react'
import * as TE from 'fp-ts/TaskEither'
import * as E from 'fp-ts/Either'
import { pipe } from 'fp-ts/function'

// Wrap fetch in TaskEither
const fetchJson = <T>(url: string): TE.TaskEither<Error, T> =>
  TE.tryCatch(
    async () => {
      const res = await fetch(url)
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      return res.json()
    },
    (err) => err instanceof Error ? err : new Error(String(err))
  )

// Custom hook
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null)
  const [error, setError] = useState<Error | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    setError(null)

    pipe(
      fetchJson<T>(url),
      TE.match(
        (err) => {
          setError(err)
          setLoading(false)
        },
        (result) => {
          setData(result)
          setLoading(false)
        }
      )
    )()
  }, [url])

  return { data, error, loading }
}

// Usage
function UserList() {
  const { data, error, loading } = useFetch<User[]>('/api/users')

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>
  return (
    <ul>
      {data?.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  )
}
```

### Chaining API Calls

```typescript
// Fetch user, then fetch their posts
const fetchUserWithPosts = (userId: string) => pipe(
  fetchJson<User>(`/api/users/${userId}`),
  TE.flatMap(user => pipe(
    fetchJson<Post[]>(`/api/users/${userId}/posts`),
    TE.map(posts => ({ ...user, posts }))
  ))
)
```

### Parallel API Calls

```typescript
import { sequenceT } from 'fp-ts/Apply'

// Fetch multiple things at once
const fetchDashboardData = () => pipe(
  sequenceT(TE.ApplyPar)(
    fetchJson<User>('/api/user'),
    fetchJson<Stats>('/api/stats'),
    fetchJson<Notifications[]>('/api/notifications')
  ),
  TE.map(([user, stats, notifications]) => ({
    user,
    stats,
    notifications
  }))
)
```

---

## 4. RemoteData Pattern (The Right Way to Handle Async State)

Stop using `{ data, loading, error }` booleans. Use a proper state machine.

### The Pattern

```typescript
// RemoteData has exactly 4 states - no impossible combinations
type RemoteData<E, A> =
  | { _tag: 'NotAsked' }                    // Haven't started yet
  | { _tag: 'Loading' }                     // In progress
  | { _tag: 'Failure'; error: E }           // Failed
  | { _tag: 'Success'; data: A }            // Got it!

// Constructors
const notAsked = <E, A>(): RemoteData<E, A> => ({ _tag: 'NotAsked' })
const loading = <E, A>(): RemoteData<E, A> => ({ _tag: 'Loading' })
const failure = <E, A>(error: E): RemoteData<E, A> => ({ _tag: 'Failure', error })
const success = <E, A>(data: A): RemoteData<E, A> => ({ _tag: 'Success', data })

// Pattern match all states
function fold<E, A, R>(
  rd: RemoteData<E, A>,
  onNotAsked: () => R,
  onLoading: () => R,
  onFailure: (e: E) => R,
  onSuccess: (a: A) => R
): R {
  switch (rd._tag) {
    case 'NotAsked': return onNotAsked()
    case 'Loading': return onLoading()
    case 'Failure': return onFailure(rd.error)
    case 'Success': return onSuccess(rd.data)
  }
}
```

### Hook with RemoteData

```typescript
function useRemoteData<T>(fetchFn: () => Promise<T>) {
  const [state, setState] = useState<RemoteData<Error, T>>(notAsked())

  const execute = async () => {
    setState(loading())
    try {
      const data = await fetchFn()
      setState(success(data))
    } catch (err) {
      setState(failure(err instanceof Error ? err : new Error(String(err))))
    }
  }

  return { state, execute }
}

// Usage
function UserProfile({ userId }: { userId: string }) {
  const { state, execute } = useRemoteData(() =>
    fetch(`/api/users/${userId}`).then(r => r.json())
  )

  useEffect(() => { execute() }, [userId])

  return fold(
    state,
    () => <button onClick={execute}>Load User</button>,
    () => <Spinner />,
    (err) => <ErrorMessage message={err.message} onRetry={execute} />,
    (user) => <UserCard user={user} />
  )
}
```

### Why RemoteData Beats Booleans

```typescript
// ❌ BAD: Impossible states are possible
interface BadState {
  data: User | null
  loading: boolean
  error: Error | null
}
// Can have: { data: user, loading: true, error: someError } - what does that mean?!

// ✅ GOOD: Only valid states exist
type GoodState = RemoteData<Error, User>
// Can only be: NotAsked | Loading | Failure | Success
```

---

## 5. Referential Stability (Preventing Re-renders)

fp-ts values like `O.some(1)` create new objects each render. React sees them as "changed".

### The Problem

```typescript
// ❌ BAD: Creates new Option every render
function BadComponent() {
  const [value, setValue] = useState(O.some(1))

  useEffect(() => {
    // This runs EVERY render because O.some(1) !== O.some(1)
    console.log('value changed')
  }, [value])
}
```

### Solution 1: useMemo

```typescript
// ✅ GOOD: Memoize Option creation
function GoodComponent() {
  const [rawValue, setRawValue] = useState<number | null>(1)

  const value = useMemo(
    () => O.fromNullable(rawValue),
    [rawValue]  // Only recreate when rawValue changes
  )

  useEffect(() => {
    // Now this only runs when rawValue actually changes
    console.log('value changed')
  }, [rawValue])  // Depend on raw value, not Option
}
```

### Solution 2: fp-ts-react-stable-hooks

```bash
npm install fp-ts-react-stable-hooks
```

```typescript
import { useStableO, useStableEffect } from 'fp-ts-react-stable-hooks'
import * as O from 'fp-ts/Option'
import * as Eq from 'fp-ts/Eq'

function StableComponent() {
  // Uses fp-ts equality instead of reference equality
  const [value, setValue] = useStableO(O.some(1))

  // Effect that understands Option equality
  useStableEffect(
    () => { console.log('value changed') },
    [value],
    Eq.tuple(O.getEq(Eq.eqNumber))  // Custom equality
  )
}
```

---

## 6. Dependency Injection with Context

Use ReaderTaskEither for testable components with injected dependencies.

### Setup Dependencies

```typescript
import * as RTE from 'fp-ts/ReaderTaskEither'
import { pipe } from 'fp-ts/function'
import { createContext, useContext, ReactNode } from 'react'

// Define what services your app needs
interface AppDependencies {
  api: {
    getUser: (id: string) => Promise<User>
    updateUser: (id: string, data: Partial<User>) => Promise<User>
  }
  analytics: {
    track: (event: string, data?: object) => void
  }
}

// Create context
const DepsContext = createContext<AppDependencies | null>(null)

// Provider
function AppProvider({ deps, children }: { deps: AppDependencies; children: ReactNode }) {
  return <DepsContext.Provider value={deps}>{children}</DepsContext.Provider>
}

// Hook to use dependencies
function useDeps(): AppDependencies {
  const deps = useContext(DepsContext)
  if (!deps) throw new Error('Missing AppProvider')
  return deps
}
```

### Use in Components

```typescript
function UserProfile({ userId }: { userId: string }) {
  const { api, analytics } = useDeps()
  const [user, setUser] = useState<RemoteData<Error, User>>(notAsked())

  useEffect(() => {
    setUser(loading())
    api.getUser(userId)
      .then(u => {
        setUser(success(u))
        analytics.track('user_viewed', { userId })
      })
      .catch(e => setUser(failure(e)))
  }, [userId, api, analytics])

  // render...
}
```

### Testing with Mock Dependencies

```typescript
const mockDeps: AppDependencies = {
  api: {
    getUser: jest.fn().mockResolvedValue({ id: '1', name: 'Test User' }),
    updateUser: jest.fn().mockResolvedValue({ id: '1', name: 'Updated' }),
  },
  analytics: {
    track: jest.fn(),
  },
}

test('loads user on mount', async () => {
  render(
    <AppProvider deps={mockDeps}>
      <UserProfile userId="1" />
    </AppProvider>
  )

  await screen.findByText('Test User')
  expect(mockDeps.api.getUser).toHaveBeenCalledWith('1')
})
```

---

## 7. React 19 Patterns

### use() for Promises (React 19+)

```typescript
import { use, Suspense } from 'react'

// Instead of useEffect + useState for data fetching
function UserProfile({ userPromise }: { userPromise: Promise<User> }) {
  const user = use(userPromise)  // Suspends until resolved
  return <div>{user.name}</div>
}

// Parent provides the promise
function App() {
  const userPromise = fetchUser('1')  // Start fetching immediately

  return (
    <Suspense fallback={<Spinner />}>
      <UserProfile userPromise={userPromise} />
    </Suspense>
  )
}
```

### useActionState for Forms (React 19+)

```typescript
import { useActionState } from 'react'
import * as E from 'fp-ts/Either'

interface FormState {
  errors: string[]
  success: boolean
}

async function submitForm(
  prevState: FormState,
  formData: FormData
): Promise<FormState> {
  const data = {
    email: formData.get('email') as string,
    password: formData.get('password') as string,
  }

  // Use Either for validation
  const result = pipe(
    validateForm(data),
    E.match(
      (errors) => ({ errors, success: false }),
      async (valid) => {
        await saveToServer(valid)
        return { errors: [], success: true }
      }
    )
  )

  return result
}

function SignupForm() {
  const [state, formAction, isPending] = useActionState(submitForm, {
    errors: [],
    success: false
  })

  return (
    <form action={formAction}>
      <input name="email" type="email" />
      <input name="password" type="password" />

      {state.errors.map(e => <p key={e} className="error">{e}</p>)}

      <button disabled={isPending}>
        {isPending ? 'Submitting...' : 'Sign Up'}
      </button>
    </form>
  )
}
```

### useOptimistic for Instant Feedback (React 19+)

```typescript
import { useOptimistic } from 'react'

function TodoList({ todos }: { todos: Todo[] }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (state, newTodo: Todo) => [...state, { ...newTodo, pending: true }]
  )

  const addTodo = async (text: string) => {
    const newTodo = { id: crypto.randomUUID(), text, done: false }

    // Immediately show in UI
    addOptimisticTodo(newTodo)

    // Actually save (will reconcile when done)
    await saveTodo(newTodo)
  }

  return (
    <ul>
      {optimisticTodos.map(todo => (
        <li key={todo.id} style={{ opacity: todo.pending ? 0.5 : 1 }}>
          {todo.text}
        </li>
      ))}
    </ul>
  )
}
```

---

## 8. Common Patterns Cheat Sheet

### Render Based on Option

```typescript
// Pattern 1: match
pipe(
  maybeUser,
  O.match(
    () => <LoginButton />,
    (user) => <UserMenu user={user} />
  )
)

// Pattern 2: fold (same as match)
O.fold(
  () => <LoginButton />,
  (user) => <UserMenu user={user} />
)(maybeUser)

// Pattern 3: getOrElse for simple defaults
const name = pipe(
  maybeUser,
  O.map(u => u.name),
  O.getOrElse(() => 'Guest')
)
```

### Render Based on Either

```typescript
pipe(
  validationResult,
  E.match(
    (errors) => <ErrorList errors={errors} />,
    (data) => <SuccessMessage data={data} />
  )
)
```

### Safe Array Rendering

```typescript
import * as A from 'fp-ts/Array'

// Get first item safely
const firstUser = pipe(
  users,
  A.head,
  O.map(user => <Featured user={user} />),
  O.getOrElse(() => <NoFeaturedUser />)
)

// Find specific item
const adminUser = pipe(
  users,
  A.findFirst(u => u.role === 'admin'),
  O.map(admin => <AdminBadge user={admin} />),
  O.toNullable  // or O.getOrElse(() => null)
)
```

### Conditional Props

```typescript
// Add props only if value exists
const modalProps = {
  isOpen: true,
  ...pipe(
    maybeTitle,
    O.map(title => ({ title })),
    O.getOrElse(() => ({}))
  )
}
```

---

## When to Use What

| Situation | Use |
|-----------|-----|
| Value might not exist | `Option<T>` |
| Operation might fail (sync) | `Either<E, A>` |
| Async operation might fail | `TaskEither<E, A>` |
| Need loading/error/success UI | `RemoteData<E, A>` |
| Form with multiple validations | `Either` with validation applicative |
| Dependency injection | Context + `ReaderTaskEither` |
| Prevent re-renders with fp-ts | `useMemo` or `fp-ts-react-stable-hooks` |

---

## Libraries

- **[fp-ts](https://github.com/gcanti/fp-ts)** - Core library
- **[fp-ts-react-stable-hooks](https://github.com/mblink/fp-ts-react-stable-hooks)** - Stable hooks
- **[@devexperts/remote-data-ts](https://github.com/devexperts/remote-data-ts)** - RemoteData
- **[io-ts](https://github.com/gcanti/io-ts)** - Runtime type validation
- **[zod](https://github.com/colinhacks/zod)** - Schema validation (works great with fp-ts)


<!-- MERGED INTO: react-expert on 2026-04-18 -->
<!-- Use `react-expert` instead. -->

---

<!-- fp-ts-react -->
Practical patterns for React apps. No jargon, just code that works.

## When to Use This Skill

- When building React apps with fp-ts for type-safe state management
- When handling loading/error/success states in data fetching
- When implementing form validation with error accumulation
- When using React 18/19 or Next.js 14/15 with functional patterns

---

## Quick Reference

| Pattern | Use When |
|---------|----------|
| `Option` | Value might be missing (user not loaded yet) |
| `Either` | Operation might fail (form validation) |
| `TaskEither` | Async operation might fail (API calls) |
| `RemoteData` | Need to show loading/error/success states |
| `pipe` | Chaining multiple transformations |

---

## 1. State with Option (Maybe It's There, Maybe Not)

Use `Option` instead of `null | undefined` for clearer intent.

### Basic Pattern

```typescript
import { useState } from 'react'
import * as O from 'fp-ts/Option'
import { pipe } from 'fp-ts/function'

interface User {
  id: string
  name: string
  email: string
}

function UserProfile() {
  // Option says "this might not exist yet"
  const [user, setUser] = useState<O.Option<User>>(O.none)

  const handleLogin = (userData: User) => {
    setUser(O.some(userData))
  }

  const handleLogout = () => {
    setUser(O.none)
  }

  return pipe(
    user,
    O.match(
      // When there's no user
      () => <button onClick={() => handleLogin({ id: '1', name: 'Alice', email: 'alice@example.com' })}>
        Log In
      </button>,
      // When there's a user
      (u) => (
        <div>
          <p>Welcome, {u.name}!</p>
          <button onClick={handleLogout}>Log Out</button>
        </div>
      )
    )
  )
}
```

### Chaining Optional Values

```typescript
import * as O from 'fp-ts/Option'
import { pipe } from 'fp-ts/function'

interface Profile {
  user: O.Option<{
    name: string
    settings: O.Option<{
      theme: string
    }>
  }>
}

function getTheme(profile: Profile): string {
  return pipe(
    profile.user,
    O.flatMap(u => u.settings),
    O.map(s => s.theme),
    O.getOrElse(() => 'light') // default
  )
}
```

---

## 2. Form Validation with Either

Either is perfect for validation: `Left` = errors, `Right` = valid data.

### Simple Form Validation

```typescript
import * as E from 'fp-ts/Either'
import * as A from 'fp-ts/Array'
import { pipe } from 'fp-ts/function'

// Validation functions return Either<ErrorMessage, ValidValue>
const validateEmail = (email: string): E.Either<string, string> =>
  email.includes('@')
    ? E.right(email)
    : E.left('Invalid email address')

const validatePassword = (password: string): E.Either<string, string> =>
  password.length >= 8
    ? E.right(password)
    : E.left('Password must be at least 8 characters')

const validateName = (name: string): E.Either<string, string> =>
  name.trim().length > 0
    ? E.right(name.trim())
    : E.left('Name is required')
```

### Collecting All Errors (Not Just First One)

```typescript
import * as E from 'fp-ts/Either'
import { sequenceS } from 'fp-ts/Apply'
import { getSemigroup } from 'fp-ts/NonEmptyArray'
import { pipe } from 'fp-ts/function'

// This collects ALL errors, not just the first one
const validateAll = sequenceS(E.getApplicativeValidation(getSemigroup<string>()))

interface SignupForm {
  name: string
  email: string
  password: string
}

interface ValidatedForm {
  name: string
  email: string
  password: string
}

function validateForm(form: SignupForm): E.Either<string[], ValidatedForm> {
  return pipe(
    validateAll({
      name: pipe(validateName(form.name), E.mapLeft(e => [e])),
      email: pipe(validateEmail(form.email), E.mapLeft(e => [e])),
      password: pipe(validatePassword(form.password), E.mapLeft(e => [e])),
    })
  )
}

// Usage in component
function SignupForm() {
  const [form, setForm] = useState({ name: '', email: '', password: '' })
  const [errors, setErrors] = useState<string[]>([])

  const handleSubmit = () => {
    pipe(
      validateForm(form),
      E.match(
        (errs) => setErrors(errs),     // Show all errors
        (valid) => {
          setErrors([])
          submitToServer(valid)         // Submit valid data
        }
      )
    )
  }

  return (
    <form onSubmit={e => { e.preventDefault(); handleSubmit() }}>
      <input
        value={form.name}
        onChange={e => setForm(f => ({ ...f, name: e.target.value }))}
        placeholder="Name"
      />
      <input
        value={form.email}
        onChange={e => setForm(f => ({ ...f, email: e.target.value }))}
        placeholder="Email"
      />
      <input
        type="password"
        value={form.password}
        onChange={e => setForm(f => ({ ...f, password: e.target.value }))}
        placeholder="Password"
      />

      {errors.length > 0 && (
        <ul style={{ color: 'red' }}>
          {errors.map((err, i) => <li key={i}>{err}</li>)}
        </ul>
      )}

      <button type="submit">Sign Up</button>
    </form>
  )
}
```

### Field-Level Errors (Better UX)

```typescript
type FieldErrors = Partial<Record<keyof SignupForm, string>>

function validateFormWithFieldErrors(form: SignupForm): E.Either<FieldErrors, ValidatedForm> {
  const errors: FieldErrors = {}

  pipe(validateName(form.name), E.mapLeft(e => { errors.name = e }))
  pipe(validateEmail(form.email), E.mapLeft(e => { errors.email = e }))
  pipe(validatePassword(form.password), E.mapLeft(e => { errors.password = e }))

  return Object.keys(errors).length > 0
    ? E.left(errors)
    : E.right({ name: form.name.trim(), email: form.email, password: form.password })
}

// In component
{errors.email && <span className="error">{errors.email}</span>}
```

---

## 3. Data Fetching with TaskEither

TaskEither = async operation that might fail. Perfect for API calls.

### Basic Fetch Hook

```typescript
import { useState, useEffect } from 'react'
import * as TE from 'fp-ts/TaskEither'
import * as E from 'fp-ts/Either'
import { pipe } from 'fp-ts/function'

// Wrap fetch in TaskEither
const fetchJson = <T>(url: string): TE.TaskEither<Error, T> =>
  TE.tryCatch(
    async () => {
      const res = await fetch(url)
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      return res.json()
    },
    (err) => err instanceof Error ? err : new Error(String(err))
  )

// Custom hook
function useFetch<T>(url: string) {
  const [data, setData] = useState<T | null>(null)
  const [error, setError] = useState<Error | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    setLoading(true)
    setError(null)

    pipe(
      fetchJson<T>(url),
      TE.match(
        (err) => {
          setError(err)
          setLoading(false)
        },
        (result) => {
          setData(result)
          setLoading(false)
        }
      )
    )()
  }, [url])

  return { data, error, loading }
}

// Usage
function UserList() {
  const { data, error, loading } = useFetch<User[]>('/api/users')

  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error.message}</div>
  return (
    <ul>
      {data?.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  )
}
```

### Chaining API Calls

```typescript
// Fetch user, then fetch their posts
const fetchUserWithPosts = (userId: string) => pipe(
  fetchJson<User>(`/api/users/${userId}`),
  TE.flatMap(user => pipe(
    fetchJson<Post[]>(`/api/users/${userId}/posts`),
    TE.map(posts => ({ ...user, posts }))
  ))
)
```

### Parallel API Calls

```typescript
import { sequenceT } from 'fp-ts/Apply'

// Fetch multiple things at once
const fetchDashboardData = () => pipe(
  sequenceT(TE.ApplyPar)(
    fetchJson<User>('/api/user'),
    fetchJson<Stats>('/api/stats'),
    fetchJson<Notifications[]>('/api/notifications')
  ),
  TE.map(([user, stats, notifications]) => ({
    user,
    stats,
    notifications
  }))
)
```

---

## 4. RemoteData Pattern (The Right Way to Handle Async State)

Stop using `{ data, loading, error }` booleans. Use a proper state machine.

### The Pattern

```typescript
// RemoteData has exactly 4 states - no impossible combinations
type RemoteData<E, A> =
  | { _tag: 'NotAsked' }                    // Haven't started yet
  | { _tag: 'Loading' }                     // In progress
  | { _tag: 'Failure'; error: E }           // Failed
  | { _tag: 'Success'; data: A }            // Got it!

// Constructors
const notAsked = <E, A>(): RemoteData<E, A> => ({ _tag: 'NotAsked' })
const loading = <E, A>(): RemoteData<E, A> => ({ _tag: 'Loading' })
const failure = <E, A>(error: E): RemoteData<E, A> => ({ _tag: 'Failure', error })
const success = <E, A>(data: A): RemoteData<E, A> => ({ _tag: 'Success', data })

// Pattern match all states
function fold<E, A, R>(
  rd: RemoteData<E, A>,
  onNotAsked: () => R,
  onLoading: () => R,
  onFailure: (e: E) => R,
  onSuccess: (a: A) => R
): R {
  switch (rd._tag) {
    case 'NotAsked': return onNotAsked()
    case 'Loading': return onLoading()
    case 'Failure': return onFailure(rd.error)
    case 'Success': return onSuccess(rd.data)
  }
}
```

### Hook with RemoteData

```typescript
function useRemoteData<T>(fetchFn: () => Promise<T>) {
  const [state, setState] = useState<RemoteData<Error, T>>(notAsked())

  const execute = async () => {
    setState(loading())
    try {
      const data = await fetchFn()
      setState(success(data))
    } catch (err) {
      setState(failure(err instanceof Error ? err : new Error(String(err))))
    }
  }

  return { state, execute }
}

// Usage
function UserProfile({ userId }: { userId: string }) {
  const { state, execute } = useRemoteData(() =>
    fetch(`/api/users/${userId}`).then(r => r.json())
  )

  useEffect(() => { execute() }, [userId])

  return fold(
    state,
    () => <button onClick={execute}>Load User</button>,
    () => <Spinner />,
    (err) => <ErrorMessage message={err.message} onRetry={execute} />,
    (user) => <UserCard user={user} />
  )
}
```

### Why RemoteData Beats Booleans

```typescript
// ❌ BAD: Impossible states are possible
interface BadState {
  data: User | null
  loading: boolean
  error: Error | null
}
// Can have: { data: user, loading: true, error: someError } - what does that mean?!

// ✅ GOOD: Only valid states exist
type GoodState = RemoteData<Error, User>
// Can only be: NotAsked | Loading | Failure | Success
```

---

## 5. Referential Stability (Preventing Re-renders)

fp-ts values like `O.some(1)` create new objects each render. React sees them as "changed".

### The Problem

```typescript
// ❌ BAD: Creates new Option every render
function BadComponent() {
  const [value, setValue] = useState(O.some(1))

  useEffect(() => {
    // This runs EVERY render because O.some(1) !== O.some(1)
    console.log('value changed')
  }, [value])
}
```

### Solution 1: useMemo

```typescript
// ✅ GOOD: Memoize Option creation
function GoodComponent() {
  const [rawValue, setRawValue] = useState<number | null>(1)

  const value = useMemo(
    () => O.fromNullable(rawValue),
    [rawValue]  // Only recreate when rawValue changes
  )

  useEffect(() => {
    // Now this only runs when rawValue actually changes
    console.log('value changed')
  }, [rawValue])  // Depend on raw value, not Option
}
```

### Solution 2: fp-ts-react-stable-hooks

```bash
npm install fp-ts-react-stable-hooks
```

```typescript
import { useStableO, useStableEffect } from 'fp-ts-react-stable-hooks'
import * as O from 'fp-ts/Option'
import * as Eq from 'fp-ts/Eq'

function StableComponent() {
  // Uses fp-ts equality instead of reference equality
  const [value, setValue] = useStableO(O.some(1))

  // Effect that understands Option equality
  useStableEffect(
    () => { console.log('value changed') },
    [value],
    Eq.tuple(O.getEq(Eq.eqNumber))  // Custom equality
  )
}
```

---

## 6. Dependency Injection with Context

Use ReaderTaskEither for testable components with injected dependencies.

### Setup Dependencies

```typescript
import * as RTE from 'fp-ts/ReaderTaskEither'
import { pipe } from 'fp-ts/function'
import { createContext, useContext, ReactNode } from 'react'

// Define what services your app needs
interface AppDependencies {
  api: {
    getUser: (id: string) => Promise<User>
    updateUser: (id: string, data: Partial<User>) => Promise<User>
  }
  analytics: {
    track: (event: string, data?: object) => void
  }
}

// Create context
const DepsContext = createContext<AppDependencies | null>(null)

// Provider
function AppProvider({ deps, children }: { deps: AppDependencies; children: ReactNode }) {
  return <DepsContext.Provider value={deps}>{children}</DepsContext.Provider>
}

// Hook to use dependencies
function useDeps(): AppDependencies {
  const deps = useContext(DepsContext)
  if (!deps) throw new Error('Missing AppProvider')
  return deps
}
```

### Use in Components

```typescript
function UserProfile({ userId }: { userId: string }) {
  const { api, analytics } = useDeps()
  const [user, setUser] = useState<RemoteData<Error, User>>(notAsked())

  useEffect(() => {
    setUser(loading())
    api.getUser(userId)
      .then(u => {
        setUser(success(u))
        analytics.track('user_viewed', { userId })
      })
      .catch(e => setUser(failure(e)))
  }, [userId, api, analytics])

  // render...
}
```

### Testing with Mock Dependencies

```typescript
const mockDeps: AppDependencies = {
  api: {
    getUser: jest.fn().mockResolvedValue({ id: '1', name: 'Test User' }),
    updateUser: jest.fn().mockResolvedValue({ id: '1', name: 'Updated' }),
  },
  analytics: {
    track: jest.fn(),
  },
}

test('loads user on mount', async () => {
  render(
    <AppProvider deps={mockDeps}>
      <UserProfile userId="1" />
    </AppProvider>
  )

  await screen.findByText('Test User')
  expect(mockDeps.api.getUser).toHaveBeenCalledWith('1')
})
```

---

## 7. React 19 Patterns

### use() for Promises (React 19+)

```typescript
import { use, Suspense } from 'react'

// Instead of useEffect + useState for data fetching
function UserProfile({ userPromise }: { userPromise: Promise<User> }) {
  const user = use(userPromise)  // Suspends until resolved
  return <div>{user.name}</div>
}

// Parent provides the promise
function App() {
  const userPromise = fetchUser('1')  // Start fetching immediately

  return (
    <Suspense fallback={<Spinner />}>
      <UserProfile userPromise={userPromise} />
    </Suspense>
  )
}
```

### useActionState for Forms (React 19+)

```typescript
import { useActionState } from 'react'
import * as E from 'fp-ts/Either'

interface FormState {
  errors: string[]
  success: boolean
}

async function submitForm(
  prevState: FormState,
  formData: FormData
): Promise<FormState> {
  const data = {
    email: formData.get('email') as string,
    password: formData.get('password') as string,
  }

  // Use Either for validation
  const result = pipe(
    validateForm(data),
    E.match(
      (errors) => ({ errors, success: false }),
      async (valid) => {
        await saveToServer(valid)
        return { errors: [], success: true }
      }
    )
  )

  return result
}

function SignupForm() {
  const [state, formAction, isPending] = useActionState(submitForm, {
    errors: [],
    success: false
  })

  return (
    <form action={formAction}>
      <input name="email" type="email" />
      <input name="password" type="password" />

      {state.errors.map(e => <p key={e} className="error">{e}</p>)}

      <button disabled={isPending}>
        {isPending ? 'Submitting...' : 'Sign Up'}
      </button>
    </form>
  )
}
```

### useOptimistic for Instant Feedback (React 19+)

```typescript
import { useOptimistic } from 'react'

function TodoList({ todos }: { todos: Todo[] }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (state, newTodo: Todo) => [...state, { ...newTodo, pending: true }]
  )

  const addTodo = async (text: string) => {
    const newTodo = { id: crypto.randomUUID(), text, done: false }

    // Immediately show in UI
    addOptimisticTodo(newTodo)

    // Actually save (will reconcile when done)
    await saveTodo(newTodo)
  }

  return (
    <ul>
      {optimisticTodos.map(todo => (
        <li key={todo.id} style={{ opacity: todo.pending ? 0.5 : 1 }}>
          {todo.text}
        </li>
      ))}
    </ul>
  )
}
```

---

## 8. Common Patterns Cheat Sheet

### Render Based on Option

```typescript
// Pattern 1: match
pipe(
  maybeUser,
  O.match(
    () => <LoginButton />,
    (user) => <UserMenu user={user} />
  )
)

// Pattern 2: fold (same as match)
O.fold(
  () => <LoginButton />,
  (user) => <UserMenu user={user} />
)(maybeUser)

// Pattern 3: getOrElse for simple defaults
const name = pipe(
  maybeUser,
  O.map(u => u.name),
  O.getOrElse(() => 'Guest')
)
```

### Render Based on Either

```typescript
pipe(
  validationResult,
  E.match(
    (errors) => <ErrorList errors={errors} />,
    (data) => <SuccessMessage data={data} />
  )
)
```

### Safe Array Rendering

```typescript
import * as A from 'fp-ts/Array'

// Get first item safely
const firstUser = pipe(
  users,
  A.head,
  O.map(user => <Featured user={user} />),
  O.getOrElse(() => <NoFeaturedUser />)
)

// Find specific item
const adminUser = pipe(
  users,
  A.findFirst(u => u.role === 'admin'),
  O.map(admin => <AdminBadge user={admin} />),
  O.toNullable  // or O.getOrElse(() => null)
)
```

### Conditional Props

```typescript
// Add props only if value exists
const modalProps = {
  isOpen: true,
  ...pipe(
    maybeTitle,
    O.map(title => ({ title })),
    O.getOrElse(() => ({}))
  )
}
```

---

## When to Use What

| Situation | Use |
|-----------|-----|
| Value might not exist | `Option<T>` |
| Operation might fail (sync) | `Either<E, A>` |
| Async operation might fail | `TaskEither<E, A>` |
| Need loading/error/success UI | `RemoteData<E, A>` |
| Form with multiple validations | `Either` with validation applicative |
| Dependency injection | Context + `ReaderTaskEither` |
| Prevent re-renders with fp-ts | `useMemo` or `fp-ts-react-stable-hooks` |

---

## Libraries

- **[fp-ts](https://github.com/gcanti/fp-ts)** - Core library
- **[fp-ts-react-stable-hooks](https://github.com/mblink/fp-ts-react-stable-hooks)** - Stable hooks
- **[@devexperts/remote-data-ts](https://github.com/devexperts/remote-data-ts)** - RemoteData
- **[io-ts](https://github.com/gcanti/io-ts)** - Runtime type validation
- **[zod](https://github.com/colinhacks/zod)** - Schema validation (works great with fp-ts)


<!-- MERGED INTO: react-expert on 2026-04-18 -->
<!-- Use `react-expert` instead. -->

---

<!-- react-modernization -->
Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation.

## Use this skill when

- Upgrading React applications to latest versions
- Migrating class components to functional components with hooks
- Adopting concurrent React features (Suspense, transitions)
- Applying codemods for automated refactoring
- Modernizing state management patterns
- Updating to TypeScript
- Improving performance with React 18+ features

## Do not use this skill when

- The task is unrelated to react modernization
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.


<!-- MERGED INTO: react-expert on 2026-04-18 -->
<!-- Use `react-expert` instead. -->
