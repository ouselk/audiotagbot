from audiotag.AudioTag import AudioTag
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


AUDIOTAG_API_KEY = ''
TELEGRAM_API_KEY = ''

def audio(update, context):
    file = update.message.audio if (update.message.audio) else update.message.voice
    if (not file):
        update.message.reply_text("Некорректный ввод")
        return None

    file = file.get_file().download("./temp.mp3")
    at = AudioTag(AUDIOTAG_API_KEY)
    answer = at.identifyAndGetResult(open("temp.mp3", 'rb'))
    update.message.reply_text(answer)

def main():
    updater = Updater(TELEGRAM_API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.audio, audio))
    dp.add_handler(MessageHandler(Filters.voice, audio))

    updater.start_polling()

if __name__ == '__main__':
    main()
