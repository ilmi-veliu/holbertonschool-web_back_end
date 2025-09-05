const express = require('express');

const countStudents = require('./3-read_file_async');

const databaseFile = process.argv[2];
const app = express();

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');

  if (!databaseFile) {
    res.end('Cannot load the database');
    return;
  }

  const originalLog = console.log;
  const lines = [];
  console.log = (...args) => { lines.push(args.join(' ')); };

  countStudents(databaseFile)
    .then(() => {
      console.log = originalLog;
      res.end(lines.join('\n'));
    })
    .catch((err) => {
      console.log = originalLog;
      res.end(err.message);
    });
});

app.listen(1245);
module.exports = app;
