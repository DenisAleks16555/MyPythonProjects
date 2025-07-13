with open("additional_info.txt", "r", encoding="utf-8") as additional_file:
    #  additional_content = additional_file.read()
name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")
mail = input("Введите вашу электронную почту: ")
city = input("Введите город проживания: ")
school = input("Введите название школы: ")
school_years = input("Введите годы обучения в школе: ")
secondary_education = input("Введите название среднего образования: ")
university = input("Введите название ВУЗа: ")
university_years = input("Введите годы обучения в ВУЗе: ")
degree = input("Введите полученную специальность, степень: ")
portfolio = input("Введите ссылку на ваше портфолио: ")

experience = input("Введите ваш опыт работы: ")
company_name = input("Введите название компании:")
job_title = input("Введите вашу должность: ")
years = input("Введите годы работы: ")
skills = input("Введите ваши навыки: ")

experience = input("Введите ваш опыт работы: ")
company = input("Введите название компании: ")
position = input("Введите название должности: ")
years = input("Введите годы работы: ")
skills = input("Введите ваши навыки: ")


# test = ""

# test += f"Опыт работы: {input("Введите ваш опыт работы: ")}\n"
# test += f"Стаж: {input("Введите количество лет на этой работе: ")}\n"

resume_template = f"""
Имя: {name}
Фамилия: {surname}
Возраст: {age}
Электронная_почта: {mail}
Город: {city}
Школа: {school}
Годы обучения в школе: {school_years}
Среднее образование: {secondary_education}
ВУЗ: {university}
Годы обучения в ВУЗе: {university_years}
Специальность/степень: {degree}
Портфолио: {portfolio}


Опыт работы: {experience}
Название компании: {company_name}
Должность: {job_title}
Годы работы: {years}
Навыки: {skills}

Опыт работы: {experience}
Название компании: {company}
Должность: {position}
Годы работы: {years}
Навыки: {skills}
"""

# Сохраняем резюме в файл resume.txt
with open("resume.txt", "w", encoding="utf-8") as file:
    file.write(resume_template)

# Считываем данные из текстового файла additional_info.txt
with open("additional_info.txt", "r", encoding="utf-8") as additional_file:
    additional_content = additional_file.read()

# Объединяем резюме и дополнительную информацию
combined_content = resume_template + "\nДополнительная информация:\n" + additional_content

# Сохраняем объединённое содержимое в новый файл combined_resume.txt
with open("combined_resume.txt", "w", encoding="utf-8") as file:
    file.write(combined_content)

print("Резюме успешно сохранено в resume.txt и объединённое резюме в combined_resume.txt")