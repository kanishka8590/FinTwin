const API_BASE = 'http://localhost:8000/api'

const request = async (path, options = {}) => {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: {
      'Content-Type': 'application/json',
    },
    ...options,
  })

  if (!response.ok) {
    throw new Error(`FinTwin API: ${response.status}`)
  }

  return response.json()
}

export const api = {
  health: () => request('/health'),

  overview: () => request('/overview'),

  investigate: (question) =>
    request('/investigations', {
      method: 'POST',
      body: JSON.stringify({ question }),
    }),

  simulate: (payment_success, refund_rate) =>
    request('/simulations', {
      method: 'POST',
      body: JSON.stringify({
        payment_success,
        refund_rate,
      }),
    }),

  transactions: (limit = 25) =>
    request(`/transactions?limit=${limit}`),

  risk: () =>
    request('/risk/incidents'),

  incident: (id) =>
    request(`/risk/incidents/${id}`),

  forecast: (days = 30) =>
    request(`/forecast?days=${days}`),

  opportunities: () =>
    request('/revenue/opportunities'),

  twin: () =>
    request('/twin/graph'),
}