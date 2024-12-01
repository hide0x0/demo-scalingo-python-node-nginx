const express = require('express')
const app = express()
const port = 8000

app.get('/', (req, res) => {
  res.send('<h1>Subdomain takeover By abir</h1>')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
