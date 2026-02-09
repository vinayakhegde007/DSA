# The Mestri API - Visual ER Diagram (Mermaid)

View this file in GitHub or any Mermaid-compatible markdown viewer to see the visual diagram.

```mermaid
erDiagram
    USERS ||--o{ USER_ROLES : has
    USERS ||--o{ ADDRESSES : has
    USERS ||--o| OPERATOR_PROFILES : may_have
    USERS ||--o{ WORK : posts_as_provider
    USERS ||--o{ REVIEWS : writes
    USERS ||--o{ PAYMENTS : pays
    USERS ||--o{ PAYMENTS : receives
    USERS ||--o{ NOTIFICATIONS : receives

    SKILLS ||--o{ SKILL_TRANSLATIONS : has
    SKILLS ||--o{ OPERATOR_SKILLS : offered_by_operators
    SKILLS ||--o{ WORK : required_for

    OPERATOR_PROFILES ||--o{ OPERATOR_SKILLS : has
    OPERATOR_PROFILES ||--o{ WORK : assigned_to
    OPERATOR_PROFILES ||--o{ WORK_APPLICATIONS : submits
    OPERATOR_PROFILES ||--o{ WORK_REQUESTS : receives

    OPERATOR_SKILLS ||--o{ REVIEWS : reviewed_on

    WORK ||--o{ WORK_IMAGES : has
    WORK ||--o{ WORK_APPLICATIONS : receives
    WORK ||--o{ WORK_REQUESTS : sends
    WORK ||--o{ REVIEWS : receives
    WORK ||--o{ PAYMENTS : triggers

    ADDRESSES ||--o{ WORK : located_at

    USERS {
        BIGINT id PK
        VARCHAR username UK
        VARCHAR email UK
        VARCHAR password
        VARCHAR first_name
        VARCHAR last_name
        VARCHAR phone_number
        ENUM gender
        VARCHAR profile_image_url
        BOOLEAN is_active
        BOOLEAN is_deleted
        BOOLEAN phone_number_verified
        VARCHAR reset_password_token
        VARCHAR preferred_locale
        TIMESTAMP last_login_at
        VARCHAR fcm_token
        TIMESTAMP created_at
        TIMESTAMP updated_at
    }

    USER_ROLES {
        BIGINT user_id FK
        ENUM role
    }

    ADDRESSES {
        BIGINT id PK
        BIGINT user_id FK
        VARCHAR line1
        VARCHAR line2
        VARCHAR city
        VARCHAR village
        VARCHAR state
        VARCHAR country
        VARCHAR postal_code
        DOUBLE latitude
        DOUBLE longitude
        ENUM address_type
        BOOLEAN is_deleted
    }

    SKILLS {
        BIGINT id PK
        VARCHAR name UK
        TEXT description
        VARCHAR skill_image_url
    }

    SKILL_TRANSLATIONS {
        BIGINT id PK
        BIGINT skill_id FK
        VARCHAR language_code
        VARCHAR translated_name
        TEXT translated_description
    }

    OPERATOR_PROFILES {
        BIGINT id PK
        BIGINT user_id FK "UNIQUE"
        TEXT bio
        BOOLEAN is_available
        BOOLEAN is_verified
        DOUBLE average_rating
        BIGINT total_reviews
        BOOLEAN is_deleted
    }

    OPERATOR_SKILLS {
        BIGINT id PK
        BIGINT operator_id FK
        BIGINT skill_id FK
        VARCHAR description
        ENUM pricing_type
        DOUBLE rate
        INTEGER experience_years
        DOUBLE average_rating
        BIGINT total_reviews
        BOOLEAN is_deleted
    }

    WORK {
        BIGINT id PK
        VARCHAR title
        TEXT description
        BIGINT job_type_id FK
        ENUM status
        BIGINT work_provider_id FK
        BIGINT work_address_id FK
        BIGINT assigned_operator_id FK
        DECIMAL budget
        INTEGER estimated_hours
        DATE scheduled_date
        TIMESTAMP started_at
        TIMESTAMP completed_at
        DATE due_date
        BOOLEAN is_deleted
    }

    WORK_IMAGES {
        BIGINT id PK
        BIGINT work FK
        VARCHAR image_url
        BOOLEAN is_primary
    }

    WORK_APPLICATIONS {
        BIGINT id PK
        BIGINT work_id FK
        BIGINT operator_profile_id FK
        ENUM status
        TEXT message
        TIMESTAMP applied_at
        TIMESTAMP reviewed_at
        BOOLEAN is_deleted
    }

    WORK_REQUESTS {
        BIGINT id PK
        BIGINT work_id FK
        BIGINT operator_profile_id FK
        ENUM status
        TEXT message
        TIMESTAMP sent_at
        TIMESTAMP responded_at
        BOOLEAN is_deleted
    }

    REVIEWS {
        BIGINT id PK
        BIGINT work FK
        BIGINT reviewer_id FK
        BIGINT operator_skill_id FK
        INTEGER rating
        TEXT comment
        BOOLEAN is_deleted
    }

    PAYMENTS {
        BIGINT id PK
        BIGINT job_id FK
        BIGINT payer_id FK
        BIGINT recipient_id FK
        DECIMAL amount
        VARCHAR payment_method
        VARCHAR transaction_id
        ENUM status
        TIMESTAMP payment_date
    }

    NOTIFICATIONS {
        BIGINT id PK
        BIGINT recipient_id FK
        ENUM type
        ENUM channel
        ENUM status
        ENUM priority
        VARCHAR subject
        TEXT body
        VARCHAR reference_id
        VARCHAR reference_type
        TIMESTAMP scheduled_at
        TIMESTAMP dispatched_at
        TIMESTAMP delivered_at
        TIMESTAMP read_at
        TEXT delivery_context
    }
```

## Diagram Legend

- **PK**: Primary Key
- **FK**: Foreign Key
- **UK**: Unique Constraint
- **FK "UNIQUE"**: Foreign Key with Unique Constraint (One-to-One relationship)
- **||--o{**: One-to-Many relationship
- **||--o|**: One-to-One relationship

## Color Coding (when rendered)

The diagram shows relationships between entities. Key patterns:

1. **User-centric design**: Users at the center connecting to multiple modules
2. **Operator workflow**: Users → Operator Profiles → Operator Skills → Reviews
3. **Work lifecycle**: Users → Work → Applications/Requests → Assignments → Reviews → Payments
4. **Skill management**: Skills → Translations & Skills → Operator Skills
5. **Notification system**: All activities trigger notifications to users
