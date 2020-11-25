_counter = 0


def instances_counter(cls):
    """
    Написать декоратор instances_counter, который применяется к любому классу
    и добавляет ему 2 метода:
    get_created_instances - возвращает количество созданых экземпляров класса
    reset_instances_counter - сбросить счетчик экземпляров,
    возвращает значение до сброса
    Имя декоратора и методов не менять
    """

    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            global _counter
            _counter += 1

        @staticmethod
        def get_created_instances():
            return _counter

        @staticmethod
        def reset_instances_counter():
            global _counter
            count, _counter = _counter, 0
            return count

    return NewClass
