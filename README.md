## PubMed API Wrapper


> The U.S. government's PubMed ([website](https://pubmed.ncbi.nlm.nih.gov)) is a vast resource for biomedical information. This project provides a **FastAPI** wrapper that simplifies access to PubMed's search functionality. Users can search for articles by publication date, title, and abstract.

**Example Search URL**: Find ACL articles published in 2024: [Search for ACL articles in 2024](https://pubmed.ncbi.nlm.nih.gov/?term=acl&filter=dates.2024/1/1-2024/12/31)

## Table of Contents

* [Setup Instructions](#setup-instructions)
* [Code Structure](#code-structure)
* [Scalability Considerations](#scalability-considerations)
* [Limitations](#limitations)

## Setup Instructions

**Prerequisites:**

* Python 3.8+
* Git (for cloning)
* Docker (optional, for containerized deployment)

**Steps:**

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Set Up Virtual Environment (Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**

   ```bash
   uvicorn app.main:app --reload
   ```

   This starts the FastAPI server at http://localhost:8000.

5. **Run Tests:**

   ```bash
   pytest
   ```

## Code Structure

Here's an overview of the code and key files:

```
.
├── app/
│   ├── main.py                # FastAPI app & endpoint definitions
│   ├── services.py            # Functions for PubMed API calls
│   ├── schemas.py             # Data models for API responses
│   └── config.py              # Configuration settings (API URLs)
│
├── tests/
│   └── test_services.py       # Unit tests for service functions
│
├── Dockerfile                 # Docker configuration for containerizing the app
├── requirements.txt           # List of Python dependencies
└── README.md                  # Documentation
```

**key files:**

- `app/main.py`: Defines the FastAPI application and endpoints for searching.
- `app/services.py`: Contains functions interacting with the PubMed API.
- `app/schemas.py`: Defines data models (using Pydantic) for API responses.
- `tests/test_services.py`: Houses service function tests, verifying outputs.
- `Dockerfile`: Sets up the container environment for the application.
- `requirements.txt`: Lists dependencies needed to run the application.

## Scalability Considerations

This project can be easily scaled and optimized in these ways:

* **Database Storage:** Consider storing PubMed data in a database (e.g., PostgreSQL) for extensive data analysis and improved query performance.
* **Caching:** Implement a caching layer (e.g., Redis) to store frequently accessed data and reduce API calls.
* **Rate Limiting:**  Control request frequency (especially for public-facing use cases) by implementing rate limiting.
* **Load Balancing:** Distribute requests across multiple servers using load balancing for high-traffic applications.
 

## Limitations

Keep these limitations in mind:

* **Limited Search Parameters:** This implementation focuses on publication date, title, and abstract.  Adding more filters (author, journal) would require additional endpoints and logic.
* **API Rate Limits:**  The PubMed API might have rate limits. Implement request throttling and error handling to prevent service interruptions.
* **Data Volume:** PubMed returns large amounts of data. This wrapper retrieves specific information (publication date, title, abstract). Extensive analysis might require additional filtering and pagination features.

