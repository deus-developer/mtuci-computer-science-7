CREATE TABLE subject (
    name VARCHAR(255) PRIMARY KEY
);
CREATE TABLE teacher (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR,
    subject VARCHAR(255) REFERENCES subject
);
CREATE TABLE timetable (
    id SERIAL PRIMARY KEY,
    day SMALLINT,
    subject VARCHAR(255) REFERENCES subject,
    room_numb SMALLINT,
    start_time SMALLINT
);

INSERT INTO subject (name) VALUES ('Философия');
INSERT INTO subject (name) VALUES ('Основы российской государственности');
INSERT INTO subject (name) VALUES ('Физика');
INSERT INTO subject (name) VALUES ('Линейная алгебра и аналитическая геометрия');
INSERT INTO subject (name) VALUES ('Русский язык и культура речи');
INSERT INTO subject (name) VALUES ('Введение в информационные технологии');
INSERT INTO subject (name) VALUES ('Физическая культура и спорт');
INSERT INTO subject (name) VALUES ('Иностранный язык');
INSERT INTO subject (name) VALUES ('Высшая математика');
INSERT INTO subject (name) VALUES ('Введение в профессию');


INSERT INTO teacher (full_name, subject) VALUES ('Девайкин И.А', 'Философия');
INSERT INTO teacher (full_name, subject) VALUES ('Хуснутдинова Л.Г.', 'Основы российской государственности');
INSERT INTO teacher (full_name, subject) VALUES ('Тренин А.Е.', 'Физика');
INSERT INTO teacher (full_name, subject) VALUES ('Пискарев С.И.', 'Линейная алгебра и аналитическая геометрия');
INSERT INTO teacher (full_name, subject) VALUES ('Кораблева Е.В.', 'Философия');
INSERT INTO teacher (full_name, subject) VALUES ('Иноземцева Н.Г.', 'Физика');
INSERT INTO teacher (full_name, subject) VALUES ('Бочарова Т.И.', 'Русский язык и культура речи');
INSERT INTO teacher (full_name, subject) VALUES ('Рабенандрасана Ж.', 'Введение в информационные технологии');
INSERT INTO teacher (full_name, subject) VALUES ('Денеко М.В. ', 'Иностранный язык');
INSERT INTO teacher (full_name, subject) VALUES ('Алмохамед М.', 'Высшая математика');
INSERT INTO teacher (full_name, subject) VALUES ('Алмохамед М.', 'Линейная алгебра и аналитическая геометрия');
INSERT INTO teacher (full_name, subject) VALUES ('Солиев Ю.С.', 'Высшая математика');
INSERT INTO teacher (full_name, subject) VALUES ('Антонова В.М.', 'Введение в профессию');


--     Первая неделя
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (1, 'Философия', 436, 570);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (1, 'Философия', 412, 680);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (1, 'Основы российской государственности', 316, 790);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (1, 'Физика', 342, 925);

INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (2, 'Линейная алгебра и аналитическая геометрия', 508, 570);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (2, 'Философия', 227, 680);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (2, 'Физика', 216, 790);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (2, 'Русский язык и культура речи', 330, 925);

INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (3, 'Введение в информационные технологии', 702, 570);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (3, 'Введение в информационные технологии', 207, 680);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (3, 'Введение в информационные технологии', 702, 790);

INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (4, 'Русский язык и культура речи', 535, 570);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (4, 'Физическая культура и спорт', 0, 680);

INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (6, 'Иностранный язык', 517, 680);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (6, 'Высшая математика', 308, 790);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (6, 'Линейная алгебра и аналитическая геометрия', 308, 925);

--     Вторая неделя
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (8, 'Русский язык и культура речи', 301, 570);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (8, 'Иностранный язык', 318, 680);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (8, 'Основы российской государственности', 456, 790);

INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (9, 'Высшая математика', 330, 570);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (9, 'Физическая культура и спорт', 0, 680);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (9, 'Физика', 216, 790);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (9, 'Основы российской государственности', 535, 925);

INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (10, 'Линейная алгебра и аналитическая геометрия', 404, 570);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (10, 'Физическая культура и спорт', 0, 680);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (10, 'Философия', 535, 790);

INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (11, 'Высшая математика', 508, 570);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (11, 'Физическая культура и спорт', 0, 680);

INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (12, 'Введение в профессию', 0, 680);
INSERT INTO timetable ("day", subject, room_numb, start_time) VALUES (12, 'Введение в профессию', 0, 790);
