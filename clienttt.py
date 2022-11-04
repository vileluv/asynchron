import asyncio


async def tcp_echo_client(msg):
    reader, writer = await asyncio.open_connection('127.0.0.1', port)
    print(f'Отправил сообщение: {msg}')
    writer.write(msg.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Получил: {data.decode()}')
    writer.close()


try:
    port = input("Введите номер порта или def для стандартного: ")
    if port == '':
        port = 9090
        port = int(port)
    if type(port) == int and 0 <= port <= 65535:
        pass
    else:
        port = 9090
except ValueError:
    port = 9090
    print("Введен некорректный порт. По умолчанию - 9090.")

msg = input('Введите сообщение: ')
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(msg))
loop.close()