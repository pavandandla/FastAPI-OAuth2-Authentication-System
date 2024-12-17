# **FastAPI OAuth2 Authentication System**

## **Description**

The **FastAPI OAuth2 Authentication System** is an application built using **FastAPI** that integrates OAuth2 authentication with third-party providers like **Google** or **GitHub**. The system utilizes **Authlib** for OAuth2 authentication and **JWT** for securing the API with token-based authorization. This solution provides a robust and scalable way to authenticate users using third-party accounts while ensuring security and maintainability.



## **Features**

- **FastAPI Framework**: Provides the foundation for building high-performance web applications with automatic interactive documentation.
- **SQLAlchemy**: Efficiently handles database operations, storing user data and related information.
- **OAuth2 Authentication**: Uses third-party OAuth2 providers (like Google, GitHub) for easy user login and authentication.
- **JWT**: Secure, token-based authentication system to manage user sessions after OAuth2 login.
- **Middleware**: Handles cross-cutting concerns, including authentication and session management.
- **Templates**: Allows for rendering HTML views to display interactive authentication pages (if applicable).
- **Configuration Management**: Manages application settings and environment variables for flexible configuration.
- **Project Structure**: Ensures scalability and maintainability with a clear separation of concerns.


## Prerequisites

- Python 3.9+
- pip
- Virtual environment support
## **Libraries Used**

- **FastAPI** 
- **Authlib** 
- **JWT** 
- **SQLAlchemy** 
- **Python-dotenv** 



## **Installation and Setup**

### **1. Clone the Repository**

```bash
git clone https://github.com/pavandandla/FastAPI-OAuth2-Authentication-System.git
cd FastAPI-OAuth2-Authentication-System
```



### **2. Create a Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```



### **3. Install Dependencies**

```bash
pip install -r src/requirements.txt
```



### **4. Configure Environment Variables**

Create a `.env` file in the root directory with the following configuration:

```plaintext
SECRET_KEY=your_secret_key
OAUTH2_GOOGLE_CLIENT_ID=your_google_client_id
OAUTH2_GOOGLE_CLIENT_SECRET=your_google_client_secret
OAUTH2_GITHUB_CLIENT_ID=your_github_client_id
OAUTH2_GITHUB_CLIENT_SECRET=your_github_client_secret
DATABASE_URL=sqlite:///./test.db  # Or MySQL connection string
JWT_SECRET_KEY=your_jwt_secret_key
FLASK_ENV=development
```

- **SECRET_KEY**: Key for securely signing JWT tokens.
- **OAUTH2_GOOGLE_CLIENT_ID** and **OAUTH2_GOOGLE_CLIENT_SECRET**: Credentials for Google OAuth2.
- **OAUTH2_GITHUB_CLIENT_ID** and **OAUTH2_GITHUB_CLIENT_SECRET**: Credentials for GitHub OAuth2.
- **DATABASE_URL**: SQLite or MySQL connection string for user data storage.
- **JWT_SECRET_KEY**: Key used for encoding and decoding JWT tokens.
- **FLASK_ENV**: Set to `development` for debugging.



### **5. Set Up the Database**

Run the following command to initialize the database and create necessary tables:

```bash
python src/init_db.py
```



### **6. Run the Application**

To run the FastAPI application, execute:

```bash
uvicorn src.app:app --reload
```

The application will be available at: `http://127.0.0.1:8000`






## **Example Workflow**

1. **User OAuth2 Login**  
    Users can log in using either **Google** or **GitHub** via the respective login endpoints (`/login/google` or `/login/github`). The authentication will happen via OAuth2.
    
2. **Token Generation**  
    After successful login, the user is redirected and an API token (JWT) is generated via the `/token` endpoint.
    
3. **Secure Routes**  
    The generated JWT token is used to authenticate requests to secure routes (e.g., `/user`).
    



## **Environment Configuration**

Example `.env` file:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///./test.db
JWT_SECRET_KEY=your_jwt_secret_key
```



## **Contact**

For questions, suggestions, or issues, contact:

- GitHub: [pavandandla](https://github.com/pavandandla)
