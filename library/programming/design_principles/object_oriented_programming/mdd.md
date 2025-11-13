# Model Driven Design (MDD)
Methodology in which the design of a system is represented by a set of models (e.g.: UML diagrams), and the models are used to drive the development of the system.
### History
Launched as part of Model-Driven Architecture (MDA) in 2001. It is a form of automation to generate code from models (class diagramas like UML).
#### Relationship with DDD
Domain-Driven Design was created in 2003 by Eric Evans and it was a result of the very abstract work MDD was creating. It aims to move the diagrams as a living language and model within the codebase to avoid generic abstractions.
## Domain Models
Used to provide a clear and consistent representation of the problem domain, and to capture the business requirements and constraints of the system.

In OOP, a domain model is typically represented by a set of classes and interfaces, with each class or interface representing a specific concept or object within the domain.

```python
from datetime import datetime
from typing import List, Optional

class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.posts: List['Post'] = []

    def write_post(self, title: str, content: str) -> 'Post':
        post = Post(title, content, author=self)
        self.posts.append(post)
        return post

class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
        self.comments: List['Comment'] = []

    def add_comment(self, author: User, text: str) -> 'Comment':
        comment = Comment(text, author, post=self)
        self.comments.append(comment)
        return comment

class Comment:
    def __init__(self, text: str, author: User, post: Post):
        self.text = text
        self.author = author
        self.post = post
        self.created_at = datetime.now()
```

- We treat **User**, **Post**, and **Comment** as _Entities_ (they have identity and lifecycle).
- Relationships are modeled via object references (`author`, `comments`, etc.).
- Business logic (like `write_post`, `add_comment`) lives **inside the domain objects**, not separate service classes
## Anemic Models
Is a type of domain model in which the domain objects only contain data (attributes) and lack behavior. An anemic model often results in the use of data-transfer objects (DTO) and service layer to handle the behavior.

An anemic model is considered an anti-pattern in object-oriented programming (OOP) because it violates the principles of encapsulation and separation of concerns.

```python
from datetime import datetime
from typing import List


# --- Entities / Data Models ---
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()
        self.comments: List['Comment'] = []

class Comment:
    def __init__(self, text: str, author: User, post: Post):
        self.text = text
        self.author = author
        self.post = post
        self.created_at = datetime.now()

class BlogService:
    """Contains domain logic for managing posts and comments."""

    def write_post(self, author: User, title: str, content: str) -> Post:
        post = Post(title, content, author)
        # Here you’d persist it, e.g., post_repository.save(post)
        print(f"Post '{title}' created by {author.username}")
        return post

    def add_comment(self, post: Post, author: User, text: str) -> Comment:
        comment = Comment(text, author, post)
        post.comments.append(comment)
        print(f"Comment added by {author.username} on post '{post.title}'")
        return comment
```

- Entities become **just data containers** (no domain logic).
- Business rules live in **service classes** that manipulate these data structures.
## Domain Language
Specific vocabulary and set of concepts used to describe and communicate about a specific area of knowledge or business.

In software development, a domain language is used to model the objects and concepts within a specific domain, and to capture the relationships and constraints between them.
## Class Invariants
Set of conditions that must be true for any object of a class, at any point in time.

In OOP, class invariants are used to define the valid states of an object and to ensure that the object always remains in a valid state.

Class invariants are typically defined in the constructor of a class and are enforced through the use of private methods and data members that are used to validate the state of the object.

They are also checked in the class's methods before and after any operation that can change the state of the object.

```python
import re

class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self._check_invariant()

    def change_email(self, new_email: str):
        self.email = new_email
        self._check_invariant()

    def _check_invariant(self):
        assert re.match(r"[^@]+@[^@]+\.[^@]+", self.email), \
            f"Invariant violated: invalid email {self.email}"
```

- A **class invariant** is a rule that must **always hold true** for a valid object.
- You check it:
    - **After construction**, and
    - **After any method** that changes state.