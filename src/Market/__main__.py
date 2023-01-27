import uvicorn as uvicorn

uvicorn.run(
    'Market.app:app',
    reload='True'
)