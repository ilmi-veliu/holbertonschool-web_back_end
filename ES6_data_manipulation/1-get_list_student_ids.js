export default function getListStudentIds(students) {
    if (Array.isArray(students)) {
        return students.map(function(student) {
            return student.id;
        });
    } else {
        return [];
    }
}
