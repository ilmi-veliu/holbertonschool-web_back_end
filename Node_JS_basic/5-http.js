const http = require('http');
const countStudents = require('./3-read_file_async');

const databaseFile = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');

    if (!databaseFile) {
      res.end('Cannot load the database');
      return;
    }

    const originalLog = console.log;
    const lines = [];
    console.log = (...args) => {
      lines.push(args.join(' '));
    };

    countStudents(databaseFile)
      .then(() => {
        console.log = originalLog;
        res.end(lines.join('\n'));
      })
      .catch((err) => {
        console.log = originalLog;
        res.end(err.message);
      });
    return;
  }
  res.statusCode = 404;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Not found');
});

app.listen(1245);

module.exports = app;
