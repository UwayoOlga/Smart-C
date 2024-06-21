const express = require('express');
const app = express();
const port = 3000;

// Middleware to serve static files
app.use(express.static('public'));

// Route handling
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
