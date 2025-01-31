import requests

# URL с доменами
#url = 'https://p.thenewone.lol/domains-export.txt'
url = 'https://raw.githubusercontent.com/GhostRooter0953/discord-voice-ips/refs/heads/master/voice_domains/discord-voice-domains-list'

# Имя выходного файла
output_file = 'formatted_domains.lst'

# Функция для загрузки доменов и сохранения в файл
def download_and_format_domains(url, output_file):
    try:
        # Скачиваем список доменов
        response = requests.get(url)
        response.raise_for_status()  # Проверяем успешность запроса

        # Получаем строки доменов
        domains = response.text.splitlines()

        # Открываем файл для записи
        with open(output_file, 'w') as file:
            for domain in domains:
                domain = domain.strip()  # Убираем пробелы и переносы строк
                if domain:  # Если домен не пуст
                    # Форматируем домен без лишних пробелов
                    formatted_domain = f"nftset=/{domain}/4#inet#fw4#vpn_domains"
                    file.write(formatted_domain + '\n')  # Записываем в файл

        print(f"Данные успешно сохранены в {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке доменов: {e}")

# Вызов функции
download_and_format_domains(url, output_file)
