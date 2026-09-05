import React, { useEffect, useState } from 'react'
import { createRoot } from 'react-dom/client'
import {
  LayoutDashboard,
  Network,
  Search,
  TrendingUp,
  ShieldAlert,
  FlaskConical,
  LineChart,
  Receipt,
  ArrowUpRight,
  Check,
  Menu
} from 'lucide-react'
import { api } from './api'
import './style.css'

const nav = [
  ['Overview', LayoutDashboard],
  ['Financial Twin', Network],
  ['AI Investigator', Search],
  ['Revenue Intelligence', TrendingUp],
  ['Risk & Anomalies', ShieldAlert],
  ['What-If Lab', FlaskConical],
  ['Forecast', LineChart],
  ['Transactions', Receipt]
]

const rupees = n =>
  '₹' +
  new Intl.NumberFormat('en-IN', {
    maximumFractionDigits: 0
  }).format(n || 0)

const Label = ({ type = 'FACT' }) => (
  <span className={'label ' + type.toLowerCase()}>{type}</span>
)

function Landing({ enter }) {
  return (
    <main className="landing">
      <header>
        <div className="brand">
          <i />
          FinTwin
        </div>

        <nav>
          <a>Product</a>
          <a>How it works</a>
          <a>For teams</a>
        </nav>

        <button onClick={enter}>
          Explore twin <ArrowUpRight size={15} />
        </button>
      </header>

      <section className="hero">
        <div className="eyebrow">
          FINANCIAL INTELLIGENCE, REIMAGINED
        </div>

        <h1>
          Your business has thousands of financial events.
          <br />
          <em>FinTwin turns them into decisions.</em>
        </h1>

        <p>
          Build a living financial twin that detects problems,
          uncovers why they happened, and safely tests what to do next.
        </p>

        <div className="actions">
          <button onClick={enter}>
            Explore Financial Twin <ArrowUpRight size={17} />
          </button>

          <button className="ghost" onClick={enter}>
            Run AI Investigation
          </button>
        </div>
      </section>

      <section className="ecosystem">
        <div className="orbit o1">Customers</div>
        <div className="orbit o2">Orders</div>
        <div className="orbit o3">Payments</div>

        <div className="core">
          Bloom & Co.
          <small>Financial Twin</small>
        </div>

        <div className="orbit o4">Refunds</div>
        <div className="orbit o5">Settlements</div>
        <div className="orbit o6">Cash flow</div>
      </section>
    </main>
  )
}

function Overview({ go }) {
  const [d, setD] = useState()

  useEffect(() => {
    api.overview().then(setD)
  }, [])

  if (!d) return <Loading />

  const cards = [
    ['Total Revenue', rupees(d.total_revenue), 'peach'],
    ['Net Revenue', rupees(d.net_revenue), 'pink'],
    ['Transactions', d.transactions.toLocaleString(), 'yellow'],
    ['Payment Success', d.payment_success + '%', 'lav']
  ]

  return (
    <>
      <Head
        title="Good afternoon, Bloom & Co."
        text="Here’s what changed in your business."
        action={() => go('AI Investigator')}
      />

      <section className="metrics">
        {cards.map((x, i) => (
          <div className={'metric ' + x[2]} key={x[0] + i}>
            <p>{x[0]}</p>
            <b>{x[1]}</b>
            <small>Live, seeded financial data</small>
          </div>
        ))}
      </section>

      <section className="grid wide">
        <article className="panel">
          <Label />
          <h2>Business pulse</h2>

          <div className="bigmoney">
            {rupees(d.total_revenue)}
          </div>

          <div className="chart">
            Live transactional revenue baseline
            <br />
            <strong>
              Payment success: {d.payment_success}% · Refund rate:{' '}
              {d.refund_rate}%
            </strong>
          </div>
        </article>

        <article className="flow">
          <Label type="FACT" />

          <h3>Where your money is going</h3>

          <div>
            <span>Revenue</span>
            <b>{rupees(d.total_revenue)}</b>
          </div>

          <div>
            <span>Potential leakage</span>
            <b>{rupees(d.potential_leakage)}</b>
          </div>

          <div className="net">
            <span>Net revenue</span>
            <b>{rupees(d.net_revenue)}</b>
          </div>
        </article>
      </section>

      <h2 className="sectiontitle">
        AI discovered <em>3 things</em>
      </h2>

      <section className="insights">
        {[
          [
            'PAYMENT HEALTH',
            'UPI success dropped during evening peak.',
            '₹4.2L revenue at risk.',
            'AI Investigator'
          ],
          [
            'REVENUE LEAKAGE',
            'Recoverable subscription revenue detected.',
            'Prioritized by expected net benefit.',
            'Revenue Intelligence'
          ],
          [
            'RISK',
            '17 accounts form a coordinated refund cluster.',
            '3 shared device clusters.',
            'Risk & Anomalies'
          ]
        ].map((x, i) => (
          <article className="insight pink" key={x[0] + i}>
            <Label />

            <h3>{x[0]}</h3>

            <p>{x[1]}</p>

            <small>{x[2]}</small>

            <button onClick={() => go(x[3])}>
              Investigate →
            </button>
          </article>
        ))}
      </section>
    </>
  )
}

function Investigator() {
  const [q, setQ] = useState(
    'Something seems wrong with my business. Investigate.'
  )

  const [r, setR] = useState()
  const [busy, setBusy] = useState(false)

  async function run() {
    setBusy(true)

    try {
      setR(await api.investigate(q))
    } finally {
      setBusy(false)
    }
  }

  return (
    <>
      <Head
        title="AI Investigator"
        text="Ask FinTwin to investigate your business."
      />

      <section className="investigate">
        <div className="ask">
          <textarea
            value={q}
            onChange={e => setQ(e.target.value)}
          />

          <button onClick={run}>
            {busy ? 'Investigating…' : 'Investigate'}
            <ArrowUpRight size={16} />
          </button>
        </div>

        {r && (
          <div className="result">
            <div className="process">
              <Label type="PREDICTION" />

              <h3>Investigation complete</h3>

              {r.steps.map((x, i) => (
                <p key={i}>
                  <Check size={15} />
                  {x}
                </p>
              ))}
            </div>

            <div className="finding">
              <Label />

              <h2>{r.root_cause}</h2>

              <p>
                Evidence came from bounded financial-analysis tools;
                the explanation does not invent financial facts.
              </p>

              <div className="evidence">
                <div>
                  <small>PAYMENT SUCCESS</small>
                  <b>
                    {r.evidence.payment_success_before}% →{' '}
                    {r.evidence.payment_success_after}%
                  </b>
                </div>

                <div>
                  <small>AFFECTED</small>
                  <b>
                    {r.evidence.affected_transactions.toLocaleString()}
                  </b>
                </div>

                <div>
                  <small>AT RISK</small>
                  <b>
                    {rupees(r.evidence.revenue_at_risk)}
                  </b>
                </div>
              </div>
            </div>

            <aside>
              <Label type="RECOMMENDATION" />
              <b>{r.recommendation}</b>
            </aside>
          </div>
        )}
      </section>
    </>
  )
}

function Twin() {
  const [g, setG] = useState()

  useEffect(() => {
    api.twin().then(setG)
  }, [])

  if (!g) return <Loading />

  return (
    <>
      <Head
        title="Financial Twin"
        text="A living model of your business."
      />

      <section className="twin">
        <div className="network">
          {g.edges.map((e, i) => (
            <div
              className="node"
              key={`${e.source}-${e.target}-${i}`}
              style={{
                left: (i % 3) * 29 + 5 + '%',
                top: (i % 2) * 53 + 18 + '%'
              }}
            >
              <b>
                {g.nodes.find(n => n.id === e.source)?.label}
              </b>

              <small>
                connected to{' '}
                {g.nodes.find(n => n.id === e.target)?.label}
              </small>
            </div>
          ))}
        </div>

        <aside className="detail">
          <Label />

          <h3>Connected entities</h3>

          <p>
            Network edges are returned by the twin API and reflect
            the seeded ledger relationships.
          </p>

          {g.nodes.map(n => (
            <div key={n.id}>
              <span>{n.type}</span>
              <b>{n.label}</b>
            </div>
          ))}
        </aside>
      </section>
    </>
  )
}

function Lab() {
  const [s, setS] = useState(94.8)
  const [r, setR] = useState(2.7)
  const [out, setOut] = useState()

  useEffect(() => {
    api.simulate(s, r).then(setOut)
  }, [s, r])

  return (
    <>
      <Head
        title="What-If Lab"
        text="Test decisions before they affect your business."
      />

      <section className="lab">
        <div className="controls">
          <h3>Scenario controls</h3>

          <label>
            Payment success <b>{s}%</b>

            <input
              type="range"
              min="80"
              max="100"
              step=".1"
              value={s}
              onChange={e => setS(+e.target.value)}
            />
          </label>

          <label>
            Refund rate <b>{r}%</b>

            <input
              type="range"
              min="1"
              max="6"
              step=".1"
              value={r}
              onChange={e => setR(+e.target.value)}
            />
          </label>
        </div>

        {out && (
          <div>
            <div className="simcards">
              <article>
                <Label />
                <p>CURRENT STATE</p>
                <b>{rupees(out.current_revenue)}</b>
              </article>

              <article className="sim">
                <Label type="SIMULATION" />
                <p>SIMULATED STATE</p>
                <b>{rupees(out.simulated_revenue)}</b>
              </article>

              <article className="impact">
                <p>NET IMPACT</p>
                <b>{rupees(out.net_impact)}</b>
              </article>
            </div>

            <article className="recommend">
              <Label type="RECOMMENDATION" />

              <h3>Prioritize payment reliability</h3>

              <p>
                This deterministic scenario has the highest expected
                net benefit at the selected values.
              </p>
            </article>
          </div>
        )}
      </section>
    </>
  )
}

function DataPage({ page }) {
  const [rows, setRows] = useState(null)
  const [error, setError] = useState(null)

  useEffect(() => {
    setRows(null)
    setError(null)

    let fn

    if (page === 'Risk & Anomalies') {
      fn = api.risk
    } else if (page === 'Forecast') {
      fn = () => api.forecast(30)
    } else if (page === 'Revenue Intelligence') {
      fn = api.opportunities
    } else {
      fn = () => api.transactions()
    }

    fn()
      .then(data => {
        console.log('FinTwin data received:', data)
        setRows(data)
      })
      .catch(err => {
        console.error('FinTwin data error:', err)
        setError(err.message || 'Unable to load data')
      })
  }, [page])

  if (error) {
    return (
      <div className="generic">
        <Label type="FACT" />
        <h2>Unable to load FinTwin data</h2>
        <p>{error}</p>
      </div>
    )
  }

  if (rows === null) {
    return <Loading />
  }

  const list = Array.isArray(rows) ? rows : []

  return (
    <>
      <Head
        title={page}
        text="Live analytical results from the FinTwin service."
      />

      <section className="generic">
        {page === 'Forecast' && (
          <article>
            <Label type="PREDICTION" />

            <p>Expected revenue, next 30 days</p>

            <h1>{rupees(rows.expected_revenue)}</h1>

            <span>
              Range {rupees(rows.lower_bound)} —{' '}
              {rupees(rows.upper_bound)}
            </span>
          </article>
        )}

        {page === 'Transactions' || list.length > 0 ? (
          <table>
            <thead>
              <tr>
                {Object.keys(list[0] || {}).map(k => (
                  <th key={k}>
                    {k.replaceAll('_', ' ')}
                  </th>
                ))}
              </tr>
            </thead>

            <tbody>
              {list.slice(0, 25).map((x, i) => (
                <tr key={i}>
                  {Object.values(x).map((v, j) => {
                    const key = Object.keys(x)[j]

                    return (
                      <td key={key}>
                        {typeof v === 'number' &&
                        [
                          'amount',
                          'impact',
                          'expected_net_benefit'
                        ].some(k => key.includes(k))
                          ? rupees(v)
                          : String(v)}
                      </td>
                    )
                  })}
                </tr>
              ))}
            </tbody>
          </table>
        ) : null}
      </section>
    </>
  )
}

function Head({ title, text, action }) {
  return (
    <section className="pagehead">
      <div>
        <p className="overline">
          BLOOM & CO. · LIVE DEMO DATA
        </p>

        <h1>{title}</h1>

        <p>{text}</p>
      </div>

      {action && (
        <button onClick={action}>
          Run AI Investigation
          <ArrowUpRight size={16} />
        </button>
      )}
    </section>
  )
}

function Loading() {
  return (
    <div className="generic">
      <Label type="PREDICTION" />
      <h2>Loading FinTwin data…</h2>
    </div>
  )
}

function App() {
  const [land, setLand] = useState(true)
  const [page, setPage] = useState('Overview')
  const [mobile, setMobile] = useState(false)

  if (land) {
    return (
      <Landing
        enter={() => setLand(false)}
      />
    )
  }

  const C =
    page === 'Overview'
      ? Overview
      : page === 'AI Investigator'
      ? Investigator
      : page === 'Financial Twin'
      ? Twin
      : page === 'What-If Lab'
      ? Lab
      : DataPage

  return (
    <div className="app">
      <aside className={mobile ? 'side open' : 'side'}>
        <div className="brand">
          <i />
          FinTwin
        </div>

        <div className="merchant">
          B
          <span>
            Bloom & Co.
            <small>Demo merchant</small>
          </span>
        </div>

        <nav>
          {nav.map(([n, I]) => (
            <button
              key={n}
              className={page === n ? 'active' : ''}
              onClick={() => {
                setPage(n)
                setMobile(false)
              }}
            >
              <I size={18} />
              {n}
            </button>
          ))}
        </nav>

        <div className="bottom">
          <span>● Demo Mode</span>
        </div>
      </aside>

      <main className="workspace">
        <header className="top">
          <button
            className="hamb"
            onClick={() => setMobile(!mobile)}
          >
            <Menu />
          </button>

          <div className="crumb">
            Bloom & Co. / Last 30 days
          </div>

          <div className="status">
            <i />
            FinTwin AI · Online
          </div>
        </header>

        <div className="content">
          <C page={page} go={setPage} />
        </div>
      </main>
    </div>
  )
}

createRoot(document.getElementById('root')).render(
  <App />
)