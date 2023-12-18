# main.py
from fastapi import FastAPI
from routes import router as routes_router

app = FastAPI(title="Student Register Form", docs_url="/")


# Include the router from the routes module
app.include_router(routes_router, prefix="/api")

