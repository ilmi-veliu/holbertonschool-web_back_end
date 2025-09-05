// 3-read_file_async.js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split(/\r?\n/);
      const students = lines.slice(1).filter((line) => line.trim() !== '');
      console.log(`Number of students: ${students.length}`);

      const groups = {};
      for (const line of students) {
        const cols = line.split(',');
        const firstname = cols[0].trim();
        const field = cols[cols.length - 1].trim();
        if (!groups[field]) groups[field] = [];
        groups[field].push(firstname);
      }
      for (const [field, list] of Object.entries(groups)) {
        console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      }
      resolve();
    });
  });
}

module.exports = countStudents;
