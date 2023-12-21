# main.py
from fastapi import FastAPI
from routes import router as routes_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Student Register Form", docs_url="/")


# Configure CORS middleware
origins = [
        "http://localhost:3000",
        # Add more allowed origins if needed
        ]
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )
# Include the router from the routes module
app.include_router(routes_router, prefix="/api")

