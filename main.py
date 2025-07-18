from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import declarative_base, sessionmaker

# Настройки базы данных
Base = declarative_base()
DB_NAME = 'opros_ultima.db'
engine = create_engine(f'sqlite:///{DB_NAME}')
Session = sessionmaker(bind=engine)
session = Session()

# Структура таблицы
class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answer1 = Column(String)
    answer2 = Column(String)
    answer3 = Column(String)
    answer4 = Column(String)
    answer5 = Column(String)
    answer6 = Column(String)
    answer7 = Column(String)

# Создание таблицы
Base.metadata.create_all(engine)

# Список вопросов
questions = [
    'Как дела?',
    'Сколько тебе лет?',
    'Который час?',
    'ФИО?',
    'Да или Нет?',
    'Мальчик вырос в камышах?',
    'Ультима тест?'
]

# Массив для хранения ответов
#answers = [''] * len(questions)
answers = [None, None, None, None, None, None, None]


# Начало опроса
print('Добро пожаловать в опрос компании Ультима!\n')

try:
    # Сбор всех ответов
    # Проверяем максимальный ID в таблице
    last_answer = session.query(Answer).all()
    if last_answer:
        last_answer = last_answer[-1]
        list_of_answer = [last_answer.answer1, last_answer.answer2, last_answer.answer3, last_answer.answer4, last_answer.answer5,
                      last_answer.answer6, last_answer.answer7]
        max_id = last_answer.id
        print(list_of_answer)
        try:
            past_write = list_of_answer.index(None)
        except:
            past_write = 0
        print(past_write)
        for i in range(past_write, len(questions)):
            user_input = input(f'{questions[i]}\n')
            list_of_answer[i] = user_input
            answer_obj = Answer(
            id=max_id,
            answer1=list_of_answer[0],
            answer2=list_of_answer[1],
            answer3=list_of_answer[2],
            answer4=list_of_answer[3],
            answer5=list_of_answer[4],
            answer6=list_of_answer[5],
            answer7=list_of_answer[6]
        )
            session.merge(answer_obj)
            session.commit()
        max_id +=1
        print('Дозапись завершена.')
    
    
    if not last_answer:
        max_id = 1
    #new_id = max_id + 1
    
    for i, question in enumerate(questions):
        user_input = input(f'{question}\n')
        answers[i] = user_input
        # Создаём и сохраняем объект с всеми ответами
        answer_obj = Answer(
        id=max_id,
        answer1=answers[0],
        answer2=answers[1],
        answer3=answers[2],
        answer4=answers[3],
        answer5=answers[4],
        answer6=answers[5],
        answer7=answers[6]
    )
        session.merge(answer_obj)
        session.commit()


    print('\nСпасибо за участие! Ваши ответы сохранены.')

except Exception as e:
    print(f'Произошла ошибка: {e}')
    session.rollback()

finally:
    session.close()