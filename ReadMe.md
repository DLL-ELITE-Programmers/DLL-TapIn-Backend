# QR TapIn
#### DLL BSIT Department x IT Paradigm x DLL E.L.I.T.E

---

### Introduction

> This project is a QR-based attendance and event management system designed for institutional use. It facilitates efficient tracking of participants and management of departments, organizations, and events.

---

### Tech Stack & Versions

- **Language:** Python 3.13.7
- **Framework:** Django 6.0.5
- **API:** Django REST Framework 3.17.1
- **Authentication:** JWT (SimpleJWT 5.5.1)
- **Database:** PostgreSQL (psycopg2-binary)
- **Data Processing:** Pandas, NumPy, Openpyxl
- **Deployment:** Vercel, WhiteNoise, Gunicorn/Uvicorn

---

### Project Structure

```text
.
├── Accounts/          # User management, profiles, and signals
├── BaseAuth/          # Base authentication mixins, paginators, and shared logic
├── Departments/       # Department management and viewsets
├── DLL_TapIn/         # Project configuration, settings, and URL routing
├── Events/            # Event management and participant tracking
├── Feedbacks/         # Feedback collection and analysis
├── Organizations/     # Organization management
├── core/              # Core application logic, updates, and templates
├── certs/             # Security certificates (e.g., Aiven CA)
├── backup_data/       # Exported data and backups (CSV/Excel)
├── manage.py          # Django management script
├── requirements.txt   # Project dependencies
└── vercel.json        # Vercel deployment configuration
```

---

### System Overview

#### Database Schema
The following diagram illustrates the relationships between core entities in the system:

```mermaid
erDiagram
    USER }o--|| DEPARTMENT : "belongs to"
    USER ||--o{ PARTICIPANT : "participates in"
    USER ||--o{ FEEDBACK : "gives"
    DEPARTMENT }o--o{ ORGANIZATION : "associated with"
    ORGANIZATION }o--o{ EVENT : "hosts"
    EVENT ||--o{ PARTICIPANT : "has"
    EVENT ||--o{ FEEDBACK : "receives"

    USER {
        uuid id PK
        string username
        string first_name
        string last_name
        string middle_name
        int sex
        boolean verified
    }

    DEPARTMENT {
        int id PK
        string department_id
        string department_name
    }

    ORGANIZATION {
        int id PK
        string organization_id
        string organization_name
    }

    EVENT {
        string event_id PK
        string event_name
        string event_description
        string event_venue
    }

    PARTICIPANT {
        int id PK
        datetime time_in
        datetime time_out
    }

    FEEDBACK {
        int id PK
        string title
        string message
        datetime time_added
    }
```

#### Process Flow
The typical interaction flow for event attendance and management:

```mermaid
sequenceDiagram
    participant U as User (Student)
    participant S as System (Backend)
    participant O as Officer/Admin
    participant DB as Database

    O->>S: Create Event
    S->>DB: Save Event Info
    DB-->>S: Event Created
    S-->>O: Return event_id (QR Code generation)

    U->>S: Tap-In (Submit Event ID & Username)
    S->>DB: Validate User & Event
    DB-->>S: Validated
    S->>DB: Create Participant Record (Time-in)
    DB-->>S: Saved
    S-->>U: Participation Confirmed

    U->>S: Submit Event Feedback
    S->>DB: Save Feedback
    DB-->>S: Saved
    S-->>U: Feedback Received

    O->>S: Request Participant Report (Export)
    S->>DB: Query Participants for Event
    DB-->>S: Participant Data
    S->>S: Process Data (Pandas)
    S-->>O: Download Excel Report (.xlsx)
```

---

### Installation

<h3><font color="red">Please note that you need first to activate your <code>Virtual Environment</code> before you install these dependencies. You may install it using <code>pip install virtualenv</code> and activate it using <code>python -m venv venv</code>.</font></h3>

```bash
# Clone the repository
git clone <repository-url>

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic
```

---

### For testing with frontend

```bash
python manage.py runserver 0.0.0.0:8000
```

---

### Contribution Guidelines

We welcome contributions from students and developers. To maintain a professional and organized workflow, please follow these rules:

1. **Feature Branching:** Always create a new branch for any feature or bug fix. Do not commit directly to the `main` or `master` branch.
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Branch Cleanup:** Once a feature is completed and successfully merged, the feature branch **must be deleted** immediately to keep the repository clean.
3. **Professional Commenting:** Since this project serves as a learning archive for students, use clear and professional comments. Explain the *why* behind complex logic to help future student developers understand the codebase.
4. **No Environment Secrets:** Never commit `.env` files or hardcode sensitive credentials.

---

### Contributors

1. [Abdul Barry Adam](https://github.com/warebar) - Backend Developer
2. [Kurt Cyrus Atoat](https://github.com/seiyanndev) - Head Designer
3. [Peter Paul Eclavea](https://github.com/lpeter29) - Tester
4. [Bernard Gabito](https://github.com/brrnrd) - Tester
5. [Rogemson Molina](https://github.com/Rogemson) - Designer
6. [Ryann Kim Sesgundo](https://github.com/RyannKim327) - Developer

### Credits

- **Documentation & Assistant:** [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Provided architectural guidance, documentation updates, and development assistance.

---

### License

This project is licensed under a custom **Institutional and Educational License**. See [LICENSE.md](LICENSE.md) for full details. 
**Note:** Commercial use, selling the software, or selling gathered data for advertising is strictly prohibited.
