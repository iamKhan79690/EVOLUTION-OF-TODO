# Development Hierarchy - Todo Full-Stack Application

## Overview
**Project**: The Evolution of Todo  
**Phase**: Hackathon II - Phase II  
**Deadline**: December 14, 2025, 11:59 PM  
**Points**: 150 (base) + up to 50 (bonuses)

---

## Implementation Order

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PHASE 0: PROJECT SETUP (Day 1)                       │
│                         ⬇️ FOUNDATION FIRST                             │
├─────────────────────────────────────────────────────────────────────────┤
│  1. Initialize Frontend (Next.js 16+)                                   │
│  2. Initialize Backend (FastAPI + Python)                               │
│  3. Create Neon PostgreSQL Database                                     │
│  4. Set up Environment Variables (.env files)                           │
│  5. Create Feature Specifications (/specs/features/)                    │
└─────────────────────────────────────────────────────────────────────────┘
                                   ⬇️
┌─────────────────────────────────────────────────────────────────────────┐
│               PHASE 1: DATABASE LAYER (Day 2)                          │
│                    ⬇️ DATA BEFORE LOGIC                                │
├─────────────────────────────────────────────────────────────────────────┤
│  Agent: @Database-Architect                                             │
│  ─────────────────────────────────                                      │
│  1. Configure Neon PostgreSQL connection                                │
│  2. Create SQLModel models (User, Task)                                 │
│  3. Set up database.py with connection pooling                          │
│  4. Test database connection                                            │
│  5. Verify tables created                                               │
└─────────────────────────────────────────────────────────────────────────┘
                                   ⬇️
┌─────────────────────────────────────────────────────────────────────────┐
│            PHASE 2: BACKEND API (Days 3-4)                             │
│               ⬇️ API BEFORE FRONTEND                                   │
├─────────────────────────────────────────────────────────────────────────┤
│  Agent: @Backend-Architect                                              │
│  ─────────────────────────────────                                      │
│  1. Create Pydantic schemas (TaskCreate, TaskUpdate, TaskResponse)      │
│  2. Implement health check endpoint (GET /api/health)                   │
│  3. Implement 5 CRUD endpoints:                                         │
│     • GET    /api/{user_id}/tasks          (list tasks)                 │
│     • POST   /api/{user_id}/tasks          (create task)                │
│     • GET    /api/{user_id}/tasks/{id}     (get task)                   │
│     • PUT    /api/{user_id}/tasks/{id}     (update task)                │
│     • DELETE /api/{user_id}/tasks/{id}     (delete task)                │
│     • PATCH  /api/{user_id}/tasks/{id}/complete (toggle complete)       │
│  4. Test all endpoints via /docs (Swagger UI)                           │
└─────────────────────────────────────────────────────────────────────────┘
                                   ⬇️
┌─────────────────────────────────────────────────────────────────────────┐
│          PHASE 3: AUTHENTICATION (Days 5-6)                            │
│              ⬇️ AUTH BEFORE PROTECTED ROUTES                           │
├─────────────────────────────────────────────────────────────────────────┤
│  Agent: @BetterAuth-Engineer                                            │
│  ─────────────────────────────────                                      │
│  BACKEND:                                                               │
│  1. Install python-jose for JWT verification                            │
│  2. Create auth.py with JWT middleware                                  │
│  3. Add authentication to all API routes                                │
│  4. Implement user authorization check                                  │
│                                                                         │
│  FRONTEND:                                                              │
│  1. Install Better Auth                                                 │
│  2. Configure Better Auth with Neon PostgreSQL                          │
│  3. Create auth API route handler                                       │
│  4. Create SignIn and SignUp forms                                      │
│  5. Store JWT token for API calls                                       │
│  6. Test full auth flow                                                 │
└─────────────────────────────────────────────────────────────────────────┘
                                   ⬇️
┌─────────────────────────────────────────────────────────────────────────┐
│          PHASE 4: FRONTEND UI (Days 7-9)                               │
│              ⬇️ UI AFTER API IS READY                                  │
├─────────────────────────────────────────────────────────────────────────┤
│  Agent: @Frontend-Specialist                                            │
│  ─────────────────────────────────                                      │
│  1. Create API client (lib/api.ts) with JWT handling                    │
│  2. Create TypeScript types (lib/types.ts)                              │
│  3. Build auth pages:                                                   │
│     • /auth/signin - Sign in page                                       │
│     • /auth/signup - Sign up page                                       │
│  4. Build dashboard page (/(protected)/dashboard)                       │
│  5. Build task components:                                              │
│     • TaskList - List all tasks                                         │
│     • TaskItem - Single task with actions                               │
│     • TaskForm - Create/edit task form                                  │
│  6. Add loading states and error handling                               │
│  7. Style with Tailwind CSS                                             │
│  8. Make mobile responsive                                              │
└─────────────────────────────────────────────────────────────────────────┘
                                   ⬇️
┌─────────────────────────────────────────────────────────────────────────┐
│         PHASE 5: INTEGRATION & TESTING (Days 10-11)                    │
│                ⬇️ TEST EVERYTHING TOGETHER                             │
├─────────────────────────────────────────────────────────────────────────┤
│  Agent: @Testing-Coordinator + @API-Contract-Manager                    │
│  ─────────────────────────────────                                      │
│  1. End-to-end integration testing                                      │
│  2. Authentication flow testing (signup → signin → signout)             │
│  3. CRUD operations testing                                             │
│  4. Security testing (user isolation)                                   │
│  5. UI/UX testing (mobile, browsers)                                    │
│  6. Fix bugs and issues                                                 │
│  7. CORS verification                                                   │
└─────────────────────────────────────────────────────────────────────────┘
                                   ⬇️
┌─────────────────────────────────────────────────────────────────────────┐
│           PHASE 6: DEPLOYMENT (Day 12)                                 │
│              ⬇️ DEPLOY WHEN TESTED                                     │
├─────────────────────────────────────────────────────────────────────────┤
│  Agent: @Deployment-Coordinator                                         │
│  ─────────────────────────────────                                      │
│  1. Deploy frontend to Vercel                                           │
│     • Connect GitHub repo                                               │
│     • Set environment variables                                         │
│  2. Deploy backend to Railway/Render                                    │
│     • Configure start command                                           │
│     • Set environment variables                                         │
│  3. Verify production deployment                                        │
│  4. Test all features in production                                     │
└─────────────────────────────────────────────────────────────────────────┘
                                   ⬇️
┌─────────────────────────────────────────────────────────────────────────┐
│        PHASE 7: DOCUMENTATION & DEMO (Day 13)                          │
│                ⬇️ DOCUMENT EVERYTHING                                  │
├─────────────────────────────────────────────────────────────────────────┤
│  1. Complete README.md with setup instructions                          │
│  2. Ensure all specs are documented                                     │
│  3. Record demo video (< 90 seconds)                                    │
│  4. Final checklist review                                              │
└─────────────────────────────────────────────────────────────────────────┘
                                   ⬇️
┌─────────────────────────────────────────────────────────────────────────┐
│            PHASE 8: SUBMISSION (Day 14 - Dec 14)                       │
│                    🎯 DEADLINE 11:59 PM                                │
├─────────────────────────────────────────────────────────────────────────┤
│  1. Submit to hackathon                                                 │
│  2. Include deployment URLs                                             │
│  3. Include demo video link                                             │
│  4. ✅ All 150 points achieved!                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Phase Details

### Phase 0: Project Setup
**Duration**: 1 day  
**Dependencies**: None (starting point)

| Task | Command | Status |
|------|---------|--------|
| Initialize Frontend | `npx create-next-app@latest frontend` | ⏳ |
| Initialize Backend | `mkdir backend && cd backend && uv init` | ⏳ |
| Create Neon Database | Sign up at neon.tech | ⏳ |
| Setup .env files | Create .env.local and .env | ⏳ |
| Create specs | mkdir specs/features | ⏳ |

---

### Phase 1: Database Layer
**Duration**: 1 day  
**Dependencies**: Phase 0 complete  
**Agent**: @Database-Architect

| Task | File | Status |
|------|------|--------|
| Database connection | `backend/app/database.py` | ⏳ |
| SQLModel models | `backend/app/models.py` | ⏳ |
| Test connection | Run backend, check logs | ⏳ |

---

### Phase 2: Backend API
**Duration**: 2 days  
**Dependencies**: Phase 1 complete  
**Agent**: @Backend-Architect

| Endpoint | Method | Path | Status |
|----------|--------|------|--------|
| Health check | GET | `/api/health` | ⏳ |
| List tasks | GET | `/api/{user_id}/tasks` | ⏳ |
| Create task | POST | `/api/{user_id}/tasks` | ⏳ |
| Get task | GET | `/api/{user_id}/tasks/{id}` | ⏳ |
| Update task | PUT | `/api/{user_id}/tasks/{id}` | ⏳ |
| Delete task | DELETE | `/api/{user_id}/tasks/{id}` | ⏳ |
| Toggle complete | PATCH | `/api/{user_id}/tasks/{id}/complete` | ⏳ |

---

### Phase 3: Authentication
**Duration**: 2 days  
**Dependencies**: Phase 2 complete  
**Agent**: @BetterAuth-Engineer

| Task | Location | Status |
|------|----------|--------|
| JWT verification | `backend/app/auth.py` | ⏳ |
| Better Auth setup | `frontend/lib/auth.ts` | ⏳ |
| Auth API routes | `frontend/app/api/auth/[...all]/route.ts` | ⏳ |
| SignIn form | `frontend/components/auth/SignInForm.tsx` | ⏳ |
| SignUp form | `frontend/components/auth/SignUpForm.tsx` | ⏳ |

---

### Phase 4: Frontend UI
**Duration**: 3 days  
**Dependencies**: Phase 3 complete  
**Agent**: @Frontend-Specialist

| Component | Path | Status |
|-----------|------|--------|
| API client | `frontend/lib/api.ts` | ⏳ |
| Types | `frontend/lib/types.ts` | ⏳ |
| SignIn page | `frontend/app/auth/signin/page.tsx` | ⏳ |
| SignUp page | `frontend/app/auth/signup/page.tsx` | ⏳ |
| Dashboard | `frontend/app/(protected)/dashboard/page.tsx` | ⏳ |
| TaskList | `frontend/components/tasks/TaskList.tsx` | ⏳ |
| TaskItem | `frontend/components/tasks/TaskItem.tsx` | ⏳ |
| TaskForm | `frontend/components/tasks/TaskForm.tsx` | ⏳ |

---

### Phase 5: Integration & Testing
**Duration**: 2 days  
**Dependencies**: Phase 4 complete  
**Agent**: @Testing-Coordinator

| Test Category | Tests | Status |
|---------------|-------|--------|
| Authentication | signup, signin, signout, protected routes | ⏳ |
| CRUD | create, read, update, delete, toggle | ⏳ |
| Security | user isolation, invalid JWT, no JWT | ⏳ |
| UI/UX | mobile, browsers, loading states | ⏳ |

---

### Phase 6: Deployment
**Duration**: 1 day  
**Dependencies**: Phase 5 complete  
**Agent**: @Deployment-Coordinator

| Service | Platform | Status |
|---------|----------|--------|
| Frontend | Vercel | ⏳ |
| Backend | Railway/Render | ⏳ |
| Database | Neon (already set up) | ⏳ |

---

### Phase 7: Documentation & Demo
**Duration**: 1 day  
**Dependencies**: Phase 6 complete

| Task | Status |
|------|--------|
| README.md complete | ⏳ |
| All specs documented | ⏳ |
| Demo video recorded (< 90s) | ⏳ |

---

### Phase 8: Submission
**Duration**: Final day (Dec 14)  
**Deadline**: 11:59 PM

| Task | Status |
|------|--------|
| Submit to hackathon | ⏳ |
| Include deployment URLs | ⏳ |
| Include demo video | ⏳ |

---

## Quick Reference

### Agent Commands
```bash
@Database-Architect: Set up database schema
@Backend-Architect: Implement API endpoints
@BetterAuth-Engineer: Implement authentication
@Frontend-Specialist: Create UI components
@Testing-Coordinator: Run manual tests
@Deployment-Coordinator: Deploy to production
```

### Development Commands
```bash
# Frontend (port 3000)
cd frontend && npm run dev

# Backend (port 8000)
cd backend && uvicorn app.main:app --reload
```

---

## Success Criteria

| Category | Points | Requirements |
|----------|--------|--------------|
| Functional | 100 | Auth + CRUD + User isolation |
| Technical | 30 | Next.js + FastAPI + Neon + Better Auth |
| Documentation | 20 | README + Specs + Demo video |
| **Total** | **150** | |

---

*"Foundation first, API second, UI third, test everything, deploy confidently."*
