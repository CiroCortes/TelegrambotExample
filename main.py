from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler,ContextTypes
from Controllers.TodoController import TodoController

TOKEN = "7862329646:AAEHNihtNBkCxojWgzRsSa-r6OfrYdLg9kE"

application  = ApplicationBuilder().token(TOKEN).build()

## He we captured the event from the API (WHIT COMMAND)

application.add_handler(CommandHandler("add", TodoController.add_todo))
application.add_handler(CommandHandler("list", TodoController.list_todo))
application.add_handler(CommandHandler("check", TodoController.check_todo))
application.add_handler(CommandHandler("clear", TodoController.clear_todos))

## In this line we say react the all user send 
application.run_polling(allowed_updates=Update.ALL_TYPES)