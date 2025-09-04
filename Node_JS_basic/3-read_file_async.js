const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }

      const lines = data.split('\n')
        .map((line) => line.trim())
        .filter((line) => line.length > 0);

      const header = lines[0];
      const rows = lines.slice(1);

      console.log(`Number of students: ${rows.length}`);

      const byField = {};

      for (const row of rows) {
        const parts = row.split(',');
        const firstName = parts[0].trim();
        const field = parts[3].trim();

        if (!byField[field]) {
          byField[field] = [];
        }
        byField[field].push(firstName);
      }

      for (const field of Object.keys(byField)) {
        const list = byField[field];
        console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
