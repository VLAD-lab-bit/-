import asyncio
from clickhouse_driver import Client

async def execute_clickhouse_query(query, query_number, delay=0):
    await asyncio.sleep(delay)  # Имитация задержки
    client = Client(host='g2.plzvpn.ru',
                    user='default',
                    password='1',
                    port='9000',
                    database='test',
                    settings={'use_numpy': True})
    result = client.execute(query)
    print(f"Запрос {query_number} завершен с задержкой {delay} секунд.")
    return result

async def main():
    query1 = "SELECT * FROM Tabl8"
    query2 = "SELECT * FROM Tabl8"
    
    # Запускаем оба запроса асинхронно
    task1 = asyncio.create_task(execute_clickhouse_query(query1, 1, delay=2))
    task2 = asyncio.create_task(execute_clickhouse_query(query2, 2))
    
    # Ожидаем завершения обоих запросов
    await task1
    await task2
    
    return task1.result(), task2.result()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    results1, results2 = loop.run_until_complete(main())
    print("Результат запроса 1:", results1)
    print("Результат запроса 2:", results2)

