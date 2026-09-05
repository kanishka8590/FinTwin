# FinTwin

Competition-ready financial digital twin for Bloom & Co. It combines deterministic financial facts, statistical anomaly signals, decision simulations, and an explainable investigation flow.

## Run

For the complete product stack, run `docker compose up --build` from this folder. Open `http://localhost:5173`; the API is served at `http://localhost:8000/docs`.

For UI-only iteration, run `npm install` then `npm run dev` from this folder.

## Architecture

The API is FastAPI with SQLAlchemy, Pydantic validation and PostgreSQL. It owns seeded transaction, customer, refund and settlement data; investigation and simulation routes return structured, deterministic results. The UI API client is in `src/api.js`, with Vite proxying `/api` during local development. Simulation values are deterministic functions of the scenario controls; facts, predictions, simulations and recommendations are visibly labeled.

## Demo flow

Overview → Run AI Investigation → Financial Twin → Risk & Anomalies → What-If Lab.
