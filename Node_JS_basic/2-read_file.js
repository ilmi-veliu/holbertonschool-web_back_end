const fs = require('fs');

function countStudents(path) {
  try {
    const database = fs.readFileSync(path, 'utf-8');
    const lines = database.split('\n').filter(line => line.trim() !== '');
    const etudiant = lines.slice(1);
    const total = etudiant.length;

    console.log(`Number of students: ${total}`);

    const fields = {};

    etudiant.forEach((line) => {
      const parts = line.split(',');
      const firstname = parts[0];
      const field = parts[3];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    for (const [field, list] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
    }

  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
