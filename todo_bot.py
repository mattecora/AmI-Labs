from telegram.ext import Updater, CommandHandler, MessageHandler
from todo_manager import list_tasks, ins_task, del_task, del_all_tasks, read_tasks, write_tasks

my_token = ""

with open("token.txt") as tok_file:
    my_token = tok_file.read()

sep = " "

# Handler for /start
def start_handler(bot, update):
    update.message.reply_text("Welcome to the Todo Manager, {}!".format(update.message.from_user.first_name))

# Handler for /showTasks
def show_handler(bot, update):
    tasks = list_tasks()
    if len(tasks) == 0:
        update.message.reply_text("No tasks inserted.")
    else:
        reply = "Inserted tasks:\n"
        for task in tasks:
            reply += task + "\n"
        update.message.reply_text(reply)

# Handler for /newTask
def new_handler(bot, update, args):
    task = sep.join(args)
    if ins_task(task):
        update.message.reply_text("The task was successfully inserted.")
    else:
        update.message.reply_text("There was an error in the insertion.")

# Handler for /removeTask
def rem_handler(bot, update, args):
    task = sep.join(args)
    if del_task(task):
        update.message.reply_text("The task was successfully deleted.")
    else:
        update.message.reply_text("There was an error in the deletion.")

# Handler for /removeAllTasks
def rem_all_handler(bot, update, args):
    task = sep.join(args)
    deleted_tasks = del_all_tasks(task)
    if len(deleted_tasks) == 0:
        update.message.reply_text("No tasks deleted.")
    else:
        reply = "Removed tasks:\n"
        for task in deleted_tasks:
            reply += task + "\n"
        update.message.reply_text(reply)

def main():
    # Updater creating
    updater = Updater(my_token)
    print("Your token is: {}".format(my_token))

    # Tasks reading
    read_tasks()

    # Registering handlers
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("showTasks", show_handler))
    updater.dispatcher.add_handler(CommandHandler("newTask", new_handler, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("removeTask", rem_handler, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler("removeAllTasks", rem_all_handler, pass_args=True))

    # Bot starting
    updater.start_polling()
    print("Bot started: {}".format(updater.bot.username))
    updater.idle()

    # Tasks writing
    write_tasks()
    print("Bot stopped.")

if __name__ == "__main__":
    main()