# Meal Prep


## Purpose
- Recipe tracking application allowing users to create and discover new recipes
- Streamline meal planning and preperation
- Future features: to support health and budget management

## MVP Features
- Public recipe browsing
- User authentication
- Basic recipt CRUD operations
- Search functionality

## Tech Stack
- Backend: Python/Flask
- Frontend: React/Next.js/Jotai
- Database: PostgresSQL
- ORM: SQLAlchemy

## Technical Decisions
### Backend - Flask:
- Lightweight and flexible framework
- Direct Python practice opportunity
- Excellent for Rest API development
- Previous experience reduces initial learning curve
- Clean integration with SQLAlchemy

### Database - PostgressSQL:
- Good for structured data like the recipe tables
- Strog relationship handling (to handle my junction tables)
- ACID compliant (data integrity)
- Works well with SQLAlchemy
- Better for complex queries (will be necessary with future implementation)
- Free and open source

### Database Architecture:
- Junction table for ingredients instead of JSON storage because:
    - Better long-term scalability
    - Easier ingredient standardization
    - Simplified search functionality
    - More efficient for future features like grocery lists
    - Reduces future refactoring needs
- Addition of a measurements table to:
    - Enable dynamic addition of new measurement types
    - Facilitates future conversion calculations between units
    - Standardizes measurement options across recipes
    - Makes scaling recipes more accurate and consistent
    - Supports international measurement variations 
    - Simplifies grocery list consolidation (combining ingredients with different measurements)

### Frontend - React and Next.js:
- React benifits:
    - Component reusability
    - Virtual DOM for efficient updates
    - Large community support
    - Strong ecosystem of libraries
    - Industry standard skill

- Next.js benifits:
    - Built-in documentation support 
    - Server-side rendering capabilities
    - Improved SEO potential
    - Optimized performance
    - File-based routing
    - API route support
    - Enhanced developer experience

### State Management - Jotai:
- Lightweight and simple compared to Redux
- Efficient data persistence:
    - Recipe data can be atomically stored
    - User authentication state is easily managed
    - Seach states can be preserved
- Atomic approach reduces unnexessary rerenders:
    - Recipe updates can be handled efficiently
- Familiar from current work experience
- Great for server state caching
- Easy CRUD updated
- Less boilerplate than Redux


## Database Structure 
- Users
- Recipes
- Ingredients
- Measurements

## Getting Started
- Requirements:
    - Python 3.x
    - Node.js
    - PostgesSQL

- Installation:
    - Comming soon...


## Future Features:
- Google Calender integration for meal planning
- Automated grocery list generation
- Serving Size calculator
- Cost estimation per recipe/meal
- Nutritional information tracking
- Recipe scaling functionality
- Favorite recipes collection
- Meal prep organization tools
- Shopping cost tracking
- Recipe sharing between users