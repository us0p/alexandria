# Planning
Improve morning routine
## Routine - 12h
06:30 - 07:00 - Reading
07:00 - 07:30 - DSA
07:30 - 09:30 - Study
10:00 - 13:00 - Work
13:00 - 14:00 - Lunch
14:00 - 17:00 - Work
17:00 - 19:00 - Work related study
19:00 - 23:00 - Free Time
## Pomodoro timers
- **3h:** 45m/w + 10m/sr + 25m/lr -> 75% work rate
- **1h:** 50m/w + 10m/lr -> 83% work rate
- **2h:** 30m/w + 5m/r + 20m/lr -> 75% work rate
## Design Hierarchy
- System Design: Encompasses everything needed to build and run the system. Includes hardware, infrastructure, networking, APIs, and software architecture.
	- Software Architecture: Focuses on software system structure and how components interact. Defines service boundaries, data flow, tech stack, architectural patterns.
		- Software Design: Concerned with the implementation details inside each component or module. Cover class-level design, design patterns, data structures, and detailed workflows.

Software Architecture Patterns: High-level blueprints for structuring systems.
- Microservices
- Monolithic
- Event-Driven Architecture
- CQRS
- Client-Server
- Layered Architecture
- etc

Software Architecture Principles: Guide architecture decision-making and ensure system qualities (performance, maintainability, etc.)>
- Separation of concerns (SoC)
- Scalability
- CAP Theorem
- Loose Coupling & High Cohesion
- Resilience
- etc

Software Design Patterns: Reusable solutions to common programming problems:
- Singleton
- Factory
- Strategy
- Observer
- Adapter
- Decorator
- etc

Software Design Principles: Guidelines that promote clean, maintainable, and scalable code
- SOLID
- DRY
- KISS
- YAGNI
- etc
## Visual metaphor:
- System Design: Designing an entire city (roads, power grid, zones).
- Software Architecture: Designing a building within that city (layout, plumbing, electrical plans).
- Software Design: Designing the interior rooms (furniture placement, wiring, lighting).
## To study
- [x] OOP
- [x] SOLID
- [x] Clean Architecture
- [x] Testing strategies
    - [x] Technical debt
    - [x] Test priorization
    - [x] Testing approaches
    - [x] Test isolation
    - [x] Testing Techniques
        - [x] TDD
        - [x] BDD
    - [x] Test objects
	- [x] Test fixtures
	- [x] patching
	- [x] monkey patching
	- [x] Snapshot testing
    - [x] unit testing
    - [x] unit testing implications, should you use?
    - [x] integration testing
	    - [x] examples
	- [x] Integration testing implications, should you use?
	- [x] review and summary all the information
- [x] AI Agents - Overview
- [x] Python
	- [x] language basics
		- [ ] dictionary methods
		- [ ] Enum
		- [ ] requests
		- [ ] psycopg2
		- [ ] FastAPI
	- [x] exception handling
	- [x] classes
	- [x] mocking
- [x] `pytest`
- [ ] Terraform
- [ ] GitHub actions
- [ ] AWS 
	- [ ] CloudWatch
	- [ ] Fargate
---
- [ ] AI Agents (Deep Dive)
- [ ] AI MCP
- [ ] More about Python
	- [ ] BDD framework
	- [ ] fake framework
	- [ ] PEP 8
- [ ] Kubernetes
- [ ] Redis
- [ ] Kafka
- [ ] Design Patterns
    - [ ] factory
    - [ ] builder
    - [v] singleton
    - [ ] adapter
    - [ ] facade
    - [ ] proxy
    - [ ] command
    - [ ] strategy
- [ ] Backend: overall backend knowledge
- [ ] Linux - System Administration
- [ ] Network basics

1. DSA (practice every day)
2. System Design (get an overall knowledge, then start creating designs)
3. Backend General Knowledge (fundamental base knowledge, get an overall knowledge, deepen as needed)
	- Internet
	- Learn about APIs
	- Web Security
4. Software Architecture (More advanced knowledge, get an overall knowledge specially to know when and where to apply it, study implementation as needed)
	- Architectural Styles
	- Architectural Patterns
5. Software Design (More advanced knowledge, get an overall knowledge specially to know when and where to apply it, study implementation as needed)
	- Design Patterns
	- Development Principles
6. Technologies (low level knowledge, hard to reuse as it depends on each team, get an overall knowledge, study as needed)
	- Terraform
	- GitHub Actions
	- AWS
		- Fargate
		- CloudWatch
		- Event Bridge

You want to be really good in:
1. DSA
2. Software Design and Architecture

Once you get a good overall understanding of all of this topics, if you work in a small single project every weekend, you'll be able to work points 2 to 5 together as needed and deepen your knowledge in the areas you need the most at that time.