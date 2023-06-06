import json
import os
from datetime import datetime

NOTES_FILE_PATH = 'notes.json'

if not os.path.exists(NOTES_FILE_PATH):
    with open(NOTES_FILE_PATH, 'w') as f:
        json.dump([], f)


def get_notes():
    with open(NOTES_FILE_PATH) as f2:
        notes_list = json.load(f2)
    return notes_list


def add_note():
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
    date = datetime.now()
    notes = get_notes()
    new_note_id = 1 if not notes else max(note['note_id'] for note in notes) + 1
    new_note = {'note_id': new_note_id, 'title': title, 'text': text, 'date': date.isoformat()}
    notes.append(new_note)
    save_notes(notes)
    print(f'Заметка "{new_note["title"]}" создана с ID {new_note["note_id"]}')


def edit_note():
    note_id = int(input('Введите ID заметки, которую хотите отредактировать: '))
    notes = get_notes()
    found_note = next((note for note in notes if note['note_id'] == note_id), None)
    if not found_note:
        print(f'Заметка с ID {note_id} не найдена')
        return
    new_title = input('Введите новый заголовок (enter, чтобы пропустить): ')
    new_text = input('Введите новый текст заметки (enter, чтобы пропустить): ')
    if new_title:
        found_note['title'] = new_title
    if new_text:
        found_note['text'] = new_text
    save_notes(notes)
    print(f'Заметка "{found_note["title"]}" отредактирована')


def delete_note():
    note_id = int(input('Введите ID заметки, которую хотите удалить: '))
    notes = get_notes()
    filtered_notes = [note for note in notes if note['note_id'] != note_id]
    if len(filtered_notes) == len(notes):
        print(f'Заметка с ID {note_id} не найдена')
    else:
        save_notes(filtered_notes)
        print(f'Заметка с ID {note_id} успешно удалена')


def filter_notes():
    date = input('Введите дату для фильтрации заметок (в формате ДД.ММ.ГГГГ): ')
    try:
        date = datetime.strptime(date, '%d.%m.%Y').date()
    except ValueError:
        print('Некорректный формат даты')
        return
    notes = get_notes()
    filtered_notes = [note for note in notes if
                      datetime.strptime(note['timestamp'], '%Y-%m-%dT%H:%M:%S.%f').date() == date]
    if not filtered_notes:
        print(f'Заметки на {date} не найдены')
    else:
        print(f'Список заметок с датой {date}:')
        for note in filtered_notes:
            print(f'{note["note_id"]}: {note["title"]}, создано {note["timestamp"]}')


def save_notes(notes_list):
    with open(NOTES_FILE_PATH, 'w') as f3:
        json.dump(notes_list, f3)


while True:
    action = input('Выберите действие: Создать "create", редактировать "edit", '
                   'удалить "delete", фильтровать "filter" или выйти "exit": ')
    if action == 'create':
        add_note()
    elif action == 'edit':
        edit_note()
    elif action == 'delete':
        delete_note()
    elif action == 'filter':
        filter_notes()
    elif action == 'exit':
        break
    else:
        print('Некорректное действие')
