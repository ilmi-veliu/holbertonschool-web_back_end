const fs = require('fs'); // using fs module

function countStudents(path) {
  try {
    // Lire le fichier en UTF-8
    const content = fs.readFileSync(path, 'utf8');

    // Découper en lignes (compatible \n et \r\n)
    const lines = content.split(/\r?\n/);

    // Ignorer l'en-tête et les lignes vides
    const students = lines.slice(1).filter((line) => line.trim() !== '');

    // Nombre total d'étudiants
    console.log(`Number of students: ${students.length}`);

    // Regrouper par filière
    const groups = {};
    for (const line of students) {
      const cols = line.split(',');
      const firstname = cols[0].trim();
      const field = cols[cols.length - 1].trim();

      if (!groups[field]) groups[field] = [];
      groups[field].push(firstname);
    }

    // Afficher les stats par filière
    for (const [field, list] of Object.entries(groups)) {
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
