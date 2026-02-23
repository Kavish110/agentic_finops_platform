from fastapi import FastAPI
# #region agent log
import json; open(r'd:\agentic_finops_platform\.cursor\debug.log', 'a').write(json.dumps({"id":"log_main_start","timestamp":int(__import__('time').time()*1000),"location":"app/main.py:2","message":"Starting main.py imports","data":{},"runId":"run1","hypothesisId":"E"})+"\n")
# #endregion
try:
    from app.api.routes import router
    # #region agent log
    open(r'd:\agentic_finops_platform\.cursor\debug.log', 'a').write(json.dumps({"id":"log_routes_imported","timestamp":int(__import__('time').time()*1000),"location":"app/main.py:4","message":"Routes imported successfully","data":{},"runId":"run1","hypothesisId":"E"})+"\n")
    # #endregion
except Exception as e:
    # #region agent log
    open(r'd:\agentic_finops_platform\.cursor\debug.log', 'a').write(json.dumps({"id":"log_routes_import_error","timestamp":int(__import__('time').time()*1000),"location":"app/main.py:6","message":"Routes import failed","data":{"error_type":type(e).__name__,"error_message":str(e)},"runId":"run1","hypothesisId":"A,B,E"})+"\n")
    # #endregion
    raise
from app.core.logging import setup_logging

setup_logging()

from app.db.base import Base
from app.db.session import engine

# #region agent log
open(r'd:\agentic_finops_platform\.cursor\debug.log', 'a').write(json.dumps({"id":"log_before_create_all","timestamp":int(__import__('time').time()*1000),"location":"app/main.py:15","message":"Before Base.metadata.create_all","data":{"engine_exists":engine is not None},"runId":"run1","hypothesisId":"D"})+"\n")
# #endregion
try:
    Base.metadata.create_all(bind=engine)
    # #region agent log
    open(r'd:\agentic_finops_platform\.cursor\debug.log', 'a').write(json.dumps({"id":"log_create_all_success","timestamp":int(__import__('time').time()*1000),"location":"app/main.py:18","message":"Base.metadata.create_all succeeded","data":{},"runId":"run1","hypothesisId":"D"})+"\n")
    # #endregion
except Exception as e:
    # #region agent log
    open(r'd:\agentic_finops_platform\.cursor\debug.log', 'a').write(json.dumps({"id":"log_create_all_error","timestamp":int(__import__('time').time()*1000),"location":"app/main.py:20","message":"Base.metadata.create_all failed","data":{"error_type":type(e).__name__,"error_message":str(e)},"runId":"run1","hypothesisId":"D"})+"\n")
    # #endregion
    raise
app = FastAPI(title="Agentic AI Financial Operations Platform")
app.include_router(router)