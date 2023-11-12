from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn

async def homepage(request):
    return JSONResponse({'Welcome To': 'The Home Route'})

async def about(request):
    return JSONResponse({'The Author Is: ': 'Sam Xue'})

async def contact(request):
    return JSONResponse({'Access Denied: ': 'You may not contact the admin.'})

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/about', about),
    Route('/contact', contact)
])

if __name__ == "__main__":
    uvicorn.run("starlette_api:app", host="0.0.0.0", port=8000, reload=True)