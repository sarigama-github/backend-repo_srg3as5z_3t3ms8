import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Minimal tombstone API: everything is permanently gone (410)
app = FastAPI(title="Service Removed", docs_url=None, redoc_url=None, openapi_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.api_route("/", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])  # Root also gone
def root():
    raise HTTPException(status_code=410, detail="This service has been permanently removed.")

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE"])  # Catch-all
def gone(path: str):
    raise HTTPException(status_code=410, detail="This endpoint has been permanently removed.")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
