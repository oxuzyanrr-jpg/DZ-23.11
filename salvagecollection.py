class SalvageCollection:
    def __init__(self, age: int, engine_displacement: int, subject: str):
        self.age = age
        self.engine_displacement = engine_displacement
        self.subject = subject

    def coefficient(self) -> float:
        if self.age > 3 and self.subject == "Человек" and self.engine_displacement == 0:
            return 20000 * 0.17
        elif self.age > 3 and self.subject == "Человек" and 0 < self.engine_displacement <= 1000:
            return 20000 * 0.17
        elif self.age > 3 and self.subject == "Человек" and 1001 <= self.engine_displacement <= 2000:
            return 20000 * 0.17
        elif self.age > 3 and self.subject == "Человек" and 2001 <= self.engine_displacement <= 3000:
            return 20000 * 0.17
        elif self.age > 3 and self.subject == "Человек" and 3001 <= self.engine_displacement <= 3500:
            return 20000 * 107.67
        elif self.age > 3 and self.subject == "Человек" and 3500 < self.engine_displacement:
            return 20000 * 137.11
        elif self.age < 3 and self.subject == "Человек" and self.engine_displacement == 0:
            return 20000 * 0.26
        elif self.age < 3 and self.subject == "Человек" and 0 < self.engine_displacement <= 1000:
            return 20000 * 0.26
        elif self.age < 3 and self.subject == "Человек" and 1001 <= self.engine_displacement <= 2000:
            return 20000 * 0.26
        elif self.age < 3 and self.subject == "Человек" and 2001 <= self.engine_displacement <= 3000:
            return 20000 * 0.26
        elif self.age < 3 and self.subject == "Человек" and 3001 <= self.engine_displacement <= 3500:
            return 20000 * 164.84
        elif self.age < 3 and self.subject == "Человек" and 3500 < self.engine_displacement:
            return 20000 * 180.24
        elif self.age > 3 and self.subject == "Организация" and self.engine_displacement == 0:
            return 20000 * 33.37
        elif self.age > 3 and self.subject == "Организация" and 0 < self.engine_displacement <= 1000:
            return 20000 * 9.01
        elif self.age > 3 and self.subject == "Организация" and 1001 <= self.engine_displacement <= 2000:
            return 20000 * 33.37
        elif self.age > 3 and self.subject == "Организация" and 2001 <= self.engine_displacement <= 3000:
            return 20000 * 93.77
        elif self.age > 3 and self.subject == "Организация" and 3001 <= self.engine_displacement <= 3500:
            return 20000 * 107.67
        elif self.age > 3 and self.subject == "Организация" and 3500 < self.engine_displacement:
            return 20000 * 137.11
        elif self.age < 3 and self.subject == "Организация" and self.engine_displacement == 0:
            return 20000 * 58.7
        elif self.age < 3 and self.subject == "Организация" and 0 < self.engine_displacement <= 1000:
            return 20000 * 23
        elif self.age < 3 and self.subject == "Организация" and 1001 <= self.engine_displacement <= 2000:
            return 20000 * 58.7
        elif self.age < 3 and self.subject == "Организация" and 2001 <= self.engine_displacement <= 3000:
            return 20000 * 141.97
        elif self.age < 3 and self.subject == "Организация" and 3001 <= self.engine_displacement <= 3500:
            return 20000 * 164.84
        elif self.age < 3 and self.subject == "Организация" and 3500 < self.engine_displacement:
            return 20000 * 180.24

    def show_info(self):
        print(f"Возраст машины {self.age},Обьём двигателя {self.engine_displacement},Приобретается на {self.subject}, Утильсбор {self.coefficient()} руб.")
