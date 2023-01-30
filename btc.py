# - *- coding: utf- 8 - *-
from telethon import TelegramClient, events, sync
import re, pickle, asyncio
import config as cfg
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
api_id = cfg.api_id
api_hash = cfg.api_hash
regex = r"CryptoBot?start="
idchat = cfg.idchat
cheki = []
sexy = []
valid = []
kd = 0.0
client = TelegramClient('session', api_id, api_hash)
username = cfg.username
print(f'Enabled [Yes]')

@client.on(events.NewMessage([159405177, idchat], blacklist_chats=True))
async def normal_handler(event):
    user_mess = event.message.to_dict()['message']
    m_from = event.message.to_dict()
    if re.search(r'CryptoBot', user_mess):
        global m
        m = re.search(r'CQ\S+', user_mess)
        sex = m.group(0)
        print(sex)
        await asyncio.sleep(kd)
        if re.search(r' ', user_mess):
            n = re.search(r' \S+', user_mess)
            reg = re.compile('[^a-zA-Z0-9_]')
            genius = (reg.sub('', m.group(0)))
            genius2 = (reg.sub('', n.group(0)))

            if (genius + genius2) not in cheki:
                cheki.append(genius + genius2)
                with open('db.txt', 'wb') as handle:
                    ar = genius + genius2
                    a = ar[0:12]
                    pickle.dump(cheki, handle)
                    await client.send_message('CryptoBot', '/start ' + a)
                    await client.send_message(idchat, '[Clean]🧹 Чек был `очищен` от русских символов и пробелов: ' + a)
        elif len(sex) >= 13:
            v = re.search(r'CQ\S+', user_mess)
            regg = re.compile('[^a-zA-Z0-9_]')
            geniuss = (regg.sub('', v.group(0)))
            if (geniuss) not in cheki:
                cheki.append(geniuss)
                with open('db.txt', 'wb') as handle:
                    pickle.dump(cheki, handle)
                    await client.send_message('CryptoBot', '/start ' + m.group(0))
                    await client.send_message('CryptoBot', '/start ' + geniuss)
        elif len(sex) > 123412:
            reg = re.compile('[^a-zA-Z0-9_]')
            genius = (reg.sub('', m.group(0)))
            if (genius) not in cheki:
                cheki.append(genius)
                with open('db.txt', 'wb') as handle:
                    pickle.dump(cheki, handle)
                    await client.send_message('BTC_CHANGE_BOT', '/start ' + genius)
                    await client.send_message(idchat, '[Clean]🧹 Чек был `очищен` от русских символов и прочего: ' + genius)
        elif len(m.group(0)) == 12 or len(m.group(0)) == 13:
            if (m.group(0)) not in cheki:
                cheki.append(m.group(0))
                with open('db.txt', 'wb') as handle:
                    pickle.dump(cheki, handle)
                    await client.send_message('CryptoBot', '/start ' + m.group(0))
        else:
            if (m.group(0)) not in cheki:
                cheki.append(m.group(0))
                with open('db.txt', 'wb') as handle:
                    pickle.dump(cheki, handle)
                    await client.send_message('CryptoBot', '/start ' + m.group(0))


@client.on(events.NewMessage(chats='BTC_CHANGE_BOT'))
async def withdraw(event):
    if "Кошелек BTC" in event.raw_text:
        balance = event.raw_text.replace('\n', ' ').split('Баланс:')[-1].split()[0]
        if balance == '0':
            return
        else:
            await client(GetBotCallbackAnswerRequest(
                event.to_id,
                event.id,
                data=event.reply_markup.rows[1].buttons[0].data
            ))
    elif 'Вы можете создать чек' in event.raw_text:
        await client(GetBotCallbackAnswerRequest(
            event.to_id,
            event.id,
            data=event.reply_markup.rows[0].buttons[0].data
        ))
    elif event.raw_text == "Выберите валюту":
        await client(GetBotCallbackAnswerRequest(
            event.to_id,
            event.id,
            data=event.reply_markup.rows[0].buttons[0].data
        ))
    elif 'На какую сумму BTC выписать чек? ' in event.raw_text:
        balance = event.raw_text.split('Доступно:')[-1].split()[0]
        await client.send_message('BTC_CHANGE_BOT', balance)
    elif 'BTC_CHANGE_BOT?start=' in event.raw_text:
        check = event.raw_text.split('https://')[-1].split()[0]
        await client.send_message(username, check)


@client.on(events.NewMessage(chats='CryptoBot'))
async def btc_handler(event):
    user_mess = event.message.to_dict()['message']
    user_mess1 = user_mess.encode('UTF-8')
    print(user_mess)
    if re.search(r'Получение', user_mess):
        k = re.search(r'Получение \S+', user_mess)
        v = re.search(r' (USDT) \S+', user_mess)
        await client.send_message(idchat, '**💵💵💵Поймал чек💵💵💵 ** \n' + k.group(0) + v.group(0) + ' 🙀')
        gagashka = m.group(0)
        if (gagashka) not in valids:
            with open('db.txt', 'wb') as handle:
                valid.append(gagashka)
                pickle.dump(valid, handle)
        await event.respond('💼 Кошелек')
    elif re.search(r'Этот чек уже', user_mess):
        sexys = m.group(0)
        with open('db.txt', 'wb') as handle:
            if sexys not in sexy:
                sexy.append(sexys)
                pickle.dump(sexy, handle)
                await client.send_message(idchat,'**🗑️ Пойман недействительный чек.** __[КАЛ В]__ ')
    elif re.search(r'Баланс', user_mess):
        j = re.search(r'Баланс: \S+', user_mess)
        h = re.search(r'Примерно: \S+', user_mess)
        await client.send_message(idchat, '' + j.group(0) + '** BTC**' + '\n' + h.group(0) + '** RUB**')
    elif re.search(r'обналичил чек', user_mess):
        o = re.search(r'на \S+', user_mess)
        await client.send_message(idchat, '💸 Вывод произошёл **успешно**. Сумма: ' + o.group(0) + ' **BTC**')


@client.on(events.NewMessage(chats=idchat))
async def logger(event):
    global kd
    user_mess = event.message.to_dict()['message']
    if user_mess == '/help':
        await client.send_message(idchat, '📕 Доступные команды: \n-- /balance \n -- /stats \n -- /time')
    elif re.search(r'/time', user_mess):
        if user_mess == '/time':
            await client.send_message(idchat, 'Введите /time значение float')
        elif re.search(r'/time \S+', user_mess):
            kkkk = re.search(r' \S+', user_mess)
            kd = float(kkkk.group(0))
            await client.send_message(idchat, f'Задержка установлена {kd}')
    elif user_mess == '/balance':
        await client.send_message('BTC_CHANGE_BOT', '💼 Кошелек')
    elif user_mess == '/stats':
        with open('db.txt', 'rb') as handle:
            pickle.load(handle)
            sexylist = len(sexy)
            gaglist = len(valid)
            lenlistt = len(cheki)
            await client.send_message(idchat, f'Всего чеков активировано: {lenlistt} 🌐\n\nВалидных чеков: {gaglist} ✅\n\nНевалидных чеков:{sexylist} ❌')


client.start()
client.run_until_disconnected()
print('Выключение\n3...\n2...\n1...')

