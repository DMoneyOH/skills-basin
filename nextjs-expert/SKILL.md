---
name: nextjs-expert
description: "Master Next.js 14+ App Router with Server Components, streaming, parallel routes, and advanced data fetching. Use when building Next.js applications, implementing SSR/SSG, or optimizing React Serve..."
triggers:
  - # next.js app router patterns
  - # next.js best practices
  - # react/next.js development workflow
  - ## 1. server vs client components
  - ## 10. project structure
  - ## 2. data fetching patterns
  - ## 3. routing principles
  - ## 4. api routes
  - ## 5. performance principles
  - ## 6. metadata
  - ## 7. caching strategy
  - ## 8. server actions
  - ## 9. anti-patterns
  - *client** | forms, buttons, interactive ui |
  - *server** | data fetching, layout, static content |
merged_from:
  - nextjs-best-practices
  - nextjs-app-router-patterns
  - react-nextjs-development
merged_at: 2026-04-18T17:20:54.596663
---

# nextjs-expert

<!-- nextjs-best-practices -->
> Principles for Next.js App Router development.

---

## 1. Server vs Client Components

### Decision Tree

```
Does it need...?
│
├── useState, useEffect, event handlers
│   └── Client Component ('use client')
│
├── Direct data fetching, no interactivity
│   └── Server Component (default)
│
└── Both? 
    └── Split: Server parent + Client child
```

### By Default

| Type | Use |
|------|-----|
| **Server** | Data fetching, layout, static content |
| **Client** | Forms, buttons, interactive UI |

---

## 2. Data Fetching Patterns

### Fetch Strategy

| Pattern | Use |
|---------|-----|
| **Default** | Static (cached at build) |
| **Revalidate** | ISR (time-based refresh) |
| **No-store** | Dynamic (every request) |

### Data Flow

| Source | Pattern |
|--------|---------|
| Database | Server Component fetch |
| API | fetch with caching |
| User input | Client state + server action |

---

## 3. Routing Principles

### File Conventions

| File | Purpose |
|------|---------|
| `page.tsx` | Route UI |
| `layout.tsx` | Shared layout |
| `loading.tsx` | Loading state |
| `error.tsx` | Error boundary |
| `not-found.tsx` | 404 page |

### Route Organization

| Pattern | Use |
|---------|-----|
| Route groups `(name)` | Organize without URL |
| Parallel routes `@slot` | Multiple same-level pages |
| Intercepting `(.)` | Modal overlays |

---

## 4. API Routes

### Route Handlers

| Method | Use |
|--------|-----|
| GET | Read data |
| POST | Create data |
| PUT/PATCH | Update data |
| DELETE | Remove data |

### Best Practices

- Validate input with Zod
- Return proper status codes
- Handle errors gracefully
- Use Edge runtime when possible

---

## 5. Performance Principles

### Image Optimization

- Use next/image component
- Set priority for above-fold
- Provide blur placeholder
- Use responsive sizes

### Bundle Optimization

- Dynamic imports for heavy components
- Route-based code splitting (automatic)
- Analyze with bundle analyzer

---

## 6. Metadata

### Static vs Dynamic

| Type | Use |
|------|-----|
| Static export | Fixed metadata |
| generateMetadata | Dynamic per-route |

### Essential Tags

- title (50-60 chars)
- description (150-160 chars)
- Open Graph images
- Canonical URL

---

## 7. Caching Strategy

### Cache Layers

| Layer | Control |
|-------|---------|
| Request | fetch options |
| Data | revalidate/tags |
| Full route | route config |

### Revalidation

| Method | Use |
|--------|-----|
| Time-based | `revalidate: 60` |
| On-demand | `revalidatePath/Tag` |
| No cache | `no-store` |

---

## 8. Server Actions

### Use Cases

- Form submissions
- Data mutations
- Revalidation triggers

### Best Practices

- Mark with 'use server'
- Validate all inputs
- Return typed responses
- Handle errors

---

## 9. Anti-Patterns

| ❌ Don't | ✅ Do |
|----------|-------|
| 'use client' everywhere | Server by default |
| Fetch in client components | Fetch in server |
| Skip loading states | Use loading.tsx |
| Ignore error boundaries | Use error.tsx |
| Large client bundles | Dynamic imports |

---

## 10. Project Structure

```
app/
├── (marketing)/     # Route group
│   └── page.tsx
├── (dashboard)/
│   ├── layout.tsx   # Dashboard layout
│   └── page.tsx
├── api/
│   └── [resource]/
│       └── route.ts
└── components/
    └── ui/
```

---

> **Remember:** Server Components are the default for a reason. Start there, add client only when needed.

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: nextjs-expert on 2026-04-18 -->
<!-- Use `nextjs-expert` instead. -->

---

<!-- nextjs-app-router-patterns -->
Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development.

## Use this skill when

- Building new Next.js applications with App Router
- Migrating from Pages Router to App Router
- Implementing Server Components and streaming
- Setting up parallel and intercepting routes
- Optimizing data fetching and caching
- Building full-stack features with Server Actions

## Do not use this skill when

- The task is unrelated to next.js app router patterns
- You need a different domain or tool outside this scope

## Instructions

- Clarify goals, constraints, and required inputs.
- Apply relevant best practices and validate outcomes.
- Provide actionable steps and verification.
- If detailed examples are required, open `resources/implementation-playbook.md`.

## Resources

- `resources/implementation-playbook.md` for detailed patterns and examples.


<!-- MERGED INTO: nextjs-expert on 2026-04-18 -->
<!-- Use `nextjs-expert` instead. -->

---

<!-- react-nextjs-development -->
## Overview

Specialized workflow for building React and Next.js 14+ applications with modern patterns including App Router, Server Components, TypeScript, and Tailwind CSS.

## When to Use This Workflow

Use this workflow when:
- Building new React applications
- Creating Next.js 14+ projects with App Router
- Implementing Server Components
- Setting up TypeScript with React
- Styling with Tailwind CSS
- Building full-stack Next.js applications

## Workflow Phases

### Phase 1: Project Setup

#### Skills to Invoke
- `app-builder` - Application scaffolding
- `senior-fullstack` - Full-stack guidance
- `nextjs-app-router-patterns` - Next.js 14+ patterns
- `typescript-pro` - TypeScript setup

#### Actions
1. Choose project type (React SPA, Next.js app)
2. Select build tool (Vite, Next.js, Create React App)
3. Scaffold project structure
4. Configure TypeScript
5. Set up ESLint and Prettier

#### Copy-Paste Prompts
```
Use @app-builder to scaffold a new Next.js 14 project with App Router
```

```
Use @nextjs-app-router-patterns to set up Server Components
```

### Phase 2: Component Architecture

#### Skills to Invoke
- `frontend-developer` - Component development
- `react-patterns` - React patterns
- `react-state-management` - State management
- `react-ui-patterns` - UI patterns

#### Actions
1. Design component hierarchy
2. Create base components
3. Implement layout components
4. Set up state management
5. Create custom hooks

#### Copy-Paste Prompts
```
Use @frontend-developer to create reusable React components
```

```
Use @react-patterns to implement proper component composition
```

```
Use @react-state-management to set up Zustand store
```

### Phase 3: Styling and Design

#### Skills to Invoke
- `frontend-design` - UI design
- `tailwind-patterns` - Tailwind CSS
- `tailwind-design-system` - Design system
- `core-components` - Component library

#### Actions
1. Set up Tailwind CSS
2. Configure design tokens
3. Create utility classes
4. Build component styles
5. Implement responsive design

#### Copy-Paste Prompts
```
Use @tailwind-patterns to style components with Tailwind CSS v4
```

```
Use @frontend-design to create a modern dashboard UI
```

### Phase 4: Data Fetching

#### Skills to Invoke
- `nextjs-app-router-patterns` - Server Components
- `react-state-management` - React Query
- `api-patterns` - API integration

#### Actions
1. Implement Server Components
2. Set up React Query/SWR
3. Create API client
4. Handle loading states
5. Implement error boundaries

#### Copy-Paste Prompts
```
Use @nextjs-app-router-patterns to implement Server Components data fetching
```

### Phase 5: Routing and Navigation

#### Skills to Invoke
- `nextjs-app-router-patterns` - App Router
- `nextjs-best-practices` - Next.js patterns

#### Actions
1. Set up file-based routing
2. Create dynamic routes
3. Implement nested routes
4. Add route guards
5. Configure redirects

#### Copy-Paste Prompts
```
Use @nextjs-app-router-patterns to set up parallel routes and intercepting routes
```

### Phase 6: Forms and Validation

#### Skills to Invoke
- `frontend-developer` - Form development
- `typescript-advanced-types` - Type validation
- `react-ui-patterns` - Form patterns

#### Actions
1. Choose form library (React Hook Form, Formik)
2. Set up validation (Zod, Yup)
3. Create form components
4. Handle submissions
5. Implement error handling

#### Copy-Paste Prompts
```
Use @frontend-developer to create forms with React Hook Form and Zod
```

### Phase 7: Testing

#### Skills to Invoke
- `javascript-testing-patterns` - Jest/Vitest
- `playwright-skill` - E2E testing
- `e2e-testing-patterns` - E2E patterns

#### Actions
1. Set up testing framework
2. Write unit tests
3. Create component tests
4. Implement E2E tests
5. Configure CI integration

#### Copy-Paste Prompts
```
Use @javascript-testing-patterns to write Vitest tests
```

```
Use @playwright-skill to create E2E tests for critical flows
```

### Phase 8: Build and Deployment

#### Skills to Invoke
- `vercel-deployment` - Vercel deployment
- `vercel-deploy-claimable` - Vercel deployment
- `web-performance-optimization` - Performance

#### Actions
1. Configure build settings
2. Optimize bundle size
3. Set up environment variables
4. Deploy to Vercel
5. Configure preview deployments

#### Copy-Paste Prompts
```
Use @vercel-deployment to deploy Next.js app to production
```

## Technology Stack

| Category | Technology |
|----------|------------|
| Framework | Next.js 14+, React 18+ |
| Language | TypeScript 5+ |
| Styling | Tailwind CSS v4 |
| State | Zustand, React Query |
| Forms | React Hook Form, Zod |
| Testing | Vitest, Playwright |
| Deployment | Vercel |

## Quality Gates

- [ ] TypeScript compiles without errors
- [ ] All tests passing
- [ ] Linting clean
- [ ] Performance metrics met (LCP, CLS, FID)
- [ ] Accessibility checked (WCAG 2.1)
- [ ] Responsive design verified

## Related Workflow Bundles

- `development` - General development
- `testing-qa` - Testing workflow
- `documentation` - Documentation
- `typescript-development` - TypeScript patterns


<!-- MERGED INTO: nextjs-expert on 2026-04-18 -->
<!-- Use `nextjs-expert` instead. -->
