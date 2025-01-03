from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes

async def say_hello(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Word")
    
async def echo(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)    

application  = ApplicationBuilder().token("7862329646:AAEHNihtNBkCxojWgzRsSa-r6OfrYdLg9kE").build()

## he we captured the event from the API

application.add_handler(CommandHandler("start", say_hello))
application.add_handler(CommandHandler("echo", echo))



## in this line we say react the all user send 
application.run_polling(allowed_updates=Update.ALL_TYPES)