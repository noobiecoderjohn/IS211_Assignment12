CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE quizzes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
    num_questions INTEGER NOT NULL,
    date_given TEXT NOT NULL
);

CREATE TABLE quiz_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    quiz_id INTEGER NOT NULL,
    score INTEGER CHECK(score >= 0 AND score <= 100),
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(quiz_id) REFERENCES quizzes(id)
);
