PubMed API

"The U.S. government’s PubMed [website](https://pubmed.ncbi.nlm.nih.gov) is a treasure of biomedical information."

This project is a FastAPI-based implementation that serves as a wrapper around the PubMed API, allowing users to search for articles by publication date, title, and abstract.

Example: https://pubmed.ncbi.nlm.nih.gov/?term=acl&filter=dates.2024/1/1-2024/12/31


Table of Contents

    Setup Instructions
    Code Structure
    Scalability Considerations
    Limitations

1. Setup Instructions
Prerequisites

    Python 3.8+
    Git (for cloning the repository)
    Docker (optional, if you wish to run the project in a container)

Steps

    Clone the Repository

git clone <repository_url>
cd <repository_name>

Set Up a Virtual Environment (Recommended)

python3 -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows

Install Dependencies

pip install -r requirements.txt

Run the Application

uvicorn app.main:app --reload

This starts the FastAPI server on http://localhost:8000.

Run Tests

To run the tests, use:

    pytest

2. Code Structure

Here's an overview of the code structure and key files:

.
├── app/
│   ├── main.py                # FastAPI app and route definitions
│   ├── services.py            # Functions that call PubMed API for various search types
│   ├── schemas.py             # Data models for API responses
│   └── config.py              # Configuration settings (e.g., API URLs)
│
├── tests/
│   ├── test_services.py       # Unit tests for service functions
│
├── Dockerfile                 # Docker configuration for containerizing the app
├── requirements.txt           # List of Python dependencies
└── README.md                  # Documentation

    app/main.py: Contains the FastAPI application and endpoint definitions for searching articles by date, title, and abstract.
    app/services.py: Contains core service functions that interact with the PubMed API. Includes validation to ensure dates follow YYYY-mm-dd format.
    app/schemas.py: Holds data models (using Pydantic) that define the structure of data returned by the API.
    tests/test_services.py: Contains tests for services.py functions, verifying the expected outputs of each search type.
    Dockerfile: Defines the environment for containerizing the application.
    requirements.txt: Lists the dependencies required to run the application.

3. Scalability Considerations

This project is designed for easy scaling and optimization in the following ways:

    Caching: Adding a caching layer (e.g., Redis) can store frequently accessed data, reducing repeated API calls and latency.
    Rate Limiting: Implementing rate limiting can help manage heavy loads by controlling the number of requests over time, especially if this wrapper will be public-facing.
    Load Balancing: Deploying the FastAPI app on multiple servers and load balancing requests across them will improve scalability for high-traffic applications.
    Asynchronous Requests: FastAPI’s async capabilities allow concurrent handling of requests, enabling the application to serve multiple users simultaneously with minimal response time.
    Database Storage: For applications that require more extensive data analysis, consider storing PubMed data in a local database (e.g., PostgreSQL) to reduce reliance on the API and improve query performance.

4. Limitations

There are several limitations and challenges to keep in mind:

    API Rate Limits: The PubMed API may have rate limits, restricting the number of requests per minute/hour. Implementing request throttling and error handling is recommended to prevent interruptions.
    Data Consistency: Since this wrapper retrieves real-time data from PubMed, results might change over time. Caching data locally could provide a more consistent experience, though it may become outdated.
    Data Volume: PubMed returns a large volume of data. This wrapper only fetches specific information (like publication date, title, and abstract) but may require additional filtering and pagination for extensive data.
    Limited Search Parameters: This implementation focuses on publication date, title, and abstract. Adding further filters (like author, journal) would require additional endpoints and logic.
